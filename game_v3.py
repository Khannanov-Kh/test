import numpy as np

def game_core_v3(number: int = 1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    np.random.seed(1)
    predict = np.random.randint(1, 101)
    print(predict)
    numbers_lst = list(range(1, 101))
    print(numbers_lst)
    low, high = numbers_lst[0], len(numbers_lst) # get indexes

    mid = (low + high)//2 # index, not a number
    print(mid)
    count = 0
    while low <= high:
        if predict == numbers_lst[mid]:
            count += 1
            
        elif predict < numbers_lst[mid]:
            count += 1
            high = mid-1
            
        else:
            predict > numbers_lst[mid]
            count += 1
            low = mid+1

    return count


game_core_v3()
        