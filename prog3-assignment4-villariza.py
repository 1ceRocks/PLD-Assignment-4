#Completed my basic program with absolute functionality.
print("\nWelcome to Villariza Foods! Our available product for today is apple. \n")

#Returning Multiple Variables (User Input in a Single-Filed Function)
def extract_AMA():
    """
    Input define function.
    """
    money = float(input("How much cash do you possess right now? \n> PHP: ")) 
    apple = float(input("\nWhat is the cost of an apple per item? \n> PHP: "))
    return money, apple;

accumulated_Cash, apple_cost = extract_AMA()

#Added an if-else statement concerning a systematic response based on the input of a user running a program.
def exhibit(M, A):
    """
    Process and computation define function.
    """
    if M >=  A:
        exchange = M % A
        apple_maxQuantity = M // A
        """
        Output string with print function.
        """
        print(f"\nYou can buy {apple_maxQuantity:,.0f} apple/s and your change is {exchange:,.2f} PHP.\n")
    else:
        moneyShortage = A - M
        """
        Output string with print function.
        """
        print(f"\nSorry, but you do not have enough money to buy an apple. You need {moneyShortage:,.2f} PHP in order to purchase a single apple.\n")

exhibit(M = accumulated_Cash, A = apple_cost)