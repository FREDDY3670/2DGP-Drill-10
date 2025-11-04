from pico2d import *

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

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

