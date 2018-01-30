import pygame
import time
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

car_width = 68
car_height = 135

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Kosmosemäng')
clock = pygame.time.Clock()
block = pygame.image.load("kivi.png").convert_alpha()
carImg = pygame.image.load('racecar.png').convert_alpha()
enemy = pygame.image.load("vastane.png").convert_alpha()
bullet = pygame.image.load('kuul.png').convert_alpha()
heart = pygame.image.load('süda.png').convert_alpha()
pause = 0

bkgd = pygame.image.load("tee.png").convert()
bY = 0
thingsDodged1 = 0


def spawnHeart(heartX, heartY):
    gameDisplay.blit(heart, (heartX, heartY))


def shoot(bulletx, bullety, bulletspeed):
    gameDisplay.blit(bullet, (bulletx, bullety))


def things_dodged(count):
    global thingsDodged1
    thingsDodged1 = 0
    font = pygame.font.Font('freesansbold.ttf', 25)
    text = font.render("Mahalaske: " + str(count), 1, white)
    gameDisplay.blit(text, (0, 0))
    thingsDodged1 += count


def things(thingx, thingy):
    gameDisplay.blit(block, (thingx, thingy))


def enemyCar(carx, cary):
    gameDisplay.blit(enemy, (carx, cary))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, 1, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((800 / 2), (600 / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    global thingsDodged1
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects("Avarii", largeText)
    TextRect.center = ((800 / 2), (600 / 2))
    gameDisplay.blit(TextSurf, TextRect)

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects("Su skoor: " + str(thingsDodged1), smallText)
    textRect.center = ((800 / 2), (370))
    gameDisplay.blit(textSurf, textRect)

    maxScore = open("maxScore.txt", "r")

    MaxScore = maxScore.readlines()

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects("Parim skoor: " + str(MaxScore[-1]), smallText)
    textRect.center = ((800 / 2), (400))
    gameDisplay.blit(textSurf, textRect)

    maxScore.close()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Proovi uuesti", 150, 450, 140, 50, green, bright_green, game_loop)
        button("Välju", 550, 450, 100, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)


def crash1():
    global thingsDodged1
    gameDisplay.fill(white)
    largeText = pygame.font.Font('freesansbold.ttf', 90)
    TextSurf, TextRect = text_objects("Jäid eludest ilma!", largeText)
    TextRect.center = ((800 / 2), (600 / 2))
    gameDisplay.blit(TextSurf, TextRect)

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects("Su skoor: " + str(thingsDodged1), smallText)
    textRect.center = ((800 / 2), (370))
    gameDisplay.blit(textSurf, textRect)

    maxScore = open("maxScore.txt", "r")

    MaxScore = maxScore.readlines()

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects("Parim skoor: " + str(MaxScore[-1]), smallText)
    textRect.center = ((800 / 2), (400))
    gameDisplay.blit(textSurf, textRect)

    maxScore.close()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Proovi uuesti", 150, 450, 140, 50, green, bright_green, game_loop)
        button("Välju", 550, 450, 100, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    global thingsDodged
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
            thingsDodged1 = 0
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_quit():
    pygame.quit()
    quit()


def game_intro():
    intro = 1
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Liigu nooltega vasakule ja paremale. Vajuta ""P"", et panna mäng pausile", smallText)
        textRect.center = ((800 / 2), (370))
        gameDisplay.blit(textSurf, textRect)

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Kosmosemäng", largeText)
        TextRect.center = ((800 / 2), (600 / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Alusta", 150, 450, 100, 50, green, bright_green, game_loop)
        button("Välju", 550, 450, 100, 50, red, bright_red, game_quit)

        maxScore = open("maxScore.txt", "r")

        MaxScore = maxScore.readlines()

        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects("Parim skoor: " + str(MaxScore[-1]), smallText)
        textRect.center = ((800 / 2), (400))
        gameDisplay.blit(textSurf, textRect)

        maxScore.close()

        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pause = 0


def paused():
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("PAUS", largeText)
        TextRect.center = ((800 / 2), (600 / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Jätka", 150, 450, 100, 50, green, bright_green, unpause)
        button("Välju", 550, 450, 100, 50, red, bright_red, game_quit)

        pygame.display.update()
        clock.tick(15)


def game_loop():
    global pause
    global bY
    global thingsDodged1

    x = (800 * 0.45)
    y = (600 * 0.8)

    xChange = 0

    carStartx = random.randrange(190 + car_width, 606 - car_width)
    carStarty = -600
    carSpeed = 6

    heartStartx = random.randrange(190, 530)
    heartStarty = 0
    heartWidth = 50
    heartHeight = 50

    thingStartx = random.randrange(190, 530)
    thingStarty = -600
    thingSpeed = 6
    bkgdSpeed = 4
    thingWidth = 68
    thingHeight = 135

    bulletSpeed = 17

    bulletWidth = 5
    bulletHeight = 14

    heartOn = 0

    lives = 3

    dodged = 0

    newCar = 0

    thingsDodged1 = 0

    gameExit = 0

    bulletOn = 0

    while not gameExit:
        rel_y = bY % bkgd.get_rect().width
        gameDisplay.blit(bkgd, (0, rel_y - bkgd.get_rect().width))
        if rel_y < 800:
            gameDisplay.blit(bkgd, (0, rel_y))
        bY += bkgdSpeed

        if lives > 4:
            lives = 4
        if lives == 4:
            gameDisplay.blit(heart, (750, 0))
            gameDisplay.blit(heart, (700, 0))
            gameDisplay.blit(heart, (650, 0))
            gameDisplay.blit(heart, (600, 0))
        if lives == 3:
            gameDisplay.blit(heart, (750, 0))
            gameDisplay.blit(heart, (700, 0))
            gameDisplay.blit(heart, (650, 0))
        if lives == 2:
            gameDisplay.blit(heart, (750, 0))
            gameDisplay.blit(heart, (700, 0))
        if lives == 1:
            gameDisplay.blit(heart, (750, 0))
        if lives <= 0:
            crash1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -7
                if event.key == pygame.K_RIGHT:
                    xChange = 7
                if event.key == pygame.K_p:
                    pause = 1
                    paused()
                if event.key == pygame.K_SPACE:
                    bulletX = x + 34
                    bulletY = y
                    bulletOn = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0

        """for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot(x, y, bulletSpeed)
                    print(bulletY)"""
        x += xChange

        # things(thingx, thingy, thingw, thingh, color)
        # things(thingStartx, thingStarty)
        # thingStarty += thingSpeed
        car(x, y)
        things_dodged(dodged)

        if x > 598 - car_width or x < 192:
            crash()

        #thingSpawnTime = random.randint(1, 10)

        """if thingStarty > 600:
            thingStarty = 0 - thingHeight
            thingStartx = random.randrange(190, 530)
            lives -= 1
            maxScore = open("maxScore.txt", "r+")
            lineList = maxScore.readlines()
            if dodged > int(lineList[-1]):
                if str(dodged) not in str(lineList[-1]):
                    maxScore.write("\n" + str(dodged))
            maxScore.close()
            if dodged % 3 == 0:
                thingSpeed += 1"""

        if dodged % 14 == 0 and dodged != 0:
            heartOn = 1

        if heartOn == 1:
            heartStarty += bkgdSpeed
            spawnHeart(heartStartx, heartStarty)
            if heartStarty > 600:
                heartStarty = 0
                heartStartx = random.randrange(190, 530)
                heartOn = 0

        carStarty += carSpeed
        enemyCar(carStartx, carStarty)
        if carStarty > 600:
            carStarty = 0 - car_height
            carStartx = random.randrange(190 + car_width, 606 - car_width)
            carSpeed -= 1
            lives -= 1
            maxScore = open("maxScore.txt", "r+")
            lineList = maxScore.readlines()
            if dodged > int(lineList[-1]):
                if str(dodged) not in str(lineList[-1]):
                    maxScore.write("\n" + str(dodged))
            maxScore.close()

        if dodged % 6 == 0 and dodged != 0:  # and dodged != 0
            newCar = 1

        if newCar == 1:
            thingStarty += thingSpeed
            things(thingStartx, thingStarty)
            if thingStarty > 600:
                thingStarty = 0 - thingHeight
                thingStartx = random.randrange(190, 530)
                lives -= 1
                maxScore = open("maxScore.txt", "r+")
                lineList = maxScore.readlines()
                if dodged > int(lineList[-1]):
                    if str(dodged) not in str(lineList[-1]):
                        maxScore.write("\n" + str(dodged))
                maxScore.close()
                newCar = 0

        if bulletOn == 1:
            shoot(bulletX, bulletY, bulletSpeed)
            bulletY -= bulletSpeed
            if bulletY < 1:
                bulletY = 600
                bulletOn = 0
            if bulletY < thingStarty + thingHeight:
                if bulletX > thingStartx and bulletX < thingStartx + thingWidth or bulletX + bulletWidth > thingStartx and bulletX + bulletWidth < thingStartx + thingWidth:
                    bulletOn = 0
                    thingStarty = -200
                    thingStartx = random.randrange(190, 530)
                    thingSpeed += 0.2
                    dodged += 1
                    maxScore = open("maxScore.txt", "r+")
                    lineList = maxScore.readlines()
                    if dodged > int(lineList[-1]):
                        if str(dodged) not in str(lineList[-1]):
                            maxScore.write("\n" + str(dodged))
                    maxScore.close()
                    newCar = 0
            if bulletY < carStarty + car_height:
                if bulletX > carStartx and bulletX < carStartx + car_width or bulletX + car_width > carStartx and bulletX + car_width < carStartx + car_width:
                    bulletOn = 0
                    carStarty = -200
                    carStartx = random.randrange(190 + car_width, 606 - car_width)
                    carSpeed += 0.1
                    dodged += 1
                    maxScore = open("maxScore.txt", "r+")
                    lineList = maxScore.readlines()
                    if dodged > int(lineList[-1]):
                        if str(dodged) not in str(lineList[-1]):
                            maxScore.write("\n" + str(dodged))
                    maxScore.close()

        if y < thingStarty + thingHeight:
            if x > thingStartx and x < thingStartx + thingWidth or x + car_width > thingStartx and x + car_width < thingStartx + thingWidth:
                lives -= 1
                thingStarty = -100

        if y < heartStarty + heartHeight:
            if x > heartStartx and x < heartStartx + heartWidth or x + car_width > heartStartx and x + car_width < heartStartx + heartWidth:
                heartOn = 0
                heartStarty = -200
                lives += 1

        if y < carStarty + car_height:
            if x > carStartx and x < carStartx + car_width or x + car_width > carStartx and x + car_width < carStartx + car_width:
                lives -= 1
                carStarty = -100

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
