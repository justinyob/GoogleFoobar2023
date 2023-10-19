import logging
logging.basicConfig(level=logging.DEBUG)

def test(x, y):
    if [int(x), int(y)] == [1, 1]:
        return True
    else:
        return False


#M and F variables in prompt?
def solution(x, y):
    if test(x, y):
        logging.debug(f"I finished and my result is 0")
        return '0'
    else:
        steps = 0
        intX = int(x)
        intY = int(y)
        logging.debug(f"Variables are {intX} and {intY}")
        while True:
            
            if intX == intY or (intX % 2 == 0 and intY % 2 == 0):
                logging.debug(f"I finished and my result is impossible")
                return "impossible"

            varComp = [intX, intY]
            if intX > intY:
                intX -= intY
                steps += 1
                logging.debug([intX, intY])
            elif intX < intY:
                intY -= intX
                steps += 1
                logging.debug([intX, intY])
            
            if [intX, intY] == [1, 1]:
                logging.debug(f"I finished and my result is {str(steps)}")
                return str(steps)
        
            if [intX, intY] == varComp:
                logging.debug(f"I finished and my result is impossible")
                return "impossible"
            logging.debug(steps)

            
                 
print(solution('5000000000','5000000001'))
