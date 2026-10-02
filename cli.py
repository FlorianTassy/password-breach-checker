import getpass
import sys

def ask_password():
    try:
        password = getpass.getpass("Password: ")
     except (EOFError, KeyboardInterrupt):
        return None
    
    if password == "":
        print("Password is empty")
        return None

    return password
