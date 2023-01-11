# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


route = 'PYTHON\Homework_seminar_4\\task_5.1_.txt'
data = open(route, 'r')
for line in data:
    print(line)

 
route1 = 'PYTHON\Homework_seminar_4\\task_5.2_.txt'
data1 = open(route1, 'r')
for line1 in data1:
    print(line1)

line = line.replace(" ","")
text = line.split('+')
text1 = text[0].split('=')
text3 = text[1:]+text1[1:]
print(text3)

line1 = line1.replace(" ","")
txt = line1.split('+')
txt1 = txt[0].split('=')
txt3 = txt[1:]+txt1[1:]
print(txt3)

text_final  = text3+txt3
print(text_final)


sum = 0
for char in text_final:
    if char.isdigit():
        sum = sum+int(char)
print(sum)


for m in range(len(text_final)):
    text_final1 = text_final[m].split('*')
    print(text_final1)

'x' in text3[0] 
