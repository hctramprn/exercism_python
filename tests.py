number = 2453

def run():
    armstrong_num = 0
    for num in str(number):
        armstrong_num += int(num)**int(len(str(number)))
    print(armstrong_num == number)


if __name__ == '__main__':
    run()
