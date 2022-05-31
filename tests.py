def run():
    number = 16
    factors = []
    for num in range(1,number):
        if number % num == 0:
            factors.append(num)
    print(factors)

if __name__ == '__main__':
    run()
