# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('lightblue'))

# draw a house with a roof
draw.rect(gameDisplay, Color('brown'), Rect(200, 50, 50, 300))
draw.polygon(gameDisplay, Color('black'), [(400, 200), (250,50), (250, 200)])
draw.rect(gameDisplay, Color('orange'), Rect(100, 350, 300,100))
draw.polygon(gameDisplay, Color('orange'), [(50, 350), (100,400), (400, 350)])
draw.polygon(gameDisplay, Color('orange'), [(450, 350), (400,400), (400, 350)])
# draw blue water
draw.rect(gameDisplay, Color('midnightblue'), Rect(0, 400, 500, 100))
draw.circle(gameDisplay, Color('midnightblue'), (0, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (30, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (80, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (130, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (180, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (230, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (280, 430),50)
draw.circle(gameDisplay, Color('midnightblue'), (330, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (380, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (430, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (480, 430), 50)
draw.circle(gameDisplay, Color('midnightblue'), (500, 430), 50)
# draw a sun
draw.circle(gameDisplay, Color('yellow'), (50, 50), 50)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")