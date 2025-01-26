import time

print("Please insert Your CARD")

# Simulate card processing
time.sleep(5)

password = 1234
pin = int(input("Enter your ATM PIN: "))

balance = 5000
transactions = []  # To store transaction history

if pin == password:1
while True:
        print(""" 
            1 == Balance Inquiry
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == View Transaction History
            5 == Change PIN
            6 == Exit
        """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid option.")
            continue

        if option == 1:
            print(f"Your current balance is ₹{balance}")
            transactions.append(f"Checked Balance: ₹{balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdrawal amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            elif withdraw_amount <= 0:
                print("Invalid amount.")
            else:
                balance -= withdraw_amount
                print(f"₹{withdraw_amount} is debited from your account.")
                print(f"Your updated balance is ₹{balance}")
                transactions.append(f"Withdrawn: ₹{withdraw_amount}, Updated Balance: ₹{balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            if deposit_amount <= 0:
                print("Invalid amount.")
            else:
                balance += deposit_amount
                print(f"₹{deposit_amount} is credited to your account.")
                print(f"Your updated balance is ₹{balance}")
                transactions.append(f"Deposited: ₹{deposit_amount}, Updated Balance: ₹{balance}")

        elif option == 4:
            print("Transaction History:")
            if transactions:
                for t in transactions:
                    print(t)
            else:
                print("No transactions yet.")

        elif option == 5:
            old_pin = int(input("Enter your old PIN: "))
            if old_pin == password:
                new_pin = int(input("Enter your new PIN: "))
                password = new_pin
                print("PIN changed successfully.")
                transactions.append("PIN changed successfully.")
            else:
                print("Incorrect old PIN.")

        elif option == 6:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Wrong PIN. Please try again.")
