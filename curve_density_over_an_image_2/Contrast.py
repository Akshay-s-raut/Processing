def contrast(input,cont,bright):
    w = input.width
    h = input.height
    input.loadPixels()
    
    for i in range(0,w*h):
        inColor = input.pixels[i]
        
        r = red(input.pixels[i])
        g = green(input.pixels[i])
        b = blue(input.pixels[i])
        
        r = (r*cont + bright)
        g = (g*cont + bright)
        b = (b*cont + bright)
        
        if(r<0):
            r = 0
        elif(r>255):
            r = 255
        if(g<0):
            g = 0
        elif(g>255):
            g = 255
        if(b<0):
            b = 0
        elif(b>255):
            b = 255
        
        input.pixels[i] = color(r,g,b)
        input.updatePixels()
