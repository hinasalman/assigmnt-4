import wave
import struct
import math
import os
import random

def create_wave_file(filename, duration, freq, volume=0.5, sample_rate=44100):
    """General function to create wave sounds"""
    if os.path.exists(filename):
        print(f"'{filename}' already exists. Overwriting...")
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sample_rate)

        for i in range(int(sample_rate * duration)):
            value = int(volume * 32767.0 * math.sin(2 * math.pi * freq * (i / sample_rate)))
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

    print(f"'{filename}' file created successfully!")

# Bounce sound — short and high-pitched
def create_bounce_sound():
    freq = 600 + random.randint(-30, 30)  # slight variation
    create_wave_file("bounce.wav", duration=0.2, freq=freq, volume=0.5)

# Score sound — longer and deeper tone
def create_score_sound():
    create_wave_file("score.wav", duration=0.4, freq=400, volume=0.6)

# Game over sound — slow descending sound
def create_game_over_sound():
    filename = "game_over.wav"
    sample_rate = 44100
    duration = 1.0
    start_freq = 800
    end_freq = 200
    if os.path.exists(filename):
        print(f"'{filename}' already exists. Overwriting...")
    with wave.open(filename, 'w') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)

        for i in range(int(sample_rate * duration)):
            # Frequency linearly decreasing
            current_freq = start_freq - (start_freq - end_freq) * (i / (sample_rate * duration))
            value = int(0.5 * 32767.0 * math.sin(2 * math.pi * current_freq * (i / sample_rate)))
            data = struct.pack('<h', value)
            wav_file.writeframesraw(data)

    print(f"'{filename}' file created successfully!")

# Call all sounds
if __name__ == "__main__":
    create_bounce_sound()
    create_score_sound()
    create_game_over_sound()
    print("All sound files created successfully!")