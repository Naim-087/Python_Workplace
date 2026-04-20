
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS =3
COLS =3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2
}


def check_winnings(columns,lines,bet,values):
    winning = 0
    winning_lines =[]
    for line in range(lines):
        symbol =  columns[0][line]
        for column in columns:
            symble_to_check = column[line]
            if symbol != symble_to_check:
                break

        else:
            winning +=values[symbol] * bet
            winning_lines.append(lines + 1)
    return winning, winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
              print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()

def deposit():
    while True:
        amount = input("What you like to deposite ? $ : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Amount must be greater than 0 .")

        else:
            print("Please Enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 -"+str(MAX_LINES)+")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES :
                break
            else:
                print("Enter a valid number of lines.")

        else:
            print("Please Enter a number.")

    return lines

def get_bet():
    while True:
        bet = input("Enter the amount you wanna bet on each line: "+str(MIN_BET)+" - "+ str(MAX_BET)+" $")
        if bet.isdigit():
            bet = int( bet)
            if MIN_BET<= bet <= MAX_BET :
                break
            else:
                print("Please enter a valid amount .")

        else:
            print("Please your betting amount.")

    return bet
def spin(balance):
    lines = get_number_of_lines()
    while True:
         
         bet = get_bet()
         total_bet = bet * lines
         if total_bet > balance:
             
             print(f"you do not have sufficient balance. Your current balance :${balance}")

         else:
             break

         
         
    print(f"You betting ${bet} on {lines} lines. Total bet is :${total_bet}")

    slots = get_slot_machine_spin(ROWS,COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines= check_winnings(slots,lines,bet,symbol_value)
    print(f"You want ${winning}.")
    print(f"You won on lines:" , *winning_lines)
    return winning - total_bet
   
   

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is : ${balance}")
        spins = input("Press enter to play ( q to Quit). ")
        if spins == "q":
            break
        balance +=spin(balance)

    print(f"You left with {balance}")
 

main()

