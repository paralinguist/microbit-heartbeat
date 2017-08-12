from microbit import *

#Define a string to display a custom image.
heart = "09090:99999:99999:09990:00900"

#Declare empty lists for our hearts
brighter_hearts = []
fade_hearts = []
all_hearts = []

#We're going to start with the brightest heart: 9 is brightest, 0 is off.
last = 9

#Create a list of hearts with fading brightness
for brightness in range(8, 1, -1):
    fade_hearts.append(Image(heart))
    heart = heart.replace(str(last), str(brightness))
    last = brightness

#Create a list of hearts with increasing brightness - reverse the existing list.
brighter_hearts = list(reversed(fade_hearts))

#Join the two lists together - our heart gets dimmer and then brighter.
all_hearts = fade_hearts + brighter_hearts

#Display from dimmest to brightest in a loop - a beating heart.
display.show(all_hearts, loop=True, delay=100)