import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import keyboard
import os

# Set the sampling frequency
fs = 44100  # You can adjust this based on your preferences

# Set the file name for the WAV file
output_file = "recorded_audio.wav"

# Initialize variables for recording
recording = False
audio_data = []

print(
    "Press and hold the space bar to start recording. Release the space bar to stop recording."
)

# Record audio while the space bar is pressed
with sd.InputStream(samplerate=fs, channels=1, dtype="int16") as stream:
    while True:
        if keyboard.is_pressed("space"):
            if not recording:
                print("Space bar pressed. Recording audio...")
                recording = True
                audio_data = []

            audio_chunk, overflowed = stream.read(fs)
            audio_data.append(audio_chunk)
        elif recording:
            print("Space bar released. Stopping recording...")
            break

# Concatenate the recorded audio chunks
full_audio = np.concatenate(audio_data, axis=0)

# Save the recorded audio to a WAV file
write(output_file, fs, full_audio)

print(f"Audio saved as {output_file}. Exiting.")
