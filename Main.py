import pygame
import Render
import GenerateMap
import moveTick
import os

FPS = 60

pygame.display.set_caption("Portal")


COLORS = {
    "BLACK" : (0,0,0),
    "RED" : (255,0,0),
    "BLUE" : (0,0,255),
    "GREEN" : (0,255,0),
    "WHITE" : (255,255,255)
}

SPRITE_SIZE = 32
SIZE_MULTIPLIER = 2 #size multiplier, to make bigger or smaller
PLAYER_SIZE = 20

#this means the level map is SPRITE_SIZE*AmountOfWalls = SCREEN_X or SCREEN_Y

#cell list is like: [[[[t,h], [t,h]]]] - thre reason we need height is because if we wanted an empty space right below solid block.
CELLS = [[[[ ]]]] #y[x[cell[th[]]]]
#also portals have [t,h,p] as in type, height, portal type (1 through 4)

#dictionary of all the paths to sprites
IMAGE_PATHS = {
    "player_1" : "assets/player_1.png",
    "wall" : "assets/wall.png",
    "goal" : "assets/goal.png",
    "side_goal": "assets/goal_side.png",
    "portal_1" : "assets/portal_1.png",
    "portal_2" : "assets/portal_2.png",
    "portal_3" : "assets/portal_3.png",
    "portal_4" : "assets/portal_4.png",
    "spawn" : "assets/spawn.png",
    "background": "assets/background.png",
}

class Main:
    def __init__(self):
        #vel and pos for player:
        self.velX = 0
        self.velY = 0
        self.posX = 0
        self.posY = 0
        self.pz = 0 #player z, will not change like y does
        self.cells, map_x, map_y = self.loadLevel(3)
        
        screen_x = map_x * SPRITE_SIZE * SIZE_MULTIPLIER
        screen_y = map_y * SPRITE_SIZE * SIZE_MULTIPLIER

        self.screen = pygame.display.set_mode((screen_x, screen_y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame, COLORS, SPRITE_SIZE, SIZE_MULTIPLIER, PLAYER_SIZE)
        self.mouseX = 0
        self.mouseY = 0

        self.portalCounter = 0


        self.currentDim = 0 #current Dimension

        self.inventory = [] #inventory is going to be organized like so: t, so depending on the block type you will know what to place down
       
    def mousePos(self):
        return pygame.mouse.get_pos()

    def loadLevel(self, level):
        imagePaths = []

        for x in range(len(os.listdir("Levels/l%s" % level))):
            imagePaths.append("Levels/l%s/%d.png" % (level, x)) #for each slice add one

        map = GenerateMap.getLevelMap(imagePaths)
        x,y = GenerateMap.getSpawnLocation(map) 
        self.posX = x * PLAYER_SIZE * SIZE_MULTIPLIER
        self.posY = y * PLAYER_SIZE * SIZE_MULTIPLIER
        return(map)

    def mainLoop(self):
        while True:
            self.posX,self.posY,self.velX,self.velY,self.currentDim, self.portalCounter = moveTick.moveTick(self.posX, self.posY, self.velX, self.velY, self.currentDim, self.cells, SPRITE_SIZE,SIZE_MULTIPLIER, PLAYER_SIZE, self.portalCounter)
            for event in pygame.event.get():
                                                                                                                                                                                                                                                                                                        
                if(event.type == pygame.QUIT):
                    pygame.quit()
            
            
            self.renderer.render(self.cells, IMAGE_PATHS, self.currentDim, self.posX, self.posY)
            self.clock.tick(FPS)
            
if __name__ == "__main__":
    main = Main()
    main.mainLoop()