from player import Player

import time

class SongPlayer(Player):
    SECONDS_IN_ONE_MINUTE = 60

    def __init__(self, bpm, generic_midi_sf2_path, audio_driver):
        self._bpm = bpm
        self._player = Player(generic_midi_sf2_path, audio_driver)

    def play(self, song):
        for (note, instrument) in song:
            if note is None:
                time.sleep(self.SECONDS_IN_ONE_MINUTE / self._bpm)
            else:
                self._player.set_instrument(instrument)
                self._player.play_note(note)
                time.sleep(self.SECONDS_IN_ONE_MINUTE / self._bpm)
