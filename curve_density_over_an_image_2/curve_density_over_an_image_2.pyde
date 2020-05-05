from Contrast import*
from Points import*
import random

# Enter path of the image here
path = ""
im = loadImage(path)
im.filter(GRAY)
offsetx,offsety = 30,30
p = 0.1

# print(im.width,im.height)

def getPtsDfs(N):
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
        
                
    

def setup():
    global a, p, prob
    size((im.width+2*offsetx)*2,im.height+2*offsety)
    background(200,200,200)
    
    # 0<contrast<5 and -128<brightness<128
    contrast(im,1.8,0)
    image(im,offsetx+im.width,offsety)
    # print(filterImage(im))
    a = filterImage(im)
    # frameRate(30)
    # prob = getProbability(p)
    
def draw():
    global a, offsetx, offsety, im, prob
    N = 100
    # N = random.choice([30,30,30,30,50,50,80,100])
    pts = getPtsDfs(N)
    # if(random.choice(prob)==True):
    #     pts.append([random.randrange(0,im.width),random.randrange(0,im.height)])
    #     random.shuffle(pts)
    if(len(pts)>2):
        # print("Here")
        # print(pts)
        beginShape()
        noFill()
        stroke(0,0,0,100)
        strokeWeight(3)
        curveVertex(offsetx + pts[0][0],offsety + pts[0][1])
        for i in pts:
            curveVertex(offsetx + i[0],offsety + i[1])
        curveVertex(offsetx+pts[-1][0],offsety+pts[-1][1])
        endShape()
