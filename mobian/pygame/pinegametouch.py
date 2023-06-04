import pygame
## needs pygame 2+
pygame.init()
WIDTH=300
HEIGHT=600
pineDisplay = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('touch me')
clock = pygame.time.Clock()

BLACK = (  0,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
CYAN  = (  0, 255, 255)
red   = (255,   0,   0)
MAGENTA=(255, 0,   255)
YELLOW= (255, 255,   0)
WHITE = (255, 255, 255)
ORANGE= (255, 165,   0)
PURPLE= (160,  32, 240)

rainbow=[BLACK,PURPLE,BLUE,GREEN,CYAN,red,ORANGE,MAGENTA,YELLOW]

ZOOM = 300

def game_loop():

    loop = True
    x = 150
    y = 300
    xrel = 10
    yrel = 10
    text = 'read me'
    angle = 0
    angle_raw = 0
    rain = 0
    fingerlist = []
    while loop:
        for event in pygame.event.get():
            print(event)
            #print(event.type)
            text='no touch'
            if event.type == pygame.FINGERDOWN:
                text="finger down"
                fingerlist.append(event.finger_id)

            if event.type == pygame.FINGERUP:
                text="finger up"
                fingerlist.remove(event.finger_id)

            if event.type == pygame.FINGERMOTION:
                x = int(event.x * WIDTH)
                y = int(event.y * HEIGHT)
                text='single move'
            
            if event.type == pygame.MULTIGESTURE:
                #print(f"{x},{y} x {event.x} y {event.y} pinched {event.pinched} rotated {event.rotated} nf {event.num_fingers}")
                print(f"{x},{y} pinched {event.pinched} rotated {event.rotated} ")
                x = int(event.x * WIDTH)
                y = int(event.y * HEIGHT)
                nf = event.num_fingers
                angle_raw -= event.rotated * 100
                angle = angle_raw
                angle %= 360
                pinch = int(event.pinched * ZOOM)
                xrel += event.pinched * ZOOM
                yrel += event.pinched * ZOOM
                if xrel < 0:
                    xrel = 0
                if yrel < 0:
                    yrel = 0
                text=f'm {nf} {len(fingerlist)} {int(xrel)} {int(angle)}'


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        if len(fingerlist) == 3:
            rain += 1
            if rain > 6:
                rain = 0
        pineDisplay.fill(WHITE)
        statusText = pygame.font.Font('freesansbold.ttf',32)
        textsurface = statusText.render(text, False, rainbow[rain])        
        rotatedsurf = pygame.transform.rotate(textsurface, angle)
        pineDisplay.blit(textsurface, (20,20))
        pineDisplay.blit(rotatedsurf, (20,90))

        for r in range(len(rainbow)):
            pygame.draw.rect(pineDisplay, rainbow[r],(30 + r * 30,540,30,30))

        pygame.draw.rect(pineDisplay, BLUE,(x,y,25,25))
        pygame.draw.rect(pineDisplay, PURPLE,(x,y,xrel,yrel))


        pygame.display.update()
        clock.tick(25)

game_loop()
