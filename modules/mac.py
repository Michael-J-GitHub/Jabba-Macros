# * Copyright Michael Johnston - All Rights Reserved
# * Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
# * via any medium is strictly prohibited unless given explicit permission by the copyright holder.
# * Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021

import pyperclip
import keyboard


def mac(string):
    # Making all lowercase uppercase
    # print("Original: ", string)
    string = string.upper()
    # print("All uppercase: ", string)
    # Adding ":"" every 2 characters
    string = ':'.join(string[i:i + 2] for i in range(0, len(string), 2))
    keyboard.write(string)
    # print("Here is the MAC address: ", string)
