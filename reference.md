# Reference
## audio
<details><summary><code>client.audio.<a href="src/speechify/audio/client.py">speech</a>(...) -> GetSpeechResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synthesize speech audio from text or SSML. Returns the complete audio
file plus billing and speech-mark metadata in a single JSON response.
For low-latency playback or long-form text, use POST /v1/audio/stream.
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.audio.speech(
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

<details><summary><code>client.audio.<a href="src/speechify/audio/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Synthesize speech and stream the audio back as it is generated, for
low-latency playback. The Accept header selects the audio container;
the response is raw audio bytes (HTTP chunked). For Base64-encoded
audio with speech-mark metadata in a single JSON response, use
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.audio.stream(
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

Selects the audio container/codec for the streamed response. The
response Content-Type echoes this value, except `audio/pcm` returns
`audio/L16` with rate and channels parameters (raw 16-bit linear
PCM, 24 kHz mono, little-endian).
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## voices
<details><summary><code>client.voices.<a href="src/speechify/voices/client.py">list</a>(...) -> ListVoicesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists the voices available to the caller - the shared voice
catalog plus the workspace's personal cloned voices. By default
the full catalogue is returned in one response. Pagination is
opt-in: pass `limit` (and then `cursor` from the previous
response) to page through the list while `has_more` is true. Max
page size is 200.
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.voices.list()

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

**limit:** `typing.Optional[int]` — Max items per page (default 50, max 200).
    
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

<details><summary><code>client.voices.<a href="src/speechify/voices/client.py">create</a>(...) -> GetVoice</code></summary>
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.voices.create(
    sample="example_sample",
    avatar="example_avatar",
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
not_specified GenderNotSpecified
    
</dd>
</dl>

<dl>
<dd>

**sample:** `core.File` — Audio sample file
    
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

**avatar:** `typing.Optional[core.File]` — Avatar image file
    
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

<details><summary><code>client.voices.<a href="src/speechify/voices/client.py">get</a>(...) -> GetVoice</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fetch a single voice by id - a shared catalogue voice or one of
the caller's own personal (cloned) voices. A personal voice that
belongs to another workspace returns 404, identical to an
unknown id, so voice inventory is never enumerable across tenants.
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.voices.get(
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

**voice_id:** `str` — The ID of the voice to fetch
    
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

<details><summary><code>client.voices.<a href="src/speechify/voices/client.py">delete</a>(...)</code></summary>
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.voices.delete(
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

**voice_id:** `str` — The ID of the voice to delete
    
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

<details><summary><code>client.voices.<a href="src/speechify/voices/client.py">download_sample</a>(...) -> typing.Iterator[bytes]</code></summary>
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
from speechify.environment import SpeechifyEnvironment

client = Speechify(
    token="<token>",
    environment=SpeechifyEnvironment.DEFAULT,
)

client.voices.download_sample(
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

**voice_id:** `str` — The ID of the voice to download sample for
    
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

