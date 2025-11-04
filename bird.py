from pico2d import *

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x = 800
        self.y = 500
        self.frame = 0
    def update(self):
        pass
    def draw(self):
        self.image.clip_draw(183,168,183,168,self.x,self.y,75,75)

