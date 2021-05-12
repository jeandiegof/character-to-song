from parser import Parser
from song_builder import SongBuilder
from song_player import SongPlayer
from main_window import MainWindow


class App():
    def __init__(self, generic_midi_sf2_path, audio_driver):
        self._main_window = MainWindow(self.event_handler)
        self._parser = Parser()
        self._song_builder = SongBuilder()
        self._song_player = SongPlayer(
            120, generic_midi_sf2_path, audio_driver)

    def run(self):
        self._main_window.run()

    def event_handler(self, song):
        print('Playing song: ' + song)
        self._main_window.update_status_output_element('Playing')
        self._play(song)
        self._export_midi_file('/home/jeandiego/dev/tcp/output.mid')
        self.clear()
        self._main_window.update_status_output_element('Waiting')

    def _play(self, song_string):
        for character in song_string:
            command = self._parser.parse(character)
            self._song_builder.execute(command)

        resulting_song = self._song_builder.get_resulting_song()
        self._song_player.play(resulting_song)

    def clear(self):
        self._song_builder = SongBuilder()

    def _export_midi_file(self, path):
        self._song_builder.save_midi_to_file(path)
