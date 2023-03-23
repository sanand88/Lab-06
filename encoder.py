# Seher Anand
def print_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
# defines the menu



def encoder(pwd):
# define the encoding function
    global result
    result = ""
    for i in pwd:
        i = int(i) + 3
        if i >= 7:
            i = i - 10
            i = str(i)
        else:
            i = str(i)
        result += i
    return result

def decoder():

def main():
    cont = True

    while cont:
        print_menu()
        option = int(input("Please enter your password to encode: "))
        print()

        if option == 1:
            pwd = input("Please enter your password: ")
            encoder(pwd)
            print("Your password has been encoded and stored!")
        if option == 2:
            decoded_pwd = decoder()
            print(f"The encoded password is {encoder(pwd)}, and the original password is {decoded_pwd}.")
            print()
        if option == 3:
            break


