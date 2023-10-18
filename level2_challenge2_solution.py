def solution(l, t):
    for l_count, l_value in enumerate(l):
        values_remaining = len(l) - l_count - 1
        add_range = range(l_count, l_count + values_remaining)
        solution_value = l_value
        if l_value == t:
            return [l_count, l_count]
        for add_count, add_value in enumerate(add_range):
            solution_value += l[add_value + 1]
            if solution_value == t:
                solution = [l_count, l_count + add_count + 1]
                return solution
    return [-1, -1]

print(solution([4, 3, 5, 7, 5], 12))