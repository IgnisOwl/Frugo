import pygame

#Decides new positional data depending on User Input


def gravity(velX, velY, dampFactor): #function for getting updated gravity, note that it does not handle any type of collision detection
    velY = velY + 0.5 + dampFactor
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


    #to fix drifting:
    if(velX<dampFactor and velX>0):
        velX = 0
    if(velX>-dampFactor and velX<0):
        velX = 0

    if(velY<dampFactor and velY>0):
        velY = 0
    if(velY>-dampFactor and velY<0):
        velY = 0

    return(velX, velY)

def moveTick(posX, posY, velX, velY, dim, objects, sprite_size, size_multiplier, player_size, portalCounter, renderSlice):
    acceleration = 2
    maxSpeed = 5 #not implemented yet
    damping = 0.7 #basically the friction
    dampingCollisionFactor = 2 #multiply the damping if its colliding
    bounceDampening = 15 #-vel/BD
    jumpAcceleration = 5


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
        
        renderSlice = round(posY/(sprite_size*size_multiplier)) #must round to nearest factor of the sprite size, so each row
        #renderSlice = 8
        print(renderSlice)
    
    if(dim == 1):
        velX, velY = gravity(velX, velY, damping); #we want the gravity to overcome the damp factor
        key = pygame.key.get_pressed()
        #velX, velY = dampVelocity(velX, velY, damping)
        if key[pygame.K_a]:
            if(-velX <= maxSpeed):
                velX = velX - acceleration
        if key[pygame.K_d]:
            if(velX <= maxSpeed):
                velX = velX + acceleration
        if key[pygame.K_w]: #jump
            #if(onGround()): #on ground
            #    velY = velY - jumpAcceleration
            if(velY > -5): #on ground
                velY = velY - jumpAcceleration

    #now calculate the positions and if they should apply from the velocities
    possibleX, possibleY = posFromVel(posX, posY, velX, velY)
    #now check if the collision happens, if it does, don't actually update the values

    col = collision(objects, possibleX, possibleY, dim, sprite_size, size_multiplier, player_size, portalCounter, renderSlice)
    if(not col[0]):
        posX, posY = possibleX, possibleY
    else:
        velX, velY = -(velX/bounceDampening), -(velY/bounceDampening)
        

    return(posX, posY, velX, velY, col[1], col[2], renderSlice)

def onGround():
    return(True)

def collision(objects, posX, posY, dim, sprite_size, size_multiplier, player_size, portalCounter, renderSlice):
    
    
    if(dim == 0):
        #go through every wall
        for sliceIndex in range(len(objects)):
            for cellIndex in range(len(objects[sliceIndex])):
                if(len(objects[sliceIndex][cellIndex])> 0):
                    wallX = round(cellIndex * sprite_size * size_multiplier)
                    wallY = round(sliceIndex * sprite_size * size_multiplier)
                    wall_width = round(sprite_size * size_multiplier)
                    wallType = objects[sliceIndex][cellIndex][0][0]

                    if(posX > wallX and posX  < wallX+wall_width and posY  > wallY and posY < wallY+wall_width or
                           posX+(player_size* size_multiplier)  > wallX and posX+(player_size* size_multiplier)  < wallX+(player_size* size_multiplier) and posY  > wallY and posY  < wallY+wall_width or
                           posX > wallX and posX < wallX + wall_width and posY+(player_size* size_multiplier) > wallY and posY+(player_size* size_multiplier) < wallY+wall_width or
                           posX+(player_size* size_multiplier)  > wallX and posX+(player_size* size_multiplier)  < wallX+wall_width and posY+(player_size* size_multiplier)  >wallY and posY+(player_size* size_multiplier)  <wallY+wall_width): #if its in the bounds
                        if(not isPassable(wallType)):

                            return(True, dim, portalCounter)
                        else:
                            if(isPortal(objects[sliceIndex][cellIndex])[0] == True):
                                portalCounter+=1 #for the countdown
                                #print(portalCounter)
                                if(isPortal(objects[sliceIndex][cellIndex])[1] == 0 or isPortal(objects[sliceIndex][cellIndex])[1] == 2):
                                    if(portalCounter>50):#reached time
                                        portalCounter = 0
                                        return(True, 1, portalCounter)
                    #else:
                    #        portalCounter = 0

    if(dim == 1):
        for renderCell in range(len(objects[renderSlice])):
            for verticalBlockIndex in range(len(objects[renderSlice][renderCell])):
                wallX = round(renderCell * sprite_size * size_multiplier)
                wallY = round(sprite_size * size_multiplier * 9 - sprite_size * size_multiplier *verticalBlockIndex) #9 change
                #print(posY)
                #print(posX)
                #print(wallY)
                #print(wallX)
                wallType = objects[renderSlice][renderCell][verticalBlockIndex][0]
                wall_width = round(sprite_size * size_multiplier)

                if(posX > wallX and posX  < wallX+wall_width and posY  > wallY and posY < wallY+wall_width or
                           posX+(player_size* size_multiplier)  > wallX and posX+(player_size* size_multiplier)  < wallX+(player_size* size_multiplier) and posY  > wallY and posY  < wallY+wall_width or
                           posX > wallX and posX < wallX + wall_width and posY+(player_size* size_multiplier) > wallY and posY+(player_size* size_multiplier) < wallY+wall_width or
                           posX+(player_size* size_multiplier)  > wallX and posX+(player_size* size_multiplier)  < wallX+wall_width and posY+(player_size* size_multiplier)  >wallY and posY+(player_size* size_multiplier)  <wallY+wall_width or
                           posY > sprite_size * size_multiplier * len(objects[renderSlice]) - sprite_size): #ground

                        if(not isPassable(wallType)):
                            return(True, dim, portalCounter)
                        else:
                            #print(isPortalD(objects[renderSlice][renderCell][verticalBlockIndex]))
                            if(isPortalD(objects[renderSlice][renderCell][verticalBlockIndex])[0] == True):
                            #if(objects[renderSlice][renderCell][verticalBlockIndex][0] =="portal"):
                                portalCounter+=1 #for the countdown
                                #print(portalCounter)
                                if(isPortalD(objects[renderSlice][renderCell][verticalBlockIndex])[1] == 0 or isPortalD(objects[renderSlice][renderCell][verticalBlockIndex])[1] == 2):
                                    if(portalCounter>50):#reached time
                                        portalCounter = 0
                                        return(True, 0, portalCounter)

                    #else:
                    #        portalCounter = 0

    return(False, dim, portalCounter)

def isPassable(wallType):
    if(wallType == "portal" or wallType == "goal"):
        return(True)
    else:
        return(False)

def isPortal(block):
    z=0
    if(block[z][0] == "portal"):
        return(True, block[z][2]) #portal type
    else:
        return(False, None)

def isPortalD(block):
    if(block[0] == "portal"):
        return(True, block[2]) #portal type
    else:
        return(False, None)