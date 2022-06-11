from tkinter import Scale
from turtle import onclick, position
from ursina import *

app = Ursina()

player = Entity(model ='sphere', color = rgb(230, 143, 67), scale = (3,3,1) )


def update():
    player.x += held_keys['d'] * time.dt
    player.x -= held_keys['a'] * time.dt

coppy = player.y

def input(key):
    if key == 'space':
        player.y += 1
        invoke(setattr, player, 'y', player.y - 1, delay = .25)
    if player.y == range(3,100):
       player.y -= coppy




# if player.y == range(100):
#     player.y -= coppy

app.run() 