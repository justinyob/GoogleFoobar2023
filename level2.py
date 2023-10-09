move_dict = {
    (0, 0): 0,
    (0, 1): 3,
    (0, 2): 2,
    (0, 3): 3,
    (0, 4): 2,
    (0, 5): 3,
    (0, 6): 4,
    (0, 7): 5,
    (1, 0): 3,
    (1, 1): 4,
    (1, 2): 1,
    (1, 3): 2,
    (1, 4): 3,
    (1, 5): 4,
    (1, 6): 3,
    (1, 7): 4,
    (2, 0): 2,
    (2, 1): 1,
    (2, 2): 4,
    (2, 3): 3,
    (2, 4): 2,
    (2, 5): 3,
    (2, 6): 4,
    (2, 7): 5,
    (3, 0): 3,
    (3, 1): 2,
    (3, 2): 3,
    (3, 3): 2,
    (3, 4): 3,
    (3, 5): 4,
    (3, 6): 3,
    (3, 7): 4,
    (4, 0): 2,
    (4, 1): 3,
    (4, 2): 2,
    (4, 3): 3,
    (4, 4): 4,
    (4, 5): 3,
    (4, 6): 4,
    (4, 7): 5,
    (5, 0): 3,
    (5, 1): 4,
    (5, 2): 3,
    (5, 3): 4,
    (5, 4): 3,
    (5, 5): 4,
    (5, 6): 5,
    (5, 7): 4,
    (6, 0): 4,
    (6, 1): 3,
    (6, 2): 4,
    (6, 3): 3,
    (6, 4): 4,
    (6, 5): 5,
    (6, 6): 4,
    (6, 7): 5,
    (7, 0): 5,
    (7, 1): 4,
    (7, 2): 5,
    (7, 3): 4,
    (7, 4): 5,
    (7, 5): 4,
    (7, 6): 5,
    (7, 7): 6
}

def convert(num):
    x = num % 8 + 1
    y = num // 8
    y = -(y - 8)
    coords = [x, y]
    return coords

"""

def validate(coords):
    x = coords[0]
    y = coords[1]
    if x > 0 and y > 0 and x < 9 and y < 9:
        return True
    else:
        return False 



def gen_moves(coords):
    moves = []
    x = coords[0]
    y = coords[1]
    options = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    for i in options:
        move_coords = [x, y]
        x_move = i[0]
        y_move = i[1]
        move_coords[0] = move_coords[0] + x_move
        move_coords[1] = move_coords[1] + y_move
        if validate(move_coords):
            moves.append(move_coords)
            print(move_coords)
            print("Valid Move")
      
def move(x, y):
    while x != 0 or y != 0:
        while abs(x) > abs(y):
            print("X distance is bigger")
            if x < 0:
                if y <= 0:
                    x += 2
                    y +=1
                print([x, y])
            elif x

        elif abs(x) == abs(y):
            print("X and Y distance's are equal")
            if x 

        else:
            print("Y distance is bigger")    
"""
def calc(x_diff, y_diff):
    tuple_dist = (x_diff, y_diff)
    for i in move_dict:
        if i == tuple_dist:
            return move_dict[i]

def solution(src, dest):
    src_coords = convert(src)
    dest_coords = convert(dest)
    distance = [(dest_coords[0] - src_coords[0]), (dest_coords[1] - src_coords[1])]

    x_diff = abs(distance[0])
    y_diff = abs(distance[1])

    
    return calc(x_diff, y_diff)