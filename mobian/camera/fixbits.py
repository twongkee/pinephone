#!/usr/bin/env python3
import numpy as np

raw = np.fromfile('frame.raw', np.uint8)


if len(raw) == 24385536: # using pixelformat=422P
    w=4032
    h=3024
else:                    # using pixelformat=RGGB and larger size 
    w=4208
    h=3120


g=16


def fix(arr,x,y):
    avg = ( int(arr[4*w+x+y]) + int(arr[-4*w+x+y]) + int(arr[x+y+4]) + int(arr[x+y-4]) ) /4
    return avg

for x in range(0,(w-g*2*2)*2,g*2):
    for y in range(0,(h-g*2*2)*2,g*2*2):
        #print(w*(29  +y)+26    +x, end=" ")
        raw[w*(29*2  +y)+26*2    +x]= fix(raw,w*(29*2+y),26*2+x) #good
        raw[w*(32*2  +y)+25*2    +x]= fix(raw,w*(32*2+y),25*2+x) #good

        raw[w*(29*2+g*2+y)+26*2+g*2-8*2+x]= fix(raw,w*(45*2+y),34*2+x)
        raw[w*(32*2+g*2+y)+25*2+g*2-8*2+x]= fix(raw,w*(48*2+y),33*2+x)



raw.tofile('numpy.raw')  
