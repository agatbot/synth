from gtts import gTTS


class GttsService:
    def save_text_as_sound(self, text: str, path: str):
        audio = gTTS(text=text, lang="pl")
        audio.save(path)
