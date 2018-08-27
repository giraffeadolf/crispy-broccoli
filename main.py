import sys
from PyQt5 import QtWidgets
import design
from db import user, session


class Chat(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendButton.clicked.connect(self.on_clicked_button)
        self.chatTextField.returnPressed.connect(self.on_clicked_button)

        user_list = session.query(user).all()
        for u in user_list:
            self.listWidget.addItem(u)

    def on_clicked_button(self):
        text = self.chatTextField.text().toUtf8()
        self.chat.addItem(text)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Chat()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
