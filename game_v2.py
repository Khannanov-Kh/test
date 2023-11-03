import numpy as np

def random_predict(number:int=1) -> int:
    """number of tries to guess some number
    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_ => return number of tries
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break # end cycle
    return count

def score_game(random_predict):
    
    count_ls = [] # list to keep number of tries
    np.random.seed(1)
    random_array = np.random.randint(1,101, size = (1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return score

score_game(random_predict)