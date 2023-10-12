#Home work
def my_pow(number, degree):
    if degree <= 1:
        return number
    return number * my_pow(number, degree - 1)
print(my_pow(2, 4))
