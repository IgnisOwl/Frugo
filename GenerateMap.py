from PIL import Image

#converts the images to a map

#NOTE: in the future we might just want to types instead of a 4d array. Then you can just have each class instance having a property

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
                    cell.append(["portal", imageYW-y, 1])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_LEFT"]):
                    cell.append(["portal", imageYW-y, 2])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_BOTTOM"]):
                    cell.append(["portal", imageYW-y, 3])

                elif(Image.open(paths[i]).getpixel((x,y))[0:3] == key["PORTAL_RIGHT"]):
                    cell.append(["portal", imageYW-y, 0])

            map[i].append(cell)
                #cell will now contain the various blocks at different heights for one cell
    return(map, imageXW, imageYW)

def getSpawnLocation(objects, levelvarthing):
    if(levelvarthing == 1):
        return(0,2)
    elif(levelvarthing == 2):
        return(0,2)
    elif(levelvarthing == 3):
        return(0,4)
    elif(levelvarthing == 4):
        return(0,15)
    
    
#     lif(levelvarthing == 3):
#         return(0,9)
#     elif(levelvarthing == 4):
#         return(14,14)
    
    
    
    
    
    #print(objects) #spawn block and get its location
#     for xslice in range(len(objects)) :
#         for ycell in range(len(objects)) :
#             print(objects[xslice][ycell]
#             if(len(objects[xslice][ycell]) > 0) :
#                 if(objects[xslice][ycell][0][0] == "spawn"):
#                     return(ycell, xslice)
#                 #else :
#                     #return(0,0)
#             #else :
#                 #return(0,0)
