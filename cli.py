import argparse
import getpass
import sys

from entropy import characters_pool_size, families, naive_entropy

def ask_password():
    try:
        password = getpass.getpass("Password: ")
    except (EOFError, KeyboardInterrupt):
        return None
    
    if password == "":
        print("Password is empty")
        print("\nAborted")
        return None

    return password

def main(argv=None):
    parser = argparse.ArgumentParser(prog="pwcheck", description="Password strength checker.")
    parser.parse_args(argv)
 
    password = ask_password()
    if password is None:
        return 2
 
    print(len(password))

    print("Entropy = " + str(naive_entropy(password)))

    return 0

if __name__ == "__main__":
    sys.exit(main())
