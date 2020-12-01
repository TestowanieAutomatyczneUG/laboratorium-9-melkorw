from Play import Play


class Checker:
    def __init__(self):
        self.play = Play()

    def remainder(self, file):
        hour = self.play.get_time()
        if int(hour) > 17:
            self.play.play_wav_file(file)

    def was_played(self, file):
        result = self.play.wav_was_played(file)
        self.play.reset_wav(file)
        return result
