class Render:
    def __init__(self, screen, pygame, colors, spriteSize, sizeMultiplier):
        self.screen = screen
        self.pygame = pygame
        self.colors = colors
        self.size_multiplier = sizeMultiplier
        self.sprite_size = spriteSize
    
    def render(self, objects, sprite_image_paths):
        self.screen.fill(self.colors["WHITE"])
        
        #get the current object we are handling in all the objects provided
        for sliceIndex in range(len(objects)):
            #if the object is a player, get the sprite based on the facing, and gun position
            for cellIndex in range(len(objects[sliceIndex])):
                #print(objects[sliceIndex])
                  #  objectImg = self.pygame.image.load(sprite_image_paths["player_1"])
                #elif(object[3] == "left"):
                #    objectImg = self.pygame.image.load(sprite_image_paths["player_2"])
                if(len(objects[sliceIndex][cellIndex])> 0):
                    #print(objects[sliceIndex][cellIndex])
                    if(objects[sliceIndex][cellIndex][0][0] == "wall"): #0 is automatically the top, because the way the map generates, the top is added in last
                    #if(objects[sliceIndex][cellIndex][self.getTop(objects[sliceIndex][cellIndex])][0] == "wall"):
                        objectImg = self.pygame.image.load(sprite_image_paths["solid_wall"])
                else:
                    objectImg = self.pygame.image.load(sprite_image_paths["player_1"])
                    
                objectX = round(cellIndex * self.sprite_size * self.size_multiplier)
                objectY = round((len(objects) - sliceIndex) * self.sprite_size * self.size_multiplier)
            
                objectImg = self.pygame.transform.scale(objectImg, (round(self.sprite_size * self.size_multiplier), round(self.sprite_size * self.size_multiplier)))
                self.screen.blit(objectImg, (objectX, objectY))
        
        self.pygame.display.update()


#beans
        
