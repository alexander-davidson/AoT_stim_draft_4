import pygame as pg
import stim_surface as surf
from state import state as st
import random as rng

class Ball:

    restitution = 1

    def __init__(self, x: float, y: float, colour: tuple, speed: float, id: str):
        
        self.pos = pg.Vector2(x, y)
        self.col = colour
        self.rad = 14
        self.speed = speed
        self.vel = pg.math.Vector2(rng.uniform(-1, 1), rng.uniform(-1, 1)).normalize() * speed
        self.id = id

    def update(self, dt: float):

        self.pos += self.vel
    
    def resolve_collision(self, other: 'Ball'):
        delta = self.pos - other.pos
        dist = delta.length()

        if dist == 0 or dist > self.rad + other.rad:
            return

        normal = delta.normalize()
        overlap = (self.rad + other.rad) - dist
        self.pos += normal * (overlap / 2)
        other.pos -= normal * (overlap / 2)

        rel_vel = self.vel - other.vel
        speed = rel_vel.dot(normal)

        if speed >= 0:
            return

        impulse = speed * (1 + self.restitution)
        self.vel -= impulse * normal * 0.5
        other.vel += impulse * normal * 0.5

    def resolve_boundary(self, width: int, height: int):
        if self.pos.x - self.rad < 0:
            self.pos.x = self.rad
            self.vel.x *= -self.restitution
        elif self.pos.x + self.rad > width:
            self.pos.x = width - self.rad
            self.vel.x *= -self.restitution

        if self.pos.y - self.rad < 0:
            self.pos.y = self.rad
            self.vel.y *= -self.restitution
        elif self.pos.y + self.rad > height:
            self.pos.y = height - self.rad
            self.vel.y *= -self.restitution
    

    def draw(self, screen: pg.Surface):

        pg.draw.aacircle(st.grd_surface, self.col, self.pos, self.rad)
        screen.blit(st.grd_surface, (screen.get_width()/2 - st.w/2,
                                     screen.get_height()-st.h))

def make_balls():
    grn_balls = []
    blu_balls = []
    for y in st.stim_y_coords:
        offs_y = y*st.cell+st.cell/2
        for x in st.stim_x_coords_grn:
            offs_x = x*st.cell+st.cell/2
            grn_balls.append(Ball(offs_x, offs_y, (0, 255, 0), 2.2, 'grn'))
    for y in st.stim_y_coords:
        offs_y = y*st.cell+st.cell/2
        for x in st.stim_x_coords_blu:
            offs_x = x*st.cell+st.cell/2
            grn_balls.append(Ball(offs_x, offs_y, (0, 0, 255), 2.2, 'blu'))
    return blu_balls + grn_balls

def get_x_coords_of_balls(balls, screen):
    
    st.grn_posx = [ball.pos[0] for ball in balls if ball.id == 'grn']
    st.blu_posx = [ball.pos[0] for ball in balls if ball.id == 'blu']

    # checking x position with lines
    # for b in st.grn_posx:
    #     pg.draw.line(st.grd_surface, (255, 0, 255), (b - st.rad, 0), (b - st.rad, st.grd_surface.get_height()), 1)
    #     screen.blit(st.grd_surface, (screen.get_width()/2 - st.w/2,
    #                                  screen.get_height()-st.h))

def check_for_parity(width: float):

    count = int((len(st.stim_x_coords_blu) * len(st.stim_y_coords)) // 2)
    mid = int(width // 2)

    # half_blu_on_left = [x for x in st.blu_posx if x + st.rad < mid]
    # half_grn_on_left = [x for x in st.grn_posx if x + st.rad < mid]
    # half_blu_on_right = [x for x in st.blu_posx if x - st.rad > mid]
    # half_grn_on_right = [x for x in st.grn_posx if x - st.rad > mid]
    half_blu_on_left = [x for x in st.blu_posx if x < mid]
    half_grn_on_left = [x for x in st.grn_posx if x < mid]
    half_blu_on_right = [x for x in st.blu_posx if x > mid]
    half_grn_on_right = [x for x in st.grn_posx if x > mid]


    # case_a = (len(half_blu_on_left) == count) and (len(half_grn_on_right) == count)
    # case_b = (len(half_grn_on_left) == count) and (len(half_blu_on_right) == count)

    # if case_a or case_b:
    #     st.parity_achieved = True
    # else:
    #     st.parity_achieved = False

    if len(half_blu_on_left) == 6 and len(half_grn_on_right) == 6:
        st.parity_achieved = True
    elif len(half_blu_on_right) == 6 and len(half_grn_on_left) == 6:
        st.parity_achieved = True
    else: st.parity_achieved = False

