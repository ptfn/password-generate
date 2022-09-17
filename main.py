from random import randint, choice
from colorama import Fore, Style
from base64 import b64encode
from hashlib import sha512
from math import log
import argparse

chars = """ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopq\
rstuvwxyz0123456789!?@#$%^&*=<>()[]/|,.+-_"'"""


def crt(string):
    char = {}
    for i in range(len(string)):
        try:
            char[string[i]] += 1
        except Exception:
            char[string[i]] = 1
    arr = [char[i] for i in char]
    return arr


def pass_ent(arr):
    total = sum(arr)
    entropy = 0
    for i in range(len(arr)):
        p = arr[i] / total
        if p > 0:
            entropy -= p * log(p, 2)
    return entropy / 8 * 100


def pass_lvl(num):
    if num < 37.5:
        return txt_rd('Bad')
    elif num < 40:
        return txt_yel('Weak')
    elif num < 50:
        return txt_grn('Good')
    else:
        return txt_grn('Excellent')


def pass_hash(string, lenght):
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

    args = parser.parse_args()
    leng = args.leng
    random = args.random
    hsh = args.hash

    if random:
        password = pass_rand(leng)
        entropy = round(pass_ent(crt(password)), 4)
        level = pass_lvl(entropy)
        print(f"Password\t{txt_grn(password)}\
\nEntropy\t\t{txt_grn(level)} ({entropy})")
    elif hsh:
        password = pass_hash(pass_rand(randint(1, leng)), leng)
        entropy = round(pass_ent(crt(password)), 4)
        level = pass_lvl(entropy)
        print(f"Password\t{txt_grn(password)}\
\nEntropy\t\t{txt_grn(level)} ({entropy})")
    else:
        print(txt_rd("Error!"))


if __name__ == "__main__":
    main()
