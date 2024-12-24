# Вводим числа в список
# Находим суммы чисел списка
# ===================================

# Функция определения суммы списка
def listsum(numList):
    sum = 0
    for i in numList:
        sum = sum + i
    return sum

# Функция main
def main():
    list_data = [int(a) for a in input("Введите список чисел через пробел ").split()]
    print ("Сумма чисел в вашем списке", listsum(list_data))


if __name__ == '__main__':
    main()