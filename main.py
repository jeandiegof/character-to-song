from app import App

import time


def run():
    app = App("/home/jeandiego/dev/tcp/GeneralUser_GS_SoftSynth_v144.sf2", "alsa")
    app.run()


if __name__ == "__main__":
    run()
