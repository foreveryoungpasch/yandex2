import sqlite3
import sys
from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow


class CoffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.info_button.clicked.connect(self.run)

    def run(self):
        self.items_result = self.con.cursor().execute(f"""SELECT * FROM coffee
                                                           WHERE name = '{self.name_edit.text()}'""").fetchall()
        self.fill_page(self.items_result[0])

    def fill_page(self, result):
        self.id_edit.setText(str(result[0]))
        self.roast_edit.setText(result[2])
        self.type_edit.setText(result[3])
        self.description_edit.setPlainText(result[4])
        self.price_edit.setText(str(result[5]))
        self.size_edit.setText(str(result[6]))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeInfo()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
