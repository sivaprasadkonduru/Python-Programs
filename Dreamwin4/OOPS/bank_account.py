class BankAccount:

    #minimum_balance = 500

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient Funds")

        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


customer = BankAccount(5000)
print(customer.get_balance())

print(customer.deposit(1000))
print(customer.get_balance())

customer.withdraw(3000)
print(customer.get_balance())

customer.withdraw(7000)

customer1 = BankAccount(50000)
