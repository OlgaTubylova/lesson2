BASE = 16
HEX_DIGITS = '0123456789ABCDEF'

number = int(input('Введите число: '))
print(f"Проверка через функцию hex(): {hex(number)[2:].upper()}")

result = ''
if number == 0:
    result = '0'
else:
    while number > 0:
        result = HEX_DIGITS[number % BASE] + result
        number //= BASE

print(f"Результат: {result}")