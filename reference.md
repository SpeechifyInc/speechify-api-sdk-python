# Reference
## Agent
<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List voice agents owned by the caller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a voice agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.create(
    name="name",
    prompt="prompt",
    first_message="first_message",
    voice_id="voice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `str` — Greeting spoken verbatim at session start when included in the agent's flow graph.
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `str` — Voice slug from the VMS catalog (see GET /v1/voices). Required — the server rejects writes with an unknown or empty slug.
    
</dd>
</dl>

<dl>
<dd>

**slug:** `typing.Optional[str]` — Optional. Server derives slug from name with a random suffix when omitted; if you supply your own, a collision returns 400 'slug already taken'.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — ISO 639-1 code. Defaults to 'en' when omitted.
    
</dd>
</dl>

<dl>
<dd>

**llm_provider:** `typing.Optional[CreateAgentRequestLlmProvider]` 

LLM backend. Leave empty (or omit both `llm_provider` and
`llm_model`) to use the platform default (today: Speechify
Kimi K2.6, resolved server-side at dispatch). When set,
must be paired with a non-empty `llm_model`; mixing a
populated provider with an empty model is rejected as a
400. `custom` additionally requires `llm_base_url`.
    
</dd>
</dl>

<dl>
<dd>

**llm_model:** `typing.Optional[str]` 

Chat model slug. Leave empty to use the platform default.
For `openai` / `speechify` the (provider, model) pair must
be in the allowed table; for `custom` it is free-form.
    
</dd>
</dl>

<dl>
<dd>

**llm_base_url:** `typing.Optional[str]` 

Custom OpenAI/vLLM-compatible endpoint base URL. Required
when `llm_provider` is `custom`, rejected otherwise.
    
</dd>
</dl>

<dl>
<dd>

**llm_api_key:** `typing.Optional[str]` 

Bearer key for the custom endpoint. Write-only - stored
encrypted, never returned (GET exposes `llm_api_key_set`).
Optional even for `custom` (keyless endpoints); rejected
for any other provider.
    
</dd>
</dl>

<dl>
<dd>

**llm_extra_body:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Optional JSON object forwarded verbatim to the custom
endpoint as the chat.completions `extra_body` (reasoning /
sampling knobs). Valid only when `llm_provider` is
`custom`.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature in the range 0.0–1.0. Defaults to 0.5 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**widget_config:** `typing.Optional[WidgetConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[bool]` — Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**hostname_allowlist:** `typing.Optional[typing.Sequence[str]]` — Optional per-agent hostname allowlist (see Agent schema).
    
</dd>
</dl>

<dl>
<dd>

**memory_enabled:** `typing.Optional[bool]` — Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**memory_retention_days:** `typing.Optional[int]` — Defaults to 90 when omitted.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Customer-facing post-call webhook URL.
    
</dd>
</dl>

<dl>
<dd>

**webhook_secret:** `typing.Optional[str]` 

HMAC-SHA256 secret seed. Write-only — never echoed back on
reads; clients see `webhook_secret_set: true` instead.
    
</dd>
</dl>

<dl>
<dd>

**amd:** `typing.Optional[AmdConfig]` — AMD routing config. Optional on create; omitted means AMD off. See AMDConfig schema.
    
</dd>
</dl>

<dl>
<dd>

**save_audio_recording:** `typing.Optional[bool]` — When set, opts the agent into per-conversation audio recording. Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**navigator_mode:** `typing.Optional[bool]` — When set, opts the agent into IVR-tuned turn handling. Defaults to false when omitted.
    
</dd>
</dl>

<dl>
<dd>

**ivr_memory_enabled:** `typing.Optional[bool]` — When omitted, defaults to true. Set to false to opt-out of the IVR-memory cache lookup for this agent.
    
</dd>
</dl>

<dl>
<dd>

**tts_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**tts_playback_rate:** `typing.Optional[float]` 

Post-process pitch-preserving time-stretch on the synthesized
audio. See the field on Agent for semantics.
    
</dd>
</dl>

<dl>
<dd>

**response_delay_seconds:** `typing.Optional[float]` 

Per-agent override for the worker's endpointing min_delay on
the VAD path (seconds). See the field on Agent for semantics.
Range 0.0..5.0; null means use the stack default.
    
</dd>
</dl>

<dl>
<dd>

**inactivity_timeout_seconds:** `typing.Optional[int]` 

Per-agent silence-tolerance override in seconds. Send `0`
to clear the override and fall back to the platform
default. Negative values are rejected.
    
</dd>
</dl>

<dl>
<dd>

**background_noise_preset:** `typing.Optional[CreateAgentRequestBackgroundNoisePreset]` 

Pre-mixed ambient bed slug. Send empty string ("") to
disable the bed, which also clears `background_noise_volume`.
    
</dd>
</dl>

<dl>
<dd>

**background_noise_volume:** `typing.Optional[float]` 

Volume of the background-noise bed (0..1). Ignored when
`background_noise_preset` is empty.
    
</dd>
</dl>

<dl>
<dd>

**stt_override:** `typing.Optional[CreateAgentRequestSttOverride]` 

Optional non-default streaming-STT stack for this agent.
Omit to use the worker's default stack (today: whisper-v3).
See the Agent schema for the full option semantics.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_agent_voices</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the curated voice catalogue available for voice agents.
Matches the `ai-api-agents` VMS scope one-for-one, so the same
slug set is accepted by POST/PATCH /v1/agents. Personal
(cloned) voices are NOT included — they stay on
`GET /v1/voices`. The JSON layout intentionally mirrors the
TTS `/v1/voices` shape so the console feeds both endpoints
into the same voice-picker component.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_agent_voices()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a voice agent by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a voice agent. Conversations and attached tools remain. Tests whose only agent is this one are deleted with it; tests also attached to other agents survive, minus the attachment.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a voice agent. Only fields present on the request body are changed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_provider:** `typing.Optional[UpdateAgentRequestLlmProvider]` 

LLM backend. Send an empty string together with
`llm_model: ""` to clear the pair to the platform default
(today: Speechify Kimi K2.6). Sending one populated and
one empty is rejected as a 400. Omit both to leave the
stored pair unchanged. Switching to a non-`custom` provider
clears any stored `llm_base_url` / `llm_api_key` /
`llm_extra_body`.
    
</dd>
</dl>

<dl>
<dd>

**llm_model:** `typing.Optional[str]` 

Chat model slug. Empty string + empty `llm_provider`
clears the pair to the platform default. For `openai` /
`speechify` the (provider, model) pair must be in the
allowed table; for `custom` it is free-form.
    
</dd>
</dl>

<dl>
<dd>

**llm_base_url:** `typing.Optional[str]` 

Custom-endpoint base URL. Required when the resulting
provider is `custom`, rejected otherwise.
    
</dd>
</dl>

<dl>
<dd>

**llm_api_key:** `typing.Optional[str]` 

Bearer key for the custom endpoint. Write-only. Omit to
keep the stored key, send "" to clear it, send a value to
replace it. Rejected for non-`custom` providers.
    
</dd>
</dl>

<dl>
<dd>

**llm_extra_body:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

JSON object forwarded to the custom endpoint as
chat.completions `extra_body`. Omit to leave unchanged;
a JSON object (including `{}`) replaces it. Valid only
when the resulting provider is `custom`.
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` — Sampling temperature in the range 0.0–1.0. Omit to leave unchanged.
    
</dd>
</dl>

<dl>
<dd>

**widget_config:** `typing.Optional[WidgetConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**allowed_origins:** `typing.Optional[typing.Sequence[str]]` 
    
</dd>
</dl>

<dl>
<dd>

**hostname_allowlist:** `typing.Optional[typing.Sequence[str]]` 

When supplied, replaces the stored list. Pass an empty
array to clear enforcement (public agent is open again).
Omit the field to leave the existing value unchanged.
    
</dd>
</dl>

<dl>
<dd>

**memory_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**memory_retention_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_secret:** `typing.Optional[str]` — Rotate the HMAC secret. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**amd:** `typing.Optional[AmdConfig]` — AMD routing config (PATCH-replace, wholesale). Omit to leave the stored config unchanged.
    
</dd>
</dl>

<dl>
<dd>

**save_audio_recording:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**navigator_mode:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**ivr_memory_enabled:** `typing.Optional[bool]` — Per-agent kill switch for the IVR-memory cache lookup. nil/omit = unchanged.
    
</dd>
</dl>

<dl>
<dd>

**tts_speaking_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_tts_speaking_rate:** `typing.Optional[bool]` 

Two-headed clear: PATCH cannot distinguish "absent" from
"explicit null" reliably across stacks. Setting this to
`true` resets `tts_speaking_rate` to the voice default.
If both are sent, `clear_tts_speaking_rate` wins.
    
</dd>
</dl>

<dl>
<dd>

**tts_playback_rate:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**clear_tts_playback_rate:** `typing.Optional[bool]` 

Two-headed clear, mirroring `clear_tts_speaking_rate`.
Setting this to `true` resets `tts_playback_rate` to null
(no post-process). If both fields are sent,
`clear_tts_playback_rate` wins.
    
</dd>
</dl>

<dl>
<dd>

**response_delay_seconds:** `typing.Optional[float]` 

Per-agent silence-wait override (seconds). See the field
on Agent for semantics. Range 0.0..5.0; null is allowed
but `clear_response_delay_seconds=true` is the canonical
way to revert to the stack default.
    
</dd>
</dl>

<dl>
<dd>

**clear_response_delay_seconds:** `typing.Optional[bool]` 

Two-headed clear, mirroring `clear_tts_playback_rate`.
Setting this to `true` resets `response_delay_seconds` to
null (revert to the stack default). If both are sent,
`clear_response_delay_seconds` wins.
    
</dd>
</dl>

<dl>
<dd>

**inactivity_timeout_seconds:** `typing.Optional[int]` 

Per-agent silence-tolerance override. Send `0` to clear
the override and fall back to the platform default.
Negative values are rejected.
    
</dd>
</dl>

<dl>
<dd>

**background_noise_preset:** `typing.Optional[UpdateAgentRequestBackgroundNoisePreset]` 

Pre-mixed ambient bed slug. Send empty string ("") to
disable the bed, which also clears `background_noise_volume`.
    
</dd>
</dl>

<dl>
<dd>

**background_noise_volume:** `typing.Optional[float]` 

Volume of the background-noise bed (0..1). Ignored when
the preset is empty; clearing the preset also clears
this field server-side.
    
</dd>
</dl>

<dl>
<dd>

**stt_override:** `typing.Optional[UpdateAgentRequestSttOverride]` 

Streaming-STT stack override. Send an empty string ("") to
clear the override and fall back to the worker default
(today: whisper-v3). Any non-empty value must be a known
stack name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_tools</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tools currently attached to the agent. Bare list — an
agent's tool attachment count is bounded by configuration, so
this endpoint does not paginate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_tools(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">attach_tool</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach an existing tool to the agent so the LLM can call it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.attach_tool(
    id="id",
    tool_id="toolId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">detach_tool</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a tool from the agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.detach_tool(
    id="id",
    tool_id="toolId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">get_evaluation_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the agent's post-call evaluation criteria + data-collection config.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.get_evaluation_config(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">update_evaluation_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the agent's evaluation criteria + data-collection fields.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import DataCollectionField, EvaluationCriterion, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.update_evaluation_config(
    id="id",
    criteria=[
        EvaluationCriterion(
            id="id",
            name="name",
            description="description",
        )
    ],
    data_collection=[
        DataCollectionField(
            key="key",
            description="description",
            type="string",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**criteria:** `typing.Sequence[EvaluationCriterion]` 
    
</dd>
</dl>

<dl>
<dd>

**data_collection:** `typing.Sequence[DataCollectionField]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">get_dynamic_variables</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the agent's customer-scope dynamic variables and the read-only
catalogue of reserved `system__*` keys. The system variables list is
provided so editor UIs can render the reference list without maintaining
a client-side copy of the catalogue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.get_dynamic_variables(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">update_dynamic_variables</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the agent's customer-scope dynamic variable definitions.
The supplied list overwrites the stored list wholesale (same
semantics as `updateEvaluationConfig`). Pass an empty array to
clear all variables. Up to 20 variables per agent. Keys must
match `[a-zA-Z0-9_]+` and must not start with the reserved
`system__` prefix.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import DynamicVariable, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.update_dynamic_variables(
    id="id",
    variables=[
        DynamicVariable(
            key="product_name",
            type="string",
            default="Speechify",
            description="Product the agent is supporting.",
        ),
        DynamicVariable(
            key="support_tier",
            type="number",
            default=1,
        ),
        DynamicVariable(
            key="account_metadata",
            type="json",
            description="Arbitrary account context injected into tool bodies.",
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Sequence[DynamicVariable]` — The new variable list. Replaces the existing list entirely.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_builtins</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every builtin instance configured on this agent. Each row
is one instance of a worker-resident capability (`end_call`,
`play_audio`, etc.) bound to this specific agent with its own
LLM-facing name, description, and per-call config. Same builtin
may appear N times on one agent — typically two `play_audio`
rows bound to different audio assets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_builtins(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">create_builtin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new builtin instance on this agent. `builtin` must
resolve to one of the names returned by
`GET /v1/agents/tools/system-builtins`; unknown values are rejected.
`name` is the LLM-facing identifier the model uses to call the
tool; it must match the tool-name regex and be unique within
the agent's builtin set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.create_builtin(
    id="id",
    builtin="builtin",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**builtin:** `SystemBuiltin` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — LLM-facing tool name. Must match the tool-name regex and be unique within the agent's builtin set.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Per-instance configuration matching the per-builtin schema.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` — Per-call parameter descriptors.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` — Defaults to true on the server when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">get_builtin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch one builtin instance by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.get_builtin(
    id="id",
    builtin_id="builtinId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**builtin_id:** `str` — Agent builtin instance ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">delete_builtin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a builtin instance from this agent. Idempotent on
already-deleted ids (404). Does NOT detach references from
flow nodes that name the instance; the worker logs and skips
on missing-row at session start (fail-soft).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.delete_builtin(
    id="id",
    builtin_id="builtinId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**builtin_id:** `str` — Agent builtin instance ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">update_builtin</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a builtin instance. All fields optional; omitting a
field leaves it unchanged. The underlying `builtin` (which
capability the instance maps to) is intentionally NOT
patchable — change of identity would surprise the worker, so
the customer should delete and recreate instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.update_builtin(
    id="id",
    builtin_id="builtinId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**builtin_id:** `str` — Agent builtin instance ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Per-instance configuration matching the per-builtin schema.
    
</dd>
</dl>

<dl>
<dd>

**params:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` — Per-call parameter descriptors.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">create_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start a new voice conversation with the agent. Returns a realtime
voice session + short-lived client token so the caller can
connect the audio pipeline directly. The agent is dispatched
server-side; no additional client action required.

Pass `dynamic_variables` to supply per-session values that override
the agent's stored variable defaults for this one conversation.
Keys in the `system__` namespace are rejected at this boundary.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.create_conversation(
    id="agent_01HS...",
    dynamic_variables={
        "product_name": "Acme Pro",
        "support_tier": 2,
        "account_metadata": {"plan": "enterprise", "seats": 50},
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[str]` — Transport hint. Omit to use the agent's default.
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Per-session variable overrides that merge on top of the agent's
stored variable defaults for this one conversation. Keys in the
reserved `system__` namespace are rejected. Values must match the
declared type of the corresponding variable definition on the agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">create_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a realtime voice session for the given agent. Widget-friendly
counterpart to `createConversation` — same response shape, dual
authentication:

* **Authenticated (Bearer)**: works for any agent the caller
  owns. Typical server-to-server flow where the embedding
  site's backend mints a token and hands it to the browser so
  the API key never reaches the client.
* **Unauthenticated**: works only when `agent.is_public = true`
  AND the request's `Origin` header matches `agent.allowed_origins`
  (or that list is empty). When `agent.hostname_allowlist` is
  non-empty, the `Origin` hostname must additionally be a
  member of that list. Used directly by the
  `<speechify-agent>` web component.

Responds with the same `CreateConversationResponse` as
`createConversation`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.create_session(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_identity:** `typing.Optional[str]` — Opaque identifier for the end-user (e.g. your app's user ID). Stamped onto the conversation. Optional - defaults to an anonymous per-session ID.
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Per-session variable overrides that merge on top of the agent's
stored variable defaults for this one session. Keys in the
reserved `system__` namespace are rejected at this boundary.
Values must match the declared type of the corresponding variable
definition on the agent (a `string` type expects a JSON string,
`number` expects a JSON number, etc.).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_agent_knowledge_bases</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List knowledge bases attached to an agent. Bare list — the
attachment count is bounded by configuration, not by data
scale, so this endpoint does not paginate.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_agent_knowledge_bases(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">attach_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a knowledge base to an agent. The `search_knowledge` tool
is auto-registered on the next conversation and can only query the
attached knowledge bases.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.attach_knowledge_base(
    id="id",
    kb_id="kbId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kb_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">detach_knowledge_base</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a knowledge base from an agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.detach_knowledge_base(
    id="id",
    kb_id="kbId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kb_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_memories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List per-caller memories extracted for an agent. Memories are
written post-call by the built-in extractor when `memory_enabled`
is true on the agent; the list is sorted newest-first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_memories(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum rows to return. Defaults to 100, capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of rows to skip. Combine with `limit` to page through older memories.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">delete_memories_by_caller</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete every memory ever extracted for a specific caller on
this agent. Privacy / GDPR surface. Returns the count of rows
soft-deleted; rows become permanently unreachable immediately
and are hard-deleted by the retention job after the tenant's
configured retention window.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.delete_memories_by_caller(
    id="id",
    agent_id="agent_id",
    caller_identity="caller_identity",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**caller_identity:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">list_tests</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all tests configured for the agent. Each entry includes the
most recent run so the console can render pass/fail badges without
an extra round-trip.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.list_tests(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">create_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new test for the agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import ParameterCheck, Speechify, ToolCallConfig

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.create_test(
    id="agent_01HS...",
    name="Order lookup by id",
    description="Agent looks up the order id supplied via test variables.",
    type="tool",
    config=ToolCallConfig(
        context="Look up order {{order_id}} for {{customer_name}}",
        expected_tool="lookup_order",
        parameter_checks=[
            ParameterCheck(
                path="order_id",
                mode="exact",
                expected='"{{order_id}}"',
            )
        ],
    ),
    variables={"order_id": "ORD-123", "customer_name": "Alice"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Short human-readable label for the test.
    
</dd>
</dl>

<dl>
<dd>

**type:** `TestType` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateAgentTestRequestConfig` — Type-specific configuration. Must match the shape for the given `type`.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional longer description of what this test verifies.
    
</dd>
</dl>

<dl>
<dd>

**tool_mock_config:** `typing.Optional[ToolMockConfig]` — Optional tool-mocking config applied during every run of this test.
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Per-test variable values substituted into string fields of the
config at run-start. Keys use the same rules as agent-level
`DynamicVariable` keys.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Prefixed wire identifier (`folder_<26 char Crockford base32>`)
of the folder to place the test in. Omit / null for root.
    
</dd>
</dl>

<dl>
<dd>

**attached_agent_ids:** `typing.Optional[typing.Sequence[str]]` 

Optional list of additional agents this test should also run
against. The owner agent (path param) is always attached
implicitly.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">run_all_tests</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueue runs for every test on the agent concurrently. Up to 50
tests are dispatched in one call. Each returned run starts in
`queued` status; poll `GET /v1/agents/tests/runs/{id}` for the terminal
result.

An optional request body runs the whole suite against
a proposed config: a `config_override` (prompt / model / tools)
applied to every test without editing the tests, and/or a
`flow_version_id` to target a specific flow version instead of
the agent's active flow. Omit the body to run against the
agent's live config and active flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.run_all_tests(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Agent ID.
    
</dd>
</dl>

<dl>
<dd>

**config_override:** `typing.Optional[TestRunConfigOverride]` 
    
</dd>
</dl>

<dl>
<dd>

**flow_version_id:** `typing.Optional[str]` 

Targets a specific flow version (an `agent_versions` row)
instead of the agent's active flow — version-targeted
regression. Must be a flow version of the agent under test.
Raw UUID; flow versions carry no prefixed wire id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.<a href="src/speechify/agent/client.py">get_widget_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the embed-widget appearance config for an agent. Works
unauthenticated for public agents; the body is cosmetic only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.get_widget_config(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Tools
<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tools in the caller's workspace, most recently updated
first. Cursor-paginated: omit `cursor` to fetch the first page.
Default page size is 50 and max is 200. Walk pages while
`has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.tools.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max tools per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a tool. For webhook tools, the response includes the HMAC
`webhook_secret` exactly once — store it immediately; subsequent
reads return a masked placeholder.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import ClientToolConfig, Speechify, ToolParam

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.create(
    name="navigate_to",
    description="Scroll the page to a named section.",
    kind="client",
    config=ClientToolConfig(
        timeout_ms=4000,
        params=[
            ToolParam(
                name="section",
                type="string",
                description="Section name",
                required=True,
                enum=["pricing", "docs", "contact"],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**kind:** `ToolKind` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `CreateToolRequestConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a tool by ID. Webhook secrets are always masked here.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a tool. Agents that had it attached get a soft-detach.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a tool. Tool kind is immutable — create a new tool to change it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[UpdateToolRequestConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">list_attached_agents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the agents in the caller's workspace that currently have
this tool attached. Useful before deleting a tool, to surface
which agents will lose access. Soft-deleted agents are filtered
out. Bounded by the number of agents per workspace (tens), so
the response is not paginated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.list_attached_agents(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">rotate_secret</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rotate the HMAC signing secret on a webhook tool. The tool id
is preserved so attached agents keep working; only the secret
rolls. The new plaintext is returned on `webhook_secret`
exactly once — store it immediately, subsequent reads always
return the masked placeholder. The previous secret is
invalidated immediately on success.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.rotate_secret(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">list_system_builtins</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read-only catalogue of every system builtin the worker knows
about. The console fetches this at runtime rather than
maintaining a parallel client-side list; the server
is the single source of truth for the label and description
copy a customer sees in the builtin-instance picker.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.list_system_builtins()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">test_mcp_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Probe a customer-supplied MCP server config without persisting
anything. The server opens the configured transport, runs the
`initialize` + `list_tools` handshake, and returns either the
discovered tool catalogue or a structured error string. Pass
`tool_id` from the edit-form flow when the auth payload carries
`_set` markers but no plaintext, so the server can hydrate the
stored secret from the encrypted column before probing.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import McpAuth_None, McpToolConfig, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.test_mcp_connection(
    config=McpToolConfig(
        endpoint="endpoint",
        auth=McpAuth_None(),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config:** `McpToolConfig` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `typing.Optional[str]` 

Optional `tool_<crockford>` id of the existing tool to hydrate
stored secrets from. Raw UUIDs and other-resource prefixes are
rejected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tools.<a href="src/speechify/agent/tools/client.py">test_webhook_connection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Probe a customer-supplied webhook tool config without persisting
anything. The server fires the exact request shape the worker
sends on a real invocation — same JSON body, same HMAC-SHA256
signature — with an empty argument set, and reports the
endpoint's status code, latency, and a truncated response body,
or a transport-level failure reason. The probe carries an
`X-Speechify-Webhook-Test: true` header so a careful endpoint
can recognise the test and skip its real side effect. Pass
`tool_id` from the edit-form flow so the server signs the probe
with the tool's stored HMAC secret.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify, WebhookToolConfig

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tools.test_webhook_connection(
    config=WebhookToolConfig(
        url="url",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**config:** `WebhookToolConfig` 
    
</dd>
</dl>

<dl>
<dd>

**tool_id:** `typing.Optional[str]` 

Optional `tool_<crockford>` id of the existing tool to sign
the probe with. Raw UUIDs and other-resource prefixes are
rejected.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent AudioAssets
<details><summary><code>client.agent.audio_assets.<a href="src/speechify/agent/audio_assets/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every non-deleted audio asset in the caller's workspace.
Audio assets are pre-recorded WAV clips (intro jingles, legal
disclaimers, hold cues) referenced from `play_audio` flow nodes
and the corresponding system builtin.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.audio_assets.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.audio_assets.<a href="src/speechify/agent/audio_assets/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a new audio asset. The body is a multipart/form-data
request with a single `file` field carrying the WAV bytes.

The WAV is validated server-side against a strict format
contract — PCM 16-bit signed, mono, 48000 Hz, ≤30s, ≤4 MiB —
before any bytes hit storage. The strict shape matches the
LiveKit room sample rate so the worker reads bytes straight
into `rtc.AudioFrame` with no decode dependency on either side;
convert MP3 sources with `ffmpeg -i in.mp3 -ar 48000 -ac 1
-sample_fmt s16 out.wav`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.audio_assets.upload()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.audio_assets.<a href="src/speechify/agent/audio_assets/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch one audio asset's metadata. Returns 404 for missing,
soft-deleted, or foreign-tenant assets — existence information
is never leaked across tenants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.audio_assets.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Audio asset ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.audio_assets.<a href="src/speechify/agent/audio_assets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete an audio asset. The underlying GCS object is
retained so any flow node or tool still referencing the asset
keeps working until the config is updated; the worker logs
and skips on missing-row at session start (fail-soft).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.audio_assets.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Audio asset ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.audio_assets.<a href="src/speechify/agent/audio_assets/client.py">get_bytes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream the raw WAV bytes for an audio asset. Byte-stream
sibling of the metadata endpoint at /v1/agents/audio-assets/{id}.
The LiveKit worker fetches through here for the play_audio
builtin; SDK consumers can also download originals. Returns 404
for missing / soft-deleted / foreign-tenant assets.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.audio_assets.get_bytes(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Audio asset ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent IvrMemory
<details><summary><code>client.agent.ivr_memory.<a href="src/speechify/agent/ivr_memory/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the active IVR menus the caller's workspace has learned.
One row per (fingerprint, tenant).
Invalidated rows and the cross-tenant shared slot are excluded.
Sorted by `last_observed_at` DESC so the freshest IVRs land at
the top. Capped at 200 rows.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.ivr_memory.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**fingerprint:** `typing.Optional[str]` — Optional SHA-256 fingerprint hash to narrow the list to one menu.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.ivr_memory.<a href="src/speechify/agent/ivr_memory/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch one menu's full shape. Returns 404 for missing,
soft-deleted, or foreign-tenant menus — existence information
is never leaked across tenants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.ivr_memory.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — IVR menu ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.ivr_memory.<a href="src/speechify/agent/ivr_memory/client.py">update_label</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-label one option in the stored menu_tree, matched on the
supplied DTMF value. The label is what the console displays in
the detail panel and what the worker reads back at navigate
time to surface the option semantically. Unknown DTMF values
are a no-op (the response echoes the unchanged menu).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.ivr_memory.update_label(
    id="id",
    dtmf="dtmf",
    label="label",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — IVR menu ID.
    
</dd>
</dl>

<dl>
<dd>

**dtmf:** `str` — DTMF value of the option to relabel (e.g. "1", "*", "#").
    
</dd>
</dl>

<dl>
<dd>

**label:** `str` — New label. Capped at 256 chars server-side.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.ivr_memory.<a href="src/speechify/agent/ivr_memory/client.py">invalidate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-invalidate the named menu. Future lookups skip it; the
next discovery for the same fingerprint replaces it (clearing
the invalidation). Idempotent: re-invalidating
an already-invalidated row returns 404.

Reason is optional and is captured in structured logs for
operator triage. A future audit table may persist it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.ivr_memory.invalidate(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — IVR menu ID.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Operator-debug cause string. Bounded to 256 chars.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Callers
<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the workspace's callers, ordered by most-recently-seen first.
A caller is the per-(tenant, agent, identity) entity that owns
long-term memories and conversation history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.callers.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Narrow the list to callers attached to one agent.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` 

Identity-prefix search. Filters to rows where `identity LIKE q + '%'`
(`%`/`_` characters in the input are escaped as literals).
    
</dd>
</dl>

<dl>
<dd>

**last_seen_after:** `typing.Optional[dt.datetime]` 

RFC 3339 timestamp. Narrows to callers active strictly AFTER the
supplied moment. Useful for "active this week / month" filters.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a single caller by id. Returns 404 for soft-deleted or
foreign-tenant rows — GDPR-purged callers appear as "not found"
to the API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.callers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Caller ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete the caller AND cascade soft-delete every memory row
pointing at it. Conversations survive (forensic / billing records)
but their caller pointer surfaces as "deleted" through the API.

Idempotent — re-deleting an already-purged caller returns
`{caller_purged: 0, memories_purged: 0}`. Audit row counts
accompany every response so a privacy operator has direct
evidence of the purge without re-querying.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.callers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Caller ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the customer-editable fields on a caller. PATCH semantics:
omitted fields are unchanged, present fields overwrite. To clear
a nullable field (`display_name`, `external_ref`) pass an empty
string. `metadata` REPLACES the existing JSONB blob when supplied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.callers.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Caller ID.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Operator-editable display name. Empty string clears the column.
    
</dd>
</dl>

<dl>
<dd>

**external_ref:** `typing.Optional[str]` — Optional handle into the customer's own CRM. Empty string clears the column.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Replacement metadata JSONB. Must not be `null`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">list_memories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List one page of memories belonging to the caller, newest first.
Soft-deleted memories AND memories whose parent caller is
soft-deleted are hidden — the GDPR purge semantics require the
API to behave as if those rows do not exist.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.callers.list_memories(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Caller ID.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.callers.<a href="src/speechify/agent/callers/client.py">list_conversations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List one page of conversations belonging to the caller, newest
started first. Same wire envelope as the workspace-wide
`GET /v1/agents/conversations`, narrowed to one caller.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.callers.list_conversations(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Caller ID.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Conversations
<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List conversations owned by the caller, ordered by most recent.
Cursor-paginated: omit `cursor` to fetch the first page; pass the
previous response's `next_cursor` back to fetch the next page.
Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.conversations.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max conversations per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter to conversations for this agent.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConversationStatus]` — Filter by conversation status.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[ConversationTransport]` — Filter by transport.
    
</dd>
</dl>

<dl>
<dd>

**caller_identity:** `typing.Optional[str]` — Filter by caller identity.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Free-text search across conversation content.
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — Only conversations started at or after this RFC 3339 timestamp.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — Only conversations started at or before this RFC 3339 timestamp.
    
</dd>
</dl>

<dl>
<dd>

**duration_min_ms:** `typing.Optional[int]` — Minimum conversation duration in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**duration_max_ms:** `typing.Optional[int]` — Maximum conversation duration in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">stats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregated counts and averages over the caller's conversations, scoped by the same filters as the list endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.conversations.stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Filter to conversations for this agent.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ConversationStatus]` — Filter by conversation status.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[ConversationTransport]` — Filter by transport.
    
</dd>
</dl>

<dl>
<dd>

**caller_identity:** `typing.Optional[str]` — Filter by caller identity.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Free-text search across conversation content.
    
</dd>
</dl>

<dl>
<dd>

**started_after:** `typing.Optional[dt.datetime]` — Only conversations started at or after this RFC 3339 timestamp.
    
</dd>
</dl>

<dl>
<dd>

**started_before:** `typing.Optional[dt.datetime]` — Only conversations started at or before this RFC 3339 timestamp.
    
</dd>
</dl>

<dl>
<dd>

**duration_min_ms:** `typing.Optional[int]` — Minimum conversation duration in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**duration_max_ms:** `typing.Optional[int]` — Maximum conversation duration in milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">recent_callees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Distinct phone numbers the caller's workspace has dialled on
outbound calls, ordered by most recent. Feeds the batch-calls
composer's "Suggested from history" surface. Cursor-paginated:
omit `cursor` to fetch the first page. Default page size is 50
and max is 200. Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.conversations.recent_callees()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of distinct phone numbers per page. Defaults to 50; clamped to 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a conversation by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.conversations.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the transcript for a conversation in started_at order
(oldest first). Cursor-paginated: omit `cursor` to fetch the
first page. Default page size is 50 and max is 200. Walk pages
while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.conversations.list_messages(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max messages per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list_evaluations</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve post-call evaluation results for a conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.conversations.list_evaluations(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">stream_recording</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Proxy the GCS-stored audio recording for a conversation through
the Cloud Run service identity. Returns OGG/Opus bytes (LiveKit
room-composite egress default). The response is streamed so a
long recording does not buffer in memory; `<audio src>` consumers
can seek directly. Only present when the agent had
`save_audio_recording` enabled at session start.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.conversations.stream_recording(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list_webhook_deliveries</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List post-call webhook delivery attempts for a conversation,
newest first. Rows appear once the LiveKit `room_finished`
webhook has fired and the post-call webhook has been
dispatched to the agent's configured URL. One row per
`(conversation, webhook-url)`, updated in place across retries.
Cursor-paginated: omit `cursor` to fetch the first page.
Default page size is 50 and max is 200. Walk pages while
`has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.conversations.list_webhook_deliveries(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max deliveries per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list_retrieval_log</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Per-conversation retrieval log, newest first — one row per
`search_knowledge` invocation made during the call. Each entry
records the query, ranked chunks (denormalised so deletions
don't render history unreadable), `top_k`, and hit count.
Powers the Retrieval panel on the conversation detail view.
Cursor-paginated: omit `cursor` to fetch the first page.
Default page size is 50 and max is 200. Walk pages while
`has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.conversations.list_retrieval_log(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max retrieval log entries per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.conversations.<a href="src/speechify/agent/conversations/client.py">list_memories</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List memories extracted from a specific conversation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.conversations.list_memories(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Admin
<details><summary><code>client.agent.admin.<a href="src/speechify/agent/admin/client.py">shadow_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mint a listen-only LiveKit access token so an authorized observer
can join an ongoing voice-agent conversation as a hidden
participant. Caller must be an `owner` or `admin` of the
workspace the conversation belongs to. The token cannot publish
audio or data; the observer is invisible to the caller and the
agent. Speechify support engineers reach this endpoint the same
way as any other observer — by being granted the owner/admin
role on the customer's workspace (typically under an NDA-backed
support arrangement).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.admin.shadow_token(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.admin.<a href="src/speechify/agent/admin/client.py">force_end</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Force-terminate the LiveKit room for an ongoing conversation.
Idempotent: rooms that LiveKit has already cleaned up return
204 the same as a successful first-time termination. Same
owner/admin role gating as the shadow-token endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.admin.force_end(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent KnowledgeBases
<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List knowledge bases owned by the caller. Cursor-paginated:
omit `cursor` to fetch the first page. The default page size is
50 and the max is 200; values outside that range are clamped.
Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.knowledge_bases.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max knowledge bases per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable label.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a knowledge base by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a knowledge base. Documents and chunks are cascaded.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.update(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List documents ingested into a knowledge base. Cursor-paginated:
omit `cursor` to fetch the first page. Default page size is 50
and max is 200. Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.knowledge_bases.list_documents(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder filter: omit for root-level documents, pass `all` for
every document in the KB, or a folder id to scope to that
folder.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring match on filename and source_url.
    
</dd>
</dl>

<dl>
<dd>

**source_kind:** `typing.Optional[str]` — Comma-separated source kinds (file|url|text).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max documents per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">upload_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a document (PDF, plain text, markdown, or HTML) to a
knowledge base. The document is extracted, chunked, embedded, and
indexed synchronously; expect a few seconds per MB of input.
Maximum 10 MB per upload.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.upload_document(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">get_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a document by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.get_document(
    id="id",
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">delete_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a document and all its chunks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.delete_document(
    id="id",
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">update_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a document. Currently supports moving the document
between folders via `folder_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.update_document(
    id="id",
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Destination folder. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null moves the
document to the knowledge base root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list_chunks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the chunks for a document. Cursor-paginated: omit `cursor`
to fetch the first page. Default page size is 50 and max is 200.
Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.knowledge_bases.list_chunks(
    id="id",
    doc_id="docId",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max chunks per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_text_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a document from inline pasted text. Content is chunked,
embedded, and indexed synchronously.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_text_document(
    id="id",
    name="name",
    content="content",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder to drop the document into. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted = root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_url_document</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a URL via Firecrawl and ingest the rendered content as a
document. The fetch happens synchronously; expect a few
seconds per page. Use the sitemap / crawl endpoints for
multi-page imports.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_url_document(
    id="id",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder to drop the document into. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted = root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_sitemap_import</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Kick off an async sitemap import. Returns 202 with the import
job row; client polls `GET /{id}/imports` for progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_sitemap_import(
    id="id",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder to import the documents into. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted = root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_crawl_import</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Kick off an async website crawl. Returns 202 with the import
job row; client polls `GET /{id}/imports` for progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_crawl_import(
    id="id",
    url="url",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**max_pages:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**max_depth:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder to import the documents into. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted = root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_url_batch_import</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Kick off an async multi-URL import. Accepts 1..N URLs in a
single job (capped per-deployment, default 50) and runs the
same per-URL pipeline as the sitemap worker. Returns 202 with
the import job row; client polls `GET /{id}/imports` for
progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_url_batch_import(
    id="id",
    urls=["urls"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**urls:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Folder to import the documents into. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted = root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list_import_jobs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List import jobs (sitemap / crawl / refresh) for a knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.list_import_jobs(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">cancel_import_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a non-terminal import job. Idempotent on terminal jobs
(completed / failed / cancelled) — the cancel call returns the
unchanged row.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.cancel_import_job(
    id="id",
    import_id="importId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**import_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">batch_delete_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete multiple documents in a single transaction. All ids
must belong to the supplied knowledge base; mismatches fail
the request with 400 before any rows are touched. Capped at
200 ids per call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.batch_delete_documents(
    id="id",
    ids=["ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">batch_move_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move multiple documents into a folder in a single transaction.
Pass `folder_id: null` to move every doc to root. Capped at
200 ids per call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.batch_move_documents(
    id="id",
    ids=["ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ids:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Destination folder. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null moves every
document to the knowledge base root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">update_refresh_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the per-document auto-refresh state. Only meaningful
for url-sourced documents; file and text rows reject the
request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.update_refresh_config(
    id="id",
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**interval_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**auto_remove_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list_refresh_history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List recent auto-refresh attempts for a document.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.list_refresh_history(
    id="id",
    doc_id="docId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**doc_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">list_folders</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List folders inside a knowledge base. Root-level folders have
`parent_folder_id: null`. Cursor-paginated: omit `cursor` to
fetch the first page. Default page size is 50 and max is 200.
The console builds the folder tree from `parent_folder_id`, so
consumers should walk every page until `has_more` is `false`
before rendering the tree.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.knowledge_bases.list_folders(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max folders per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">create_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a folder inside a knowledge base.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.create_folder(
    id="id",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` 

Parent folder. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`); null/omitted creates a
root-level folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">delete_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a folder. Documents inside the folder are moved to root
(not deleted). Sub-folders are detached likewise.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.delete_folder(
    id="id",
    folder_id="folderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` — When true, delete the folder even if it still contains documents or sub-folders; contents are moved to root.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">update_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a folder. Pass `parent_folder_id: null` to move to
root; omit the field to leave it unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.update_folder(
    id="id",
    folder_id="folderId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` 

Folder to reparent under. Prefixed wire identifier
(`kfolder_<26 char Crockford base32>`).
    
</dd>
</dl>

<dl>
<dd>

**clear_parent_folder_id:** `typing.Optional[bool]` 

When `true`, moves the folder to root (clears
`parent_folder_id`). Wins over `parent_folder_id` when both
are sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.knowledge_bases.<a href="src/speechify/agent/knowledge_bases/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Semantic search across a caller-owned list of knowledge bases.
Returns ranked chunks with source filename and a cosine-similarity
score. Limited to 50 results per request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.knowledge_bases.search(
    query="query",
    kb_ids=["kb_ids"],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**query:** `str` — Natural-language search query.
    
</dd>
</dl>

<dl>
<dd>

**kb_ids:** `typing.Sequence[str]` — Knowledge bases to search across. Results scoped to caller-owned entries; unknown IDs are silently ignored.
    
</dd>
</dl>

<dl>
<dd>

**top_k:** `typing.Optional[int]` — Max hits to return (default 5, capped at 50).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Memories
<details><summary><code>client.agent.memories.<a href="src/speechify/agent/memories/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete one memory row.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.memories.delete(
    memory_id="memoryId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**memory_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Tests
<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">get_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a test by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.get_test(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">delete_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a test and all its run history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.delete_test(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">update_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a test. Only fields present on the request body are changed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.update_test(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test ID.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[UpdateAgentTestRequestConfig]` — Replaces the test config when present.
    
</dd>
</dl>

<dl>
<dd>

**tool_mock_config:** `typing.Optional[ToolMockConfig]` — Replaces the tool-mock config when present.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` 

Prefixed wire identifier (`folder_<26 char Crockford base32>`)
of the folder to move the test into.
    
</dd>
</dl>

<dl>
<dd>

**clear_folder_id:** `typing.Optional[bool]` 

When `true`, moves the test back to root (clears
`folder_id`). Wins over `folder_id` when both are sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">list_test_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List one page of run history for a test, newest first.
Paginate by passing `cursor` from the previous response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.tests.list_test_runs(
    id="id",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test ID.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">run_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueue a single run of the test. The returned run starts in
`queued` status. Poll `GET /v1/agents/tests/runs/{id}` until the status
reaches a terminal state (`passed`, `failed`, or `error`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.run_test(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test ID.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Run the test against this agent instead of the test's default agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">get_test_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a single test run by ID. Poll this endpoint until
`status` reaches a terminal state (`passed`, `failed`, or `error`).
The `result` field is populated on terminal states.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.get_test_run(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Test run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">list_suite_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List one page of suite runs (test invocations), newest first.
A suite run groups every test run dispatched by one Run All,
batch, or resubmit call. Paginate by passing `cursor` from the
previous response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.tests.list_suite_runs()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Narrow the list to the suite runs of one agent.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">get_suite_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a suite run by ID with its child runs and the derived
aggregate status and pass/fail/error counts.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.get_suite_run(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Suite run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">resubmit_suite_run</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-run the failed and errored tests of a suite run as a fresh
suite run, linked back to the original via
`parent_suite_run_id`. Returns 400 when the suite run has no
failed or errored tests to re-run.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.resubmit_suite_run(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Suite run ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">list_all_tests</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Workspace-wide list of tests across every agent the caller owns.
Supports filters (agent, type, last-run status, folder), full-text
search on name/description, and cursor pagination. Each row carries
its newest run and attached agent IDs so the list renders without
N+1 round-trips. Walk pages while `has_more` is true.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.tests.list_all_tests()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` — Comma-separated agent IDs to filter on.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — Comma-separated test types (reply|tool|simulation).
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Comma-separated last-run statuses.
    
</dd>
</dl>

<dl>
<dd>

**folder_id:** `typing.Optional[str]` — Folder ID to filter on, or "root" for unfiled tests.
    
</dd>
</dl>

<dl>
<dd>

**updated_after:** `typing.Optional[str]` — Only return tests updated after this RFC3339 timestamp.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring match on name or description.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max tests per page (default 50, max 200).
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque pagination cursor from a previous response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">get_test_stats</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregate pass-rate metrics over the last N days. Returns dense
daily buckets (one entry per day, zero-filled) plus totals and a
per-type breakdown. Powers the header chart on the global tests
page. Default window is 30 days, max 90.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.get_test_stats()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**window_days:** `typing.Optional[int]` — Trailing window in days (default 30, max 90).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">run_tests_batch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue runs for every (test, agent) pair in the body. Entries
without an `agent_id` fan out to every agent the test is
attached to. Total expanded runs are capped at 100 per call.
Each entry in the response is a queued run; poll
`GET /v1/agents/tests/runs/{id}` for each.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import BatchRunEntry, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.run_tests_batch(
    entries=[
        BatchRunEntry(
            test_id="test_01ky612y9cb7dbaj638x46msxv",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entries:** `typing.Sequence[BatchRunEntry]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">list_test_attachments</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every agent a test is attached to.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.list_test_attachments(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">attach_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach a test to an additional agent. After this call, the test
will also run as part of that agent's regression suite (and
against its prompt + tool config when invoked with
`agent_id = {agentId}`). Idempotent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.attach_test(
    id="id",
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">detach_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detach a test from an agent. The owner agent (the agent the test
was authored against) cannot be detached; delete the test
instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.detach_test(
    id="id",
    agent_id="agentId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">list_test_folders</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every test folder the caller owns. Flat list; build the tree client-side.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.list_test_folders()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">create_test_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a test folder. Max depth is 3.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.create_test_folder(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` 

Prefixed wire identifier (`folder_<26 char Crockford base32>`)
of the parent folder. Omit / null for a root-level folder.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">delete_test_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft-delete a folder. Child tests drop back to root.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.delete_test_folder(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.tests.<a href="src/speechify/agent/tests/client.py">update_test_folder</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename or reparent a test folder. Cycles are rejected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.tests.update_test_folder(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**parent_folder_id:** `typing.Optional[str]` 

Prefixed wire identifier (`folder_<26 char Crockford base32>`)
of the folder to reparent this folder under.
    
</dd>
</dl>

<dl>
<dd>

**clear_parent_folder_id:** `typing.Optional[bool]` 

When `true`, reparents this folder to root (clears
`parent_folder_id`). Wins over `parent_folder_id` when
both are sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent PhoneNumbers
<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all phone numbers in the caller's workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">import_</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Import a phone number into the workspace. The `source` field
determines the provisioning path:

- `livekit` - LiveKit purchases the number on your behalf. US
  inbound only. Quickest path for local testing.
- `twilio` - Provide your Twilio Account SID, Auth Token, and
  the E.164 number you already own. We provision an Elastic SIP
  Trunk on your Twilio account automatically.
- `byoc` - Provide an existing SIP trunk ID. The number is
  registered against that trunk.

Returns 402 when the workspace has reached the 100-number cap.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify, TwilioImportSpec

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.import_(
    e164="+12025551234",
    source="twilio",
    label="Support line",
    agent_id="agent_01HS...",
    twilio=TwilioImportSpec(
        account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        auth_token="your_twilio_auth_token",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**e164:** `str` 

The phone number in E.164 format. For `source=livekit` this
is the number you want LiveKit to purchase. For `source=twilio`
and `source=byoc` it is the number you already own.
    
</dd>
</dl>

<dl>
<dd>

**source:** `PhoneNumberSource` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Optional human-readable label.
    
</dd>
</dl>

<dl>
<dd>

**trunk_id:** `typing.Optional[str]` 

For `source=byoc`: the SIP trunk to bind this number to.
Prefixed wire identifier (`trunk_<26 char Crockford base32>`).
Not required for `source=livekit` or `source=twilio`.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 

Optional agent to bind on import. Prefixed wire identifier
(`agent_<26 char Crockford base32>`).
    
</dd>
</dl>

<dl>
<dd>

**twilio:** `typing.Optional[TwilioImportSpec]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">search_available</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search carrier inventory for phone numbers available to purchase.
Currently restricted to the US (`country=US`); pass `area_code`
to narrow to a specific NPA. The returned numbers are not held;
a subsequent `POST /v1/agents/phone-numbers/purchase` against the same
E.164 may fail with 4xx if the number has been taken in the
meantime.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.search_available()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**country:** `typing.Optional[str]` — ISO-3166 alpha-2 country code. Defaults to "US"; only "US" is supported in v1.
    
</dd>
</dl>

<dl>
<dd>

**area_code:** `typing.Optional[str]` — Three-digit NPA to filter inventory to a region.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max results to return. Capped at 50.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">purchase</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purchase a phone number on Speechify's master Twilio account.
The number is billed to Speechify until released. A plan that
includes no purchased numbers (e.g. Free) returns 402; a plan
that has used its full included quota returns 422. This is
independent of the overall 100-number cap.
`e164` must come from a recent `SearchAvailablePhoneNumbers`
response — carriers reject buys against numbers that are no
longer in inventory. The returned phone number is wired for
both inbound (when `agent_id` is set, or after a later
`PATCH`) and outbound calls (via the workspace's shared
outbound trunk).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.purchase(
    e164="+14155552671",
    label="Sales line",
    agent_id="agent_01HS...",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**e164:** `str` — The E.164 number to buy. Must currently be in carrier inventory.
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — Optional human-readable label.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 

Optional agent to bind the number to at purchase time.
Prefixed wire identifier (`agent_<26 char Crockford base32>`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a phone number by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a phone number from the workspace. For Twilio and LiveKit
numbers this also deprovisions the backing SIP trunk and dispatch
rule on LiveKit Cloud.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.phone_numbers.<a href="src/speechify/agent/phone_numbers/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a phone number. Only `label` and `agent_id` are mutable;
`source` and `e164` are immutable after import. Pass `null` for
`agent_id` to unbind the number from its current agent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.phone_numbers.update(
    id="id",
    label="After-hours line",
    agent_id="agent_01HS4X9VBCDEF1234567890AB",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**label:** `typing.Optional[str]` — New label. Pass an empty string to clear.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `typing.Optional[str]` 

Agent to bind the number to. Prefixed wire identifier
(`agent_<26 char Crockford base32>`).
    
</dd>
</dl>

<dl>
<dd>

**clear_agent_id:** `typing.Optional[bool]` 

When `true`, unbinds the current agent (clears `agent_id`).
Wins over `agent_id` when both are sent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent SipTrunks
<details><summary><code>client.agent.sip_trunks.<a href="src/speechify/agent/sip_trunks/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all SIP trunks in the caller's workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.sip_trunks.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.sip_trunks.<a href="src/speechify/agent/sip_trunks/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a SIP trunk. For `kind=byoc` supply `sip_address` plus
optional digest credentials and IP allowlist. For `kind=twilio`
use `ImportPhoneNumber` with a `twilio` spec instead - trunk
creation is handled automatically. Returns 402 when the workspace
has reached the 20-trunk cap.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.sip_trunks.create(
    name="Telnyx BYOC",
    kind="byoc",
    direction="both",
    sip_address="sip.telnyx.com",
    auth_username="myuser",
    auth_password="mypassword",
    transport="auto",
    media_encryption="allow",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable name for the trunk.
    
</dd>
</dl>

<dl>
<dd>

**kind:** `SipTrunkKind` 
    
</dd>
</dl>

<dl>
<dd>

**direction:** `SipTrunkDirection` 
    
</dd>
</dl>

<dl>
<dd>

**sip_address:** `typing.Optional[str]` — SIP endpoint hostname. Required for `kind=byoc`.
    
</dd>
</dl>

<dl>
<dd>

**auth_username:** `typing.Optional[str]` — SIP digest auth username.
    
</dd>
</dl>

<dl>
<dd>

**auth_password:** `typing.Optional[str]` — SIP digest auth password. Write-only.
    
</dd>
</dl>

<dl>
<dd>

**allowed_addresses:** `typing.Optional[typing.Sequence[str]]` — IP / CIDR allowlist for inbound connections. Empty means any source is accepted.
    
</dd>
</dl>

<dl>
<dd>

**destination_country:** `typing.Optional[str]` — ISO 3166-1 alpha-2 country for the outbound dial plan.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[SipTransport]` 
    
</dd>
</dl>

<dl>
<dd>

**media_encryption:** `typing.Optional[SipMediaEncryption]` 
    
</dd>
</dl>

<dl>
<dd>

**credentials:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Provider-specific credential blob (for future extensibility).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.sip_trunks.<a href="src/speechify/agent/sip_trunks/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a SIP trunk by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.sip_trunks.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.sip_trunks.<a href="src/speechify/agent/sip_trunks/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a SIP trunk. This also removes the backing LiveKit inbound
trunk, outbound trunk, and dispatch rule if they were provisioned
by us. Phone numbers attached to this trunk are left in place but
become non-functional until rebound to a new trunk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.sip_trunks.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent OutboundCalls
<details><summary><code>client.agent.outbound_calls.<a href="src/speechify/agent/outbound_calls/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Place an outbound call from an agent to a phone number. LiveKit
originates the SIP INVITE through the outbound trunk bound to the
agent's workspace; the agent worker is dispatched into the room
automatically.

The response is returned as soon as LiveKit accepts the INVITE.
Poll `GET /v1/agents/conversations/{conversation_id}` for status
transitions: `pending` → `active` (answered) → `completed`.

Requires a Twilio or BYOC trunk. LiveKit-native numbers are
inbound-only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.outbound_calls.create(
    agent_id="agent_01HS...",
    to="+41791234567",
    dynamic_variables={
        "customer_name": '"Alice"',
        "order_id": '"ORD-8821"',
        "outstanding_balance": "142.50",
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `str` — ID of the agent that handles the answered call.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Destination phone number in E.164 format (e.g. `+12025559876`).
    
</dd>
</dl>

<dl>
<dd>

**caller_id_number:** `typing.Optional[str]` 

The number shown to the callee as caller ID, in E.164 format.
Defaults to the first outbound-capable number in the workspace.
Useful for multi-number campaigns where you want to rotate
caller IDs.
    
</dd>
</dl>

<dl>
<dd>

**dtmf_prefix:** `typing.Optional[str]` 

DTMF digits dialed automatically after the call is answered,
before the agent begins speaking. Use this for IVR navigation
(e.g. `1ww2` presses 1, waits two seconds, presses 2). `w`
is a half-second pause; `W` is a one-second pause.
    
</dd>
</dl>

<dl>
<dd>

**dynamic_variables:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 

Per-call variable overrides merged on top of the agent's stored
defaults. Keys must not use the reserved `system__` prefix.
Useful for injecting per-call context (customer name, order ID)
into the agent prompt.
    
</dd>
</dl>

<dl>
<dd>

**ringing_timeout_ms:** `typing.Optional[int]` 

How long to wait for the callee to answer before abandoning,
in milliseconds. Defaults to 30000 (30s). Capped at 80000 (80s).
    
</dd>
</dl>

<dl>
<dd>

**amd:** `typing.Optional[AmdConfig]` 

Optional per-call override for the AMD routing config. When
set, wholesale-replaces the agent's stored AMD shape for
this single call (PATCH-replace, not merge). Unlocks the
batch-campaign pattern: one agent dialling many recipients
with per-row tailored voicemail messages via the existing
dynamic_variables substitution. Validation rules match
the agent-update boundary.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent BatchCalls
<details><summary><code>client.agent.batch_calls.<a href="src/speechify/agent/batch_calls/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one page of batch calls for the workspace, newest first.
Paginate by passing `cursor` from the previous response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
response = client.agent.batch_calls.list()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a prior response's `next_cursor`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Page size. Defaults to 50; capped at 200.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.batch_calls.<a href="src/speechify/agent/batch_calls/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Dial a list of phone numbers through one of your voice agents in a
single request. Each recipient can receive personalised dynamic
variables that your agent prompt references via `{{key}}` placeholders.
Batches can run immediately or be scheduled up to 30 days in advance.

Accepts `application/json` or `multipart/form-data` (with a CSV file).
Max 1000 recipients per batch.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from speechify import BatchRecipientRequest, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.batch_calls.create(
    name="Monday morning follow-ups",
    agent_id="agent_01HS...",
    scheduled_at=datetime.datetime.fromisoformat(
        "2025-05-05 09:00:00+00:00",
    ),
    recipients=[
        BatchRecipientRequest(
            phone="+14155551234",
            dynamic_vars={"first_name": "Alice"},
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Human-readable batch name.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — Agent that handles each call.
    
</dd>
</dl>

<dl>
<dd>

**recipients:** `typing.Sequence[BatchRecipientRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**phone_number_id:** `typing.Optional[str]` — Caller-ID override. Falls back to the agent's bound number.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[dt.datetime]` — Schedule the batch for a future time (RFC 3339). Omit to start immediately.
    
</dd>
</dl>

<dl>
<dd>

**ringing_timeout_ms:** `typing.Optional[int]` 

Ringing timeout in milliseconds applied to every call in the
batch (how long each recipient rings before the dial gives
up). Range 1000-80000 (1-80s). Omit to use the 30s default.
The console collects this in seconds and converts to
milliseconds.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.batch_calls.<a href="src/speechify/agent/batch_calls/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the batch row plus all recipients so the detail view renders
without a second round-trip.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.batch_calls.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Batch call ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.batch_calls.<a href="src/speechify/agent/batch_calls/client.py">cancel</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a scheduled or pending batch before it starts dialing.
Returns 409 if the batch is already running or completed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.batch_calls.cancel(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Batch call ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Agent Flow
<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">get_flow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the agent's flow graph: the current draft (if any), the
active published graph (if any), and the version history.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.get_flow(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">update_flow</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace the agent's draft flow graph. The graph is validated
before it is stored; publish it separately to make it active.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.update_flow(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
    nodes=[{"key": "value"}],
    edges=[{"key": "value"}],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**nodes:** `typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**edges:** `typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**variables:** `typing.Optional[typing.Sequence[typing.Dict[str, typing.Optional[typing.Any]]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">discard_draft</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Discard the agent's unpublished draft flow graph.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.discard_draft(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">publish</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish the agent's draft graph as a new active flow version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.publish(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Optional changelog note recorded on the published version.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">rollback</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Publish a prior flow version as the active graph.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.rollback(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
    version_id="9c1e8a40-3b2d-4f6a-8e11-2a7d5c9f0b34",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` — The flow version to roll back to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">deactivate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deactivate the agent's published flow so the agent runs the synthesized default flow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.deactivate(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">list_versions</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every published flow version for the agent, newest first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.list_versions(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">get_version</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the full flow graph for a specific published version.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.get_version(
    id="agent_01k7m6etzwf057j6w0zmdsgppr",
    version_id="9c1e8a40-3b2d-4f6a-8e11-2a7d5c9f0b34",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Prefixed agent id.
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `str` — Flow version UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">get_schema</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return the JSON Schema describing the flow graph node taxonomy.
Unauthenticated; flow editors fetch it to validate graphs client-side.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.get_schema()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">list_templates</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the reusable flow templates available to the workspace.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.list_templates()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">create_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a reusable flow template from a graph.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import FlowGraphInput, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.create_template(
    key="key",
    name="name",
    graph=FlowGraphInput(
        nodes=[{"key": "value"}],
        edges=[{"key": "value"}],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**graph:** `FlowGraphInput` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Defaults to "custom" when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">get_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a flow template by id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.get_template(
    id="3f7b1c20-9d4e-4a18-b6c2-8e0f1a2b3c4d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow template UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">delete_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a flow template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.delete_template(
    id="3f7b1c20-9d4e-4a18-b6c2-8e0f1a2b3c4d",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow template UUID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">update_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace a flow template. The whole template is replaced, not patched field-by-field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import FlowGraphInput, Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.update_template(
    id="3f7b1c20-9d4e-4a18-b6c2-8e0f1a2b3c4d",
    key="key",
    name="name",
    graph=FlowGraphInput(
        nodes=[{"key": "value"}],
        edges=[{"key": "value"}],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow template UUID.
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**graph:** `FlowGraphInput` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[str]` — Defaults to "custom" when omitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.flow.<a href="src/speechify/agent/flow/client.py">clone_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Clone a flow template onto an agent as a new draft graph.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.agent.flow.clone_template(
    id="3f7b1c20-9d4e-4a18-b6c2-8e0f1a2b3c4d",
    agent_id="agent_01k7m6etzwf057j6w0zmdsgppr",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Flow template UUID.
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The agent that receives the cloned graph as a new draft.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tts Audio
<details><summary><code>client.tts.audio.<a href="src/speechify/tts/audio/client.py">speech</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synthesize speech audio from text or SSML. Returns the complete audio
file plus billing and speech-mark metadata in a single response. For
low-latency playback or long-form text, use POST /v1/audio/stream.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.audio.speech(
    audio_format="mp3",
    input="Hello! This is the Speechify text-to-speech API.",
    model="simba-english",
    voice_id="george",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**input:** `str` 

Plain text or SSML to be synthesized to speech.
Refer to https://docs.speechify.ai/docs/api-limits for the input size limits.
Emotion, Pitch and Speed Rate are configured in the ssml input, please refer to the ssml documentation for more information: https://docs.speechify.ai/docs/ssml#prosody
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `str` — Id of the voice to be used for synthesizing speech. Refer to /v1/voices endpoint for available voices
    
</dd>
</dl>

<dl>
<dd>

**audio_format:** `typing.Optional[GetSpeechRequestAudioFormat]` — The format for the output audio. Note, that the current default is "wav", but there's no guarantee it will not change in the future. We recommend always passing the specific param you expect.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 

Language of the input. Follow the format of an ISO 639-1 language code and an ISO 3166-1 region code, separated by a hyphen, e.g. en-US.
Please refer to the list of the supported languages and recommendations regarding this parameter: https://docs.speechify.ai/docs/language-support.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[GetSpeechRequestModel]` — Model used for audio synthesis. `simba-english` is optimized for English, `simba-multilingual` for non-English or mixed input. `simba-3.0` is the streaming-native model with lower TTFB and richer expressivity. Currently English only; multilingual coming soon. Non-English voices return 400 until multilingual support ships.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[GetSpeechOptionsRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.audio.<a href="src/speechify/tts/audio/client.py">stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synthesize speech and stream the audio back as it is generated, for
low-latency playback. The Accept header selects the audio container.
For short text where receiving the whole file at once is fine, use
POST /v1/audio/speech.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.audio.stream(
    accept="audio/mpeg",
    input="input",
    voice_id="voice_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**accept:** `StreamAudioRequestAccept` 
    
</dd>
</dl>

<dl>
<dd>

**input:** `str` 

Plain text or SSML to be synthesized to speech.
Refer to https://docs.speechify.ai/docs/api-limits for the input size limits.
Emotion, Pitch and Speed Rate are configured in the ssml input, please refer to the ssml documentation for more information: https://docs.speechify.ai/docs/ssml#prosody
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `str` — Id of the voice to be used for synthesizing speech. Refer to /v1/voices endpoint for available voices
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 

Language of the input. Follow the format of an ISO 639-1 language code and an ISO 3166-1 region code, separated by a hyphen, e.g. en-US.
Please refer to the list of the supported languages and recommendations regarding this parameter: https://docs.speechify.ai/docs/language-support.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[GetStreamRequestModel]` — Model used for audio synthesis. `simba-english` is optimized for English, `simba-multilingual` for non-English or mixed input. `simba-3.0` is the streaming-native model with lower TTFB and richer expressivity. Currently English only; multilingual coming soon. Non-English voices return 400 until multilingual support ships.
    
</dd>
</dl>

<dl>
<dd>

**options:** `typing.Optional[GetStreamOptionsRequest]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Tts Voices
<details><summary><code>client.tts.voices.<a href="src/speechify/tts/voices/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the list of voices available for the user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.voices.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.voices.<a href="src/speechify/tts/voices/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a personal (cloned) voice for the user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.voices.create(
    name="name",
    gender="male",
    consent="consent",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name of the personal voice
    
</dd>
</dl>

<dl>
<dd>

**gender:** `CreateVoicesRequestGender` 

Gender marker for the personal voice
male GenderMale
female GenderFemale
notSpecified GenderNotSpecified
    
</dd>
</dl>

<dl>
<dd>

**sample:** `from __future__ import annotations

core.File` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**consent:** `str` 

A **string** representing the user consent information in JSON format
This should include the fullName and email of the consenting individual.
For example, `{"fullName": "John Doe", "email": "john@example.com"}`
    
</dd>
</dl>

<dl>
<dd>

**locale:** `typing.Optional[str]` — Native language (locale) of the personal voice (e.g. en-US, es-ES, etc.)
    
</dd>
</dl>

<dl>
<dd>

**avatar:** `from __future__ import annotations

typing.Optional[core.File]` — See core.File for more documentation
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.voices.<a href="src/speechify/tts/voices/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a personal (cloned) voice
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.voices.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the voice to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.voices.<a href="src/speechify/tts/voices/client.py">download_sample</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Download a personal (cloned) voice sample
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.voices.download_sample(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — The ID of the voice to download sample for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

