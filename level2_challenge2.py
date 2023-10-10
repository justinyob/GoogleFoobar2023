


"""
def solution(l, t):
    init_index = 0
    for i in l:
        print("index is " + str(init_index))
        if i == t:
                return (init_index, init_index) 
                print("solution is" + init_index + end_index)
        else:
            for p in range(1, len(l)):
                print(len(l))
                i = i + l[p]
                end_index =  init_index + p
                print(i)
                if i == t:
                    return (init_index, end_index)
                    print("solution is" + init_index + end_index)
        init_index = init_index + 1
"""
            
            
def solution(l, t):
    for i in l:
        if i == t:
            return [0, 0]
        for x in range(1, len(l)):
            z = i + l[x]
            if z == t:
                print(str([i, i + x]))

solution([4, 3, 5, 7, 8], 12)    
