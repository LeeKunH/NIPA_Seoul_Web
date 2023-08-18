

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __repr__(self):
        return f"계좌 소유자 : {self.owner} , 잔액 : {self.balance} "

    def deposit(self, money):
        # print(self.balance)
        self.balance += money
        return print(f"입금한 돈 : {money}  현재 돈 : {self.balance}")

    def withdraw(self, money):
        if (self.balance >= money):
            self.balance -= money
            return print(f"인출한 돈 : {money}  현재 돈 : {self.balance}")
        else:
            print("계좌잔액이 부족합니다")

        return print(self.balance)


# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.deposit(100)
acct1.deposit(100)
acct1.deposit(100)
acct1.deposit(100)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)
