import re


class PhoneNumber:
    def __init__(self, number):
        self.number = self.nanp(number)
        self.area_code = self.number[:3]

    def nanp(self, number):
        phone = ''.join(re.findall(r'\d', number))

        if (re.search(r'[a-zA-Z]+', number)):
            raise ValueError("letters not permitted")
        if (re.search(r'[@:!]+', number)):
            raise ValueError("punctuations not permitted")

        if phone[-7] == '0':
            raise ValueError("exchange code cannot start with zero")
        if phone[-7] == '1':
            raise ValueError("exchange code cannot start with one")

        if len(phone) > 11:
            raise ValueError("more than 11 digits")
        elif len(phone) == 11 and phone[0] != '1':
            raise ValueError("11 digits must start with 1")
        elif len(phone) >= 10:
            if phone[-10] == '0':
                raise ValueError("area code cannot start with zero")
            if phone[-10] == '1':
                raise ValueError("area code cannot start with one")
        elif len(phone) < 10:
            raise ValueError("incorrect number of digits")

        return phone[-10:]
    
    def pretty(self):
        return f'({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}'
