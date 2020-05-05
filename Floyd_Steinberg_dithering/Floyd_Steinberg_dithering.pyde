# Enter path of the image here
path = ""
img = loadImage(path)
img.filter(GRAY)
parts = 8
# print(img.width,img.height)
print(7/16.0)
def getLocation(x,y):
    global img
    return x + y*img.width

def getColor(value,parts):
    return round(parts * value/255)*(255/4)

def setup():
    global img
    size(img.width,img.height)
    background(255,255,255)
    colorMode(RGB)

def draw():
    loadPixels()
    for i in range(0,img.height-1):
        for j in range(1,img.width-1):
            loc = getLocation(j,i)
            # print("FFF",j,i,loc)
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            
            # print(img.pixels[loc])
            newr = getColor(r,parts)
            newg = getColor(g,parts)
            newb = getColor(b,parts)
            
            erR = r-newr
            erG = g-newg
            erB = b-newb
            
            # print(r,g,b)
            # print(newr,newg,newb)
            # ellipseMode(CENTER)
            # fill(newr,newg,newb)
            # ellipse(j,i,20,20)
            # print(j,i,10,10)
            # point(j,i)
            img.pixels[loc] = color(newr,newg,newb)
            
            img.pixels[getLocation(j+1,i)] = color(red(img.pixels[getLocation(j+1,i)])+erR*(7/16.0), green(img.pixels[getLocation(j+1,i)])+erG*(7/16.0), blue(img.pixels[getLocation(j+1,i)])+erB*(7/16.0))
            img.pixels[getLocation(j-1,i+1)] = color(red(img.pixels[getLocation(j-1,i+1)])+erR*(3/16.0), green(img.pixels[getLocation(j-1,i+1)])+erG*(3/16.0), blue(img.pixels[getLocation(j-1,i+1)])+erB*(3/16.0))
            img.pixels[getLocation(j,i+1)] = color(red(img.pixels[getLocation(j,i+1)])+erR*(5/16.0), green(img.pixels[getLocation(j,i+1)])+erG*(5/16.0), blue(img.pixels[getLocation(j,i+1)])+erB*(5/16.0))
            img.pixels[getLocation(j+1,i+1)] = color(red(img.pixels[getLocation(j+1,i+1)])+erR*(1/16.0), green(img.pixels[getLocation(j+1,i+1)])+erG*(1/16.0), blue(img.pixels[getLocation(j+1,i+1)])+erB*(1/16.0))
    updatePixels()
    print("Done")
    image(img,0,0)
    noLoop()
            
    
