from pico2d import *

class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
    def update(self):
        pass
    def draw(self):
        pass

