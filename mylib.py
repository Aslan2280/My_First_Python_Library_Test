def codir(c):
    c = int(input('Number: '))
    print('Racshifrovano:')
    print(c / 2 + 6)
    print('Zashifrovano:')
    return (c - 6) * 2

def cod():
    a = input('Введите код для привет ')
    while True:
        b = input('Введите код ')
        if b == a:
            print('Hello')
        elif b == 0:
            print('Неверный код')
        return 