def convert(num):
    x = num % 8 + 1
    y = num // 8
    y = -(y - 8)
    coords = [x, y]
    return coords

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
        
            







def solution(src, dest):
    src_coords = convert(src)
    dest_coords = convert(dest)
    distance = [(src_coords[0] - dest_coords[0]), (src_coords[1] - dest_coords[1])]
    
    print(src_coords)
    print(dest_coords)
    print(distance)

    x_diff = distance[0]
    y_diff = distance[1]

    move(x_diff, y_diff)
    





"""   
    while x != 0 and y != 0:
        if abs(x) > abs(y):
            print("X distance is bigger")
            if x < 0:
                if y < 0:
                    x += 2
                    y +=1
                print([x, y])
        elif abs(x) == abs(y):
            print("X and Y distance's are equal")
        else:
            print("Y distance is bigger")
"""