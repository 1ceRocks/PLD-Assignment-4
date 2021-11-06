#Added an if-else statement concerning a systematic response based on the input of a user running a program.
print("\nYour Personal Information\n")

def extract_NAA():
    nameCredential = input("Enter your NAME here. \n> ")
    ageCredential = float(input("\nEnter your YEAR OF AGE here in numbers. \n> "))
    addressCredential = input("\nEnter your ADDRESS here. \n> ")
    return nameCredential, ageCredential, addressCredential;

def exhibit(n, a, ad):
    print(f"\nHi, my name is {n}. I am {a:,.0f} years old and I live in {ad}.\n")

nameC, ageC, addressC = extract_NAA()

if ageC < 0:
    print(f"\nIt seems that your YEAR OF AGE input is not a realistic response. No Age can display a negative integer such as: {ageC:,.0f}\n")
else:
    exhibit(nameC, ageC, addressC)