#Rendered a welcoming greet to a user after the initialization of the program.
print("\nWelcome to Villariza Foods! \nThe Price of an Apple is 20 PHP, while the Price of an Orange is 25 PHP.")

#Returning Multiple Variables (User Input in a Single-Filed Function)
def exhibit_UserPrice():
    """
    Input define function.
    """
    apple = int(input("\nPlease quantify how many apples you need to purchase... \n> Quantity: "))
    orange = int(input("\nPlease quantify how many oranges you need to purchase... \n> Quantity: "))
    """
    Output string with print function.
    """
    _grand_total = obtain_totalPrice(A = apple, O = orange)
    print(f"\nThe total amount is {_grand_total:,.0f} PHP.\n")

def obtain_totalPrice(A, O):
    """
    Process and computation define function.
    """
    obtain_apple = 20 * A
    obtain_orange = 25 * O
    total = obtain_apple + obtain_orange
    return total;

exhibit_UserPrice()