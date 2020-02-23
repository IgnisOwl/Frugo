from PIL import Image

#converts the images to a map

def getLevelMap(paths, itemSize):
    images = []

    for i in paths:
        images.append(Image.open(i))
    
    imageXW, imageYW = images[0].size() #each of these images should be the same
    
    #each block and their color
    key = {
        "WALL" : (255,0,0),
        "START" : "BLUE",
        "WIN" : "GREEN"
    }
    
    #output map
    map = []

    #go through the slices and construct the map based off that, we don't actually need a top down map because these slices will make it
    for i in images: #each image represents an row.
        for x in range(imageXW): #now insde of this one row, deal with each cell  individually
            map.append([[ ]]]) #create new cell in map
            for y in range(imageYW): #y is the height, so it needs to cycle through each possible block in this height stack
                cell = [] 
                #NOTE: by default it goes from top left to bottom left but we need it to go from bottom left to top left, thats y we are subtracting it from size
                if(i.getpixel((x,imageYW-y))[0:3] == key["WALL"]):
                    cell.append([cellCode["wall"], imageYW-y])
            
             map[i][x].append(cell) #i represents y, x represents x(aka the cell its on), and we need to add each block to this, so in the end we should have something like: [[[ ]]]
                
                #cell will now contain the various blocks at different heights for one cell

                
    return(map)