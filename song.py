class Song:
    def __init__(self):
        self._notes = []

    def append(self, note, instrument):
        self._notes.append((note, instrument))
    
    def notes(self):
        return self._notes