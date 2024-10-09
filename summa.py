input_data = open('input.txt', 'r') # открываем для чтения (литера 'r') файл и кладем его в переменую
data = input_data.read() # читаем другую переменую содержимое всего файла

for i in range(1 , 10^4):
print(i, end="; ")

output_data = open('output.txt', 'r')
                   

output_data = open('output.txt', 'w') # открываем для записи (литера 'w') файл и кладем его в переменую
# записываем результат сложения и не забываем преобразовывать его в строку (иначе 
output_data.write(c)
# output_data.write(str(int(data[0]) + int(data[1])))
# ВАЖНО!!!
# не забываем закрывать открытые ранее файлы
input_data.close()
output_data.close()