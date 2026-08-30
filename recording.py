import sounddevice as sd
import numpy as np


def record_audio(duration, fs=16000):

    print(f"Recording for {duration} seconds at {fs} Hz...")
    my_recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")

    return my_recording



def find_max_amplitude(x):

    max_val = np.abs(x).max()
    return max_val



def normalize_audio(x, target_peak=0.95):
    
    
    x_flat = x.flatten()

    max_val = find_max_amplitude(x_flat)

    if max_val > 0:
        return (x_flat/max_val) * target_peak
    
    return x_flat
