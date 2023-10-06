def translate(num):
    x = num % 8 + 1
    y = num // 8
    y = -(y - 8)
    coords = [x, y]
    return coords

def move(x, y):
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
 

def solution(src, dest):
    src_coords = translate(src)
    dest_coords = translate(dest)
    distance = [(src_coords[0] - dest_coords[0]), (src_coords[1] - dest_coords[1])]

    print(src_coords)
    print(dest_coords)
    print(distance)

    x_diff = distance[0]
    y_diff = distance[1]

    move(x_diff, y_diff)
    

solution(17, 12)


