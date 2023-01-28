# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.


# n = int(input("Input number "))

# x = 128
# y = 2

# i=0
# while x%y==0:
#     x=(x/y)
#     i+=1
# print(i)

# def Method(a, b):
#     if a % b != 0:
#         return 0
#     if a % b == 0:
#         return Method(a/b)
 


n = 63
x = 1

lst = []
while x <= n:
    if n % x == 0:
        lst.append(x)
    x += 1
print(lst)

count=0

i=1
while n%lst[i]==0:
        n = n/lst[i]
        count+=1
        print(count)
else:
       n = n/lst[i+1]
       count+=1
       print(count)




# второй способ
n = int(input("Введите число N: "))
i = 2 
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")