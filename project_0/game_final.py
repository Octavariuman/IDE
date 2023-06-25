"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def predict(number: int = 1) -> int:
    """угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    s = 0 #задаем начало диапазона угадываения
    n = 101 #задаем конец диапазона угадываения
    while True:
        count += 1
        predict_number = int((s + n) // 2)  # предполагаемое число
        if number < predict_number:
            n = predict_number #обновляем диапазон угадываения
        elif number > predict_number:
            s = predict_number #обновляем диапазон угадываения
        else:
            break  # выход из цикла если угадали           
            
    return count

def score_game(predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict)
