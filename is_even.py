# Берём любое число 
# Проверяем четное ли это число
# ======================================

# Функция определения четности числа 
def check(n):
    if int(n)%2 == 0:
        print ("Ваше число четное")
    else:
        print ("Ваше число нечетное")

# Функция main
def main():
    n = input("Введите ваше число ")
    print (check(n))


if __name__ == '__main__':
    main()