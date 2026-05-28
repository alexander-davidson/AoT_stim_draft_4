import pygame as pg
import stim_surface as surf
from state import state as st
import stimuli as stim



pg.init()
# ------------------
# window

screen = pg.display.set_mode((0, 0), flags=pg.FULLSCREEN)
scr_w = screen.get_width()
scr_h = screen.get_height()

# ------------------
# pre loop setup
clock = pg.time.Clock()

balls = stim.make_balls()

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
    # update
    dt = clock.tick(60)/1000

    for ball in balls:
        ball.update(dt)
        ball.resolve_boundary(st.grd_surface.get_width(), st.grd_surface.get_height())
    stim.get_x_coords_of_balls(balls)


    for i, ball in enumerate(balls):
        for other in balls[i+1:]:
            ball.resolve_collision(other)



    # ------------------
    # draw
    surf.draw_grid(screen)
    surf.show_indices(screen)

    for ball in balls:
        ball.draw(screen)

    pg.display.update()

pg.quit()