import sys, random, sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QListWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.grains = {
            0: 'молотый',
            1: 'в зернах'
        }
        self.load_data()

    def load_data(self):
        con = sqlite3.connect('coffee.sqlite')
        for id, name, roast, grains, taste, price, volume in con.cursor().execute('select * from coffee'):
            text = 'Номер ' + str(id) + ': "' + name + '", степень обжарки: ' + str(roast) + ', '
            text += self.grains[grains] + ', ' + taste + ', ' + str(price) + ' рублей' + ', '
            text += str(volume) + ' миллилитров'
            item = QListWidgetItem()
            item.setText(text)
            self.listWidget.insertItem(self.listWidget.currentRow() + 1, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
