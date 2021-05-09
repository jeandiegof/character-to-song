from parser import Parser
from song_builder import SongBuilder
from song_player import SongPlayer

class App():
    def __init__(self, generic_midi_sf2_path, audio_driver):
        self._parser = Parser()
        self._song_builder = SongBuilder()
        self._song_player = SongPlayer(120, generic_midi_sf2_path, audio_driver)

    def run(self):
        example_song = 'CCC CCCAACCAAaa!AA'
        self._play(example_song)
    
    def _play(self, song_string):
        for character in song_string:
            command = self._parser.parse(character)
            self._song_builder.execute(command)

        resulting_song = self._song_builder.get_resulting_song()
        self._song_player.play(resulting_song)

    def _export_midi_file(self, path):
        pass