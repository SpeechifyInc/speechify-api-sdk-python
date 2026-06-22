# Changelog

## [2.0.0](https://github.com/SpeechifyInc/speechify-api-sdk-python/compare/1.2.3...2.0.0) (2026-06-22)


### ⚠ BREAKING CHANGES

* `Speechify(token=...)` is now `Speechify(api_key=...)`. The `tts.` namespace has been removed — call sites move from `client.tts.audio.speech(...)` to `client.audio.speech(...)` and from `client.tts.voices.X` to `client.voices.X`. The `livekit` extra-dependency has been removed; if you were importing it transitively through `speechify-api`, install it explicitly. Generator-line crossed `4.x` → `5.x`, so internal/private code paths have moved.

### Features

* regenerate SDK on fern-python-sdk@5.14.20 with TTS-only surface ([#16](https://github.com/SpeechifyInc/speechify-api-sdk-python/issues/16)) ([2ebb0a5](https://github.com/SpeechifyInc/speechify-api-sdk-python/commit/2ebb0a5e81ec11eab11215f932fb3f529edaf890))
