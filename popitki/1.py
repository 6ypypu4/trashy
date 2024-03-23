import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
done = False
# Colors
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (70, 70, 70)
dark = (45, 45, 45)
basic_r = 0
basic_g = 0
basic_b = 0
whose_time = 0


font = pygame.font.SysFont("Arial", 20)
def color_choosing(event):
    global basic_r, basic_g, basic_b, whose_time
    if event.type == pygame.MOUSEBUTTONDOWN:
        #Базовые цвета
        if 15 <= event.pos[0] <= 45 and 15 <= event.pos[1] <= 45:
            basic_r = 255
            basic_g = 255
            basic_b = 255
        elif 50 <= event.pos[0] <= 80 and 15 <= event.pos[1] <= 45:
            basic_r = 0
            basic_g = 0
            basic_b = 0
        elif 85 <= event.pos[0] <= 115 and 15 <= event.pos[1] <= 45:
            basic_r = 255
            basic_g = 0
            basic_b = 0
        elif 120 <= event.pos[0] <= 150 and 15 <= event.pos[1] <= 45:
            basic_r = 0
            basic_g = 255
            basic_b = 0
        elif 155 <= event.pos[0] <= 185 and 15 <= event.pos[1] <= 45:
            basic_r = 0
            basic_g = 0
            basic_b = 255
        #Пространство для ввода:
        elif 15 <= event.pos[0] <= 77 and 80 <= event.pos[1] <= 103:
            whose_time = 1 #ввод красни
        elif 78 <= event.pos[0] <= 141 and 80 <= event.pos[1] <= 103:
            whose_time = 2 #ввод зелени
        elif 142 <= event.pos[0] <= 204 and 80 <= event.pos[1] <= 103:
            whose_time = 3 #ввод сини
        else: whose_time = 0 #ничейный ввод
    if event.type == pygame.KEYDOWN:
        if whose_time == 1: 
            if event.key == pygame.K_UP:
               basic_r = min(basic_r + 1, 255)
            elif event.key == pygame.K_DOWN:
               basic_r = max(basic_r - 1, 0)
        elif whose_time == 2: 
            if event.key == pygame.K_UP:
               basic_g = min(basic_g + 1, 255)
            elif event.key == pygame.K_DOWN:
               basic_g = max(basic_g - 1, 0)
        elif whose_time == 3: 
            if event.key == pygame.K_UP:
               basic_b = min(basic_b + 1, 255)
            elif event.key == pygame.K_DOWN:
               basic_b = max(basic_b - 1, 0)
    return (basic_r, basic_g, basic_b)
            
def drawin(event,current_color):
    global whose_time



def background():
    global basic_r, basic_g, basic_b
    #Bg:
    screen.fill(white)
    #Panel
    pygame.draw.rect(screen, grey, pygame.Rect(0, 0, screen_width, screen_height/5)) #800 x 120
    #  for colors:
    pygame.draw.rect(screen, dark, pygame.Rect(10, 10, screen_width/4, screen_height/6)) #200 x 100 210to110
    pygame.draw.rect(screen, dark, pygame.Rect(20 + screen_width/4, 10, screen_width/4, screen_height/6)) #200 x 100  for shapes 420to110
    pygame.draw.rect(screen, grey, pygame.Rect(15, 80, screen_width/4 - 10, 24)) 

    pygame.draw.rect(screen, white, pygame.Rect(15, 15, 30, 30))
    pygame.draw.rect(screen, black, pygame.Rect(50, 15, 30, 30))
    pygame.draw.rect(screen, red,   pygame.Rect(85, 15, 30, 30))
    pygame.draw.rect(screen, green, pygame.Rect(120, 15, 30, 30))
    pygame.draw.rect(screen, blue,  pygame.Rect(155, 15, 30, 30))

    screen.blit(font.render('R:', True, red), (18, 80))
    screen.blit(font.render('G:', True, green), (82, 80))
    screen.blit(font.render('B:', True, blue), (147, 80))

    screen.blit(font.render(str(basic_r), True, white), (40, 80))
    screen.blit(font.render(str(basic_g), True, white), (104, 80))
    screen.blit(font.render(str(basic_b), True, white), (169, 80))

    pygame.draw.rect(screen, (basic_r, basic_g, basic_b), pygame.Rect(15, 47, 170, 30))

    pygame.draw.rect(screen, grey, pygame.Rect(223, 12, 30, 30))
    pygame.draw.rect(screen, grey, pygame.Rect(256, 12, 30, 30))
    pygame.draw.rect(screen, grey, pygame.Rect(289, 12, 30, 30))
    pygame.draw.rect(screen, grey, pygame.Rect(322, 12, 30, 30))
    pygame.draw.rect(screen, grey, pygame.Rect(355, 12, 30, 30))
    pygame.draw.rect(screen, grey, pygame.Rect(388, 12, 30, 30))











# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        current_color = color_choosing(event)
        drawin(event, current_color)
    background()


    pygame.display.flip()
    clock.tick(50)  

pygame.quit()
