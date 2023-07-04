from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import  QMessageBox

app = QApplication([])


class AuthPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Authorization UI")
        self.setGeometry(100, 100, 400, 400)
        self.setStyleSheet("background-color:white;")
        self.loginTitle = QLabel("Log IN Form", self)
        self.loginTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginTitle.setStyleSheet("color:black;")
        self.loginTitle.setFixedSize(400, 30)
        self.loginTitle.move(0, 80)

        self.main_layout = QVBoxLayout(self)
        self.userNameLayout = QHBoxLayout()

        # username
        self.userNameLabel = QLabel("User Name")
        self.userNameLabel.setStyleSheet("color:black;")

        self.userNameEdit = QLineEdit()
        self.userNameEdit.setStyleSheet("background-color:purple")
        self.userNameEdit.setFixedSize(140, 30)

        self.userNameLayout.addStretch()
        self.userNameLayout.addWidget(self.userNameLabel)
        self.userNameLayout.addStretch()
        self.userNameLayout.addWidget(self.userNameEdit)
        self.userNameLayout.addStretch()

        # password
        self.passwordLayout = QHBoxLayout()

        self.passwordLabel = QLabel("Password")
        self.passwordLabel.setStyleSheet("color:black;")

        self.passwordEdit = QLineEdit()
        self.passwordEdit.setStyleSheet("background-color:purple")
        self.passwordEdit.setFixedSize(140, 30)

        self.passwordLayout.addStretch()
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addStretch()
        self.passwordLayout.addWidget(self.passwordEdit)
        self.passwordLayout.addStretch()

        #showMessageBox

        def showMessageBox(message):
            self.messageBox = QMessageBox()
            self.messageBox.setText(message)
            self.messageBox.exec()
            self.show()

        # buttons

        def register():
            f = open("users.txt", "a")
            f.write(self.userNameEdit.text() + "/" + self.passwordEdit.text()+"\n")
            f.close()
            self.userNameEdit.clear()
            self.passwordEdit.clear()
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
                        else:
                            status = "Parol xato kiritildi"
            else:
                status = "User hali ro'yxatdan o'tmagan"

            showMessageBox(status)
            self.userNameEdit.clear()
            self.passwordEdit.clear()


        self.buttonsLayout = QHBoxLayout()
        self.loginButton = QPushButton("Log In")
        self.registerButton = QPushButton("Register")

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
