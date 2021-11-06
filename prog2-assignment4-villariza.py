#Rendered a welcoming greet to a user after the initialization of the program.
print("\n\033[39m\033[1mWelcome to Villariza Foods!\033[0m \nThe Price of an\033[0m \033[91m\033[1mApple\033[0m is \033[92m\033[1m\033[1m20 PHP\033[0m. \n\033[39m\033[2mThe Price of an\033[0m \033[93m\033[1mOrange\033[0m \033[2mis\033[0m \033[92m\033[1m\033[1m25 PHP\033[0m.")

#Returning Multiple Variables (User Input in a Single-Filed Function)
#Added an additional feature in the program = Python Color Class
def exhibit_UserPrice():
    """
    Input define function.
    """
    apple = int(input("\nPlease \033[34m\033[1mquantify\033[0m how many \033[91m\033[1mApple\033[0m\033[1m(s)\033[0m you need to purchase... \n> \033[92m\033[1mQuantity:\033[0m\033[91m\033[1m "))
    orange = int(input("\033[0m\nPlease \033[34m\033[1mquantify\033[0m how many \033[93m\033[1mOrange\033[0m\033[1m(s)\033[0m you need to purchase... \n> \033[92m\033[1mQuantity:\033[0m\033[93m\033[1m "))
    """
    Output string with print function.
    """
    _grand_total = obtain_totalPrice(A = apple, O = orange)
    print(f"\033[0m\nThe total amount is \033[92m\033[2m₱ {_grand_total:,.2f}\033[0m\n")

def obtain_totalPrice(A, O):
    """
    Process and computation define function.
    """
    obtain_apple = 20 * A
    obtain_orange = 25 * O
    total = obtain_apple + obtain_orange
    return total;

exhibit_UserPrice()