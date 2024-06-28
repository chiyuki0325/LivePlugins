import subprocess as sp
import yaml
import time

cache = ""

while True:
    out = sp.run([
        "/usr/bin/qdbus",
        "org.mpris.MediaPlayer2.ElectronNCM",
        "/org/mpris/MediaPlayer2",
        "org.mpris.MediaPlayer2.Player.Metadata"
        ],
        stdout=sp.PIPE
    ).stdout.decode()
    info = yaml.safe_load(out)
    line = f'当前正在播放: {info["xesam:artist"]} - {info["xesam:title"]}'
    if cache != line:
        cache = line
        with open("mpris2.txt", "w") as f:
            f.write(line)
            f.close()
    time.sleep(1)
