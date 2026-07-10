# Agent instructions — speechify-api (Python SDK)

This is a **Fern-generated** SDK. It is published to **PyPI** as `speechify-api`.
The source of truth for the API surface lives in the `SpeechifyInc/speechify-api`
repo (`fern/`); this repo receives generated code on the `sdk-release` branch.

**Read this before doing anything that touches a release.** A botched release here
publishes to an immutable public registry and breaks the contract with every
customer who installs the package. This file exists because we already did that
once — see "Postmortem" below.

## The golden rule

**Publishing to PyPI is IRREVERSIBLE.** A version, once uploaded, can never be
overwritten or reused — only *yanked* (hidden from resolution), and yanking
requires a human web session (there is no token/API/CI path for it).

Never trigger a publish until you have, in order:

1. **Audited the release plumbing** (this file, the workflow, the config).
2. **Confirmed the version is correct in EVERY version-bearing file** (see checklist).
3. **Dry-run built and asserted the artifact version** matches the intended tag.
4. **Got explicit human sign-off** for the publish itself.

Do NOT admin-merge release PRs to force a publish. Do NOT bypass required reviews.

## Version-surface checklist — the mistake we keep making

The #1 failure mode is **a generated version string not getting bumped**, so the
package publishes under the wrong number (or reports a false version to the API).
A single stale string is a published contract break, not a typo.

When any version changes, **grep the whole tree and confirm ALL of these agree**
before release. Never check one and assume the rest:

- `.release-please-manifest.json` → `"."`
- `pyproject.toml` → `[project].version` **and** `[tool.poetry].version` (both!)
- `src/speechify/core/client_wrapper.py` → `User-Agent` **and** `X-Fern-SDK-Version`
- the git tag created for the release
- the version in the built artifact filename (`speechify_api-X.Y.Z-*.whl`)

Fast audit:

```bash
grep -rnE '[0-9]+\.[0-9]+\.[0-9]+' \
  .release-please-manifest.json pyproject.toml \
  src/speechify/core/client_wrapper.py | grep -v '<3.0.0'
```

`X-Fern-SDK-Version` / `User-Agent` are sent on every request. If they lie, your
telemetry, version-gating, and support debugging are all wrong for that release.

## Known plumbing traps

- **`pyproject.toml` version wiring.** release-please's Python updater **skips
  `pyproject.toml` when `[project].dynamic = ["version"]`**. If the version is
  dynamic and `extra-files` does not target it, `poetry build` builds a STALE
  version while the tag/manifest say something else. Keep the version **static**
  in `[project].version` and ensure `release-please-config.json` `extra-files`
  bumps it. (This is exactly how we shipped `2.0.1` under a `3.0.0` tag.)
- **`type: "generic"` extra-files no-op silently** unless the target line carries
  an `x-release-please-version` marker comment. Fern regenerates
  `client_wrapper.py` each run, so prefer the `toml` updaters on `pyproject.toml`
  as the real source of truth; do not rely on the generic updater alone.
- The publish job trusts whatever `poetry build` produces. There is a
  `manual-publish.yml` workflow that asserts the built version before uploading —
  prefer it for any one-off republish, and keep the assert in the automatic path.

## If a release has already gone wrong

- **Wrong version on PyPI:** it is permanent. Fix the version wiring, cut a NEW
  correct version, and **yank** the bad one (human, via
  `https://pypi.org/manage/project/speechify-api/release/<version>/`).
- **Tag points at a bad commit:** the tag/GitHub release can be recreated on the
  corrected commit (public history mutation — back up the old SHA + notes first).
- Never delete a PyPI release to "reuse" the number. You can't.

## Postmortem — the 3.0.0 release (why this file exists)

A routine regeneration was pushed straight to publish. Failures, in order:

1. Breaking-change PRs were admin-merged past the review gate.
2. release-please tagged `3.0.0`, but `poetry build` used a stale `pyproject.toml`
   version → **`speechify-api 2.0.1` was published to PyPI** (immutable), carrying
   the 3.0.0 breaking code under a patch number.
3. Each stale version string was found reactively, one at a time, instead of via
   one exhaustive version-surface audit.

Lesson: **audit the whole release surface first, dry-run, get sign-off, then
publish.** Treat one stale version string as a signal to check every other one.
