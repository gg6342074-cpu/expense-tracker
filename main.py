total = 0
while True:

    expense = int(input("Введите расход: "))
    total += expense
    if expense == 0:
        break


    print("Всего потрачено:",total)
