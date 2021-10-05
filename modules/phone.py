# * Copyright Michael Johnston - All Rights Reserved
# * Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
# * via any medium is strictly prohibited unless given explicit permission by the copyright holder.
# * Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021

import pyperclip
import keyboard


def phone(string):
    # Is the phone number 10 digits?
    length = len(string)
    # print("Length = ", length)
    if length == 11:
        # print("Phone number is 11 digits, removing the 11th")
        string = string[1:]
    keyboard.write(string)
    # print("Here is the phone number: " + string)
