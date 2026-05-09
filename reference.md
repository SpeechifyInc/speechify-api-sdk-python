# Reference
## Tts Audio
<details><summary><code>client.tts.audio.<a href="src/speechify/tts/audio/client.py">speech</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets the speech data for the given input
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

**model:** `typing.Optional[GetSpeechRequestModel]` 

Model used for audio synthesis. `simba-base` and `simba-turbo` are deprecated.
`simba-3.0` is the new streaming-native model with lower TTFB and richer expressivity. Currently English only; multilingual coming soon. Non-English voices return 400 until multilingual support ships.
    
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

Gets the stream speech for the given input
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

**model:** `typing.Optional[GetStreamRequestModel]` 

Model used for audio synthesis. `simba-base` and `simba-turbo` are deprecated.
`simba-3.0` is the new streaming-native model with lower TTFB and richer expressivity. Currently English only; multilingual coming soon. Non-English voices return 400 until multilingual support ships.
    
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

## Tts Auth
<details><summary><code>client.tts.auth.<a href="src/speechify/tts/auth/client.py">create_access_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

WARNING: This endpoint is deprecated. Create a new API token for the logged in user.
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
client.tts.auth.create_access_token(
    grant_type="client_credentials",
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

**grant_type:** `CreateAccessTokenRequestGrantType` — in: body
    
</dd>
</dl>

<dl>
<dd>

**scope:** `typing.Optional[CreateAccessTokenRequestScope]` 

The scope, or a space-delimited list of scopes the token is requested for
in: body
    
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

## Tts Agents
<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list</a>()</code></summary>
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
client.tts.agents.list()

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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">create</a>(...)</code></summary>
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
client.tts.agents.create(
    name="name",
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

**prompt:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**first_message:** `typing.Optional[str]` — Spoken verbatim at session start — no LLM round trip.
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**llm_model:** `typing.Optional[str]` — Optional chat model slug. Leave empty to use the Speechify default.
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

**hostname_allowlist:** `typing.Optional[typing.Sequence[str]]` — Optional per-agent hostname allowlist (see Agent schema).
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get</a>(...)</code></summary>
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
client.tts.agents.get(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a voice agent. Conversations and attached tools remain.
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
client.tts.agents.delete(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">update</a>(...)</code></summary>
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
client.tts.agents.update(
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

**llm_model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**voice_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**temperature:** `typing.Optional[float]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` 
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_tools</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tools currently attached to the agent.
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
client.tts.agents.list_tools(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">attach_tool</a>(...)</code></summary>
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
client.tts.agents.attach_tool(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">detach_tool</a>(...)</code></summary>
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
client.tts.agents.detach_tool(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get_evaluation_config</a>(...)</code></summary>
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
client.tts.agents.get_evaluation_config(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">update_evaluation_config</a>(...)</code></summary>
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
from speechify import Speechify
from speechify.tts import DataCollectionField, EvaluationCriterion

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.agents.update_evaluation_config(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get_dynamic_variables</a>(...)</code></summary>
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
client.tts.agents.get_dynamic_variables(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">update_dynamic_variables</a>(...)</code></summary>
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
from speechify import Speechify
from speechify.tts import DynamicVariable

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.agents.update_dynamic_variables(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">create_conversation</a>(...)</code></summary>
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
client.tts.agents.create_conversation(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">create_session</a>(...)</code></summary>
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
client.tts.agents.create_session(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_agent_knowledge_bases</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List knowledge bases attached to an agent.
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
client.tts.agents.list_agent_knowledge_bases(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">attach_knowledge_base</a>(...)</code></summary>
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
client.tts.agents.attach_knowledge_base(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">detach_knowledge_base</a>(...)</code></summary>
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
client.tts.agents.detach_knowledge_base(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_memories</a>(...)</code></summary>
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
client.tts.agents.list_memories(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">delete_memories_by_caller</a>(...)</code></summary>
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
client.tts.agents.delete_memories_by_caller(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_tests</a>(...)</code></summary>
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
client.tts.agents.list_tests(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">create_test</a>(...)</code></summary>
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
from speechify import Speechify
from speechify.tts import ScenarioConfig

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.agents.create_test(
    id="id",
    name="Greet the caller by name",
    description="Agent should greet the caller using their name when provided.",
    type="scenario",
    config=ScenarioConfig(
        context="The caller says: Hi, I'm Alice.",
        success_criteria="The agent greets Alice by name.",
        success_examples=["Hi Alice! How can I help you today?"],
        failure_examples=["Hello! How can I help you?"],
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

**folder_id:** `typing.Optional[str]` — Folder to place the test in. Omit for root.
    
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">run_all_tests</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueue runs for every test on the agent concurrently. Up to 50
tests are dispatched in one call. Each returned run starts in
`queued` status; poll `GET /v1/test-runs/{id}` for the terminal
result.
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
client.tts.agents.run_all_tests(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get_test</a>(...)</code></summary>
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
client.tts.agents.get_test(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">delete_test</a>(...)</code></summary>
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
client.tts.agents.delete_test(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">update_test</a>(...)</code></summary>
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
client.tts.agents.update_test(
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_test_runs</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the run history for a test, newest first.
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
client.tts.agents.list_test_runs(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">run_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Enqueue a single run of the test. The returned run starts in
`queued` status. Poll `GET /v1/test-runs/{id}` until the status
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
client.tts.agents.run_test(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get_test_run</a>(...)</code></summary>
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
client.tts.agents.get_test_run(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_all_tests</a>(...)</code></summary>
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
N+1 round-trips.
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
client.tts.agents.list_all_tests()

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

**type:** `typing.Optional[str]` — Comma-separated test types (scenario|tool|simulation).
    
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">get_test_stats</a>(...)</code></summary>
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
client.tts.agents.get_test_stats()

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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">run_tests_batch</a>(...)</code></summary>
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
`GET /v1/test-runs/{id}` for each.
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
from speechify.tts import BatchRunEntry

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.agents.run_tests_batch(
    entries=[
        BatchRunEntry(
            test_id="test_id",
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_test_attachments</a>(...)</code></summary>
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
client.tts.agents.list_test_attachments(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">attach_test</a>(...)</code></summary>
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
client.tts.agents.attach_test(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">detach_test</a>(...)</code></summary>
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
client.tts.agents.detach_test(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">move_test</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move a test into a folder. Pass `folder_id: null` for root.
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
client.tts.agents.move_test(
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

**folder_id:** `typing.Optional[str]` 
    
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">list_test_folders</a>()</code></summary>
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
client.tts.agents.list_test_folders()

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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">create_test_folder</a>(...)</code></summary>
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
client.tts.agents.create_test_folder(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">delete_test_folder</a>(...)</code></summary>
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
client.tts.agents.delete_test_folder(
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

<details><summary><code>client.tts.agents.<a href="src/speechify/tts/agents/client.py">update_test_folder</a>(...)</code></summary>
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
client.tts.agents.update_test_folder(
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

## Tts Tools
<details><summary><code>client.tts.tools.<a href="src/speechify/tts/tools/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List tools owned by the caller.
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
client.tts.tools.list()

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

<details><summary><code>client.tts.tools.<a href="src/speechify/tts/tools/client.py">create</a>(...)</code></summary>
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
from speechify import Speechify
from speechify.tts import SystemToolConfig

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.tools.create(
    name="name",
    description="description",
    kind="system",
    config=SystemToolConfig(
        builtin="end_call",
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

<details><summary><code>client.tts.tools.<a href="src/speechify/tts/tools/client.py">get</a>(...)</code></summary>
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
client.tts.tools.get(
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

<details><summary><code>client.tts.tools.<a href="src/speechify/tts/tools/client.py">delete</a>(...)</code></summary>
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
client.tts.tools.delete(
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

<details><summary><code>client.tts.tools.<a href="src/speechify/tts/tools/client.py">update</a>(...)</code></summary>
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
client.tts.tools.update(
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

## Tts Conversations
<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List conversations owned by the caller, ordered by most recent.
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
client.tts.conversations.list()

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

<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">stats</a>()</code></summary>
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
client.tts.conversations.stats()

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

<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">get</a>(...)</code></summary>
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
client.tts.conversations.get(
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

<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">list_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the full transcript for a conversation, in order.
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
client.tts.conversations.list_messages(
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

<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">list_evaluations</a>(...)</code></summary>
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
client.tts.conversations.list_evaluations(
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

<details><summary><code>client.tts.conversations.<a href="src/speechify/tts/conversations/client.py">list_memories</a>(...)</code></summary>
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
client.tts.conversations.list_memories(
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

## Tts KnowledgeBases
<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List knowledge bases owned by the caller.
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
client.tts.knowledge_bases.list()

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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">create</a>(...)</code></summary>
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
client.tts.knowledge_bases.create(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">get</a>(...)</code></summary>
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
client.tts.knowledge_bases.get(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">delete</a>(...)</code></summary>
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
client.tts.knowledge_bases.delete(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">update</a>(...)</code></summary>
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
client.tts.knowledge_bases.update(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">list_documents</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List documents ingested into a knowledge base.
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
client.tts.knowledge_bases.list_documents(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">upload_document</a>(...)</code></summary>
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
client.tts.knowledge_bases.upload_document(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">get_document</a>(...)</code></summary>
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
client.tts.knowledge_bases.get_document(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">delete_document</a>(...)</code></summary>
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
client.tts.knowledge_bases.delete_document(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">list_chunks</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List the chunks for a document.
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
client.tts.knowledge_bases.list_chunks(
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

<details><summary><code>client.tts.knowledge_bases.<a href="src/speechify/tts/knowledge_bases/client.py">search</a>(...)</code></summary>
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
client.tts.knowledge_bases.search(
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

## Tts Memories
<details><summary><code>client.tts.memories.<a href="src/speechify/tts/memories/client.py">delete</a>(...)</code></summary>
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
client.tts.memories.delete(
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

## Tts PhoneNumbers
<details><summary><code>client.tts.phone_numbers.<a href="src/speechify/tts/phone_numbers/client.py">list</a>()</code></summary>
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
client.tts.phone_numbers.list()

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

<details><summary><code>client.tts.phone_numbers.<a href="src/speechify/tts/phone_numbers/client.py">import_</a>(...)</code></summary>
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
from speechify import Speechify

client = Speechify(
    token="YOUR_TOKEN",
)
client.tts.phone_numbers.import_(
    request={"key": "value"},
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

**request:** `typing.Optional[typing.Any]` 
    
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

<details><summary><code>client.tts.phone_numbers.<a href="src/speechify/tts/phone_numbers/client.py">get</a>(...)</code></summary>
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
client.tts.phone_numbers.get(
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

<details><summary><code>client.tts.phone_numbers.<a href="src/speechify/tts/phone_numbers/client.py">delete</a>(...)</code></summary>
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
client.tts.phone_numbers.delete(
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

<details><summary><code>client.tts.phone_numbers.<a href="src/speechify/tts/phone_numbers/client.py">update</a>(...)</code></summary>
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
client.tts.phone_numbers.update(
    id="id",
    request={"key": "value"},
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

**request:** `typing.Optional[typing.Any]` 
    
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

## Tts SipTrunks
<details><summary><code>client.tts.sip_trunks.<a href="src/speechify/tts/sip_trunks/client.py">list</a>()</code></summary>
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
client.tts.sip_trunks.list()

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

<details><summary><code>client.tts.sip_trunks.<a href="src/speechify/tts/sip_trunks/client.py">create</a>(...)</code></summary>
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
client.tts.sip_trunks.create(
    request={"key": "value"},
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

**request:** `typing.Optional[typing.Any]` 
    
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

<details><summary><code>client.tts.sip_trunks.<a href="src/speechify/tts/sip_trunks/client.py">get</a>(...)</code></summary>
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
client.tts.sip_trunks.get(
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

<details><summary><code>client.tts.sip_trunks.<a href="src/speechify/tts/sip_trunks/client.py">delete</a>(...)</code></summary>
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
client.tts.sip_trunks.delete(
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

## Tts OutboundCalls
<details><summary><code>client.tts.outbound_calls.<a href="src/speechify/tts/outbound_calls/client.py">create</a>(...)</code></summary>
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
Poll `GET /v1/conversations/{conversation_id}` for status
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
client.tts.outbound_calls.create(
    request={"key": "value"},
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

**request:** `typing.Optional[typing.Any]` 
    
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

## Tts Workspaces
<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every workspace the authenticated user belongs to. Powers the workspace switcher.
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
client.tts.workspaces.list()

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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new workspace with the authenticated user as owner.
The caller must switch their active workspace client-side via
the `X-Tenant-ID` header to act on the new tenant.
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
client.tts.workspaces.create()

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

**name:** `typing.Optional[str]` — Display name for the new workspace. Trimmed; must be 120 characters or fewer.
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">get_current</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the workspace currently selected by the caller (via `X-Tenant-ID` or auto-resolved).
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
client.tts.workspaces.get_current()

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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">update_current</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rename the current workspace. Owner or admin only.
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
client.tts.workspaces.update_current(
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

**name:** `str` — New display name. Required; must be 120 characters or fewer.
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">list_members</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List every member of the current workspace. Any member may call this.
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
client.tts.workspaces.list_members()

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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">leave</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the authenticated caller from the current workspace.
Refused with 409 when the caller is the last owner — promote
another member to owner first.
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
client.tts.workspaces.leave()

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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">remove_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove a member from the current workspace. Owner or admin
only. The caller cannot remove themselves — use
`POST /v1/tenants/current/members/leave` instead.
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
client.tts.workspaces.remove_member(
    user_uid="user_uid",
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

**user_uid:** `str` 
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">update_member_role</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Change a member's role. Owner only — admins may add or remove
members but may not change roles. Refused with 409 when
demoting the last remaining owner.
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
client.tts.workspaces.update_member_role(
    user_uid="user_uid",
    role="owner",
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

**user_uid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**role:** `MemberRole` 
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">list_invites</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List outstanding invites for the current workspace. Invite tokens are redacted.
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
client.tts.workspaces.list_invites()

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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">create_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an invite to the current workspace. Owner or admin only.
The response contains the invite token ONCE — subsequent list
calls redact it.
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
client.tts.workspaces.create_invite(
    email="email",
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

**email:** `str` — Email of the person to invite. Validated as an RFC 5322 address.
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">revoke_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Revoke an outstanding invite. Owner or admin only. Idempotent.
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
client.tts.workspaces.revoke_invite(
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">accept_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Accept a workspace invite. The authenticated caller is joined
to the invite's workspace as a member. Expired, revoked, or
already-accepted tokens return 404 to avoid token enumeration.
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
client.tts.workspaces.accept_invite(
    token="token",
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

**token:** `str` 
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">preview_invite</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Preview a workspace invite without authenticating. Returns the
workspace name, inviter details, and expiry so the `/join/{token}`
page can render before the recipient signs in. Anyone with the
token can already accept, so this endpoint deliberately surfaces
the same information a caller would see after accepting. Invalid
tokens (unknown, expired, revoked, already-accepted, or pointing
at a soft-deleted workspace) collapse to a single 404 to prevent
enumeration.
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
client.tts.workspaces.preview_invite(
    token="token",
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

**token:** `str` 
    
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

<details><summary><code>client.tts.workspaces.<a href="src/speechify/tts/workspaces/client.py">transfer_workspace_owner</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Transfer ownership of the current workspace atomically. Promotes
the target member to owner and demotes the caller to admin in a
single transaction. Owner-only; admins cannot hand off a role
they were never granted. Prefer this over two PATCH calls to
`/v1/tenants/current/members/{user_uid}`: a sole-owner caller
cannot demote themselves first without tripping the last-owner
guard, which this endpoint sidesteps by promoting before
demoting.
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
client.tts.workspaces.transfer_workspace_owner(
    user_uid="user_uid",
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

**user_uid:** `str` — Firebase UID of the member who will become the new owner.
    
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

