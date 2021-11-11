# * Copyright Michael Johnston - All Rights Reserved
# * Unauthorized usage, copying, distribution, modification, or decompiling of this file or program,
# * via any medium is strictly prohibited unless given explicit permission by the copyright holder.
# * Written by Michael Johnston < Michael.Johnston.T@gmail.com >, September 2021

import keyboard
import pyperclip
import time

PASTE = "ctrl+v"

OFFLINE_ANTENNA = """<b>Offline Antenna:</b>

What did the customer say when they called in? Answ:
(EX: CX called saying internet not working.)
How long has this issue been happening? Answ:
Are all devices having issues or only specific devices? Answ:
(If they are specific devices what type of devices are having issues)

<b>Antenna:</b>
Does the antenna show up in the neighbors list in MT? Answ:
(This is the most import detail when checking the status of the antenna)
Have you had the customer power cycled the antenna and router? Answ:
Antenna MAC? Answ:

<b>POE:</b>
Is the light on the POE splitter on? Answ:
Is the splitter plugged into the back of the routers WAN port? Answ:
Ethernet cable plugged into wall outlet and plugged into the splitter? Answ:

<b>Router:</b>
Are there any lights on the router? Answ:
Is customers router cambium? Answ:
(If not cambium what brand is it?)
Does the router show as offline in cambium? Answ:
If you ping yahoo.com does it timeout? Answ:
Where is the router located? Answ:
(EX: Within 10ft and out in the open on top of a dresser. Make sure that it is within 30 feet, has line of sight, not too many walls)
"""

NEW_INSTALL = """<b>New Install:</b>
Internet
What speed the customer wants? Answ:
Does the customer have their own router or want one from us? Answ:
Customer aware of install fee? Answ:
If the customer is not staying at the resort currently when will they be there? Answ:

JabbaTV
Does the customer want JabbaTV? Answ:
Is the customer on a 15mbps plan or higher? Answ:
(15mbps is the minium required for JabbaTV)
Does the customer need a roku? Answ:
Is the customer aware of the install fee? Answ:
"""


def offline_antenna():
    original = str(pyperclip.paste())
    pyperclip.copy(OFFLINE_ANTENNA)
    time.sleep(0.05)
    keyboard.send(PASTE)
    time.sleep(0.05)
    pyperclip.copy(original)


def new_install():
    original = str(pyperclip.paste())
    pyperclip.copy(NEW_INSTALL)
    time.sleep(0.05)
    keyboard.send(PASTE)
    time.sleep(0.05)
    pyperclip.copy(original)
