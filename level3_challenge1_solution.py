def test(x, y):
    if [int(x), int(y)] == [1, 1]:
        return True
    else:
        return False

def solution(x, y):
    if test(x, y):
        return '0'
    else:
        steps = 0
        intX = int(x)
        intY = int(y)
        while True:
            if intX == intY or (intX % 2 == 0 and intY % 2 == 0):
                return "impossible"
            
            varComp = [intX, intY]
            if intX > intY:
                intX -= intY
                steps += 1
                
            elif intX < intY:
                intY -= intX
                steps +=1
                
            if [intX, intY] == [1, 1]:
                return str(steps)
            if [intX, intY] == varComp:
                return "impossible"