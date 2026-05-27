import pygame as pg
import stim_surface as surf
from state import state as st
import random as rng

class Ball:

    def __init__(self, x: float, y: float, colour: tuple, speed: float):
        
        self.pos = pg.Vector2(x, y)
        self.col = colour
        self.speed = speed
        self.vel = pg.Vector2(rng.uniform(-1, 1), rng.uniform(-1, 1))
