#Added an additional feature in the program = Python Color Class
print("\n\033[93m\033[1mYour Personal Information\033[0m\n")

def extract_NAA():
    nameCredential = input("Enter your \033[96m\033[1mNAME\033[0m here. \n> ")
    ageCredential = float(input("\nEnter your \033[96m\033[1mYEAR OF AGE\033[0m here in \033[92m\x1B[3m\033[1mnumbers\x1B[0m. \n> "))
    addressCredential = input("\nEnter your \033[96m\033[1mADDRESS\033[0m here. \n> ")
    return nameCredential, ageCredential, addressCredential;

def exhibit(n, a, ad):
    print(f"\nHi, my name is \033[4m\033[1m{n}\033[0m. I am \033[4m\033[1m{a:,.0f}\033[0m years old and I live in \033[4m\033[1m{ad}\033[0m.\n")

nameC, ageC, addressC = extract_NAA()

if ageC < 0:
    print(f"\nIt seems that your \033[96m\033[1mYEAR OF AGE\033[0m input is not a realistic response. No Age can display a \033[92m\x1B[3m\033[1mnegative integer\x1B[0m such as: \033[91m\033[1m{ageC:,.0f}\033[0m\n")
else:
    exhibit(nameC, ageC, addressC)