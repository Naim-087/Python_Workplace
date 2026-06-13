class ATM:

    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.__pin = pin           # Private Variable
        self.__balance = balance   # Private Variable

    def verify_pin(self, entered_pin):
        return self.__pin == entered_pin

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"৳{amount} deposited successfully.")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid amount!")

        elif amount > self.__balance:
            print("Insufficient Balance!")

        else:
            self.__balance -= amount
            print(f"৳{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ৳{self.__balance}")

    def change_pin(self, old_pin, new_pin):

        if self.__pin == old_pin:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

    def atm_menu(self):

        pin = int(input("Enter PIN: "))

        if not self.verify_pin(pin):
            print("Invalid PIN!")
            return

        while True:

            print("\n===== ATM MENU =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter choice: ")

            if choice == "1":

                amount = float(input("Enter amount: "))
                self.deposit(amount)

            elif choice == "2":

                amount = float(input("Enter amount: "))
                self.withdraw(amount)

            elif choice == "3":

                self.check_balance()

            elif choice == "4":

                old_pin = int(input("Enter old PIN: "))
                new_pin = int(input("Enter new PIN: "))
                self.change_pin(old_pin, new_pin)

            elif choice == "5":

                print("Thank you for using ATM.")
                break

            else:
                print("Invalid Choice!")


# Create Account
user1 = ATM("Naim", 1234, 5000)

# Run ATM
user1.atm_menu()




