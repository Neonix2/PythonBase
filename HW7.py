# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

distance = int(input("Введите расстояние, котрое спортсмен пробежал в первый день: "))
distance2 = int(input("Введите расстояние, для которого необходимо определеить номер дня: "))
day = (0)

while distance2 > distance:
    distance = distance + (distance * 0.1)
    day = day + 1
else:
    print(day)