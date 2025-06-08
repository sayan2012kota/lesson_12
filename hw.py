import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

bug = Actor("shark_image")
ship = Actor("submarine_image")
speed = 5
bugs = []
bugs.append(bug)
bugs[-1].x = 900
bugs[-1].y = -100
bullets = []
score = 0

ship.pos = (500, 500)

def draw():
    screen.clear()
    screen.fill("light blue")
    ship.draw()
    for V in bugs:
        V.draw()
    for R in bullets:
        R.draw()
    display_score()


def update():
    global score
    if keyboard.left:
        ship.x = ship.x - speed
        if ship.x <= 0:
            ship.x = 0

    if keyboard.right:
        ship.x = ship.x + speed
        if ship.x >= WIDTH:
            ship.x = WIDTH    
    for V in bugs:
        V.y = V.y + 5
        if V.y > 600:
            V.y = -100
            V.x = random.randint(100, 900)
    for R in bullets:
        if R.y < 0:
            bullets.remove(R)
        else:
            R.y = R.y - 5
    for Bullet in bullets:
        if bug.colliderect(Bullet):
            bullets.remove(Bullet)
            bugs.remove(bug)
            score = score + 1


def display_score():
    screen.draw.text(str(score), (50, 50))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50






pgzrun.go()