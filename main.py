from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

selected_block = "dirt"

textures = {
    "grass": load_texture("assets/textures/grass.png"),
    "dirt": load_texture("assets/textures/dirt.png"),
    "stone": load_texture("assets/textures\stone.png"),
}

class Block(Entity):
    def __init__(self, position, block_type):
        super().__init__(
            position = position,
            model = "cube",
            scale=1,
            origin_y = 0.5,
            texture = textures.get(block_type),
            collider = "box"
        ) 
        self.block_type = block_type

mini_block = Entity(
    parent = camera,
    model = "cube",
    texture = textures.get(selected_block),
    scale = 0.2,
    position = (0.35, -0.25, 0.5)
)


player = FirstPersonController(
    mouse_sensitivity=Vec2(50, 50),
    position = (0, 5, 0)
)

for x in range(-10, 10):
  for z in range(-10, 10):
      block = Block((x, 0, z), "grass")
        
    
def input(key):
    global selected_block
    #place
    if key == "left mouse down":
        hit_info = raycast(camera.world_position, camera.forward, distance=10)
        if hit_info.hit:
            block = Block(hit_info.entity.position + hit_info.normal, selected_block)
    #destroy
    if key == "right mouse down":
        destroy(mouse.hovered_entity)    
    #change block
    if key == '1':
        selected_block = "grass"
    if key =='2':
        selected_block = "dirt"
        
def update():
    mini_block.texture=textures.get(selected_block)
          
app.run()