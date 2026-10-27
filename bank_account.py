class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    # (i) Return the amount deposited
    def deposit(self, amount):
        self.balance += amount
        return amount

    # (ii) Return "Insufficient balance" or the amount withdrawn
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    # (iii) Print the current balance
    def check_balance(self):
        print("Current balance:", self.balance)

    # (iv) Print customer name, account number, date of opening and balance
    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


# Test the class
account1 = BankAccount("100234", 5000, "12-03-2024", "John Mwangi")

print("Deposited:", account1.deposit(2000))
print("Withdrawn:", account1.withdraw(1000))
print("Withdrawn:", account1.withdraw(50000))
account1.check_balance()
account1.customer_details()
