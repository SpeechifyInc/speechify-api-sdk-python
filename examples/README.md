# Examples

## Realtime voice agents — `realtime_wav.py`

Stream audio to a voice agent and save its reply. The SDK exposes the realtime
session as **raw PCM byte streams** (no microphone/speaker — you plumb the audio
yourself) plus **transcript events**:

| Surface | What it does |
|---|---|
| `session.output_audio()` | async iterator of `AudioChunk` (agent PCM16, 48 kHz mono) |
| `session.send_audio(data, sample_rate=, num_channels=)` | push caller PCM16 bytes |
| `session.on_text(cb)` | `cb(TextEvent(role, text, final))` transcript updates |
| `realtime.connect_conversation(resp)` | open the session from a `create_conversation` response |

### Run it end-to-end

```bash
pip install -e .                 # SDK + realtime support (Python 3.9+)
export SPEECHIFY_API_KEY=sk_...

# Use a hosted Speechify audio sample as the caller's voice, converted to PCM16 WAV:
curl -sL https://speechify.ai/audio/multilingual/en.mp3 -o sample.mp3
ffmpeg -i sample.mp3 -ar 48000 -ac 1 -sample_fmt s16 caller.wav

python examples/realtime_wav.py <AGENT_ID> caller.wav agent_reply.wav
```

`caller.wav` is streamed to the agent in real time; the agent's reply is written to
`agent_reply.wav` (PCM16 mono 48 kHz) and transcripts print to stdout as they stream.

Need an agent id? Create one first:

```python
from speechify import Speechify
client = Speechify(token="sk_...")
voices = client.agent.list_agent_voices()
agent = client.agent.create(
    name="Realtime demo",
    voice_id=voices[0].id,
    first_message="Hi! How can I help?",
    prompt="You are a helpful assistant.",
)
print(agent.id)
```

> Audio device capture/playback is intentionally out of scope for the SDK — wire
> `output_audio()` and `send_audio()` to whatever source/sink you need (a telephony
> bridge, a WebSocket, files, or your own capture library).
