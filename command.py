from enum import Enum


class GenericCommand:
    symbol = None


class Control(GenericCommand):
    pass


class Note(GenericCommand):
    pass


class Other(GenericCommand):
    pass


class QuestionMark:
    pass


class SpaceBar:
    pass


class Command(Enum):
    control = Control()
    note = Note()
    question_mark = QuestionMark()
    space_bar = SpaceBar()
    other = Other()
