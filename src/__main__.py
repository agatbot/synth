import os
from player import PlaysoundPlayer
from text_source import StdinTextSource
from tts import GttsService


class Synthesizer:
    def __init__(self, text_source, tts_service, player):
        self.text_source = text_source
        self.tts_service = tts_service
        self.player = player
    
    def run(self):
        while self.text_source.has_next():
            text = self.text_source.next()
            try:
                self.tts_service.save_text_as_sound(text, 'tmp.mp3')
                self.player.play('tmp.mp3')
            except:
                print('Something went wrong. Please try again.')
        
        os.remove('tmp.mp3')


if __name__ == '__main__':
    synthesizer = Synthesizer(StdinTextSource(), GttsService(), PlaysoundPlayer())
    synthesizer.run()