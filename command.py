from enum import Enum, unique


class GenericCommand:
    data = None


class ChangeInstrument(GenericCommand):
    pass


class AddOffsetToCurrentInstrument(GenericCommand):
    pass


class PlayNote(GenericCommand):
    pass


@unique
class Command(Enum):
    change_instrument = ChangeInstrument()
    add_offset_to_current_instrument = AddOffsetToCurrentInstrument()
    play_note = PlayNote()
    increase_an_octave = 1
    double_volume = 2
    repeat_or_pause = 3
