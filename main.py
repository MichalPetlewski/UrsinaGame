from ursina import *
from random import uniform
from ursina.prefabs.first_person_controller import FirstPersonController

def input(key):
    if key == "left mouse down":
        Audio("assets/Ursina-Engine_FPS_assets_laser_sound.wav")
        Animation("assets/textures/fireAnimation/spark_01.png", parent = camera.ui, scale = 0.1, position=(0.39, -0.3), loop= False)

class Wasp(Button):
    def __init__(self, x, y, z):
        super().__init__(
            parent = scene,
            position = (x, y, z),
            model = "assets/models/wasp.obj",
            color = color.white,
            collider = "box",
            scale = 0.1,
            colider = "box"
        
        )

app = Ursina()

Sky()

player = FirstPersonController(
    mouse_sensitivity=Vec2(50, 50),
    position = (0, 0, 0),
    origin_y = -0.5
)

ground = Entity(
    model = "plane",
    scale = (100, 1, 100),
    texture="assets/textures/grass.png",
    collider= "box",
    texture_scale = (1, 1)
)

wall_1 = Entity(
    model="cube", 
    collider="box", 
    position=(-8, 0, 0), 
    scale=(8,5,1),
    texture = "brick",
    colider = "box",
    color = color.brown,
    texture_scale = (5, 5)
    )

wall_2 = duplicate(wall_1, z=5)

wall_3 = duplicate(wall_1, z=10)

wall_4 = Entity(
    model="cube", 
    collider="box", 
    position=(-15, 0, 10), 
    scale=(1,5,20),
    rotation = (0, 0, 0),
    texture = "brick",
    colider = "box",
    color = color.brown,
    texture_scale = (5, 5)
    )

gun = Entity(
    model = "assets/models/gun.obj",
    parent = camera.ui,
    scale = 0.1,
    position = (0.4,-0.39),
    rotation=(-5, -10, -10),
    color = color.blue
)

num = 6
wasps = [None] * num
for i in range(num):
    wasps[i] = Wasp(uniform(-10, 10), uniform(1, 10), uniform(-10, 10))



app.run()