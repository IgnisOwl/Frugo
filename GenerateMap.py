from PIL import Image

def getLevelMap(path, colors, itemSize, defaultItems):
    image = Image.open(path)
    
    imageXW, imageYW = image.size
    
    #each block and their color
    key = {
        "WALL" : "RED",
        "START" : "BLUE",
        "WIN" : "GREEN"
    }
    
    #output map
    map = []
    
    map.append(defaultItems)
    
    for y in range(imageYW):
        for x in range(imageXW):
            if(image.getpixel((x,y))[0:3] == colors[key["WALL"]]):
                map.append(["wall", x*itemSize, y*itemSize])
            #add win and start..
                
    return(map)