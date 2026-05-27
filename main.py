import pygame as pg
import stim_surface as surf
from state import state as st



pg.init()
# ------------------
# window

screen = pg.display.set_mode((0, 0), flags=pg.FULLSCREEN)
scr_w = screen.get_width()
scr_h = screen.get_height()

# ------------------
# pre loop setup


# ------------------
# main loop

running = True

while running:

    screen.fill((0, 0, 0))
    st.grd_surface.fill((255, 255, 255))

    # ------------------
    # event
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    # ------------------
    # draw
    surf.draw_grid(screen)
    surf.show_indices(screen)


    pg.display.update()

pg.quit()