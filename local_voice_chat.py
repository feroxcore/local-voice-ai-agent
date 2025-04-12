from fastrtc import ReplyOnPause, Stream, get_stt_model, get_tts_model
from ollama import chat

stt_model = get_stt_model()  # moonshine/base
tts_model = get_tts_model()  # kokoro


def echo(audio):
    transcript = stt_model.stt(audio)
    response = chat(
        model="gemma3:1b", messages=[{"role": "user", "content": transcript}]
    )
    response_text = response["message"]["content"]
    for audio_chunk in tts_model.stream_tts_sync(response_text):
        yield audio_chunk


stream = Stream(ReplyOnPause(echo), modality="audio", mode="send-receive")
stream.ui.launch()
