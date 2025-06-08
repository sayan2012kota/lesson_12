import pgzrun
import random

WIDTH = 1000
HEIGHT = 600

bug = Actor("bug")
ship = Actor("ship")
speed = 5
bugs = []
bullets = []
score = 0
direction = 1
ship.pos = (500, 500)

for I in range(8):
    bugs.append(Actor("bug"))
    bugs[-1].x = 100 + 80 * I
    bugs[-1].y = 0



def draw():
    screen.clear()
    screen.fill("dark blue")
    ship.draw()
    for V in bugs:
        V.draw()
    for R in bullets:
        R.draw()
    display_score()


def update():
    global direction
    movedown = False
    global score
    if keyboard.left:
        ship.x = ship.x - speed
        if ship.x <= 0:
            ship.x = 0

    if keyboard.right:
        ship.x = ship.x + speed
        if ship.x >= WIDTH:
            ship.x = WIDTH    
    if len(bugs) > 0 and bugs[-1].x > WIDTH - 80 or bugs[0].x  < 0:
        movedown = True
        direction = direction * -1
    for V in bugs:
        V.x = V.x + 5 * direction
        if movedown == True:
            V.y = V.y + 5
        for Bullet in bullets:
            if V.colliderect(Bullet):
                bullets.remove(Bullet)
                bugs.remove(V)
                score = score + 1
    for R in bullets:
        if R.y < 0:
            bullets.remove(R)
        else:
            R.y = R.y - 5
    
    
    
    
def display_score():
    screen.draw.text(str(score), (50, 50))

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50



pgzrun.go()