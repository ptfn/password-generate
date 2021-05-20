import random

big_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_char = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbols = "!?@#$%^&*=<>()[]/|,.+-_"


def main():
    print("██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║")
    print("██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║")
    print("██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║")
    print("██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")

    alphabet = ""

    while True:
        choice = input("Enter code:\n* Password\n* Help\n* Exit\n:")
        
        if choice == "Password" or choice == "password":
            chars = input("Enter code:\n* BigChar -> b\n* SmallChar -> c\n* Number -> n\n* Symbols -> s\n:")
            
            if chars == "":
                print('Error code!')
                exit(0)
            else:
                alphabet = brut_alph(chars)

            length = int(input("Length passwords:"))
            password = pass_gen(length, alphabet)
            print("Password -> {}".format(password))

        elif choice == "Help" or choice == "help":
            print("The utility is designed to generate a password. To generate a password, select 'Password'")
        elif choice == "Exit" or choice == "exit":
            break
        else:
            print("Error choice\n")


def pass_gen(length, symbols):
    password = ""
    
    for i in range(length):
        password += random.choice(symbols)
    return password


def brut_alph(string):
    str_last = ""
    str_res = ""

    for i in range(len(string)):
        if string[i] not in str_last:
            if string[i] == "b":
                str_res += big_char
                str_last += "b"
            if string[i] == "c":
                str_res += small_char
                str_last += "c"
            if string[i] == "n":
                str_res += number
                str_last += "n"
            if string[i] == "s":
                str_res += symbols
                str_last += "s"
    return str_res


if __name__ == "__main__":
    main()