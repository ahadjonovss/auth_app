from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMessageBox

app = QApplication([])


class AuthPage(QWidget):
    def __init__(self):
        super().__init__()
        self.registerButton = QPushButton("Register")
        self.loginButton = QPushButton("Log In")
        self.buttonsLayout = QHBoxLayout()
        self.passwordEdit = QLineEdit()
        self.passwordLabel = QLabel("Password")
        self.passwordLayout = QHBoxLayout()
        self.userNameEdit = QLineEdit()
        self.userNameLabel = QLabel("User Name")
        self.userNameLayout = QHBoxLayout()
        self.main_layout = QVBoxLayout(self)
        self.saveButton = QPushButton("Save", self)
        self.saveButton.hide()
        self.userName = ''

        self.setWindowTitle("Authorization UI")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color:white;")
        self.loginTitle = QLabel("Log IN Form", self)
        self.loginTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginTitle.setStyleSheet("color:black;")
        self.loginTitle.setFixedSize(400, 30)
        self.loginTitle.move(0, 80)

        self.firstWindow()

    def firstWindow(self):

        def saveUserInfo():
            f = open("user_info.txt", "a")
            f.write(self.userName + "/" + self.userNameEdit.text() + "/" + self.passwordEdit.text() + "\n")
            f.close()

        def findUserData():
            f = open("user_info.txt", "r")
            self.allUserDataString = f.read()
            self.userDataList = self.allUserDataString.split('\n')
            for user in self.userDataList:
                currentUser = user.split('/')
                if currentUser[0] == self.userName:
                    self.userNameEdit.setText(currentUser[1])
                    self.passwordEdit.setText(currentUser[2])

        def showNextWindow(self):
            self.registerButton.hide()
            self.loginButton.hide()
            self.loginTitle.setText("Xush kelibsiz")
            self.userNameLabel.setText("Ism")
            self.passwordLabel.setText("Familiya")
            self.main_layout.addWidget(self.saveButton)
            self.saveButton.setStyleSheet("background-color:green;\ncolor:black")
            self.saveButton.show()
            self.saveButton.clicked.connect(saveUserInfo)
            findUserData()

        def register():
            f = open("users.txt", "a")
            f.write(self.userNameEdit.text() + "/" + self.passwordEdit.text() + "\n")
            f.close()
            self.userName = self.userNameEdit.text()
            self.userNameEdit.clear()
            self.passwordEdit.clear()
            showNextWindow(self)
            showMessageBox("Muvaffaqqiyatli ro'yxatdan o'tdingiz")

        def signIn():
            f = open("users.txt")
            listOfUsers = f.read().split('\n')
            status = ''
            usernames = []

            for user in listOfUsers:
                usernames.append(user.split('/')[0])

            if self.userNameEdit.text() in usernames:
                for i in listOfUsers:
                    if i.split('/')[0] == self.userNameEdit.text():
                        if i.split('/')[1] == self.passwordEdit.text():
                            status = "Login qila oldingiz"
                            self.userName = self.userNameEdit.text()
                            showNextWindow(self)

                        else:
                            status = "Parol xato kiritildi"
            else:
                status = "User hali ro'yxatdan o'tmagan"

            showMessageBox(status)


        def showMessageBox(message):
            self.messageBox = QMessageBox()
            self.messageBox.setText(message)
            self.messageBox.exec()
            self.show()

        # username
        self.userNameLabel.setStyleSheet("color:black;")

        self.userNameEdit.setStyleSheet("background-color:purple")
        self.userNameEdit.setFixedSize(140, 30)

        self.userNameLayout.addStretch()
        self.userNameLayout.addWidget(self.userNameLabel)
        self.userNameLayout.addStretch()
        self.userNameLayout.addWidget(self.userNameEdit)
        self.userNameLayout.addStretch()

        # password

        self.passwordLabel.setStyleSheet("color:black;")

        self.passwordEdit.setStyleSheet("background-color:purple")
        self.passwordEdit.setFixedSize(140, 30)

        self.passwordLayout.addStretch()
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addStretch()
        self.passwordLayout.addWidget(self.passwordEdit)
        self.passwordLayout.addStretch()

        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.registerButton)
        self.buttonsLayout.addStretch()
        self.buttonsLayout.addWidget(self.loginButton)
        self.buttonsLayout.addStretch()

        self.registerButton.setStyleSheet("background-color:yellow;\ncolor:black")
        self.loginButton.setStyleSheet("background-color:green;\ncolor:black")

        self.registerButton.clicked.connect(register)
        self.loginButton.clicked.connect(signIn)

        self.registerButton.move(80, 0)

        # mainLayout
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.userNameLayout)
        self.main_layout.addLayout(self.passwordLayout)
        self.main_layout.addLayout(self.buttonsLayout)
        self.main_layout.addStretch()

        self.setLayout(self.main_layout)


window = AuthPage()
window.show()
app.exec()
