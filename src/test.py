import pygame


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the tick value if needed
        continue


# Replace 'your_audio_file.mp3' with the path to your audio file
audio_file_path = "tmp_speech.mp3"
play_audio(audio_file_path)
