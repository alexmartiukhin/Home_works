# Home work
# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.

# def my_pow(number, degree):
#     if degree <= 1:
#         return number
#     return number * my_pow(number, degree - 1)
#
# print(my_pow(3, 5))


# Завдання 2.

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

def my_row(N):
    if N <= 0:
        return N
    print('*', end='')

    return my_row(N - 1)


N = int(input("Enter stars quantity(N): "))

my_row(N)
