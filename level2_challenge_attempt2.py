import logging
logging.basicConfig(level=logging.DEBUG)

def solution(l, t):
    for l_count, l_value in enumerate(l):
        values_remaining = len(l) - l_count - 1
        logging.info(f"The current value is {l_value} and the values remaining are {values_remaining}") 
        logging.info(f"The range of values to add is {range(l_count, l_count + values_remaining)}")
        add_range = range(l_count, l_count + values_remaining)
        solution_value = l_value
        logging.info(f"The adding loop should add {values_remaining} times")
        for add_count, add_value in enumerate(add_range):   
            logging.info(f"Add count is {add_count}")
            logging.info(f"Adding {l[add_value + 1]}")
            solution_value += l[add_value + 1]
            if solution_value == t:
                logging.info(f"{solution_value} passed")
                solution = [l_count, l_count + add_count + 1]
                logging.info(f"This means that the result is {solution}")
                return solution
            else:
                logging.info(f"{solution_value} failed")
    logging.info("There is no valid solution")
    return [-1, -1]

solution([4, 3, 5, 7, 5], 12)