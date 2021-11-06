#Completed my basic program with absolute functionality.
print("\nYour Personal Information\n")

def extract_NAA():
    nameCredential = input("Enter your NAME here. \n> ")
    ageCredential = float(input("\nEnter your YEAR OF AGE here in numbers. \n> "))
    addressCredential = input("\nEnter your ADDRESS here. \n> ")
    return nameCredential, ageCredential, addressCredential;

def exhibit(n, a, ad):
    print(f"\nHi, my name is {n}. I am {a:,.0f} years old and I live in {ad}.\n")

nameC, ageC, addressC = extract_NAA()
exhibit(nameC, ageC, addressC)