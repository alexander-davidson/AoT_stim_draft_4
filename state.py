import pygame as pg

pg.font.init()

class State:

    def __init__(self):
        self.cell = 28
        self.x_indices = 19
        self.y_indices = 11
        self.grd_surface = pg.Surface((self.x_indices*self.cell,
                                       self.y_indices*self.cell))
        self.w = self.grd_surface.get_width()
        self.h = self.grd_surface.get_height()
        self.rad = 14

        self.font = pg.font.SysFont('arial', 20)

        self.stim_x_coords_grn = (2, 4, 6)
        self.stim_x_coords_blu = (12, 14, 16)
        self.stim_y_coords = (2, 4, 6, 8)


state = State()