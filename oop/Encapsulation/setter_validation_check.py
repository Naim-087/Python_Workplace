class BankAccount:
    def __init__(self,balance,withdraw,deposit):
        self.__balance = balance
        self.__deposit = deposit
        self.__withdraw =withdraw
        

    
    def set_deposit(self,deposit):
        if deposit > 0:
            self.__balance += deposit
    
    def set_withdraw(self,withdraw):
        if 500 < withdraw < self.__balance:
            self.__balance -= withdraw
        else:
         print("Invalid withdrawls")

    def get_balance(self):
        return self.__balance
    
acc_one = BankAccount(0,0,0)
acc_one.set_deposit(500)
acc_one.set_withdraw(5400)
print(f'your current balance {acc_one.get_balance()}')


        
        