from tkinter import Scale
from ursina import *

app = Ursina()

player = Entity(model ='sphere', color = rgb(230, 143, 67), scale = (3,3,1) )

app.run()