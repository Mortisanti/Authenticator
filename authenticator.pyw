import sys
import pyotp
import pyperclip

# from threading import Thread
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from my_secrets import (
    DISCORD_2FA_SECRET,
    FB_2FA_SECRET,
    GITHUB_2FA_SECRET,
    TWITCH_2FA_SECRET,
    HEROKU_2FA_SECRET,
    EA_2FA_SECRET
)

WIDTH = 270
HEIGHT = 200

# View
class AuthenticatorUi(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Authenticator")
        self.setFixedSize(WIDTH, HEIGHT)
        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        self._createLabelsAndButtons()

    def _createLabelsAndButtons(self):
        self.labels = {}
        self.buttons = {}
        innerLayout = QGridLayout()
        labels = {
            "Discord":  (0, 0),
            "Facebook": (1, 0),
            "GitHub":   (2, 0),
            "Twitch":   (3, 0),
            "Heroku":   (4, 0),
            "EA":       (5, 0)
        }
        buttons = {
            DISCORD_2FA_SECRET: ("Copy code", (0, 1)),
            FB_2FA_SECRET:      ("Copy code", (1, 1)),
            GITHUB_2FA_SECRET:  ("Copy code", (2, 1)),
            TWITCH_2FA_SECRET:  ("Copy code", (3, 1)),
            HEROKU_2FA_SECRET:  ("Copy code", (4, 1)),
            EA_2FA_SECRET:      ("Copy code", (5, 1))
        }
        for labelText, pos in labels.items():
            self.labels[labelText] = QLabel(labelText)
            innerLayout.addWidget(self.labels[labelText], pos[0], pos[1])
        for buttonName, codeAndPos in buttons.items():
            self.buttons[buttonName] = QPushButton(codeAndPos[0])
            innerLayout.addWidget(self.buttons[buttonName], codeAndPos[1][0], codeAndPos[1][1])
        self.generalLayout.addLayout(innerLayout)

    def showAuthCode(self, buttonName, text):
        """Set button text to respective 2FA code"""
        self.buttons[buttonName].setText(f"Copied {text}")

class AuthenticatorCtrl:
    """Authenticator Controller class"""
    def __init__(self, model, view):
        """Controller initializer"""
        self._generate = model
        self._view = view
        # Connect signals and slots
        self._connectSignals()

    def _getAuthCode(self, serviceName):
        authCode = self._generate(service=serviceName)
        self._view.showAuthCode(serviceName, authCode)

    def _connectSignals(self):
        """Connect signals and slots"""
        for buttonName, button in self._view.buttons.items():
            button.clicked.connect(partial(self._getAuthCode, buttonName))

def generateCode(service):
    authCode = pyotp.TOTP(service).now()
    pyperclip.copy(authCode)
    return authCode
                

def main():
    authenticator = QApplication(sys.argv)
    view = AuthenticatorUi()
    view.show()
    model = generateCode
    AuthenticatorCtrl(model=model, view=view)
    sys.exit(authenticator.exec_())

if __name__ == '__main__':
    main()