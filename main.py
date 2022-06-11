from tkinter import Scale
from ursina import *

app = Ursina()

player = Entity(model ='sphere', color = rgb(230, 143, 67), scale = (3,3,1) )

def update():
    player.x += held_keys['d'] * time.dt

app.run()