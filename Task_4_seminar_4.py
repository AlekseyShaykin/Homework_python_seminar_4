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
data = open('PYTHON\Homework_seminar_4\\task_4.txt', 'w')
data.writelines(f'{text}\n')


# 2 способ___________________

from random import randint

k = int(input('Insert equation power: '))
koefs = list()
for i in range(1, k + 2):
    koefs.append(randint(1, 100))

ans = list()
for i in range(len(koefs)):
    if k == 1:
        ans.append(f'{koefs[i]}*x')
    elif k == 0:
        ans.append(f'{koefs[i]}')
    else:
        ans.append(f'{koefs[i]}*x**{k}')
    flag = randint(0, 1)
    if flag == 1:
        ans.append('+')
    elif flag == 0:
        ans.append('-')
    k -= 1

ans.pop(-1)
ans.append('=0')
fout = open('output.txt', 'w')
fout.write(''.join(ans))
fout.close()




