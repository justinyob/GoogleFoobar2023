def solution(x, y):
    master = x + y
    solution = []    
    for i in x:
        if master.count(i) == 1:
            solution.append(i)
    for i in y:
        if master.count(i) == 1:
            solution.append(i)
            
        
    return(solution[0])
