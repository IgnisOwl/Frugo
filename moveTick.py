import pygame

#Decides new positional data depending on User Input
def moveTick(pos,velo,height,walls, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo[0]=-20
            pos[0]+=velo[0]
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo[0]=20
            pos[0]+=velo[0]
        if onGround(height,walls, pos):
            if event.key == pygame.K_w or event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                velo[1]=25
                pos[1]+=velo[1]
        else:
            velo[1]-=5
            if velo[1]<-40:
                velo[1]=-40
            pos[1]+=velo[1]
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            velo[0]=0
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            velo[0]=0
    return pos,velo

def onGround(height,walls, pos):
    w=False
    for a in walls:
        if a[2]==(height+pos[1]):
            w=True
    return w