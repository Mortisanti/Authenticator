import os
import sys
import pyotp
import pyperclip
import asyncio
from cryptography.fernet import Fernet
from PyQt5.QtGui     import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore    import *
# from threading import Thread
# from my_secrets import (
#     DISCORD_2FA_SECRET, 
#     FB_2FA_SECRET,
#     GITHUB_2FA_SECRET,
#     TWITCH_2FA_SECRET,
#     HEROKU_2FA_SECRET,
#     EA_2FA_SECRET
# )

# https://realpython.com/python-pyqt-gui-calculator/

app = QApplication(sys.argv)

posX = 100
posY = 100
width = 270
height = 80

mainWindow = QWidget()
mainWindow.setWindowTitle("2FA Authenticator")
mainWindow.setGeometry(posX, posY, width, height)
layout = QGridLayout()
mainWindow.setLayout(layout)

# Labels
label0 = QLabel("Discord:")
label1 = QLabel("Facebook:")
label2 = QLabel("GitHub:")
label3 = QLabel("Twitch:")
label4 = QLabel("Heroku:")
label5 = QLabel("EA:")
layout.addWidget(label0, 0, 0)
layout.addWidget(label1, 1, 0)
layout.addWidget(label2, 2, 0)
layout.addWidget(label3, 3, 0)
layout.addWidget(label4, 4, 0)
layout.addWidget(label5, 5, 0)

# Text boxes
codeButton0 = QPushButton("315468")
codeButton1 = QPushButton("194854")
codeButton2 = QPushButton("318458")
codeButton3 = QPushButton("468513")
codeButton4 = QPushButton("976854")
codeButton5 = QPushButton("973681")
layout.addWidget(codeButton0, 0, 1)
layout.addWidget(codeButton1, 1, 1)
layout.addWidget(codeButton2, 2, 1)
layout.addWidget(codeButton3, 3, 1)
layout.addWidget(codeButton4, 4, 1)
layout.addWidget(codeButton5, 5, 1)


# Countdown timer for each code


mainWindow.show()
sys.exit(app.exec_())

auth_dict = {
    1: DISCORD_2FA_SECRET,
    2: FB_2FA_SECRET,
    3: GITHUB_2FA_SECRET,
    4: TWITCH_2FA_SECRET,
    5: HEROKU_2FA_SECRET,
    6: EA_2FA_SECRET
}

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def main():
    def generate_code(user_input):
        auth_code = pyotp.TOTP(auth_dict[user_input]).now()
        pyperclip.copy(auth_code)
        return auth_code

    print("Discord: 1")
    print("Facebook: 2")
    print("GitHub: 3")
    print("Twitch: 4")
    print("Heroku: 5")
    print("EA/Origin: 6")
    user_input = int(input("Choose a number: "))
    auth_code = generate_code(user_input)
    print(f"Code: {auth_code} copied to clipboard")
    input("Press any key to clear.")
    clear()
    input("Press any key to exit.")

if __name__ == '__main__':
    main()