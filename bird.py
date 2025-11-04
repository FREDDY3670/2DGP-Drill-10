from pico2d import *

import game_framework

TIME_PER_ACTION = 0.3
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
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
    def draw(self):
        self.image.clip_draw((int(self.frame) % 5) * 183,(2 - (int(self.frame) // 5)) * 168,183,168,self.x,self.y,75,75)

