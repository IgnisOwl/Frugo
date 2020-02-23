import pygame

#Decides new positional data depending on User Input


def gravity(velX, velY): #function for getting updated gravity, note that it does not handle any type of collision detection
    velY = velY - 0.5
    return(velX, velY)

def posFromVel(posX, posY, velX, velY):
    posX = posX + velX
    posY = posY + velY
    return(posX, posY)

def dampVelocity(velX, velY, dampFactor):
    #prone to go to 0

    if(velX < 0):
        velX = velX + dampFactor
    if(velX > 0):
        velX = velX - dampFactor


    if(velY < 0):
            velY = velY + dampFactor
    if(velY > 0):
        velY = velY - dampFactor

    return(velX, velY)

def moveTick(posX, posY, velX, velY, dim, objects, sprite_size, size_multiplier):
    acceleration = 2
    maxSpeed = 5 #not implemented yet
    damping = 0.7 #basically the friction
    dampingCollisionFactor = 2 #multiply the damping if its colliding
    bounceDampening = 15 #-vel/BD
    leway = 5 #collision leway


    if(dim == 0): #birds eye
        key = pygame.key.get_pressed()
        #if(not key[pygame.K_a] or not key[pygame.K_d] or not key[pygame.K_w] or not key[pygame.K_s]):
        velX, velY = dampVelocity(velX, velY, damping)
        if key[pygame.K_a]:
           if(-velX <= maxSpeed):
                velX = velX - acceleration
        if key[pygame.K_d]:
            if(velX <= maxSpeed):
                velX = velX + acceleration
        if key[pygame.K_w]:
           if(-velY <= maxSpeed):
                velY = velY - acceleration
        if key[pygame.K_s]:
            if(velY <= maxSpeed):
                velY = velY + acceleration
    #now calculate the positions and if they should apply from the velocities
    possibleX, possibleY = posFromVel(posX, posY, velX, velY)
    #now check if the collision happens, if it does, don't actually update the values
    if(not collision(objects, possibleX, possibleY, dim, sprite_size, size_multiplier)):
        posX, posY = possibleX, possibleY
    else:
        velX, velY = -(velX/bounceDampening), -(velY/bounceDampening)

    return(posX, posY, velX, velY)



def collision(objects, posX, posY, dim, sprite_size, size_multiplier):
    if(dim == 0):
        #go through every wall
        for sliceIndex in range(len(objects)):
            for cellIndex in range(len(objects[sliceIndex])):
                if(len(objects[sliceIndex][cellIndex])> 0):
                    wallX = round(cellIndex * sprite_size * size_multiplier)
                    wallY = round((len(objects) - sliceIndex - 1) * sprite_size * size_multiplier)
                    wall_width = round(sprite_size * size_multiplier)
                    wallType = objects[sliceIndex][cellIndex][0][0]

                    if(posX > wallX and posX < wallX+wall_width and posY > wallY and posY < wallY+wall_width or
                           posX+(sprite_size* size_multiplier) > wallX and posX+(sprite_size* size_multiplier) < wallX+(sprite_size* size_multiplier) and posY > wallY and posY < wallY+wall_width or
                           posX > wallX and posX < wallX + wall_width and posY+(sprite_size* size_multiplier) > wallY and posY+(sprite_size* size_multiplier) < wallY+wall_width or
                           posX+(sprite_size* size_multiplier) > wallX and posX+(sprite_size* size_multiplier) < wallX+wall_width and posY+(sprite_size* size_multiplier)>wallY and posY+(sprite_size* size_multiplier)<wallY+wall_width): #if its in the bounds
                        if(not isPassable(objects[sliceIndex][cellIndex][0][0])):

                            return(True)
                        else:
                            if(not isPortal(objects[sliceIndex][cellIndex]) == False):
                                pass
                                #print(isPortal(objects[sliceIndex][cellIndex]))

    return(False)

def isPassable(wallType):
    if(wallType == "portal" or wallType == "goal"):
        return(True)
    else:
        return(False)

def isPortal(block):
    z=0
    if(block[z][0] == "portal"):
        return(block[z][2]) #portal type
    else:
        return(False)