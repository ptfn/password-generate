import random
import hashlib
import base64

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?@#$%^&*=<>()[]/|,.+-_"

def main():
    while True:
        chc = input("Enter code:\n1)Password\n2)Help\n3)Exit\n:")
        
        if chc == "Password" or chc == "password" or chc == "pass":
            opt = input("Choose a way to generate your password:\n* Random\n* Hash\n:")

            if opt == "hash" or opt == "Hash":
                text = input("Enter text\n:")
                
                if text == "":
                    print("The text is not visible!")
                    exit(0)

                else:
                    leng = int(input("Length passwords(max 64)\n:"))

                    if leng <= 0:
                        print("Incorrect password length!")
                        exit(0)

                    else:
                        password = pass_hash(leng, text)
                        print("Password -> {}".format(password))
            
            elif opt == "Random" or opt == "random" or opt == "rand":
                leng = int(input("Length passwords\n:"))

                if leng <= 0:
                    print("Incorrect password length!")
                    exit(0)

                else:
                    password = pass_rand(leng)
                    print("Password -> {}".format(password))

            else:
                print("Error option!")
                exit(0)

        elif chc == "Help" or chc == "help":
            print("The utility is designed to generate a password. To generate a password, select 'Password'")

        elif chc == "Exit" or chc == "exit" or chc == "quit" or chc == "Quit":
            break

        else:
            print("Error choice!")


def pass_hash(length, text):
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


def pass_rand(length):
    password = ""

    for i in range(length):
        password += random.choice(chars)

    return password

if __name__ == "__main__":
    main()