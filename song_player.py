from player import Player

import time


class SongPlayer(Player):
    SECONDS_IN_ONE_MINUTE = 60

    def __init__(self, bpm, generic_midi_sf2_path, audio_driver):
        super().__init__(generic_midi_sf2_path, audio_driver)
        self._bpm = bpm

    def play(self, song):
        for (note, instrument) in song.notes():
            if note is not None:
                self.set_instrument(instrument)
                self.play_note(note)

            time.sleep(self.beat_duration())

    def beat_duration(self):
        return self.SECONDS_IN_ONE_MINUTE / self._bpm
