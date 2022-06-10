import math

def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    x = math.sqrt(sq)
    if x == int(x):
        return (x+1) * (x+1)
    else:
        return -1
