# This program is to validate an entered password based on

import re


def validate():
    while True:
        password = raw_input("Enter a password: ")
        if len(password) < 8:
            print("Make sure your password is at least 8 characters")
        elif len(password) > 64:
            print("Your password is too long")
