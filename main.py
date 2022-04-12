import random
import hashlib
import base64

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!?@#$%^&*=<>()[]/|,.+-_"


def main():
    print("----- \033[32mPassGen\033[0m -----")
    while True:
        chc = input("Enter code:\n1) Password\n2) Help\n3) Exit\n:")
        
        if chc == "Password" or chc == "password" or chc == "pass" or chc == "1":
            opt = input("Choose a way to generate your password:\n1) Random\n2) Hash\n:")

            if opt == "hash" or opt == "Hash" or opt == "2":
                text = input("Enter text\n:")
                
                if text == "":
                    print("\033[31m{}\033[0m\n".format("The text is not visible!"))
                    # exit(0)
                
                else:
                    leng = int(input("Length passwords (max 64)\n:"))

                    if leng <= 0:
                        print("\033[31m{}\033[0m\n".format("Incorrect password length!"))
                        # exit(0)
                    
                    else:
                        password = pass_hash(leng, text)
                        print("Password -> \033[32m{}\033[0m\n".format(password))
            
            elif opt == "Random" or opt == "random" or opt == "rand" or opt == "1":
                leng = int(input("Length passwords\n:"))

                if leng <= 0:
                    print("033[31m{}\033[0m\n".format("Incorrect password length!"))
                    # exit(0)
                
                else:
                    password = pass_rand(leng)
                    print("Password -> \033[32m{}\033[0m\n".format(password))

            else:
                print("\033[31m{}\033[0m\n".format("Error option!"))
                # exit(0)

        elif chc == "Help" or chc == "help" or chc == "2":
            print("The utility is designed to generate a password. To generate a password, select 'Password'\n")

        elif chc == "Exit" or chc == "exit" or chc == "quit" or chc == "Quit" or chc == "3":
            break

        else:
            print("\033[31m{}\033[0m\n".format("Error choice!"))


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