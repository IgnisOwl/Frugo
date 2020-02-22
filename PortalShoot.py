import math
def shootPortal(mX,mY,pos,wall,tiles):
    bool1,bool2,bool3=pygame.mouse.get_pressed()
    if bool1:#orange        
        for x in tiles:
            if x[0]=="portal_orange":
                try:
                    tiles.remove(index(x))#RETURN TILES
                except:
                    pass
            
            tiles.append(["portal_orange",x,y])
    if bool2:#bue
        pass
def detectWall(x,y,xPos,yPos,wall):
    if xPos:
        x=ceiling(x)
    else:
        x=floor(x)
    if yPos:
        y=ceiling(y)
    else:
        y=floor(y)
    for w in wall:
        if w[1]==x:
            return true,'x'
        elif w[2]==y:
            return true,'y'
    return false,'z'