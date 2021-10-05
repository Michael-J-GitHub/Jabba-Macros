# * Copyright Michael Johnston - All Rights Reserved
# * Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
# * via any medium is strictly prohibited unless given explicit permission by the copyright holder.
# * Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021

import keyboard
import pyperclip
from modules import phone
from modules import mac
from modules import forms
from modules import info


PHONE_AND_MAC = "ctrl+shift+v"
FORMS1 = "ctrl+1"
FORMS2 = "ctrl+2"
INSTRUCTIONS = "ctrl+p"
MORE_DETAIL = "ctrl+m"
LEGAL = "ctrl+l"
REMOVE = " ()[]{}-.:"


def cleanup_and_check():
    string = str(pyperclip.paste())

    original = string
    # print("Original: ", original)

    # Removing Blank Spaces, Dashes, Brackets, Period, and Colons.
    for i in REMOVE:
        string = string.replace(i, "")
    # print("Cleaned up: ", string)

    # Check string length to determine if it's a phone number or MAC.
    length = len(string)
    # print("Len: ", len(string))

    if length > 12 or length < 10:
        # print(string, "is not a phone number or MAC, pasting original.")
        keyboard.write(original)
    elif length == 12:
        # print(string, "is a MAC address. Running mac macro")
        mac.mac(string)
    else:
        # print(string, "is a phone number. Running phone macro")
        phone.phone(string)


def offline_antenna():
    forms.offline_antenna()


def new_install():
    forms.new_install()


def instructions():
    info.instructions()


def more_detail():
    info.more_detail()


def legal():
    info.legal()


keyboard.add_hotkey(PHONE_AND_MAC, cleanup_and_check, suppress=True)
keyboard.add_hotkey(FORMS1, offline_antenna, suppress=True)
keyboard.add_hotkey(FORMS2, new_install, suppress=True)
keyboard.add_hotkey(INSTRUCTIONS, instructions, suppress=True)
keyboard.add_hotkey(MORE_DETAIL, more_detail, suppress=True)
keyboard.add_hotkey(LEGAL, legal, suppress=True)
keyboard.wait

instructions()
input("")
