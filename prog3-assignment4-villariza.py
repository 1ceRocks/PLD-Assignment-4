#Completed my basic program with absolute functionality.
print("\nWelcome to Villariza Foods! Our available product for today is apple. \n")

#Returning Multiple Variables (User Input in a Single-Filed Function)
def extract_AMA():
    money = float(input("How much cash do you possess right now? \n> PHP: ")) 
    apple = float(input("\nWhat is the cost of an apple per item? \n> PHP: "))
    return money, apple;

accumulated_Cash, apple_cost = extract_AMA()

def exhibit(M, A):
        exchange = M % A
        apple_maxQuantity = M // A
        print(f"\nYou can buy {apple_maxQuantity:,.0f} apple/s and your change is {exchange:,.2f} PHP.\n")

exhibit(M = accumulated_Cash, A = apple_cost)