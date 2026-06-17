"""End-to-end realtime example: stream a WAV file to a voice agent, save its reply.

The SDK does not touch any audio device — it exposes the session as raw PCM byte
streams. This example wires those streams to WAV files so it runs anywhere.

Usage:
    export SPEECHIFY_API_KEY=sk_...
    python examples/realtime_wav.py <AGENT_ID> caller.wav agent_reply.wav

    caller.wav        PCM16 WAV sent as the caller's audio (any sample rate / channels).
    agent_reply.wav   the agent's audio, written as PCM16 mono 48 kHz.

Transcripts (caller + agent) print to stdout as they stream.
"""
import asyncio
import os
import sys
import wave

from speechify import Speechify, realtime

OUTPUT_SAMPLE_RATE = 48000  # output_audio() yields 48 kHz mono PCM16
FRAME_MS = 20               # send the caller WAV in 20 ms frames, paced to real time


async def run(agent_id: str, caller_wav: str, agent_reply_wav: str) -> None:
    client = Speechify(token=os.environ["SPEECHIFY_API_KEY"])

    # Open a realtime conversation and connect to the returned endpoint.
    conversation = client.agent.create_conversation(agent_id)
    session = await realtime.connect_conversation(conversation)
    print(f"connected to {session.room_name}")

    # Print transcripts as they arrive.
    session.on_text(
        lambda ev: print(f"[{ev.role}] {ev.text}" + (" (final)" if ev.final else ""))
    )

    # Agent audio out -> WAV file.
    out = wave.open(agent_reply_wav, "wb")
    out.setnchannels(1)
    out.setsampwidth(2)  # PCM16
    out.setframerate(OUTPUT_SAMPLE_RATE)

    async def save_agent_audio() -> None:
        async for chunk in session.output_audio():
            out.writeframes(chunk.data)

    # Caller audio in <- WAV file, streamed in real time.
    async def stream_caller_wav() -> None:
        wf = wave.open(caller_wav, "rb")
        if wf.getsampwidth() != 2:
            raise ValueError("caller.wav must be PCM signed 16-bit")
        rate, channels = wf.getframerate(), wf.getnchannels()
        frames_per_chunk = int(rate * FRAME_MS / 1000)
        while True:
            data = wf.readframes(frames_per_chunk)
            if not data:
                break
            await session.send_audio(data, sample_rate=rate, num_channels=channels)
            await asyncio.sleep(FRAME_MS / 1000)  # pace to real time
        wf.close()

    saver = asyncio.create_task(save_agent_audio())
    await stream_caller_wav()
    await asyncio.sleep(5)  # let the agent finish replying
    await session.disconnect()
    try:
        await asyncio.wait_for(saver, timeout=3)
    except asyncio.TimeoutError:
        saver.cancel()
    out.close()
    print(f"saved agent reply -> {agent_reply_wav}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    asyncio.run(run(sys.argv[1], sys.argv[2], sys.argv[3]))
