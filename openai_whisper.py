import torch
import whisper
from recording import record_audio, normalize_audio


def transcribe_audio(duration, frequency, audio_language="en", audio_for_whisper=None, model_size="small"):
    if audio_for_whisper is None:
        my_recording = record_audio(duration, frequency)
        audio_for_whisper = normalize_audio(my_recording)

    device = "cuda" if torch.cuda.is_available() else ("mps" if torch.backends.mps.is_available() else "cpu")

    model = whisper.load_model(model_size, device=device)
    result = model.transcribe(audio_for_whisper, language=audio_language, fp16=False, initial_prompt="Transcrição de áudio em português do Brasil com boa pontuação e acentuação.")

    result_text = result["text"]

    return result_text


