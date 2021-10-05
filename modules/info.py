# * Copyright Michael Johnston - All Rights Reserved
# * Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
# * via any medium is strictly prohibited unless given explicit permission by the copyright holder.
# * Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021


def instructions():
    print("""────────────────────────────────────────────────────────────────────────────────
Instructions:

Phone/MAC address Macro
    CTRL+SHIFT+V: Pastes a modified phone number or MAC address into the text box that you have selected.

Forms (Number keys or Num Pad)
    CTRL+1: Pastes offline antenna form into text box you have selected.
    CTRL+2: Pastes new customer install form into text box you have selected.

Features and more detail
    CTRL+M: Shows more detail on what the hotkeys do, how they work, and where it could be useful to use them.

Copyright
    CTRL+L: Shows copyright notice.

Press ENTER to close the program
────────────────────────────────────────────────────────────────────────────────""")


def more_detail():
    print("""────────────────────────────────────────────────────────────────────────────────
Instructions:

Phone/MAC address Macro (CTRL+SHIFT+V)
    How do I use it?
    Copy a phone number or mac address to your clipboard(CTRL+C) and press CTRL+SHIFT+V after clicking into text box where you want to paste the modified phone number or mac address.

    How does it work?
    If you have a phone number copied to your clipboard it will remove all parentheses, dashes, periods, blank spaces, and country codes from the number.
    If you have a MAC address copied to your clipboard it will make all lowercase letters uppercase, and insert a : every two spaces.

    Why is this useful and where might I use it?
    When you copy a phone number or MAC address from somewhere (snap mobile, voice mail, Meraki, etc.)
    and go to paste it into UBO or Aradial you can have issues pulling up a customers details because it's not in the correct format.

Forms (CTRL+1) (CTRL+2)
    How do I use it?
    Click into the text box in the ticket website, press CTRL+1 or CTRL+2 depending if you want the offline antenna or new customer install form.
    CTRL+1 = Offline Antenna
    CTRL+2 = New customer install

    Why is this useful?
    Speeds up writing out all of the details you need for a offline antenna or new customer install and makes sure you don't forget anything.

To show the original instructions details: CTRL+P

Press ENTER to close the program
────────────────────────────────────────────────────────────────────────────────""")


def legal():
    print("""────────────────────────────────────────────────────────────────────────────────
* Copyright Michael Johnston - All Rights Reserved
* Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
* via any medium is strictly prohibited unless given explicit permission by the copyright holder.
* Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021

To show the original instructions details: CTRL+P

Press ENTER to close the program
────────────────────────────────────────────────────────────────────────────────""")
