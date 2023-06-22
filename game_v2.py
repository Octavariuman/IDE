"""Game - guess the number 
Компьютер сам загадывает и сам угадывает
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """_summary_

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count+=1
        predict_number = np.random.randint(1, 100)
        if number == predict_number:
            break #выходим из цикла
    
    return(count)

#print(f'кол-во попыток: {random_predict(10)}')

def score_game(random_predict) -> int:
    """За какое количество попытоок в срденем зв 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): фунеуия угадывания

    Returns:
        int: среднее кол-во попыток
    """
    count_ls = []
    np.random.seed(1) #фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f'Выш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    #RUN
    score_game(random_predict)

