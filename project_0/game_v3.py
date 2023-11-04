import numpy as np

def game_core_v3(number: int = 1) -> int:
    """функция возвращает количество попыток для нахождения заданного числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    np.random.seed(3) # фиксируем случайное число (псевдо)
    predict = np.random.randint(1, 101)
    numbers_lst = list(range(1, 101))
    
    low = 0
    high = len(numbers_lst)-1
    count = 0
    
    # рекурсивно с помощью бинарного поиска считаем количество попыток
    def rec(numbers_lst, low, high, predict, count):
      
      mid = (low + high)//2 # index, not a number

      if predict == numbers_lst[mid] or predict == numbers_lst[high]:
        count += 1
        return count
      elif predict < numbers_lst[mid]:
        count += 1
        return rec(numbers_lst, low, mid-1, predict, count)
      elif predict > numbers_lst[mid]:
        count += 1
        return rec(numbers_lst, mid+1, high, predict, count)
    
    return rec(numbers_lst, low, high, predict, count)



print(game_core_v3())
        