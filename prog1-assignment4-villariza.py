#Added an additional feature in the program = Python Color Class
print("\n\033[93;1mYour Personal Information\033[0m\n")

#Added if-else with string function for more logical reponse from the program.
def extract_NAA():
    nameCredential = input("Enter your \033[96;1mNAME\033[0m here. \n> \033[96;1m")
    ageCredential = float(input("\n\033[0mEnter your \033[96;1mYEAR OF AGE\033[0m here in \033[92;1m\x1B[3mnumbers\x1B[0m. \n> \033[96;1m"))
    addressCredential = input("\n\033[0mEnter your \033[96;1mADDRESS\033[0m here. \n> \033[96;1m")
    return nameCredential, ageCredential, addressCredential;

def exhibit(nm_Cred, ag_Cred, add_Cred):
    if ag_Cred <= 1 == True:
        print(f"\n\033[0mHi, my name is \033[96;4;1m{nm_Cred}\033[0m. I am \033[96;4;1m{ag_Cred:,.0f}\033[0m year old and I live in \033[96;4;1m{add_Cred}\033[0m.\n")
    else:
        print(f"\n\033[0mHi, my name is \033[96;4;1m{nm_Cred}\033[0m. I am \033[96;4;1m{ag_Cred:,.0f}\033[0m years old and I live in \033[96;4;1m{add_Cred}\033[0m.\n")

nameC, ageC, addressC = extract_NAA()

if nameC.isdigit() and addressC.isdigit() == True and ageC < 0:
    print(f"\n\033[0mYour \033[96;1mNAME\033[0m, \033[96;1mAGE\033[0m, and \033[96;1mADDRESS\033[0m input is unlogical; therefore, Python cannot heed your request. \nPlease try again by inputting alphabetical letters.\n")
elif nameC.isdigit() and addressC.isdigit() == True:
    print(f"\n\033[0mYour \033[96;1mNAME\033[0m and \033[96;1mADDRESS\033[0m input is a digit; therefore, Python cannot heed your request. \nPlease try again by inputting alphabetical letters.\n")
elif nameC.isdigit() == True:
    print(f"\n\033[0mYour \033[96;1mNAME\033[0m input is a digit (\033[92;1m{nameC}\033[0m) < as shown; therefore, Python cannot heed your request. \nPlease try again by inputting alphabetical letters.\n")
elif ageC < 0:
    print(f"\nIt seems that your \033[96;1mYEAR OF AGE\033[0m input is not a realistic response. No Age can display a \033[92;1m\x1B[3mnegative integer\x1B[0m such as: \033[91;1m{ageC:,.0f}\033[0m\n")
elif addressC.isdigit() == True:
    print(f"\n\033[0mYour \033[96;1mADDRESS\033[0m input is a digit (\033[92;1m{addressC}\033[0m) < as shown; therefore, Python cannot heed your request. \nPlease try again by inputting alphabetical letters.\n") 
else:
    """
    Input variables are in the title function concerning a grammatical response.
    """
    exhibit(nameC.title(), ageC, addressC.title())