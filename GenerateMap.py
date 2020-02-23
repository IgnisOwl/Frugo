from PIL import Image

#converts the images to a map

def getLevelMap(paths):

    imageXW, imageYW = Image.open(paths[0]).size #each of these images should be the same
    
    #each block and their color
    key = {
        "WALL" : (255,0,0),
        "SPAWN" : (255,247,0),
        "GOAL" : (0,255,0),
        "PORTAL_TOP" : (0,255,232),
        "PORTAL_LEFT" : (0,109,255),
        "PORTAL_BOTTOM" : (161,0,255),
        "PORTAL_RIGHT" : (0,0,255)
    }
    
    #output map
    map = []

    #go through the slices and construct the map based off that, we don't actually need a top down map because these slices will make it
    for i in range(len(paths)): #each image represents an row.
        map.append([])

        for x in range(imageXW): #now insde of this one row, deal with each cell  individually

            cell = [] #holds the cell
            for y in range(imageYW): #y is the height, so it needs to cycle through each possible block in this height stack
                if(Image.open(paths[i]).getpixel((x,y))[0:3] == key["WALL"]):
                    cell.append(["wall", imageYW-y])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["SPAWN"]):
                    cell.append(["spawn", imageYW-y])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["GOAL"]):
                    cell.append(["goal", imageYW-y])
                
                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_TOP"]):
                    cell.append(["portal", imageYW-y])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_LEFT"]):
                    cell.append(["portal", imageYW-y])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_BOTTOM"]):
                    cell.append(["portal", imageYW-y])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_RIGHT"]):
                    cell.append(["portal", imageYW-y])

            map[i].append(cell)
                #cell will now contain the various blocks at different heights for one cell
    return(map)