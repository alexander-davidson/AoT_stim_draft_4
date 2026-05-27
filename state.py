import pygame as pg

pg.font.init()

class State:

    def __init__(self):
        self.cell = 28
        self.x_indices = 19
        self.y_indices = 12
        self.grd_surface = pg.Surface((self.x_indices*self.cell,
                                       self.y_indices*self.cell))
        self.w = self.grd_surface.get_width()
        self.h = self.grd_surface.get_height()

        self.font = pg.font.SysFont('arial', 20)

state = State()