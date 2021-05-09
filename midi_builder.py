from mingus.containers.instrument import MidiInstrument
from mingus.containers import Bar, Track
from mingus.midi import midi_file_out

class MidiBuilder:
    def __init__(self):
        self._instrument = MidiInstrument()
        self._track = Track(self._instrument)
        self._bar = Bar()

    def append_note(self, note):
        if self._bar.is_full():
            self._add_bar_to_track()
        
        self._bar.place_notes(note, 4)

    def append_rest(self):
        if self._bar.is_full():
            self._add_bar_to_track()
        
        self._bar.place_rest(4)

    def get_track(self):
        return self._track + self._bar

    def set_instrument(self, generic_midi_id):
        self._instrument.midi_instr = generic_midi_id

    def _add_bar_to_track(self):
        self._track = self._track + self._bar
        self._bar = Bar()

    def save_midi_to_file(self, path):
        midi_file_out.write_Track(path, self.get_track(), bpm=120, repeat=0, verbose=False)
