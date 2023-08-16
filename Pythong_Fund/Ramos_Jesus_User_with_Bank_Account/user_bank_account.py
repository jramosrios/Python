class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def make_deposit(self, amount):
        self.account.balance = amount + self.account.balance

    def make_withdrawl(self, amount):
        self.account.balance = self.account.balance - amount
    
    def display_user_balance(self):
        print(f"Balance: {self.account.balance}")

userjesus = User("jesus", "email")
print(userjesus.account.balance)
userjesus.make_deposit(200)
print(userjesus.account.balance)
userjesus.make_withdrawl(50)
print(userjesus.account.balance)
userjesus.make_deposit(500)
userjesus.display_user_balance()