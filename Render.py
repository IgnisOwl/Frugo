class Render:
    def __init__(self, screen, pygame, colors, spriteSize, sizeMultiplier):
        self.screen = screen
        self.pygame = pygame
        self.colors = colors
        self.size_multiplier = sizeMultiplier
        self.sprite_size = spriteSize
    
    def render(self, objects, sprite_image_paths, dimension, playerX, playerY):
        self.screen.fill(self.colors["WHITE"])
        
        #get the current object we are handling in all the objects provided
        for sliceIndex in range(len(objects)):
            #if the object is a player, get the sprite based on the facing, and gun position
            for cellIndex in range(len(objects[sliceIndex])):
                if(dimension == 0):
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
                        objectY = round((len(objects) - sliceIndex) * self.sprite_size * self.size_multiplier)
            
                        objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                        self.screen.blit(objectImg, (objectX, objectY))
                    
                    else:
                        objectX = round(cellIndex * self.sprite_size * self.size_multiplier)
                        objectY = round((len(objects) - sliceIndex) * self.sprite_size * self.size_multiplier)
                        
                        objectImg = self.pygame.image.load(sprite_image_paths["background"])
                        self.screen.blit(objectImg, (objectX, objectY))
                    
                    
                    playerImg = self.pygame.image.load(sprite_image_paths["player_1"])
                    self.screen.blit(playerImg, (playerX, playerY))
                    
                elif(dimension == 1):
                    print("fuck you")
                elif(dimensino == 2):
                    print("fuck you x2")
        
        self.pygame.display.update()


#beans
        
