from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainApp(QMainWindow):
    width = 900
    height = 500
    window_Title = "Image Retrieval"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.window_Title)

        #Ảnh Query
        query_image = QLabel(self)
        query_image.move(100, 100)
        pixmap = QPixmap('cat.jpg')
        query_image.resize(pixmap.width(), pixmap.height())
        query_image.setPixmap(pixmap)

        #Button chọn ảnh
        browser_button = QPushButton('Browse Image', self)
        browser_button.setToolTip('This is an example button')
        browser_button.move(int(self.width/2.5), int(self.height/1.2))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())