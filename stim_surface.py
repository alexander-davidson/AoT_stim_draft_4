import pygame as pg
from state import state as st

def draw_grid(screen: pg.Surface):

    # for x in range(st.x_indices):
    #     pg.draw.line(st.grd_surface, (0, 0, 0), (x*st.cell, 0), (x*st.cell, st.h))
    # for y in range(st.y_indices):
    #     pg.draw.line(st.grd_surface, (0, 0, 0), (0, y*st.cell), (st.w, y*st.cell))
    # pg.draw.rect(st.grd_surface, (0, 0, 0), (0, 0, st.w, st.h), 1)
    pg.draw.line(st.grd_surface, (255, 0, 0), (st.grd_surface.get_width()/2, 0),
                 (st.grd_surface.get_width()/2, st.grd_surface.get_height()), 1)
    
    screen.blit(st.grd_surface, (screen.get_width()/2 - st.w/2,
                                 screen.get_height()-st.h))

def show_indices(screen: pg.Surface):

    x = pg.mouse.get_pos()[0] - (screen.get_width()/2) + (st.w/2)
    y = pg.mouse.get_pos()[1] - (screen.get_height() - st.h)
    if x >= 0 and x < st.x_indices*st.cell:
        if y >= 0:
            text = st.font.render(f'{int(x//st.cell)}, {int(y//st.cell)}', True, (255, 255, 255))
            screen.blit(text, (10, 10))





    