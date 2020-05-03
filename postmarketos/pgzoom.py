# import pygame module in this program 
import pygame 
import sys

if len(sys.argv) > 1:
    imagefile = sys.argv[1]
else:
    imagefile='second.jpg'

# activate the pygame library . 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
print(pygame.version)
if pygame.version.vernum < (2, 0):
    print("warning, touch may not work")
    

# define the RGB value 
# for WHITE colour 
WHITE = (255, 255, 255) 

# assigning values to WIDTH and HEIGHT variable 
WIDTH = 300
HEIGHT = 600

# create the display surface object 
# of specific dimension..e(WIDTH, HEIGHT). 
display_surface = pygame.display.set_mode((WIDTH, HEIGHT )) 

# set the pygame window name 
pygame.display.set_caption('Image') 

# create a surface object, image is drawn on it. 
image = pygame.image.load(imagefile) 
angle = 0
angle_raw = 0
ZOOM = 100
x = 150
y = 300
fx = 0
fy = 0
fdx = 0
fdy = 0
px = 0
py = 0
shiftx = 0
shifty = 0
xold = x
yold = y
xrel = 100
yrel = 100
fpos = [(0,0) , (0,0), (0,0), (0,0),(0,0)]
fid = []
fdy1 = 0
fdy2 = 0
epinched = 0

def delta(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    dx = x1 -x2
    dy = y1 -y2
    print(f"{x1},{y1} {x2},{y2} {dx},{dy}")
    return (dx,dy)
# infinite loop 
while True : 

    # completely fill the surface object 
    # with WHITE colour 
    display_surface.fill(WHITE) 

    # copying the image surface object 
    # to the display surface object at 
    # (0, 0) coordinate. 
    #display_surface.blit(image, (0, 0)) 
    #angle = 0
    #rotatedsurf = pygame.transform.rotate(image, angle)
    imX,imY = image.get_rect().size
    new_imX = int(imX*xrel/100)
    new_imY = int(imY*xrel/100)
    zoomsurf = pygame.transform.scale(image,(new_imX,new_imY))
    shiftx = fx - fdx
    shifty = fy - fdy
    #display_surface.blit(rotatedsurf, (px + shiftx,py + shifty)) 
    display_surface.blit(zoomsurf, (px + shiftx,py + shifty)) 
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 
        #print(f"{px + shiftx},{py+shifty}, {xrel}, {fid}, {fpos}")
        print(f"{int(xrel)},{epinched}, {fx},{fy}")
        # print(event)

        if event.type == pygame.FINGERDOWN:
            fdx = int(event.x * WIDTH)
            fdy = int(event.y * HEIGHT)
            fx = fdx
            fy = fdy
            fid.append(event.finger_id) 

        #if event.type == pygame.FINGERDOWN:
        #    # handle two and average...
        #    print(f"down finger {event.finger_id}")
        #    fid.append(event.finger_id) 
        #    # get avg of non zero fpos and assign them....
        #    if len(fid)>1:
        #        fdx2 = int(event.x * WIDTH)
        #        fdy2 = int(event.y * HEIGHT)
        #        fdx = int((fdx1 + fdx2)/2)
        #        fdy = int((fdy1 + fdy2)/2)
        #
        #    fpos[len(fid)] = (int(event.x * WIDTH), int(event.y * HEIGHT))
        #    fdx1 = int(event.x * WIDTH)
        #    fdy1 = int(event.y * HEIGHT)

        if event.type == pygame.FINGERUP:
            xold = fx
            yold = fy
            px = px + shiftx
            py = py + shifty
            shiftx = 0
            shifty = 0
            fx = int(event.x * WIDTH)
            fy = int(event.y * HEIGHT)
            fdx = fx
            fdy = fy
            fid.remove(event.finger_id)

        if event.type == pygame.FINGERMOTION:
            fx = int(event.x * WIDTH)
            fy = int(event.y * HEIGHT)

        if event.type == pygame.MULTIGESTURE:
            #print(f"{x},{y} x {event.x} y {event.y} pinched {event.pinched} rotated {event.rotated} nf {event.num_fingers}")
            #print(f"{x},{y} pinched {event.pinched} rotated {event.rotated} ")
            #print(f"{x},{y} {xold},{yold} ")
            # delta((fx,fy),(xold,yold))
            #fx = int(event.x * WIDTH)
            # fx = fdx
            #fy = int(event.y * HEIGHT)
            #fy = fdy
            nf = event.num_fingers
            #fpos[nf] = (int(event.x * WIDTH),int(event.y * HEIGHT))
            #angle_raw -= event.rotated * 100
            #angle = angle_raw
            #angle %= 360
            xrel += event.pinched * ZOOM
            yrel += event.pinched * ZOOM
            epinched = event.pinched
            if xrel < 0:
                xrel = 0
            if xrel > 100:
                xrel = 100
            if yrel < 0:
                yrel = 0
            # print(f"{xrel},{yrel} pinched {event.pinched} rotated {event.rotated} ")

        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 

            # deactivates the pygame library 
            pygame.quit() 

            # quit the program. 
            quit() 

        # Draws the surface object to the screen. 
        pygame.display.update() 
            
