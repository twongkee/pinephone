import pygame, random, sys, os
from pygame.locals import *
from constants import *

SCALE = 10
filename = os.path.join(os.getcwd(), "resources", "Collect_Point_01a.wav")
mixer = pygame.mixer
mixer.init(buffer=512)
effect = mixer.Sound(filename)
PLAYING = True


def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2:
        return True
    else:
        return False


def die(screen, score):
    global PLAYING
    f = pygame.font.SysFont("Arial", 30)
    t = f.render("Your score was: " + str(score), True, (0, 0, 0))
    screen.blit(t, (10, 150))
    pygame.display.update()
    filename = os.path.join(os.getcwd(), "resources", "secosmic_lo1.wav")
    mixer2 = pygame.mixer
    mixer2.init(buffer=512)
    effect2 = mixer2.Sound(filename)
    effect2.play()
    pygame.time.wait(2500)
    PLAYING = False
    # sys.exit(0)


def menu():
    global PLAYING
    pygame.init()
    doneflag = 0
    keytime = 0
    xpos = 64
    ypos = 128
    xposold = 0
    yposold = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption("initial screen")

    fpsClock = pygame.time.Clock()

    screen.fill(DARKGREY)

    screen.fill(GREEN)
    f = pygame.font.SysFont("Arial", 16)
    t = f.render("start: play   menu: exit", True, (0, 0, 0))
    screen.blit(t, (10, 10))
    pygame.display.update()
    while not doneflag:
        fpsClock.tick(FPS)
        keytime += 1
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT or (
                event.type == KEYDOWN and event.key == K_ESCAPE
            ):  # If user clicked close
                doneflag = True  # Flag that we are done so we exit this loop
            elif event.type == FINGERDOWN:
                print("finger down")
                x = event.x
                y = event.y
                print(x, y)
                if x < 0.4:
                    print("left")
                    xpos -= STEP_SIZE
                if x > 0.6:
                    print("right")
                    xpos += STEP_SIZE
                if y > 0.6:
                    print("down")
                    ypos += STEP_SIZE
                if y < 0.4:
                    print("up")
                    ypos -= STEP_SIZE
            elif event.type == pygame.MULTIGESTURE:
                if 1 > 0:
                    filename = os.path.join(
                        os.getcwd(), "resources", "Jingle_Win_000.wav"
                    )
                    mixer = pygame.mixer
                    mixer.init(11025)
                    effect = mixer.Sound(filename)
                    effect.play()
                    PLAYING = True
                    pygame.event.clear()
                    play_snake()
                    pygame.event.clear()
                    PLAYING = False
                    screen.fill(LIGHTBLUE)
                    f = pygame.font.SysFont("Arial", 16)
                    t = f.render("start: play   menu: exit", True, (0, 0, 0))
                    screen.blit(t, (10, 10))
                    break

            elif event.type == KEYDOWN:
                xposold = xpos
                yposold = ypos
                print(event.key)
                print(event.unicode)
                if event.key == GK_A:
                    screen.fill(GREEN)
                if event.key == GK_B:
                    screen.fill(BLUE)
                if event.key == GK_X:
                    screen.fill(RED)
                if event.key == GK_Y:
                    screen.fill(LIGHTBLUE)
                if event.key == GK_SELECT:
                    print("select")
                    filename = os.path.join(os.getcwd(), "resources", "secosmic_lo.wav")
                    mixer2 = pygame.mixer
                    mixer2.init(11025)
                    effect = mixer2.Sound(filename)
                    effect.play()

                if event.key == GK_DOWN:
                    print("down")

                    ypos += STEP_SIZE
                if event.key == GK_LEFT:
                    print("left")

                    xpos -= STEP_SIZE
                if event.key == GK_MENU:
                    print("esc")

                if event.key == GK_UP:
                    print("up")

                    ypos -= STEP_SIZE
                if event.key == GK_RIGHT:
                    print("right")

                    xpos += STEP_SIZE
                if event.key == GK_START:
                    filename = os.path.join(
                        os.getcwd(), "resources", "Jingle_Win_000.wav"
                    )
                    mixer = pygame.mixer
                    mixer.init(11025)
                    effect = mixer.Sound(filename)
                    effect.play()
                    PLAYING = True
                    play_snake()
                    screen.fill(LIGHTBLUE)
                    f = pygame.font.SysFont("Arial", 16)
                    t = f.render("start: play   menu: exit", True, (0, 0, 0))
                    screen.blit(t, (10, 10))

            elif event.type == KEYUP:
                print("keyup")
        if xpos < 0:
            xpos += SCREEN_WIDTH
        if xpos > SCREEN_WIDTH:
            xpos -= SCREEN_WIDTH
        if ypos > SCREEN_HEIGHT:
            ypos -= SCREEN_HEIGHT
        if ypos < 0:
            ypos += SCREEN_HEIGHT
        pygame.draw.circle(screen, DARKGREY, (xpos, ypos), 8, 0)
        pygame.draw.circle(screen, LIGHTBLUE, (xposold, yposold), 8, 0)
        pygame.display.flip()


