from command import Command


class Parser:
    _control_chars = ['O', 'o', 'I', 'i', 'U', 'u', '\n', ';', ',', '!']
    _notes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    _question_mark = ['?']
    _space_bar = [' ']

    def parse(self, character):
        if character in self._control_chars or character.isdigit():
            return self._parse_control_char(character)
        elif character in self._notes:
            return self._parse_note_char(character)
        elif character in self._question_mark:
            return self._parse_question_mark()
        elif character in self._space_bar:
            return self._parse_space_bar()
        else:
            return self._parse_other_char(character)

    def _parse_control_char(self, character):
        command = Command.control
        self._set_command_symbol(command, character)
        return command

    def _parse_note_char(self, character):
        command = Command.note
        self._set_command_symbol(command, character)
        return command

    def _parse_other_char(self, character):
        command = Command.other
        self._set_command_symbol(command, character)
        return command

    def _parse_question_mark(self):
        command = Command.question_mark
        return command

    def _parse_space_bar(self):
        command = Command.space_bar
        return command

    def _set_command_symbol(self, command, character):
        command.value.symbol = character


def debug():
    music = ['O', 'o', 'I', 'i', 'U', 'u', '\n', ';', ',', '!']
    music = music + ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    music = music + ['?']
    music = music + [' ']
    music = music + ['#', '#', '#']

    parser = Parser()

    for char in music:
        result = parser.parse(char)
        if result is not Command.question_mark and result is not Command.space_bar:
            print(result.name + ' ' + result.value.symbol)
        else:
            print(result.name)

if __name__ == '__main__':
    debug()