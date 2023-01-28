# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import getcontext
from decimal import Decimal
import random
x = 11

lst = []
for i in range(x):
    lst.append(10**(-i))

lst2 = lst[1:]

y = random.randint(0, len(lst2)-1)
print(lst2[y])

c = 1/lst2[y]
index = 0
while c > 1:
    c = c/10
    index += 1


getcontext().prec = index+1
print(Decimal(22)/Decimal(7))


exit()
#2 вариант

a = int(input('введите нужную точность 1#= '))
pi_target = 0
for i in range(1, 1000000):
     pi_target += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
     print(str(pi_target)[:a + 2])