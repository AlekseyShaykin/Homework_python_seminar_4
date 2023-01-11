# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности.

lst0 = [1,2,2,2,5,5,2,1,7,3,3,2,2,9,5,0,4]
lst = sorted(lst0)
print(f'отсортированный исходный список {lst}')

lst2=[]
for i in range(len(lst)):
    for j in range(len(lst)-i-1):
        if lst[i] == lst[i+j+1] and lst[i] != lst[i-1]:
            lst2.append(lst[i])
        break     
print(f'список повторяющихся элементов {lst2}')

print('---------------------')

set1 = set(lst)      #преобразуем исходный список в множество(при этом удаляются все повторения
set2 = set(lst2)    #преобразуем список повторяющихся элементов в множество
set3 = set1^set2    # находим симметрическую разность ^ (исключающее ИЛИ)
lst3 = list(set3)   # получившиеся множество преобразуем обратно в список
print(f'ОТВЕТ: список уникальных (неповторяющихся) элементов {lst3}')



