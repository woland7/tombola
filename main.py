import simpleaudio as sa

f = open("cartellone.csv", "r")
lines = f.readlines()
f.close()

songs = {}
for l in lines:
    l_s = l.strip().split(",")
    songs[l_s[0]] = {
        "wave": sa.WaveObject.from_wave_file(l_s[2]),
        "significato": l_s[1]
    }
play = None
while True:
    try:
        number = input('Input:')
    except ValueError:
        print("Not a number")
    if number != "s":
        try:
            play = songs[number]["wave"].play()
        except KeyError:
            print("non c'è la canzone")
    else:
        print("audio bloccato")
        play.stop()


