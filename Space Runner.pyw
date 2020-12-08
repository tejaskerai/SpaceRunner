import pygame, math as m, random, time

# Initializing variables
red = (230, 2, 21)
pygame.init()
size = 1100, 650
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Space Runner")
clock = pygame.time.Clock()
# Importing images
pausescreen = pygame.image.load('Images/pausescreen.png')
instructionscreen = pygame.image.load('Images/instructions.png')
menuscreen = pygame.image.load('Images/menuscreen.png')
gameoverscreen = pygame.image.load('Images/gameover.png')
# width = 100, height = 70
ufoIMG = pygame.image.load('Images/ufo.png')
background = pygame.image.load('Images/background.png')
# width = 205, height = 206
planetIMG = pygame.image.load('Images/planet.png')
font = pygame.font.Font("Font/justice3d.ttf", 50)


# Subroutines
def planet(loc_of_planetx, loc_of_planety):
    screen.blit(planetIMG, (loc_of_planetx, loc_of_planety))


def ufo(loc_of_ufox, loc_of_ufoy):
    screen.blit(ufoIMG, (loc_of_ufox, loc_of_ufoy))


def message_to_screen(msg, colour, x, y):
    text = font.render(msg, True, colour)
    screen.blit(text, [x, y])


def instructions():
    while True:
        mouse = pygame.mouse.get_pos()
        screen.blit(instructionscreen, (0, 0))
        ##        pygame.draw.rect(screen, red, [8, 597, 272, 44]) #(x, y, w, h)
        ##        pygame.draw.rect(screen, red, [820, 595, 275 ,50])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if 8 + 272 > mouse[0] > 8 and 597 + 44 > mouse[1] > 597:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    start()
            if 820 + 275 > mouse[0] > 820 and 595 + 50 > mouse[1] > 595:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameloop()


def start():
    while True:
        mouse = pygame.mouse.get_pos()
        screen.blit(menuscreen, (0, 0))
        ##        pygame.draw.rect(screen, red, [450, 249, 194, 51]) #(x, y, w, h)
        ##        pygame.draw.rect(screen, red, [300, 335, 501, 51])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if 450 + 194 > mouse[0] > 450 and 249 + 51 > mouse[1] > 249:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameloop()
            if 300 + 501 > mouse[0] > 300 and 335 + 51 > mouse[1] > 335:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    instructions()


def pause():
    paused = True
    screen.blit(pausescreen, (0, 0))
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_m:
                    start()
        pygame.display.update()
        clock.tick(5)


def game_over(score):
    while True:
        screen.blit(gameoverscreen, (0, 0))
        message_to_screen(('Your score is ' + str(score)), red, 350, 535)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_m:
                    start()


def gameloop():
    loc_of_ufox = 200
    loc_of_ufoy = 200
    loc_of_planetx = 1100
    loc_of_planety = random.randrange(0, 440)
    ufoyspeed = 9
    ground = 550
    planetspeed = 19
    limit = -205
    planetrad = 103
    uforad = 50
    score = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ufoyspeed = -13
                elif event.key == pygame.K_p:
                    pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    ufoyspeed = 12
        screen.blit(background, (0, 0))
        loc_of_ufoy += ufoyspeed
        ufo(loc_of_ufox, loc_of_ufoy)
        planet(loc_of_planetx, loc_of_planety)
        text = font.render('Score: ' + str(score), True, red)
        screen.blit(text, [10, 10])
        # ufocircle = pygame.draw.circle(screen, blue, (loc_of_ufox+50, loc_of_ufoy+50), uforad,1)
        # planetcircle = pygame.draw.circle(screen, blue, (loc_of_planetx+103, loc_of_planety+103),planetrad,1)
        ##  Collisons  
        if (loc_of_ufoy > ground):
            time.sleep(0.5)
            game_over(score)
        if (loc_of_ufoy < 0):
            time.sleep(0.5)
            game_over(score)
        if (m.sqrt(((loc_of_ufox + 50) - (loc_of_planetx + 103)) ** 2 + (
                (loc_of_ufoy + 50) - (loc_of_planety + 103)) ** 2) <= uforad + planetrad):
            time.sleep(0.5)
            game_over(score)
        # Loops planet image to front
        if loc_of_planetx < limit:
            loc_of_planety = random.randrange(0, 440)
            loc_of_planetx = 1100
            score = score + 1
        else:
            planetspeed = planetspeed + float(0.0015)
            loc_of_planetx -= planetspeed
            pygame.display.update()


start()
