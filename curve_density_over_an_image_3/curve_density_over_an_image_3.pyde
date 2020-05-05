from Contrast import*
from Points import*
import random

# Enter path of the image here
path = ""
im = loadImage(path)
im.filter(GRAY)
offsetx,offsety = 30,30
# print(im.width,im.height)

def getPtsDfsDark(N):
    global a, im
    path = []
    imw = im.width
    imh = im.height
    x = random.randrange(0,im.width)
    y = random.randrange(0,im.height)
    subtractor = 50
    s = [[x,y]]
    visited = []
    while(len(s)!=0):
        if(len(path)==N):
            break
        t = s.pop()
        # print(t)
        temp = []
        path.append(t)
        if(t[0]>0 and a[t[1]][t[0]-1]>0 and ([t[0]-1,t[1]] not in visited)):
            temp.append([a[t[1]][t[0]-1],[t[0]-1,t[1]]])
            a[t[1]][t[0]-1] = a[t[1]][t[0]-1] - subtractor
            visited.append([t[0]-1,t[1]])
        if(t[0]<imw-1 and a[t[1]][t[0]+1]>0 and ([t[0]+1,t[1]] not in visited)):
            temp.append([a[t[1]][t[0]+1],[t[0]+1,t[1]]])
            visited.append([t[0]+1,t[1]])
            a[t[1]][t[0]+1] = a[t[1]][t[0]+1] - subtractor
        if(t[0]>0 and t[1]>0 and a[t[1]-1][t[0]-1]>0 and ([t[0]-1,t[1]-1] not in visited)):
            temp.append([a[t[1]-1][t[0]-1],[t[0]-1,t[1]-1]])
            visited.append([t[0]-1,t[1]-1])
            a[t[1]-1][t[0]-1] = a[t[1]-1][t[0]-1] - subtractor
        if(t[1]>0 and a[t[1]-1][t[0]]>0 and ([t[0],t[1]-1] not in visited)):
            temp.append([a[t[1]-1][t[0]],[t[0],t[1]-1]])
            visited.append([t[0],t[1]-1])
            a[t[1]-1][t[0]] = a[t[1]-1][t[0]] - subtractor
        if(t[1]<imh-1 and a[t[1]+1][t[0]]>0 and ([t[0],t[1]+1] not in visited)):
            temp.append([a[t[1]+1][t[0]],[t[0],t[1]+1]])
            visited.append([t[0],t[1]+1])
            a[t[1]+1][t[0]] = a[t[1]+1][t[0]] - subtractor
        if(t[0]<imw-1 and t[1]>0 and a[t[1]-1][t[0]+1]>0 and ([t[0]+1,t[1]-1] not in visited)):
            temp.append([a[t[1]-1][t[0]+1],[t[0]+1,t[1]-1]])
            visited.append([t[0]+1,t[1]-1])
            a[t[1]-1][t[0]+1] = a[t[1]-1][t[0]+1] - subtractor
        if(t[0]<imw-1 and t[1]<imh-1 and a[t[1]+1][t[0]+1]>0 and ([t[0]+1,t[1]+1] not in visited)):
            temp.append([a[t[1]+1][t[0]+1],[t[0]+1,t[1]+1]])
            visited.append([t[0]+1,t[1]+1])
            a[t[1]+1][t[0]+1] = a[t[1]+1][t[0]+1] - subtractor
        if(t[0]>0 and t[1]<imh-1 and a[t[1]+1][t[0]-1]>0 and ([t[0]-1,t[1]+1] not in visited)):
            temp.append([a[t[1]+1][t[0]-1],[t[0]-1,t[1]+1]])
            visited.append([t[0]-1,t[1]+1])
            a[t[1]+1][t[0]-1] = a[t[1]+1][t[0]-1] - subtractor
        temp.sort()
        for i in temp:
            s.append(i[1])
    return path
        
