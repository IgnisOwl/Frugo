import pygame

#Decides new positional data depending on User Input

#####
#walls is the placeholder for the map detection
#####

def moveTick(pos1,pos2,velo1,velo2,height,walls,event,dim,pWidth,pHeight):#velo 1 is left right, velo 2 is up down. dim is bool, 1 if there is y and if there is gravity
    if event.type == event.KEYDOWN:
        if event.key == event.K_A or event.key == event.K_LEFT:
            velo1=-20
            if pos1+velo < wall  and not wall == 'portal':
                for x in range(20):
                    if pos1+19-x == wall:#going left check
                        velo = 19-x
            pos1+=velo
        if event.key == event.K_D or event.key == event.K_RIGHT:
            velo1=20
            if pos1+velo > wall  and not wall == 'portal':
                for x in range(20):
                    if pos1+19-x == wall:#going left check
                        velo = 19-x
                        break
            pos1+=velo1
        if not dim:
            if event.key == event.K_S or event.key == event.K_DOWN:
                velo2=20
                if pos1+velo > wall  and not wall == 'portal':
                    for x in range(20):
                        if pos1+19-x == wall:#going left check
                            velo = 19-x
                pos2+=velo2
            if event.key == event.K_W or event.key == event.K_UP:
                velo2=-20
                if pos1+velo < wall  and not wall == 'portal':
                    for x in range(20):
                        if pos1+19-x == wall:#going left check
                            velo = 19-x
                pos2+=velo2
        else:
            if onGround(height,walls,dim,pos2):
                if event.key == event.K_w or event.key == event.K_SPACE or event.key == event.K_UP:
                    velo2=25
                    pos2+=velo2
            else:
                velo2-=1
                if velo2<-40:
                    velo2=-40
                pos2+=velo2
    elif event.type == event.KEYUP:
        if event.key == event.K_A or event.key == event.K_LEFT:
            velo1=0
        if event.key == event.K_D or event.key == event.K_RIGHT:
            velo1=0
        if not dim:
            if event.key == event.K_D or event.key == event.K_DOWN:
                velo2=0
            if event.key == event.K_S or event.key == event.K_UP:
                velo2=-0
        else:
            if onGround(height,walls,dim,pos2):
                if event.key == event.K_w or event.key == event.K_SPACE or event.key == event.K_UP:
                    velo2=25
                    pos2+=velo2
            else:
                velo2-=1
                if velo2<-40:
                    velo2=-40
                pos2+=velo2
    return pos1,pos2,velo1,velo2

def onGround(height,walls,dim,pos):
    pass
    #to be implimented for based on needs