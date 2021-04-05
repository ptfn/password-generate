import random
import sys


def main():
    big_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_char = "abcdefghijklmnopqrstuvwxyz"
    number = "0123456789"
    symbols = "!?@#$%^&*=<>()[]/|,.+-_"
    alphabet = ""
    
    print("██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║")
    print("██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║")
    print("██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║")
    print("██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")

    choice = input("Enter code:\n* BigChar -> b\n* SmallChar -> c\n* Number -> n\n* Symbols -> s\n:")
    if choice == "":
        print('Error code!')
        exit(0)
    else:
        pass


def pass_gen(length, symbols):
    password = ""
    for i in range(length):
        password += random.choice(symbols)
    return password


if __name__ == "__main__":
    main()