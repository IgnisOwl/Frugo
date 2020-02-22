def portalPlayerPos(x):
    pos = []
    for y in x:
        bool1 = False
        bool2 = False
        bool3 = False
        if y[0] == 'player':
            pos[0]=y
            bool1=True
        if y[1] == 'portalO':
            pos[1]=y
            bool2=True    
        if y[2] == 'portalB':
            pos[2]=y
            bool3=True
        if bool1 and bool2 and bool3:
            break
    if (pos[0][1] == pos[1][1] and pos[0][2]==pos[1][2]):#o to b
        if pos[2][3]=='ceiling':
            pos[0][1]=pos[2][1]
            pos[0][2]=pos[2][2]-1
        if pos[2][3]=='leftwall':
            pos[0][1]=pos[2][1]+1
            pos[0][2]=pos[2][2]
        if pos[2][3]=='floor':
            pos[0][1]=pos[2][1]
            pos[0][2]=pos[2][2]+1
        if pos[2][3]=='rightwall':
            pos[0][1]=pos[2][1]-1
            pos[0][2]=pos[2][2]
    elif (pos[0][1]==pos[2][1] and pos[0][2]==pos[2][2]):#b to o
        if pos[1][3]=='ceiling':
            pos[0][1]=pos[1][1]
            pos[0][2]=pos[1][2]-1
        if pos[1][3]=='leftwall':
            pos[0][1]=pos[1][1]+1
            pos[0][2]=pos[1][2]
        if pos[1][3]=='floor':
            pos[0][1]=pos[1][1]
            pos[0][2]=pos[1][2]+1
        if pos[1][3]=='rightwall':
            pos[0][1]=pos[1][1]-1
            pos[0][2]=pos[1][2]
    return (pos[0][1],pos[0][2])