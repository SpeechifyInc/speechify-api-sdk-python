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
Refer to https://docs.sws.speechify.com/docs/api-limits for the input size limits.
Emotion, Pitch and Speed Rate are configured in the ssml input, please refer to the ssml documentation for more information: https://docs.sws.speechify.com/docs/ssml#prosody
    
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
Please refer to the list of the supported languages and recommendations regarding this parameter: https://docs.sws.speechify.com/docs/language-support.
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[GetSpeechRequestModel]` — Model used for audio synthesis. `simba-base` and `simba-turbo` are deprecated. Use `simba-english` or `simba-multilingual` instead.
    
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
client.tts.auth.create_access_token()

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

**gender:** `VoicesCreateRequestGender` 

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

