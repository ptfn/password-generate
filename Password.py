import random
import hashlib
import base64

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?@#$%^&*=<>()[]/|,.+-_"


def main():

    print("██████╗  █████╗ ███████╗███████╗ ██████╗ ███████╗███╗   ██╗")
    print("██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝ ██╔════╝████╗  ██║")
    print("██████╔╝███████║███████╗███████╗██║  ███╗█████╗  ██╔██╗ ██║")
    print("██╔═══╝ ██╔══██║╚════██║╚════██║██║   ██║██╔══╝  ██║╚██╗██║")
    print("██║     ██║  ██║███████║███████║╚██████╔╝███████╗██║ ╚████║")
    print("╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝")

    while True:
        choice = input("Enter code:\n* Password\n* Help\n* Exit\n:")
        
        if choice == "Password" or choice == "password":
            text = input("Enter text:")
            
            if text == "":
                print('Error code!')
                exit(0)

            else:
                length = int(input("Length passwords(max 64):"))

                if length <= 0:
                    print('Error code!')
                    exit(0)

                else:
                    password = pass_gen(length, text)
                    print("Password -> {}".format(password))

        elif choice == "Help" or choice == "help":
            print("The utility is designed to generate a password. To generate a password, select 'Password'")

        elif choice == "Exit" or choice == "exit" or choice == "quit" or choice == "Quit":
            break

        else:
            print("Error choice\n")


def pass_gen(length, text):
    password = ""
    key = ""
    string = ""
    
    for i in range(len(text)):
        key += random.choice(chars)
    
    string = password + text + key
    password = hashlib.sha1(str(string).encode("ascii")).hexdigest()
    encbyte = base64.b64encode(password.encode("utf-8"))
    encstr = str(encbyte, "utf-8")

    return encstr[:length]

if __name__ == "__main__":
    main()