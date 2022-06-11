from tkinter import Scale
from ursina import *

app = Ursina()

player = Entity(model ='sphere', color = rgb(230, 143, 67), scale = (3,3,1) )


def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y - 1, delay = .25)

if player.position > 1:
    player.position = Vec3(0,0,0)

app.run() 