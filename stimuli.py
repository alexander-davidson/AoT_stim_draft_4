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
        self.vel = pg.math.Vector2(rng.uniform(-1, 1), rng.uniform(-1, 1)).normalize() * self.speed
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
            grn_balls.append(Ball(offs_x, offs_y, (0, 255, 0), 2, 'grn'))
    for y in st.stim_y_coords:
        offs_y = y*st.cell+st.cell/2
        for x in st.stim_x_coords_blu:
            offs_x = x*st.cell+st.cell/2
            grn_balls.append(Ball(offs_x, offs_y, (0, 0, 255), 2, 'blu'))
    return blu_balls + grn_balls

def get_x_coords_of_balls(balls):
    
    st.grn_posx = [ball.pos[0] for ball in balls if ball.id == 'grn']
    st.blu_posx = [ball.pos[0] for ball in balls if ball.id == 'blu']

def check_for_parity(width: float):

    half_blu_on_left = [x for x in st.blu_posx if x + st.rad*2 < width/2]
    half_grn_on_left = [x for x in st.grn_posx if x + st.rad*2 < width/2]
    half_blu_on_right = [x for x in st.blu_posx if x > width/2]
    half_grn_on_right = [x for x in st.grn_posx if x > width/2]
    print(len(half_blu_on_left))

    if (len(half_blu_on_left) == (len(st.stim_x_coords_blu)*len(st.stim_y_coords))/2 
        and len(half_grn_on_right) == (len(st.stim_x_coords_blu)*len(st.stim_y_coords))/2):
        st.parity_achieved = True
    if (len(half_blu_on_right) == (len(st.stim_x_coords_blu)*len(st.stim_y_coords))/2 
        and len(half_grn_on_left) == (len(st.stim_x_coords_blu)*len(st.stim_y_coords))/2):
        st.parity_achieved = True
    