from matplotlib.patches import Circle

def isInsideTheCircle(xa, ya, xc, yc, rc):
    circ = Circle((xc, yc), radius = rc)

    return(circ.contains_point([xa, ya]))

if __name__ == '__main__':
    xa = float(input())
    ya = float(input())
    xc = float(input())
    yc = float(input())
    rc = float(input())
    result = isInsideTheCircle(xa, ya, xc, yc, rc)
    print(result)
