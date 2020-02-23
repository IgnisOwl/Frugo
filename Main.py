import pygame
import Render
import GenerateMap
import moveTick
import os

SCREEN_X = 950
SCREEN_Y = 550
#this means the level map is SPRITE_SIZE*AmountOfWalls = SCREEN_X or SCREEN_Y

FPS = 60

pygame.display.set_caption("Portal")

COLORS = {
    "BLACK" : (0,0,0),
    "RED" : (255,0,0),
    "BLUE" : (0,0,255),
    "GREEN" : (0,255,0),
    "WHITE" : (255,255,255)
}

SPRITE_SIZE = 50
SIZE_MULTIPLIER = 1 #size multiplier, to make bigger or smaller

#cell list is like: [[[[t,h], [t,h]]]] - thre reason we need height is because if we wanted an empty space right below solid block.
CELLS = [[[[ ]]]] #y[x[cell[th[]]]]

#dictionary of all the paths to sprites
IMAGE_PATHS = {
    "player_1" : "player_1.png",
    "solid_wall" : "solid_wall.png"
}

MAP_NAME = "level_1_map.png"

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame, COLORS, SPRITE_SIZE, SIZE_MULTIPLIER)
        self.mouseX = 0
        self.mouseY = 0

        #vel and pos for player:
        self.vel1 = 0
        self.vel2 = 0
        self.pos1 = 0
        self.pos2 = 0
        self.pz = 0 #player z, will not change like y does

        self.currentDim = 0 #current Dimension

        self.cells = self.loadLevel(3)
        self.inventory = [] #inventory is going to be organized like so: t, so depending on the block type you will know what to place down
       
    def mousePos(self):
        return pygame.mouse.get_pos()

    def loadLevel(self, level):
        imagePaths = []

        for x in range(len(os.listdir("Levels/l%s" % level))):
            imagePaths.append("Levels/l%s/%d.png" % (level, x)) #for each slice add one

        return(GenerateMap.getLevelMap(imagePaths))

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                self.pos1,self.pos2,self.vel1,self.vel2 = moveTick.getNewPlayerDat(self.pos1, self.pos2, self.vel1, self.vel2, self.cells,event,self.currentDim,SPRITE_SIZE,SIZE_MULTIPLIER)
                                                                                                                                                                                                                                                                                                        
                if(event.type == pygame.QUIT):
                    pygame.quit()
            
            
            self.renderer.render(self.cells, IMAGE_PATHS, self.currentDim, self.pos1, self.pos2)
            self.clock.tick(FPS)

if __name__ == "__main__":
    main = Main()
    main.mainLoop()