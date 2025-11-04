import random

from pico2d import *

from bird import Bird
from boy import Boy
from grass import Grass
import game_world

import game_framework


boy = None
birds = []

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy
    global running
    global birds

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    birds = []
    for i in range (10):
        b = Bird(800 + random.randint(-200,200),500)
        game_world.add_object(b, 1)
        birds.append(b)

def update():
    game_world.update()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

