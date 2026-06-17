"""Realtime voice-agent session (hand-written, .fernignore'd).

Connect to a realtime voice-agent session from the ``{ url, token }`` returned by
``client.agent.create_conversation(...)`` / ``create_session(...)``.

This module deliberately does NOT capture a microphone or play to speakers — audio
device handling is the application's job. Instead it exposes the session as raw
PCM byte streams you plumb yourself, plus text (transcript) events:

    from speechify import Speechify, realtime

    client = Speechify(token="...")
    conv = client.agent.create_conversation(agent_id)
    session = await realtime.connect_conversation(conv)

    # transcripts
    session.on_text(lambda ev: print(ev.role, ev.text, ev.final))

    # agent audio out (PCM16, 48kHz mono): pipe to a file/socket/speaker yourself
    async def play():
        async for chunk in session.output_audio():
            your_sink.write(chunk.data)

    # caller audio in (PCM16): push bytes from any source (file/socket/mic lib)
    await session.send_audio(pcm16_bytes)            # sample_rate/num_channels overridable

    await session.disconnect()

The underlying realtime transport client is an internal implementation detail and is
never exposed in the public surface here.
"""
from __future__ import annotations

import asyncio
import dataclasses
import typing

from livekit import rtc as _rtc  # implementation detail; never re-exported

_DEFAULT_SAMPLE_RATE = 48000
_DEFAULT_NUM_CHANNELS = 1
_BYTES_PER_SAMPLE = 2  # PCM signed 16-bit little-endian


@dataclasses.dataclass
class AudioChunk:
    """A chunk of raw audio. ``data`` is PCM signed-16-bit little-endian."""

    data: bytes
    sample_rate: int
    num_channels: int


@dataclasses.dataclass
class TextEvent:
    """A transcript update. ``role`` is ``"agent"`` or ``"caller"``."""

    role: str
    text: str
    final: bool


class RealtimeSession:
    """A live voice-agent session exposed as PCM byte streams + text events."""

    def __init__(self, _room: "_rtc.Room") -> None:
        self._room = _room
        self._out: "asyncio.Queue[typing.Optional[AudioChunk]]" = asyncio.Queue()
        self._text_callbacks: typing.List[typing.Callable[[TextEvent], None]] = []
        self._in_source: typing.Optional["_rtc.AudioSource"] = None
        self._in_lock = asyncio.Lock()
        self._wire_events()

    # -- properties --
    @property
    def connected(self) -> bool:
        return self._room.isconnected()

    @property
    def room_name(self) -> str:
        return self._room.name

    # -- output audio: async-iterate the agent's PCM --
    async def output_audio(self) -> typing.AsyncIterator[AudioChunk]:
        """Yield agent audio as it arrives (PCM16). Ends when the session disconnects."""
        while True:
            chunk = await self._out.get()
            if chunk is None:
                return
            yield chunk

    # -- input audio: push raw PCM to the agent --
    async def send_audio(
        self,
        data: bytes,
        *,
        sample_rate: int = _DEFAULT_SAMPLE_RATE,
        num_channels: int = _DEFAULT_NUM_CHANNELS,
    ) -> None:
        """Send a chunk of caller audio (PCM signed-16-bit little-endian). The first
        call publishes the outbound track; subsequent calls stream frames."""
        async with self._in_lock:
            if self._in_source is None:
                self._in_source = _rtc.AudioSource(sample_rate, num_channels)
                track = _rtc.LocalAudioTrack.create_audio_track("caller", self._in_source)
                await self._room.local_participant.publish_track(
                    track, _rtc.TrackPublishOptions(source=_rtc.TrackSource.SOURCE_MICROPHONE)
                )
        samples_per_channel = len(data) // (_BYTES_PER_SAMPLE * num_channels)
        await self._in_source.capture_frame(
            _rtc.AudioFrame(data, sample_rate, num_channels, samples_per_channel)
        )

    # -- text events: transcripts --
    def on_text(self, callback: typing.Callable[[TextEvent], None]) -> None:
        """Register a callback invoked for each transcript update (caller + agent)."""
        self._text_callbacks.append(callback)

    # -- lifecycle --
    async def disconnect(self) -> None:
        await self._room.disconnect()

    # -- internals --
    def _wire_events(self) -> None:
        @self._room.on("track_subscribed")
        def _on_track(track: typing.Any, publication: typing.Any, participant: typing.Any) -> None:
            if getattr(track, "kind", None) == _rtc.TrackKind.KIND_AUDIO:
                asyncio.create_task(self._pump(track))

        @self._room.on("transcription_received")
        def _on_transcription(*args: typing.Any) -> None:
            segments = args[0] if args else []
            participant = args[1] if len(args) > 1 else None
            local = getattr(self._room, "local_participant", None)
            role = "caller" if participant is not None and participant is local else "agent"
            for seg in segments or []:
                ev = TextEvent(
                    role=role,
                    text=getattr(seg, "text", "") or "",
                    final=bool(getattr(seg, "final", False)),
                )
                for cb in self._text_callbacks:
                    cb(ev)

        @self._room.on("disconnected")
        def _on_disconnected(*_args: typing.Any) -> None:
            self._out.put_nowait(None)

    async def _pump(self, track: typing.Any) -> None:
        stream = _rtc.AudioStream(
            track, sample_rate=_DEFAULT_SAMPLE_RATE, num_channels=_DEFAULT_NUM_CHANNELS
        )
        async for event in stream:
            frame = event.frame
            self._out.put_nowait(
                AudioChunk(bytes(frame.data), frame.sample_rate, frame.num_channels)
            )


async def connect(*, url: str, token: str) -> RealtimeSession:
    """Open a realtime session against the ``url`` + ``token`` from create_conversation."""
    room = _rtc.Room()
    await room.connect(url, token)
    return RealtimeSession(room)


async def connect_conversation(response: typing.Any) -> RealtimeSession:
    """Convenience: connect using a create_conversation/create_session response
    (reads ``.url`` / ``.token``)."""
    return await connect(url=response.url, token=response.token)
