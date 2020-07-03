# методы получения строчки
new_strings = []#создание пустого списка
new_strings.append('First options') #список новых строчек
new_strings.append("Second options") #добавляет новый элемент в строчку
new_strings.append('''Third option''') #
new_strings.append(input()) #ввод от пользователя
new_strings.append(" ".join(['Fifth','option'])) #склеиваем два елемента
new_strings.append('Sixth' + 'option')#можем сложить две строчки без пробелов
new_strings.append(str(13**8)) # число переобразуется в строку и добавляется в конце списка
new_strings.append(chr(8364))# код переобразуется в знак(евро)# chr() обращается в таблицу кодов
new_strings.append(ord(new_strings[-1]))#
print(new_strings)


new_var = 'Some new str1ng 4 you. and 13 '
print(new_var)

multiply = new_var * 3
print(multiply)
empty_multiply = new_var * -8
print(empty_multiply)
char_in_var = 'Some' in new_var
print(char_in_var)
char_not_in_var = 'some' in new_var
print(char_not_in_var)
length_of_var = len(new_var)
print(length_of_var)
string_slice = new_var[-13:-5:2] # one more option
print(string_slice)
get_by_index = new_var[7]
print(get_by_index)



