#Rendered a welcoming greet to a user after the initialization of the program.
print("\n\033[39;1mWelcome to Villariza Foods!\033[0m \nThe Price of an \033[91;1mApple\033[0m is \033[92;1m20 PHP\033[0m. \n\033[39;2mThe Price of an\033[0m \033[93;1mOrange\033[0m \033[2mis\033[0m \033[92;1m25 PHP\033[0m.")

#Returning Multiple Variables (User Input in a Single-Filed Function)
#Added an additional feature in the program = Python Color Class
def exhibit_UserPrice():
    """
    Input define function.
    """
    apple = int(input("\nPlease \033[34;1mquantify\033[0m how many \033[91;1mApple\033[0m\033[1m(s)\033[0m you need to purchase... \n> \033[92;1mQuantity:\033[0m\033[91;1m "))
    orange = int(input("\033[0m\nPlease \033[34;1mquantify\033[0m how many \033[93;1mOrange\033[0m\033[1m(s)\033[0m you need to purchase... \n> \033[92;1mQuantity:\033[0m\033[93;1m "))
    return apple, orange;

APL_input, ORNG_input = exhibit_UserPrice()

def obtain_totalPrice(APL, ORNG):
    """
    Process and computation define function.
    """
    apl_orng_total = (20 * APL) + (25 * ORNG)
    """
    Output string with print function.
    """
    print(f"\033[0m\n\033[34;1mYour Recorded Output as Tracked\033[0m\n\033[91;1mApple\033[0m Input = \033[91;1m{APL}\033[0m\n\033[93;1mOrange\033[0m Input = \033[93;1m{ORNG}\033[0m\nThe total amount would be \033[92;4;1m₱ {apl_orng_total:,.2f}\033[0m.\n")

obtain_totalPrice(APL_input, ORNG_input)