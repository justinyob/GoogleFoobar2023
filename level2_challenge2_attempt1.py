import logging

logging.basicConfig(level=logging.DEBUG)

def solution(l, t):
    for l_index, it in enumerate(l):
        i = it 
        logging.info(f"The current working index is {l_index}")
        logging.info(f"The current working value is {i}")
        
        if i == t:
            logging.info("The current index is equal to t")
            return [0, 0]
        index = l_index
        for add_index, x in enumerate(l):
            if add_index == 0:
                logging.info("continue")
                continue
            logging.info(f"Currently testing {i + l[add_index]}")
            logging.info(f"Add Index is {add_index}")
            if i + add_index == t:
                result = [index, add_index]
                logging.info(f"Test Successful, result is {result}")
                return result
            else:
                logging.info(f"The current working index is {l_index}")
            index +=1
            i+=l[add_index]
    logging.info("No valid solution found")
    return [-1, -1]
        
solution([2, 3, 3, 7, 4], 6)

 
