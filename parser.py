from command import Command


class Parser:
    _change_instrument_symbols = [
        'O', 'o', 'I', 'i', 'U', 'u', '\n', ';', ',', '!']
    _notes_symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _increase_an_octave_symbol = ['?']
    _double_volume_symbol = [' ']
    _character_to_instrument_id = {
        'o': 7,
        'i': 7,
        'u': 7,
        '\n': 15,
        ';': 76,
        ',': 20,
        '!': 114
    }

    def parse(self, character):
        if character.isdigit():
            return self._parse_add_offset_to_current_instrument_symbol(caracter)
        if character in self._change_instrument_symbols:
            return self._parse_change_instrument_symbol(character)
        elif character in self._notes_symbols:
            return self._parse_note_symbol(character)
        elif character in self._increase_an_octave_symbol:
            return self._parse_increase_an_octave_symbol()
        elif character in self._double_volume_symbol:
            return self._parse_double_volume_symbol()
        else:
            return self._parse_repeat_or_pause_symbol()

    def _parse_add_offset_to_current_instrument_symbol(self, offset):
        return Command.add_offset_to_current_instrument(offset)

    def _parse_change_instrument_symbol(self, character):
        instrument = self._character_to_instrument(character)
        command = Command.change_instrument
        self._set_command_data(command, instrument)

        return command

    def _parse_note_symbol(self, character):
        command = Command.play_note
        self._set_command_data(command, character)
        return command

    def _parse_repeat_or_pause_symbol(self):
        return Command.repeat_or_pause

    def _parse_increase_an_octave_symbol(self):
        return Command.increase_an_octave

    def _parse_double_volume_symbol(self):
        return Command.double_volume

    def _character_to_instrument(self, character):
        return self._character_to_instrument_id[character.lower()]

    def _set_command_data(self, command, data):
        command.value.data = data


def debug():
    music = ['O', 'o', 'I', 'i', 'U', 'u', '\n', ';', ',', '!']
    music = music + ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    music = music + ['?']
    music = music + [' ']
    music = music + ['#', '#', '#']

    parser = Parser()

    for char in music:
        result = parser.parse(char)
        if result is not Command.repeat_or_pause and result is not Command.increase_an_octave and result is not Command.double_volume:
            print(char + '\t' + result.name + ' ' + str(result.value.data))
        else:
            print(char + '\t' + result.name)


if __name__ == '__main__':
    debug()
