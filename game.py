"""Game - guess the number """

import numpy as np

number = np.random.randint(1, 101) #загадываем число

#кол-во попыток
count = 0

while True:
    count+=1
    predict_number = int(input("Угадай число от 1 до 100: "))

    if predict_number > number:
        print("Число должо быть меньше!")
    
    elif predict_number < number:
        print("Число должо быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count}")
        break #конец игры и вызод из цикла
    


