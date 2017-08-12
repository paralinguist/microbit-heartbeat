from microbit import *

heart = "09090:99999:99999:09990:00900"

brighter_hearts = []
fade_hearts = []
all_hearts = []

last = 9

for brightness in range(8, 1, -1):
    fade_hearts.append(Image(heart))
    heart = heart.replace(str(last), str(brightness))
    last = brightness

brighter_hearts = list(reversed(fade_hearts))

all_hearts = fade_hearts + brighter_hearts

display.show(all_hearts, loop=True, delay=100)