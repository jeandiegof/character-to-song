from command import Command
from midi_builder import MidiBuilder
from player import Player
from song import Song

from mingus.containers import Note


class SongBuilder:
    MAXIMUM_VOLUME = 127
    MAXIMUM_VALID_INSTRUMENT = 128
    MAXIMUM_OCTAVE = 7

    DEFAULT_OCTAVE = 5
    DEFAULT_INSTRUMENT = 1
    DEFAULT_VOLUME = 50

    def __init__(self):
        self._current_octave = self.DEFAULT_OCTAVE
        self._current_volume = self.DEFAULT_VOLUME
        self._current_instrument = self.DEFAULT_INSTRUMENT
        self._last_command = None

        self._midi_builder = MidiBuilder()
        self._song = Song()

    def execute(self, command):
        if command is Command.change_instrument:
            self._execute_change_instrument(command.value.data)
        elif command is Command.add_offset_to_current_instrument:
            self._execute_add_offset_to_current_instrument(command.value.data)
        elif command is Command.play_note:
            self._execute_play_note(command.value.data)
        elif command is Command.increase_an_octave:
            self._execute_increase_an_octave()
        elif command is Command.double_volume:
            self._execute_double_volume()
        elif command is Command.repeat_or_pause:
            self._execute_repeat_or_pause()

        self._last_command = command

    def get_resulting_song(self):
        return self._song

    def save_midi_to_file(self, path):
        self._midi_builder.save_midi_to_file(path)

    def _execute_change_instrument(self, instrument):
        self._change_instrument(instrument)

    def _execute_add_offset_to_current_instrument(self, offset):
        target_instrument = self._current_instrument + offset
        new_instrument = target_instrument if target_instrument <= self.MAXIMUM_VALID_INSTRUMENT else self.DEFAULT_INSTRUMENT
        self._change_instrument(new_instrument)

    def _execute_play_note(self, note_str):
        note = Note(note_str, self._current_octave,
                    velocity=self._current_volume)
        self._midi_builder.append_note(note)
        self._song.append(note, self._current_instrument)

    def _execute_increase_an_octave(self):
        target_octave = self._current_octave + 1
        self._current_octave = target_octave if target_octave <= self.MAXIMUM_OCTAVE else self.DEFAULT_OCTAVE

    def _execute_double_volume(self):
        target_volume = self._current_volume * 2
        self._current_volume = target_volume if target_volume <= self.MAXIMUM_VOLUME else self.DEFAULT_VOLUME

    def _execute_repeat_or_pause(self):
        if self._last_command is Command.play_note:
            self._execute_play_note(self._last_command.value.data)
        else:
            self._midi_builder.append_rest()
            self._song.append(None, self._current_instrument)

    def _change_instrument(self, new_instrument):
        self._midi_builder.set_instrument(new_instrument)
        self._current_instrument = new_instrument
