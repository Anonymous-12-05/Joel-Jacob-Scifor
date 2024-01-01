class BankAccount:
    def __init__(self, name, bank_pin, balance=0):
        self.name = name
        self.bank_pin = bank_pin
        self.balance = balance

    def withdraw(self, amount,pin):
        if(pin==self.bank_pin):

            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f'Withdrawn {amount} from your account.')
            else:
                print('Invalid withdrawal ')
        else:
            print("Invalid PIN")

    def showBalance(self,pin):
        if(pin==self.bank_pin):
            print(f'Customer Name: {self.name}')
            print(f'Bank Balance: {self.balance}')
        else:
            print("Invalid PIN")

    def deposit(self, amount,pin):
        if(pin==self.bank_pin):
            if amount > 0:
        
                self.balance += amount
                print(f'Deposited {amount} into your account.')
            else:
                print('Invalid deposit amount.')
        else:
            print("Invalid PIN")


if __name__ == '__main__':
    customer1 = BankAccount("Joel", 1234, 1000)
    customer1.showBalance(1234)
    customer1.showBalance(1000)

    customer1.deposit(500,1234)
    customer1.deposit(100,1034)
    customer1.showBalance(1234)

    customer1.withdraw(200,1234)
    customer1.withdraw(200,1232)
    customer1.showBalance(1234)

    customer1.withdraw(1500,1234)
