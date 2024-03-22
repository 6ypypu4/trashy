import pygame
import os
import random
import re
import json
screen_heigth = 640
screen_width = 640
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_heigth))
clock = pygame.time.Clock()
done = False
x = y = 0

#Основа тайлов:
class Tile:
    def __init__(self, texture_path, collision=False, damage=0):
        self.texture = pygame.image.load(texture_path)
        self.texture = pygame.transform.scale2x(self.texture)
        self.collision = collision
        self.dmg = damage
#Тайлы:
class Grass(Tile):
    def __init__(self):
        super().__init__("resources/surface_sprites/grass.png", False, 0)
class Stone(Tile):
    def __init__(self):
        super().__init__("resources/surface_sprites/stone.png", True, 0)
class Lava(Tile):
    def __init__(self):
        super().__init__("resources/surface_sprites/lava.png", False, 10)

#Основа существ:
class Entity:
    def __init__(self, texture_path, helth_pts, damage, speed):
        self.texture = pygame.image.load(texture_path)
        self.hp = helth_pts
        self.dmg = damage
        self.spd = speed
#Существа:
class Player(Entity):
    def __init__(self):
        super().__init__("resources/entity_sprites/player.png", 100, 0, 10)

#Подгрузка уровня
with open("resources/levels/level1.json") as f:
    level = json.load(f)

def draw_tile(level):
    global screen
    grass_tile = Grass()
    stone_tile = Stone()
    lava_tile = Lava()
    for y, row in enumerate(level):
        for x, tile_id in enumerate(row):
            if level[x][y] == 0: screen.blit(grass_tile.texture, (y*32, x*32))
            elif level[x][y] == 1: screen.blit(stone_tile.texture, (y*32, x*32))
            elif level[x][y] == 2: screen.blit(lava_tile.texture, (y*32, x*32))

def draw_player(event):
    global screen, screen_heigth, screen_width
    global x,y
    plr = Player()
    speed = plr.spd
    diagonal_speed = (2*speed**2)**0.5/2
    #Движение:
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and pressed[pygame.K_LEFT] and y > 0 and x > 0: 
        y -= diagonal_speed
        x -= diagonal_speed
    elif pressed[pygame.K_UP] and pressed[pygame.K_RIGHT] and y > 0 and x < screen_width - 16:
        y -= diagonal_speed
        x += diagonal_speed
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_RIGHT] and x < screen_width - 16 and y < screen_heigth - 16:
        y += diagonal_speed
        x += diagonal_speed
    elif pressed[pygame.K_DOWN] and pressed[pygame.K_LEFT] and y < screen_heigth - 16 and x > 0:
        y += diagonal_speed
        x -= diagonal_speed
    else:
      if pressed[pygame.K_UP] and y > 0: y -= speed
      if pressed[pygame.K_DOWN] and y < screen_heigth - 16: y += speed
      if pressed[pygame.K_LEFT] and x > 0: x -= speed
      if pressed[pygame.K_RIGHT] and x < screen_width - 16: x += speed
    #Отрисовка:
    screen.blit(plr.texture, (x, y))


def game_sceen(event, level):
    draw_tile(level)  
    draw_player(event)
    


# Основной игровой цикл
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = not done
    game_sceen(event, level)   
    
    pygame.display.flip()
    clock.tick(60)  

        