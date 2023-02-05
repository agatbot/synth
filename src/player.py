from playsound import playsound


class PlaysoundPlayer:
    def play(self, audio_path: str):
        playsound(audio_path)
