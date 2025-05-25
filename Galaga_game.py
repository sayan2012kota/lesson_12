import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

bug = Actor("bug")
ship = Actor("ship")
speed = 5

ship.pos = (500, 500)

def draw():
    screen.clear()
    screen.fill("dark blue")
    ship.draw()


def update():
    if keyboard.left:
        ship.x = ship.x - speed
        if ship.x <= 0:
            ship.x = 0

    if keyboard.right:
        ship.x = ship.x + speed
        if ship.x >= WIDTH:
            ship.x = WIDTH    



pgzrun.go()