"""
Implementation of the Bank Account - Single account using a procedural approach.

This version uses a password checker on each operation.
"""
from os import system, name

# Declaring the account variables
account_name = "Joe"
account_balance = 100
account_password = 'soap'
# A 'safe' in case the account gets blocked
BLOCKED = False

# A set of valid operations
operations = {"b", "d", "w", "s", "q"}


def check_password():
    """
    Check the user's password against the stored password.
    The user has 3 attempts to enter the correct password.
    Returns:
        bool: True if the entered password matches the stored password, False otherwise.
    """
    global BLOCKED
    # The user has 3 attempts to correctly type his password
    attempts = 3

    while True:
        input_password = input("\nPlease type your password: ")

        if attempts == 0:
            print("There has been too many unsuccessful attempts to access your account. Your account is now blocked. ")
            BLOCKED = True
            return False

        if input_password == account_password:
            return True

        attempts -= 1
        print(f"Incorrect password. You have {attempts + 1} more attempts. \n")


def get_balance():
    """
    Display the account balance after verifying the user's password.
    Returns:
        bool: True if the password verification succeeded, False otherwise.
    """
    global account_balance
    # Verifying the user's password
    if not check_password():
        print("Unable to check your account balance. ")
        return False
    print('\nYour balance is:', account_balance)
    return True


def deposit():
    """
    Deposit an amount into the account after verifying the user's password.
    The user must enter a valid, positive amount.

    Returns:
        bool: True if the deposit operation succeeded, False otherwise.
    """
    global account_balance
    # Checking the user's password
    if not check_password():
        print("Unable to complete your deposit. ")
        return False
    # A while loop to make sure that the user enters a valid amount
    while True:
        amount = input("\nPlease enter amount to deposit: ")
        try:
            amount = int(amount)
            # No negative amounts are accepted
            if amount <= 0:
                print("\nYou cannot deposit a negative amount. Try again.")
            else:
                break
        except ValueError or TypeError:
            print("Invalid amount. Try again. ")

    # If everything is correct, increase the account balance
    account_balance += amount
    print('Your new balance is:', account_balance)
    return True


def withdraw():
    """
    Withdraw an amount from the account after verifying the user's password.
    The user must enter a valid, positive amount that is less than or equal to the account balance.

    Returns:
        bool: True if the withdrawal operation succeeded, False otherwise.
    """
    global account_balance
    # Checking the user's password
    if not check_password():
        print("Unable to complete your withdrawal. ")
        return False
    # A while loop to make sure that the user enters a valid amount
    while True:
        amount = input("\nPlease enter amount to withdraw: ")
        try:
            amount = int(amount)
            # No negative amounts are accepted
            if amount <= 0:
                print("\nYou cannot withdraw a negative amount. Try again.")
            elif amount > account_balance:
                print("\nYou cannot withdraw more than you have in your account.")
            else:
                break
        except ValueError or TypeError:
            print("Invalid amount. Try again. ")

    # If everything is correct, substract the amount from the account balance
    account_balance -= amount
    print('Your new balance is:', account_balance)
    return True


def show_account():
    """
       Display the account details after verifying the user's password.

       Returns:
           bool: True if the password verification succeeded, False otherwise.
       """
    # Checking the user's password
    if not check_password():
        print("Unable to show your account details. ")
        return False
    print('Account details:')
    print('       Name', account_name)
    print('       Balance:', account_balance)
    print('       Password:', account_password)
    print()
    return True

def show_operations():
    """
    Show the available operations to the user and get their input.

    Returns:
        str: The user's choice of operation (one character, lowercase).
    """
    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account')
    print('Press q to quit')
    print()

    while True:
        action = input('What do you want to do? ')
        if action != "":
            action = action[0].lower()  # force lowercase
            if action in operations:
                break
        print("Invalid choice. Try again.\n")
    return action


def quit():
    """
    End the main loop.

    Returns:
        bool: Always False.
    """
    return False


def clear_terminal():
    """
    Clear the terminal screen.

    Returns:
        int: The return code of the system command (0 for success).
    """
    input("\nPress any key to continue.")
    if name == "nt":
        return system("cls")
    return system("clear")


def main():
    """
    Main function that runs the banking application. Uses a while loop.
    """
    # We'll keep running unless the user prompts to stop
    run = True
    while BLOCKED is False and run is True:
        # We'll ask the user for the operation he wants to perform
        selection = show_operations()
        match selection:
            case "b":
                get_balance()
            case "d":
                deposit()
            case "q":
                run = quit()
            case "s":
                show_account()
            case "w":
                withdraw()
        # After each pass, we clear the screen.
        clear_terminal()


if __name__ == '__main__':
    main()