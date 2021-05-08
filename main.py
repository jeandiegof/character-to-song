from player import Player;
from mingus.containers import Note

import time

def app():
    player = Player()
    i = 0

    while True:
        print(i)
        player.set_volume(i)
        
        player.play_note(Note("C-5"))
        player.play_note(Note("E-5"))
        time.sleep(1)
        
        i = (i + 10) if i < 117 else 0
        

if __name__ == "__main__":
    app()
