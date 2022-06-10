def isInsideTheCircle(xa, ya, xc, yc, rc):
    dx = abs(xa-xc)
    dy = abs(ya-yc)
    
    if dx + dy <= rc: return True
    if dx > rc: return False
    if dy > rc: return False
    if dx^2 + dy^2 <= rc^2: 
        return True
    else:
        return False
