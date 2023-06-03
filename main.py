# Написать программу, которая будет выводить в консоль ёлочку заданной высоты.

# rows = int(input("Введите количество рядов в елке: "))
# count = 1
# step = " "
# step2 = 1
# star = "*"
# print(step)
# while (rows > 0):
#     fir_tree = step * (rows - count) + star * step2
#     print(fir_tree)
#     rows -=1
#     step2 +=2

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

for i in range(1,10):
    for j in range(1,10):
        print(f'{i*j:4}', end=" ")
    print()
