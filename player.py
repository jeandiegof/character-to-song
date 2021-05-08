from mingus.midi import fluidsynth


class Player:
    def __init__(self):
        self.fluidsynth = fluidsynth
        self.fluidsynth.init(
            "/home/jeandiego/dev/tcp/GeneralUser_GS_SoftSynth_v144.sf2", "alsa")

    def play_note(self, note):
        self.fluidsynth.play_Note(note)

    def change_instrument(self, general_midi_instrument_id):
        self.fluidsynth.set_instrument(1, general_midi_instrument_id)
    
    def set_volume(self, volume):
        # maximum volume is 127
        self.fluidsynth.main_volume(1, volume)
