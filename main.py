from parser import Parser
from song_builder import SongBuilder
from song_player import SongPlayer

import time

def app():
    parser = Parser()
    music_builder = SongBuilder()
    music = 'CCAACCAAaa!AA'

    # TODO: change instrument not working. Setting the midi_instr attribute doesn't work.

    for char in music:
        command = parser.parse(char)
        music_builder.execute(command)

    song = music_builder.get_resulting_song()
    for entry in song:
        print(entry)

    player = SongPlayer(120, "/home/jeandiego/dev/tcp/GeneralUser_GS_SoftSynth_v144.sf2", "alsa")
    player.play(song)

if __name__ == "__main__":
    app()
