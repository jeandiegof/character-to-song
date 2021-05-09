from parser import Parser
from command_executor import CommandExecutor
from song_player import SongPlayer

import time

def app():
    parser = Parser()
    command_executor = CommandExecutor()
    music = 'CCAACCAA AA'

    # TODO: change instrument not working. Setting the midi_instr attribute doesn't work.

    for char in music:
        command = parser.parse(char)
        command_executor.execute(command)

    song = command_executor.get_resulting_song()
    for entry in song:
        print(entry)

    player = SongPlayer(120, "/home/jeandiego/dev/tcp/GeneralUser_GS_SoftSynth_v144.sf2", "alsa")
    player.play(song)

if __name__ == "__main__":
    app()
