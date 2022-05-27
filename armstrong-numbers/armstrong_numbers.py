def is_armstrong_number(number):
    armstrong_num = 0
    for num in str(number):
        armstrong_num += int(num)**int(len(str(number)))
    return armstrong_num == number
