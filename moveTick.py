import pygame

#Decides new positional data depending on User Input

#####
#walls is the placeholder for the map detection
#####

#this is kinda janky but we were short on time
def getNewPlayerDat(pos1,pos2,vel1,vel2,objects,event,dim,sprite_size,size_multiplier):
    height = 1
    
    if(dim == 0):
        it=0
        for sliceIndex in range(len(objects)):
            for cellIndex in range(len(objects[sliceIndex])):
                if(len(objects[sliceIndex][cellIndex])> 0):
                    if(objects[sliceIndex][cellIndex][0][0] == "wall"):
                        
                        wallX = round(cellIndex * sprite_size * size_multiplier)
                        wallY = round((len(objects) - sliceIndex) * sprite_size * size_multiplier)
                        wallType = objects[sliceIndex][cellIndex][0][0]
                        #check every wall, if we find a wall that interferes, we will return that, otherwise just return one of them because they will all be the saem data
                        curPos1, curPos2, curVel1, curVel2, hitWall = moveTick(pos1, pos2,vel1,vel2,height,wallX,wallY,wallType,event,dim)
                        if(hitWall): #well it hit a wall rip, return the stuff
                            return(curPos1, curPos2, curVel1, curVel2)

        
        #ok so none of them were different so we know non of the walls will effect them
        return(curPos1, curPos2, curVel1, curVel2)




def moveTick(pos1,pos2,velo1,velo2,height,wallX,wallY,wallType,event,dim):#velo 1 is left right, velo 2 is up down. dim is bool, 1 if there is y and if there is gravity
    hitWall = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo1=-20
            if pos1+velo1 < wallX  and not wallType == 'portal':
                for x in range(20):
                    if pos1+19-x == wallX:#going left check
                        velo1 = 19-x
            pos1+=velo1
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo1=20
            if pos1+velo1 > wallX  and not wallType == 'portal':
                for x in range(20):
                    if pos1+19-x == wallX:
                        velo1 = 19-x
                        break
            pos1+=velo1
        if not dim:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                velo2=20
                if pos2+velo2 > wallY  and not wallY == 'portal':
                    for x in range(20):
                        if pos2+19-x == wallY:
                            velo2 = 19-x
                pos2+=velo2
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                velo2=-20
                if pos2+velo2 < wallY  and not wallType == 'portal':
                    for x in range(20):
                        if pos2+19-x == wallY:#going left check
                            velo2 = 19-x
                pos2+=velo2
        else:
            if onGround(height,wallY,dim,pos2):
                if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                    velo2=25
                    pos2+=velo2
            else:
                velo2-=1
                if velo2<-40:
                    velo2=-40
                pos2+=velo2
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo1=0
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo1=0
        if not dim:
            if event.key == pygame.K_d or event.key == pygame.K_DOWN:
                velo2=0
            if event.key == pygame.K_s or event.key == pygame.K_UP:
                velo2=-0
        else:
            if onGround(height,wallY,dim,pos2):
                if event.key == event.K_w or event.key == event.K_SPACE or event.key == event.K_UP:
                    velo2=25
                    pos2+=velo2
            else:
                velo2-=1
                if velo2<-40:
                    velo2=-40
                pos2+=velo2
    return pos1,pos2,velo1,velo2,hitWall

def onGround(height,wall,dim,pos):
    pass
    #to be implimented for based on needs