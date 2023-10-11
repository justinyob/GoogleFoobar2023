


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
            
index_count = 0

def solution(l, t):    
    current_index = index_count
    for i in l:
        if i == t:
            return [0, 0]
        else:
            indexes_remaining = range(len(l) - l.index(i) - 1)
            for x in indexes_remaining:
                end_index = current_index + 1
                i+=l[x + current_index + 1]
                if i == t:
                    return [current_index, end_index]                
                end_index+=1
        current_index+=1
    return [-1, -1]

solution([2, 2, 2, 2], 17)

 
