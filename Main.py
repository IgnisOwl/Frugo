import pygame
import Render
import GenerateMap
import moveTick
import PortalShoot

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

#NOTE: The item list is like: [["portal_orange", x, y, facing], ["player", x, y, facing]]    #Type, x, y, optional things... NOTE: portal can be facing 4 directions, floor, leftwall, ceiling, rightwall
DEFAULT_ITEMS = ["player", (SPRITE_SIZE*SIZE_MULTIPLIER)*2, SCREEN_Y-((SPRITE_SIZE*SIZE_MULTIPLIER)*2), "right", 0, 0, 0] #adds to the map NOTE: IN THE FUTURE MAKE A FUNCTION TO CALCULATE OFFSET FOR VALUES INSTEAD OF JUST USING SIZE AND MJLT
#format for player: [name, x, y, facing, gun_position(0-4), veloX, veloY]
#format for portal: ["portal_orange", x, y, facing]
#format for walls: ["wall", x, y] just change name to sumthin else for win or start

#dictionary of all the paths to sprites
IMAGE_PATHS = {
    "player_1" : "player_1.png",
    "solid_wall" : "solid_wall.png"
}

MAP_NAME = "level_1_map.png"


#SIDESCROLL_BOUNDS = 50 #how many pixels the player can move before sidescrolling takes place

class Main:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.clock = pygame.time.Clock()
        self.renderer = Render.Render(self.screen, pygame, COLORS, SPRITE_SIZE, SIZE_MULTIPLIER)
        self.items = GenerateMap.getLevelMap(MAP_NAME, COLORS, SPRITE_SIZE, DEFAULT_ITEMS)
        self.mouseX = 0
        self.mouseY = 0
       
    def mousePos(self):
        return pygame.mouse.get_pos()

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                ##########CCCCCHANGE LATER: !!!!!!!!!!
                self.items[0][1:3], self.items[0][5:7] = moveTick.moveTick(self.items[0][1:3:], self.items[0][5:7], SPRITE_SIZE, self.items[1:], event)
                
                if(event.type == pygame.QUIT):
                    pygame.quit()
                
            #PortalShoot.shootPortal(self.mousePos()))
            
            
            self.renderer.render(self.items, IMAGE_PATHS)
            self.clock.tick(FPS)

if __name__ == "__main__":
    main = Main()
    main.mainLoop()
