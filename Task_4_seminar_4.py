#     Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#     (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# k = int(input("Введите степень k:  "))

k =int(input("Введите степень k: "))

import random

b = random.randint(0,100)
# print(b)

w=1
text= f'{b}'
while w<=k:
    text = text + f' + {random.randint(0,100)}*x**{w}'
    w+=1
    
print(text)
data = open('PYTHON\Homework_seminar_4\\task_4.txt', 'a')
data.writelines(f'{text}\n')





