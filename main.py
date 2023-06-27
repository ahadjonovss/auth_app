from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtCore import Qt

app = QApplication([])
window = QWidget()

window.setWindowTitle("Authorization UI")
window.setGeometry(100, 100, 400, 400)
window.setStyleSheet("background-color:white;")

successfullyLabel = QLabel("You have been successfully logged in", window)
successfullyLabel.setFixedSize(400, 400)
successfullyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
successfullyLabel.setStyleSheet("color:black;\nfont-size:20px;")
successfullyLabel.hide()

loginTitle = QLabel("Login Form", window)
loginTitle.setGeometry(0, 0, 400, 80)
loginTitle.setStyleSheet("color:black;\nfont-size:18px;")
loginTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

userNameLabel = QLabel("UserName", window)
userNameLabel.setStyleSheet("color:black;\nfont-size:18px;")
userNameLabel.move(40, 120)

userNameEdit = QLineEdit(window)
userNameEdit.setGeometry(180, 115, 140, 30)
userNameEdit.placeholderText()
userNameEdit.setStyleSheet("background-color:purple;")

passwordLabel = QLabel("Password", window)
passwordLabel.setStyleSheet("color:black;\nfont-size:18px;")
passwordLabel.move(40, 160)

passwordEdit = QLineEdit(window)
passwordEdit.setGeometry(180, 155, 140, 30)
passwordEdit.setStyleSheet("background-color:purple;")

signUpButton = QPushButton("Sing Up", window)
signUpButton.move(80, 210)
signUpButton.setFixedSize(80, 30)
signUpButton.setStyleSheet("background-color:yellow;\ncolor:black;\nfont-size:12px;")

signInButton = QPushButton("Sing In", window)
signInButton.move(200, 210)
signInButton.setFixedSize(80, 30)
signInButton.setStyleSheet("background-color:green;\ncolor:black;\nfont-size:12px;")

backRegisterPageButton = QPushButton("Back to Register Window", window)
backRegisterPageButton.move(200, 210)
backRegisterPageButton.adjustSize()
backRegisterPageButton.setStyleSheet("background-color:green;\ncolor:black;\nfont-size:12px;")
backRegisterPageButton.hide()


listOfWidgets = [loginTitle, userNameLabel, userNameEdit, passwordLabel, passwordEdit, signInButton, signUpButton]


def hideRegisterPage():
    for i in listOfWidgets:
        i.hide()
    successfullyLabel.show()
    backRegisterPageButton.show()


def showRegisterPage():
    for i in listOfWidgets:
        i.show()
    successfullyLabel.hide()
    backRegisterPageButton.hide()


def signUp():
    f = open("user.txt", "a")
    userData = userNameEdit.text() + "/" + passwordEdit.text() + "\n"
    f.write(userData)
    userNameEdit.clear()
    passwordEdit.clear()
    hideRegisterPage()
    print("User data successfully written")

backRegisterPageButton.clicked.connect(showRegisterPage)
signUpButton.clicked.connect(signUp)

window.show()
app.exec()
