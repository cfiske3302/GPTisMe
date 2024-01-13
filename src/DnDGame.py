from OpenAIInterface import openAI_Interface
import json
import sounddevice as sd
from scipy.io.wavfile import write
import keyboard


class DnDGame:
    def __init__(self, api_key, prompts_file_path, audio_freq=44100):
        self.oaint = openAI_Interface(api_key)
        f = open(prompts_file_path)
        self.prompts = json.load(f)
        self.fs = audio_freq

    def get_game_log(self):
        return self.oaint.messages

    def start_game(self, prompt=None):
        self.oaint.say(self.prompts["party_promps"])
        party = self.get_audio_input()[-1]
        if self.check_finished(party):
            self.oaint.say(self.prompts["closing_remark"])
            return 1
        # add loading signal
        if prompt is not None:
            response = self.oaint.query(prompt)
        else:
            response = self.oaint.query(
                self.prompts["initial_prompt_p1"]
                + party
                + self.prompts["initial_prompt_p2"]
            )
        self.oaint.say(response)
        self.game_loop()

    def check_finished(self, response):
        done = True
        response = response.lower()
        for i in ["great", "and", "powerful", "skull", "finished", "playing"]:
            done = False if i not in response else True
        return done

    def game_loop(self):
        while True:
            player_response = self.get_audio_input()[-1]
            if self.check_finished(player_response):
                self.oaint.say(self.prompts["closing_remark"])
                return 1
            response = self.oaint.query(player_response)
            self.oaint.say(response)

    # returns filepath, transcription
    def get_audio_input(self):
        # TODO
        transcript = input(">> ")
        filepath = ""
        return filepath, transcript
