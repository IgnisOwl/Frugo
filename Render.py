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
                print(objects[sliceIndex][cellIndex])
        
                  #  objectImg = self.pygame.image.load(sprite_image_paths["player_1"])
                #elif(object[3] == "left"):
                #    objectImg = self.pygame.image.load(sprite_image_paths["player_2"])
                    
            #if(object[0][0:6] == "wall"):
                objectImg = self.pygame.image.load(sprite_image_paths["solid_wall"])
                    
            objectX = 
            objectY = object[2]
            
            objectImg = self.pygame.transform.scale(objectImg, (self.sprite_size * self.size_multiplier, self.sprite_size * self.size_multiplier))
            self.screen.blit(objectImg, (objectX, objectY))
        
        self.pygame.display.update()

#beans
        
