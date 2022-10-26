from random import randint, choice
from colorama import Fore, Style
from base64 import b64encode
from hashlib import sha512
from math import log2
import argparse

big_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small_chars = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = r'''!?@#$%^&*=<>()[]/\|,.+-_'"'''
chars = big_chars + small_chars + numbers + symbols


def pass_ent(string):
    return round(len(string) * log2(256), 4)


def pass_lvl(num):
    if num < 30:
        return txt_rd("Pathetic")

    elif num < 50:
        return txt_rd("Bad")

    elif num < 70:
        return txt_yel("Weak")

    elif num < 120:
        return txt_grn("Good")

    else:
        return txt_grn("Excellent")


def hex_to_dec(string, begin, end):
    return chr(int(string[begin:end], 16))


def pass_hash(string, lenght):
    for i in range(randint(2, 128)):
        string = sha512(str(string).encode("ascii")).hexdigest()

    strhash = ""

    for i in range(0, len(string)-2, 2):
        strhash += hex_to_dec(string, i, i+2)

    return strhash[:lenght]


def pass_base(string, lenght):
    for i in range(randint(2, 128)):
        string = sha512(str(string).encode("ascii")).hexdigest()

    encbyte = b64encode(string.encode("utf-8"))
    encstr = str(encbyte, "utf-8")[:lenght]

    return encstr


def pass_rand(length):
    password = ""

    for i in range(length):
        password += choice(chars)

    return password


def gen_pass(password):
    entropy = pass_ent(password)
    level = pass_lvl(entropy)
    return f"Password\t{txt_grn(password)}\
\nEntropy\t\t{txt_grn(level)} ({entropy} Bit)"


def txt_grn(text):
    return Fore.GREEN + text + Style.RESET_ALL


def txt_rd(text):
    return Fore.RED + text + Style.RESET_ALL


def txt_yel(text):
    return Fore.YELLOW + text + Style.RESET_ALL


def main():
    parser = argparse.ArgumentParser(description='Password Generate')
    parser.add_argument('-l', '--length', type=int,
                        dest='leng', help='Length password')
    parser.add_argument('-r', '--random', action='store_true',
                        dest='random', help='Random algorithm')
    parser.add_argument('-hs', '--hash', action='store_true',
                        dest='hash', help='Hash algorithm')
    parser.add_argument('-b', '--base', action='store_true',
                        dest='base', help='Base64 and hash algorithm')

    args = parser.parse_args()
    leng = args.leng
    random = args.random
    hsh = args.hash
    base = args.base

    if random:
        password = pass_rand(leng)
        print(gen_pass(password))

    elif hsh:
        password = pass_hash(pass_rand(randint(1, leng)), leng)
        print(gen_pass(password))

    elif base:
        password = pass_base(pass_rand(randint(1, leng)), leng)
        print(gen_pass(password))

    else:
        print(txt_rd("Error!"))


if __name__ == "__main__":
    main()
