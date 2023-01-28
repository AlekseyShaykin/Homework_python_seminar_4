# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


# route = 'PYTHON\Homework_seminar_4\\task_5.1_.txt'
# data = open(route, 'r')
# for line in data:
#     print(line)

 
# route1 = 'PYTHON\Homework_seminar_4\\task_5.2_.txt'
# data1 = open(route1, 'r')
# for line1 in data1:
#     print(line1)

# line = line.replace(" ","")
# text = line.split('+')
# text1 = text[0].split('=')
# text3 = text[1:]+text1[1:]
# # print(text3)

# line1 = line1.replace(" ","")
# txt = line1.split('+')
# txt1 = txt[0].split('=')
# txt3 = txt[1:]+txt1[1:]
# # print(txt3)

# text_final  = text3+txt3
# print(text_final)


# sum = 0
# for char in text_final:
#     if char.isdigit():
#         sum = sum+int(char)
# print(sum)


# # txt = (int(text_final[0][:-4])+int(text_final[2][:-4]))
# # print(txt)


# # if text_final[2][2:] == text_final[3][2:]:
# #     print('yes')
# # else:
# #     print('no')


# txt=[]

# for m in range(len(text_final)):
#     for n in range(len(text_final)-1):
#         if (text_final[m][2:]) == text_final[n+1][2:]:
#             txt.append((int(text_final[m][:-4]))+int((text_final[n+1][:-4])))
#         print(txt)




# решение

with open('PYTHON\Homework_seminar_4\\task_5.1_.txt', 'r') as file1:
    with open('PYTHON\Homework_seminar_4\\task_5.2_.txt', 'r') as file2:
        arg = (file1.read() + ' + ' + file2.read()).replace(' = 0', '').replace(' ', '').split('+')
dic = {}
for degree in arg:
    q = (degree + ' ').replace('*x^', ' ').replace('x^', '1 ').replace('*x', ' 1').replace('x', '1 1').split()
    q.append('0')
    if q[1] not in dic.keys():
        dic[q[1]] = [q[0]]
    else:
        dic[q[1]] += [q[0]]
dic = dict(sorted(dic.items(), reverse=True))
formula = ""
for i in dic.keys():
    sum = 0
    for j in dic[i]:
        sum += int(j)
    formula += str(sum) + '*x^' + str(i) + ' + '
formula = formula.replace('x^1', 'x').replace('*x^0', '').replace(' 1*', ' ').replace('+  +', '+').replace('+  ', '')
with open('res.txt', 'w') as file:
    file.write(formula + ' = 0')

            