def getPtsDfsLight(N):
    global b, im
    path = []
    imw = im.width
    imh = im.height
    x = random.randrange(0,im.width)
    y = random.randrange(0,im.height)
    subtractor = 5047 
    s = [[x,y]]
    visited = []
    while(len(s)!=0):
        if(len(path)==N):
            break
        t = s.pop()
        # print(t)
        temp = []
        path.append(t)
        if(t[0]>0 and b[t[1]][t[0]-1]>0 and ([t[0]-1,t[1]] not in visited)):
            temp.append([b[t[1]][t[0]-1],[t[0]-1,t[1]]])
            b[t[1]][t[0]-1] = b[t[1]][t[0]-1] - subtractor
            visited.append([t[0]-1,t[1]])
        if(t[0]<imw-1 and b[t[1]][t[0]+1]>0 and ([t[0]+1,t[1]] not in visited)):
            temp.append([b[t[1]][t[0]+1],[t[0]+1,t[1]]])
            visited.append([t[0]+1,t[1]])
            b[t[1]][t[0]+1] = b[t[1]][t[0]+1] - subtractor
        if(t[0]>0 and t[1]>0 and b[t[1]-1][t[0]-1]>0 and ([t[0]-1,t[1]-1] not in visited)):
            temp.append([b[t[1]-1][t[0]-1],[t[0]-1,t[1]-1]])
            visited.append([t[0]-1,t[1]-1])
            b[t[1]-1][t[0]-1] = b[t[1]-1][t[0]-1] - subtractor
        if(t[1]>0 and b[t[1]-1][t[0]]>0 and ([t[0],t[1]-1] not in visited)):
            temp.append([b[t[1]-1][t[0]],[t[0],t[1]-1]])
            visited.append([t[0],t[1]-1])
            b[t[1]-1][t[0]] = b[t[1]-1][t[0]] - subtractor
        if(t[1]<imh-1 and b[t[1]+1][t[0]]>0 and ([t[0],t[1]+1] not in visited)):
            temp.append([b[t[1]+1][t[0]],[t[0],t[1]+1]])
            visited.append([t[0],t[1]+1])
            b[t[1]+1][t[0]] = b[t[1]+1][t[0]] - subtractor
        if(t[0]<imw-1 and t[1]>0 and a[t[1]-1][t[0]+1]>0 and ([t[0]+1,t[1]-1] not in visited)):
            temp.append([b[t[1]-1][t[0]+1],[t[0]+1,t[1]-1]])
            visited.append([t[0]+1,t[1]-1])
            b[t[1]-1][t[0]+1] = b[t[1]-1][t[0]+1] - subtractor
        if(t[0]<imw-1 and t[1]<imh-1 and a[t[1]+1][t[0]+1]>0 and ([t[0]+1,t[1]+1] not in visited)):
            temp.append([b[t[1]+1][t[0]+1],[t[0]+1,t[1]+1]])
            visited.append([t[0]+1,t[1]+1])
            b[t[1]+1][t[0]+1] = b[t[1]+1][t[0]+1] - subtractor
        if(t[0]>0 and t[1]<imh-1 and b[t[1]+1][t[0]-1]>0 and ([t[0]-1,t[1]+1] not in visited)):
            temp.append([b[t[1]+1][t[0]-1],[t[0]-1,t[1]+1]])
            visited.append([t[0]-1,t[1]+1])
            b[t[1]+1][t[0]-1] = b[t[1]+1][t[0]-1] - subtractor
        temp.sort()
        for i in temp:
            s.append(i[1])
    return path
    
    

def setup():
    global a,b
    size((im.width+2*offsetx)*2,im.height+2*offsety)
    # background(200,200,200)
    background(255,41,41)
    # 0<contrast<5 and -128<brightness<128
    contrast(im,2.5,0)
    image(im,offsetx+im.width,offsety)
    # print(filterImage(im))
    a = filterImage(im)
    b = filterImageInvert(im)
    # frameRate(30)
    
def draw():
    global a,b, offsetx, offsety
    
    g = random.choice([1,-1])
    if(g==1):
        # N = 100
        N = random.choice([30,30,30,30,50,50,80,100])
        pts = getPtsDfsDark(N)
        if(len(pts)>2):
            # print("Here")
            # print(pts)
            beginShape()
            noFill()
            stroke(0,0,0,100)
            curveVertex(offsetx + pts[0][0],offsety + pts[0][1])
            for i in pts:
                curveVertex(offsetx + i[0],offsety + i[1])
                curveVertex(offsetx+pts[-1][0],offsety+pts[-1][1])
            endShape()
    else:
        # N = 100
        N = random.choice([30,30,30,30,50,50,80,100])
        pts = getPtsDfsLight(N)
        if(len(pts)>2):
            # print("Here")
            # print(pts)
            beginShape()
            noFill()
            stroke(255,255,255,100)
            curveVertex(offsetx + pts[0][0],offsety + pts[0][1])
            for i in pts:
                curveVertex(offsetx + i[0],offsety + i[1])
            curveVertex(offsetx+pts[-1][0],offsety+pts[-1][1])
            endShape()
