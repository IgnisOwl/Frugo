class Render:
    def __init__(self, screen, pygame, colors, spriteSize, sizeMultiplier, playerSize):
        self.screen = screen
        self.pygame = pygame
        self.colors = colors
        self.size_multiplier = sizeMultiplier
        self.sprite_size = spriteSize
        self.player_size = playerSize
    
    def render(self, objects, sprite_image_paths, dimension, playerX, playerY, renderSlice = 3, cellnum = 6):
        self.screen.fill(self.colors["BLACK"])
        #get the current object we are handling in all the objects provided
        if(dimension == 0):
            for sliceIndex in range(len(objects)):
            #if the object is a player, get the sprite based on the facing, and gun position
                for cellIndex in range(len(objects[sliceIndex])):
                #print(objects[sliceIndex])
                  #  objectImg = self.pygame.image.load(sprite_image_paths["player_1"])
                #elif(object[3] == "left"):
                #    objectImg = self.pygame.image.load(sprite_image_paths["player_2"])
                    if(len(objects[sliceIndex][cellIndex])> 0): #if there are objects in the cell
                    #print(objects[sliceIndex][cellIndex])
                        objectType = objects[sliceIndex][cellIndex][0][0] #first 0 is to access the top object in the cell, second is to access the type
                        if(objectType == "spawn"): #0 is automatically the top, because the way the map generates, the top is added in last
                            objectImg = self.pygame.image.load(sprite_image_paths["spawn"])
                        elif(objectType == "wall"):
                            objectImg = self.pygame.image.load(sprite_image_paths["wall"])
                        elif(objectType == "portal"):
                            portalType = objects[sliceIndex][cellIndex][0][2]
                            if(portalType == 0):
                                objectImg = self.pygame.image.load(sprite_image_paths["portal_1"])
                            elif(portalType == 1):
                                objectImg = self.pygame.image.load(sprite_image_paths["portal_2"])
                            elif(portalType == 2):
                                objectImg = self.pygame.image.load(sprite_image_paths["portal_3"])
                            elif(portalType == 3):
                                objectImg = self.pygame.image.load(sprite_image_paths["portal_4"])
                        elif(objectType == "goal"):
                            objectImg = self.pygame.image.load(sprite_image_paths["goal"])
                    
                        objectX = round(cellIndex * self.sprite_size * self.size_multiplier)
                        objectY = round(sliceIndex * self.sprite_size * self.size_multiplier)
                        
                        objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                        self.screen.blit(objectImg, (objectX, objectY))
                    
                    else:
                        objectX = round(cellIndex * self.sprite_size * self.size_multiplier)
                        objectY = round(sliceIndex * self.sprite_size * self.size_multiplier)
                        
                        objectImg = self.pygame.image.load(sprite_image_paths["background"])
                        objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                        self.screen.blit(objectImg, (objectX, objectY))
                    
                    
                    playerImg = self.pygame.image.load(sprite_image_paths["player_1"])
                    playerImg = self.pygame.transform.scale(playerImg, (round(self.player_size * self.size_multiplier), round(self.player_size * self.size_multiplier)))
                    self.screen.blit(playerImg, (playerX, playerY))
            #print(objects[0])
            #print("bruh")
                    
        elif(dimension == 1):
            #slice number is distance from top
            #rendercell is the cell index currently used
            #renderslice is the slice currently used, which shouldn't change until portal is touched
            for renderCell in range(len(objects[renderSlice])):
                for heightOfBackground in range(len(objects)):
                    #print("height of bg: " + str(heightOfBackground))
                    #print("rendercell: " + str(renderCell))
                    objectX = round(renderCell * self.sprite_size * self.size_multiplier)
                    objectY = round(heightOfBackground * self.sprite_size * self.size_multiplier)
                        
                    objectImg = self.pygame.image.load(sprite_image_paths["side_background"])
                    objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                    self.screen.blit(objectImg, (objectX, objectY))
            
            for renderCell in range(len(objects[renderSlice])):
                #print("render cell: " + str(renderCell))
                if(len(objects[renderSlice][renderCell])> 0):
                    #verticalBlockIndex is the index for how many solid blocks the current block is from the top block
                    for verticalBlockIndex in range(len(objects[renderSlice][renderCell])):
                        objectType = objects[renderSlice][renderCell][verticalBlockIndex][0]
                        
                        if(objectType == "spawn"): #0 is automatically the top, because the way the map generates, the top is added in last
                            objectImg = self.pygame.image.load(sprite_image_paths["spawn"])
                        elif(objectType == "wall"):
                            objectImg = self.pygame.image.load(sprite_image_paths["wall"])
                        elif(objectType == "portal"):
                            portalType = objects[renderSlice][renderCell][0][2]
                            if(portalType == 0):
                                objectImg = self.pygame.image.load(sprite_image_paths["s_portal_1"])
                            elif(portalType == 2):
                                objectImg = self.pygame.image.load(sprite_image_paths["s_portal_3"])
                        elif(objectType == "goal"):
                            objectImg = self.pygame.image.load(sprite_image_paths["side_goal"])
                            
                        objectX = round(renderCell * self.sprite_size * self.size_multiplier)
                        objectY = round((len(objects) - objects[renderSlice][renderCell][verticalBlockIndex][1])* self.sprite_size * self.size_multiplier)
                        
                        objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                        self.screen.blit(objectImg, (objectX, objectY))
                
                #else:                
                
                

                playerImg = self.pygame.image.load(sprite_image_paths["player_1"])
                playerImg = self.pygame.transform.scale(playerImg, (round(self.player_size * self.size_multiplier), round(self.player_size * self.size_multiplier)))
                self.screen.blit(playerImg, (playerX, playerY))

                
                
        elif(dimension == 2):
            pass
            #slice number is distance from left

            for slicenum in range(len(objects)):
                for heightOfBackground in range(len(objects)):
                    #print("height of bg: " + str(heightOfBackground))
                    #print("rendercell: " + str(renderCell))
                    objectX = round(slicenum * self.sprite_size * self.size_multiplier)
                    objectY = round(heightOfBackground * self.sprite_size * self.size_multiplier)
                        
                    objectImg = self.pygame.image.load(sprite_image_paths["side_background"])
                    objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                    self.screen.blit(objectImg, (objectX, objectY))
                    
            for slicenum in range(len(objects)) :
                if(len(objects[slicenum][cellnum])> 0):
                    #verticalBlockIndex is the index for how many solid blocks the current block is from the top block
                    for verticalBlockIndex in range(len(objects[slicenum][cellnum])):
                        objectType = objects[slicenum][cellnum][verticalBlockIndex][0]
                        
                        if(objectType == "spawn"): #0 is automatically the top, because the way the map generates, the top is added in last
                            objectImg = self.pygame.image.load(sprite_image_paths["spawn"])
                        elif(objectType == "wall"):
                            objectImg = self.pygame.image.load(sprite_image_paths["wall"])
                        elif(objectType == "portal"):
                            portalType = objects[renderSlice][renderCell][0][2]
                            if(portalType == 1):
                                objectImg = self.pygame.image.load(sprite_image_paths["s_portal_2"])
                            elif(portalType == 3):
                                objectImg = self.pygame.image.load(sprite_image_paths["s_portal_4"])
                        elif(objectType == "goal"):
                            objectImg = self.pygame.image.load(sprite_image_paths["side_goal"])
                            
                        objectX = round(cellnum * self.sprite_size * self.size_multiplier)
                        objectY = round((len(objects) - objects[slicenum][cellnum][verticalBlockIndex][1])* self.sprite_size * self.size_multiplier)
                        
                        objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                        self.screen.blit(objectImg, (objectX, objectY))
                        
                playerImg = self.pygame.image.load(sprite_image_paths["player_1"])
                playerImg = self.pygame.transform.scale(playerImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                self.screen.blit(playerImg, (playerX, playerY))
            
            
        self.pygame.display.update()
        def checkwin(xpos, ypos, levelvarthing):
            if(levelvarthing == 1):
                distance = sqrt((xpos)^2+(ypos-2)^2)
                if distance <= 20:
                    return(True)
            elif(levelvarthing == 2):
                distance = sqrt((xpos-2)^2+(ypos-5)^2)
                if distance <= 20:
                    return(True)
            elif(levelvarthing == 3):
                distance = sqrt((xpos)^2+(ypos-9)^2)
                if distance <= 20:
                    return(True)
            elif(levelvarthing == 4):
                distance = sqrt((xpos-14)^2+(ypos-14)^2)
                if distance <= 20:
                    return(True)
        checkWin(playerX, playerY)


#beans
        
