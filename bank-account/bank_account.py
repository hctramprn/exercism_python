class BankAccount:
    def __init__(self):
        # Initialize the account with a balance of 0 and set the account as closed
        self.balance = 0
        self.is_open = False

    def get_balance(self):
        # Return the account balance if the account is open
        if self.is_open:
            return self.balance
        else:
            # Raise an error if the account is not open
            raise ValueError('account not open')

    def open(self):
        # Open the account if it is not already open
        if not self.is_open:
            self.is_open = True
        else:
            # Raise an error if the account is already open
            raise ValueError('account already open')

    def deposit(self, amount):
        # Deposit funds into the account if it is open and the amount is positive
        if self.is_open:
            if amount > 0:
                self.balance += amount
            else:
                # Raise an error if the amount is not positive
                raise ValueError('amount must be greater than 0')
        else:
            # Raise an error if the account is not open
            raise ValueError('account not open')

    def withdraw(self, amount):
        # Withdraw funds from the account if it is open, the amount is positive,
        # and the account has sufficient balance
        if self.is_open:
            if amount > 0:
                if self.balance - amount >= 0:
                    self.balance -= amount
                else:
                    # Raise an error if the amount exceeds the balance
                    raise ValueError('amount must be less than balance')
            else:
                # Raise an error if the amount is not positive
                raise ValueError('amount must be greater than 0')
        else:
            # Raise an error if the account is not open
            raise ValueError('account not open')

    def close(self):
        # Close the account if it is open and reset the balance to 0
        if self.is_open:
            self.is_open = False
            self.balance = 0
        else:
            # Raise an error if the account is not open
            raise ValueError('account not open')