def play_snake():
    fingerm = {}
    global PLAYING
    xs = [190, 180, 170, 160, 150]
    ys = [80, 70, 60, 50, 40]
    dirs = 0
    score = 0
    applepos = (random.randint(50, 250), random.randint(50, 150))
    pygame.init()
    s = pygame.display.set_mode((320, 240))
    pygame.display.set_caption("Snake")
    appleimage = pygame.Surface((10, 10))
    appleimage.fill((0, 255, 0))
    img = pygame.Surface((SCALE, SCALE))
    img.fill((255, 0, 0))
    f = pygame.font.SysFont("Arial", 20)
    clock = pygame.time.Clock()

    while PLAYING:
        clock.tick(10 + score)
        for e in pygame.event.get():
            if e.type == QUIT:
                PLAYING = False
            elif e.type == KEYDOWN:
                if e.key == K_UP and dirs != 0:
                    dirs = 2
                elif e.key == K_DOWN and dirs != 2:
                    dirs = 0
                elif e.key == K_LEFT and dirs != 1:
                    dirs = 3
                elif e.key == K_RIGHT and dirs != 3:
                    dirs = 1
            elif e.type == pygame.FINGERDOWN:
                print("finger down")
                # x = e.x
                # y = e.y
                # if x < 0.4 and dirs != 1:
                #    dirs = 3
                # if x > 0.6 and dirs !=3:
                #    dirs = 1
                # if y < 0.4 and dirs !=0:
                #    dirs = 2
                # if y > 0.6 and dirs !=2:
                #    dirs = 0
            if e.type == pygame.FINGERUP:
                fingerm.pop(e.finger_id, None)
            if e.type == pygame.FINGERMOTION:
                dx = int(e.dx * 1000)
                dy = int(e.dy * 1000)
                fingerm[e.finger_id] = (dx, dy)
                print(dx, dy)
        xcompare = 1
        for finger, pos in fingerm.items():
            fx = pos[0]
            fy = pos[1]
            if fy != 0:
                xcompare = abs(fx) / abs(fy)
            else:
                xcompare = 10
            if xcompare > 1:
                if fx < 0 and dirs != 1:
                    dirs = 3
                if fx > 0 and dirs != 3:
                    dirs = 1
            else:
                if fy < 0 and dirs != 0:
                    dirs = 2
                if fy > 0 and dirs != 2:
                    dirs = 0

        i = len(xs) - 1
        while i >= 2:
            if collide(xs[0], xs[i], ys[0], ys[i], SCALE, SCALE, SCALE, SCALE):
                die(s, score)
            i -= 1
        if collide(xs[0], applepos[0], ys[0], applepos[1], SCALE, 10, SCALE, 10):
            score += 1
            effect.play()
            xs.append(700)
            ys.append(700)
            applepos = (random.randint(40, 260), random.randint(40, 160))
        if xs[0] < 0 or xs[0] > 300 or ys[0] < 0 or ys[0] > 220:
            die(s, score)
        i = len(xs) - 1
        while i >= 1:
            xs[i] = xs[i - 1]
            ys[i] = ys[i - 1]
            i -= 1
        if dirs == 0:
            ys[0] += SCALE
        elif dirs == 1:
            xs[0] += SCALE
        elif dirs == 2:
            ys[0] -= SCALE
        elif dirs == 3:
            xs[0] -= SCALE
        s.fill((255, 255, 255))
        for i in range(0, len(xs)):
            s.blit(img, (xs[i], ys[i]))
        s.blit(appleimage, applepos)
        t = f.render(str(score), True, (0, 0, 0))
        s.blit(t, (10, 10))
        pygame.display.update()


# play_snake()

menu()
