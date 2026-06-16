"""Realtime voice-agent session connection (hand-written, .fernignore'd in the real repo).

EXTENDS the Fern-generated SDK without touching generated files: consumes the
`url`/`token` from client.agent.create_conversation(...) / create_session(...) and opens
the realtime media session. The underlying transport is an implementation detail and is
never named in the public surface here.
"""
from __future__ import annotations

import typing

from livekit import rtc as _rtc  # implementation detail; never re-exported

_EVENT_MAP = {
    "participant_joined": "participant_connected",
    "participant_left": "participant_disconnected",
    "audio": "track_subscribed",
    "disconnected": "disconnected",
}


class RealtimeSession:
    def __init__(self, _room: "_rtc.Room") -> None:
        self._room = _room

    @property
    def room_name(self) -> str:
        return self._room.name

    @property
    def connected(self) -> bool:
        return self._room.isconnected()

    @property
    def participant_count(self) -> int:
        return self._room.num_participants

    def on(self, event: str, callback: typing.Callable[..., typing.Any]) -> None:
        mapped = _EVENT_MAP.get(event)
        if mapped is None:
            raise ValueError(f"unknown event {event!r}; supported: {sorted(_EVENT_MAP)}")
        self._room.on(mapped, callback)

    async def disconnect(self) -> None:
        await self._room.disconnect()


async def connect(*, url: str, token: str) -> RealtimeSession:
    room = _rtc.Room()
    await room.connect(url, token)
    return RealtimeSession(room)


async def connect_conversation(response: typing.Any) -> RealtimeSession:
    return await connect(url=response.url, token=response.token)
