#1 Первое задание
a = int(input("Укажите число:"))
print(a)
print(a + 1)
print(a + 2)

#5 Пятое задание
score = int(input("Укажите число:"))
print('Следующее', score, 'число:', score  + 1)
print('Для ', score, 'предыдущее число:', score - 1)

#2 Второе задание
a = int(input("Укажите число"))
b= int(input("Укажите число"))
c = int(input("Укажите число"))
print(a + b + c)

#3 Третье задание
x = int(input("Укажите число"))
print('Объем =', x * x * x)
print('Площадь полной поверхности =', 6 * x * x)

#4 Четвертое задание
a = int(input("Укажите число"))
b = int(input("Укажите число"))
print(3 * (a+b) * (a+b) * (a+b) + 275 * b * b - 127 * a - 41)

#13 Тринадцатое задание
number_of_penguins = input("Укажите число")
print('   _~_    ' * int(number_of_penguins))
print('  (o o)   ' * int(number_of_penguins))
print(' /  V  \\  ' * int(number_of_penguins))
print('/(  _  )\\ ' * int(number_of_penguins))
print('  ^^ ^^   ' * int(number_of_penguins))

#6 Шестое задание
x = int(input("Укажите число"))
y = int(input("Укажите число"))
z = int(input("Укажите число"))
c = int(input("Укажите число"))
print(3 * (x + y + z + c))

#7 Седьмое задание
a = int(input("Укажите число"))
b = int(input("Укажите число"))
c = int(input("Укажите число"))
x = a + b * (c - 1)
print(x)

#11 Одинадцатое задание
m = int(input("Укажите число"))
h = m // 60
s = m % 60
print(m, "мин - это", h, "час", s, "минут.")

#8 Восьмое задание
x = int(input("Укажите число"))
print(x, 2 * x, 3 * x, 4 * x, 5 * x, sep='---')

#9 Девятое задание
a = int(input("Укажите число"))
b = int(input("Укажите число"))
print(b // a)
print(b % a)

#10 Десятое задание
n = int(input("Укажите число"))
print(n//2 + n%2)

#12 Двенадцатое задание
num = int(input("Укажите число"))
a = num % 10
b = (num % 100) // 10
c = num // 100
print("Сумма цифр =", c + b + a)
print("Произведение цифр =", c * b * a)

#14 Четырнадцатое задание
abc = int(input("Укажите число"))
k = 1
n = (abc // 10 ** k) % 10
print(n)

#15 Пятнадцатое задание
n = int(input("Укажите число"))
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

#16 Шестнадцатое задание
n = int(input("Укажите число"))
print(1 - n)

#18 Восемьнадцатое задание
v = int(input("Укажите число"))
t = int(input("Укажите число"))
a = v * t
n = a // 109
print(-(109 * n - a))

#19 Девятнадцатое задание
h = float(input("Укажите число"))
a = float(input("Укажите число"))
b = float(input("Укажите число"))
print(int(1 + (h - b - 1) / (a - b)))

#17 Семьнадцатое задание
n = int(input("Укажите число"))
print((n//2+1)*2)

#20 Дцадцатое задание
h = int(input("Укажите число:"))
a = int(input("Укажите число:"))
b = int(input("Укажите число:"))
print((h - a) // (a - b) + 1)
