import pygame
pygame.init()
pygame.mixer.init()

clock = pygame.time.Clock()
size = 1024,768
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

blob = pygame.image.load("art/guy.png")
jump = pygame.mixer.Sound("sound/jump.wav")

class player:
    def __init__(self,posx,posy):
        self.jump_speed = 0
        self.jumps_left = 2
        self.pos = [posx,posy]
    def move(self):
        self.pos[1] += self.jump_speed
        self.jump_speed += 0.4

        if self.pos[1] > 700:
            self.pos[1] = 700
            self.jump_seed = 0
            self.jumps_left = 2

## HAI BRENDAN

        if self.dir == 'left': self.pos[0] -= 3
        if self.dir == 'right': self.pos[0] += 3
        if self.dir == 'up':    self.pos[1] -= 3
        if self.dir == 'down':  self.pos[1] += 3

guy = player(100,100)

while True:
    clock.tick(60)
    screen.fill((255,255,255))

    guy.dir = 'null'
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if guy.jumps_left > 0:
                    guy.jump_speed = -5
                    guy.jumps_left -= 1
                    jump.play()
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    if pygame.key.get_pressed()[pygame.K_UP]:    guy.dir = 'up'
    if pygame.key.get_pressed()[pygame.K_DOWN]:  guy.dir = 'down'
    if pygame.key.get_pressed()[pygame.K_LEFT]:  guy.dir = 'left'
    if pygame.key.get_pressed()[pygame.K_RIGHT]: guy.dir = 'right'

    guy.move()

    screen.blit(blob, guy.pos)
    pygame.display.flip()
