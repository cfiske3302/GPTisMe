#!/usr/bin/env python
from pathlib import Path

# from playsound import playsound
# from pydub import AudioSegment
# from pydub.playback import play
import pygame
import time
import sounddevice as sd
from scipy.io.wavfile import write
import pygame
from openai import OpenAI
import os


class openAI_Interface:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.messages = [
            {
                "role": "system",
                "content": "You are DnD dungeon master who has charming wit. Reply only with what a DnD dungeon master would say, so don't include any extraneous intro messages.",
            }
        ]

    def query(self, message):
        self.messages.append(
            {"role": "user", "content": message},
        )
        chat = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=self.messages
        )
        reply = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return reply

    def say(self, message, buf_path=None):
        if buf_path == None:
            buf_path = Path(__file__).parent / "tmp_speech.mp3"
        response = self.client.audio.speech.create(
            model="tts-1", voice="onyx", input=message
        )
        print(buf_path)
        response.stream_to_file(buf_path)
        pygame.mixer.init()
        pygame.mixer.music.load(buf_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Adjust the tick value if needed
            continue
