import ollama
from openai_whisper import transcribe_audio
from recording import get_text, get_text2


def response_text(duration, frequency, model='zarigata/Qwen2.5-0.5B-Instruct:CRAZYMODE'):

    audio_transcription = transcribe_audio(duration, frequency)
    print("Transcribed Audio:", audio_transcription)

    result = ollama.generate(model=model, prompt=audio_transcription + "\n\nBe direct and concise in your answer, only with direct text. I will use your answer to generate a voice response.")
    return result['response']


def response_AI(model='zarigata/Qwen2.5-0.5B-Instruct:CRAZYMODE'):

    audio_transcription = get_text2()

    result = ollama.generate(model=model, prompt=audio_transcription + "\n\nBe direct and concise in your answer, only with direct text. I will use your answer to generate a voice response.")
    return result['response']