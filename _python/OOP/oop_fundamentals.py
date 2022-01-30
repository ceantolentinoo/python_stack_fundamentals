
def checkAccount(accounts, thisAccount):
        for key in accounts.keys():
            if(key == thisAccount):
                break
            else:
                return False
        return True;

class User:
    def __init__(self, username, email):
        self.name = username
        self.email = email
        self.account = {"checking": BankAccount(), "savings": BankAccount()}

    def test(self, accountTo):
        print(checkAccount(self.account, accountTo))

    def make_deposit(self, amount, accountTo):
        if(checkAccount(self.account, accountTo)):
            self.account[accountTo].deposit(amount)
        else:
            return "Invalid account!"

    def make_withdrawal(self, amount, accountTo):
        if(checkAccount(self.account, accountTo)):
            self.account[accountTo].withdraw(amount)
        else:
            return "Invalid account!"
       

    def display_balance(self, accountTo):
        if(checkAccount(self.account, accountTo)):
            return self.account[accountTo].display_account_balance(self.name)
        else:
            return "Invalid account!"
        

    def transfer_money(self, amount, other):
        self.account.transfer(amount, other)

class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.account_balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposit completed! Current balance: {self.account_balance}")

    
    def withdraw(self, amount):
        if(amount > self.account_balance):
            print("Insufficient balance!")
        else:
            self.account_balance -= amount
            print(f"Withdraw completed! Current balance: {self.account_balance}")

    def display_account_balance(self, username):
        return ("User: {}, Balance: {}").format(username, self.account_balance)

    def transfer(self, amount, other):
        if(amount > self.account_balance):
            print("Insufficient balance!")
        else:
            other.account.account_balance += amount
            self.account_balance -= amount


cean = User("Cean", "cean@gmail.com")
angela = User("Angela", "angela@email.com")

# cean.make_deposit(100)
# angela.make_deposit(50)
# cean.transfer_money(50, angela)
# print(cean.display_balance())
# print(angela.display_balance())
cean.make_deposit(100, "checking")
cean.make_deposit(50, "checking")
cean.make_deposit(103, "savings")
cean.make_withdrawal(200, "checking")