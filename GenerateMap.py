from PIL import Image

#converts the images to a map

def getLevelMap(paths, colors, itemSize):
    images = []

    for i in paths:
        images.append(Image.open(i))
    
    imageXW, imageYW = images[0].size() #each of these images should be the same, NOTE the first map should be top down view
    
    #each block and their color
    key = {
        "WALL" : "RED",
        "START" : "BLUE",
        "WIN" : "GREEN"
    }
    
    #output map
    map = []

    
    #fisrt for the top down view... after this we have to go back and edit h
    for y in range(imageYW):
        for x in range(imageXW):
            if(image.getpixel((x,y))[0:3] == colors[key["WALL"]]):
                map.append(["wall", x*itemSize, y*itemSize])
            #add win and start..
                
    return(map)