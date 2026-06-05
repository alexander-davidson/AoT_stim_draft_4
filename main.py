import pygame as pg
import stim_surface as surf
from state import state as st
import stimuli as stim
import numpy as np
import cv2
import random as rng



for v_no in range(1):

    pg.init()
    # ------------------
    # window

    # screen = pg.display.set_mode((800, 500))
    screen = pg.display.set_mode((800, 500), flags= pg.FULLSCREEN)
    scr_w = screen.get_width()
    scr_h = screen.get_height()

    # ------------------
    # pre loop setup
    clock = pg.time.Clock()

    balls = stim.make_balls(1.5)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(rf'/Users/alexander/Library/CloudStorage/OneDrive-QueenMary,UniversityofLondon/05 Arrow of time/03 videos/raw_video/output_{v_no}.mp4', fourcc, 60, (screen.get_width(), screen.get_height()))

    # accumulator = 0
    # delay = 1

    # speed = 2.2

    # ------------------
    # main loop

    running = True
    set_vel = False

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
        
        # accumulator += dt
        # print(balls[0].speed)
        # if accumulator > delay and set_vel == False:
        #     for ball in balls:
        #         ball.vel = pg.math.Vector2(rng.uniform(-1, 1), rng.uniform(-1, 1)).normalize() * speed
        #     set_vel = True
        

        for ball in balls:
            ball.update(dt)
            ball.resolve_boundary(st.grd_surface.get_width(), st.grd_surface.get_height())

        for i, ball in enumerate(balls):
            for other in balls[i+1:]:
                ball.resolve_collision(other)

        stim.get_x_coords_of_balls(balls, screen)

        stim.check_for_parity(st.grd_surface.get_width())

        st.blu_posx = []
        st.grn_posx = []

        if st.parity_achieved == True:
            running = False
        # ------------------
        # draw

        surf.draw_grid(screen)
        surf.show_indices(screen)


        for ball in balls:
            ball.draw(screen)

        pg.display.update()

        frame = pg.surfarray.array3d(screen)       # pygame surface → numpy array
        frame = frame.transpose(1, 0, 2)           # pygame is (x,y) cv2 expects (y,x)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # pygame is RGB, cv2 expects BGR
        out.write(frame)

    out.release()
    pg.quit()