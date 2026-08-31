from kokoro import KPipeline
#from IPython.display import display, Audio
import soundfile as sf
import torch
from AI_call import response_text, response_AI
import sounddevice as sd


def tts_kokoro(duration, frequency, lang_code='a', voice='af_heart'):

    recording_text = response_text(duration, frequency)
    
    pipeline = KPipeline(lang_code=lang_code)
    text = recording_text   

    generator = pipeline(text, voice=voice)
    for i, (gs, ps, audio) in enumerate(generator):

        #print(i, gs, ps)
        #display(Audio(data=audio, rate=24000, autoplay=i==0))
        #sf.write(f'{i}.wav', audio, 24000)

        sd.play(audio, samplerate=24000)
        sd.wait()


#freq = 16000
#duration = 7

#tts_kokoro(duration, freq)


def kokoro(lang_code='a', voice='af_heart'):
    pipeline = KPipeline(lang_code=lang_code)
    text = response_AI()   

    generator = pipeline(text, voice=voice)
    for i, (gs, ps, audio) in enumerate(generator):

        #print(i, gs, ps)
        #display(Audio(data=audio, rate=24000, autoplay=i==0))
        #sf.write(f'{i}.wav', audio, 24000)

        sd.play(audio, samplerate=24000)
        sd.wait()


kokoro()





    
    
