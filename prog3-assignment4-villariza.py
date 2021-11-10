#Added an additional feature in the program = Python Color Class
print("\nWelcome to \033[93;1mVillariza Foods\033[0m! Our available product for today is \033[91;1mApple\033[0m. \n")

#Returning Multiple Variables (User Input in a Single-Filed Function)
def extract_AMA():
    """
    Input define function.
    """
    money = float(input("How much \033[92;1mMoney\033[0m do you possess \033[36mright now?\033[0m \n> \033[32;1mPHP: ")) 
    apple = float(input("\n\033[0mWhat is the cost of an \033[91;1mApple\033[0m \033[36mper item?\033[0m \n> \033[32;1mPHP: "))
    return money, apple;

accumulated_Cash, apple_cost = extract_AMA()

#Added an if-else statement concerning a systematic response based on the input of a user running a program.
def exhibit(MNY, APL):
    """
    Process and computation define function.
    """
    if MNY >=  APL:
        exchange = MNY % APL
        apple_maxQuantity = MNY // APL
        """
        Output string with print function.
        """
        if MNY // APL == 1:
            print(f"\033[0m\nYou can buy \033[34;1m{apple_maxQuantity:,.0f}\033[0m \033[91;1mApple\033[0m and your change is \033[32;4m₱ {exchange:,.2f}\033[0m.\n")
        else:
            print(f"\033[0m\nYou can buy \033[34;1m{apple_maxQuantity:,.0f}\033[0m \033[91;1mApple\033[0m\033[2m(s)\033[0m and your change is \033[32;4m₱ {exchange:,.2f}\033[0m.\n")
    else:
        moneyShortage = APL - MNY
        """
        Output string with print function.
        """
        print(f"\033[0m\nSorry, but you \033[36mdo not have enough\033[0m \033[32;1mMoney\033[0m. \nYou need \033[32;4m₱ {moneyShortage:,.2f}\033[0m in order to \033[93mpurchase\033[0m a single \033[91;1mApple\033[0m.\n")

exhibit(MNY = accumulated_Cash, APL = apple_cost)