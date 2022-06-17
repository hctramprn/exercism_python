class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        # Reverse the string and replaces the whitespaces with blanks
        num_lst = list(self.card_num[::-1].replace(' ', ''))

        # Returns False if special characters are present or the card num has not the minimum length
        for char in num_lst:
            if not char.isnumeric():
                return False
        if len(num_lst) <= 1:
            return False

        # Doubles each second digit from the right
        double_digits = [int(num_lst[i]) if int(i) % 2 ==
                         0 else int(num_lst[i]) * 2 for i in range(0, len(num_lst))]

        # Creates the list substracting 9 from each second digit if it is greater than 9
        double_digits_adjusted = []
        for i in range(0, len(double_digits)):
            if i % 2 == 0:
                double_digits_adjusted.append(double_digits[i])
            else:
                if double_digits[i] > 9:
                    double_digits_adjusted.append(double_digits[i] - 9)
                else:
                    double_digits_adjusted.append(double_digits[i])

        #returns bool of the final validation
        return sum(double_digits_adjusted) % 10 == 0
