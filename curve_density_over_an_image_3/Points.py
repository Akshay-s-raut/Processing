import random

def filterImage(im):
    w = im.width
    h = im.height
    im.loadPixels()
    
    threshold = 220
    points = []
    im.loadPixels()
    a = [[0 for i in range(0,w)] for j in range(0,h)]
    for i in range(0,h):
        for j in range(0,w):
            c = im.pixels[j+i*w]
            temp = (red(c)+green(c)+blue(c))/3
            # print([j,i,temp])
            if(temp<threshold):
                a[i][j] = temp 
    return a

def filterImageInvert(im):
    w = im.width
    h = im.height
    im.loadPixels()
    
    threshold = 220
    points = []
    im.loadPixels()
    a = [[0 for i in range(0,w)] for j in range(0,h)]
    for i in range(0,h):
        for j in range(0,w):
            c = im.pixels[j+i*w]
            temp = (red(c)+green(c)+blue(c))/3
            # print([j,i,temp])
            if(temp>threshold):
                a[i][j] = temp 
    return a

def getRandomFrame(offsetx,offsety):
    x = random.randrange(offsetx,width/2-offsetx)
    y = random.randrange(offsety,height-offsety)
    return [x,y]


# def getRandomPoints():
