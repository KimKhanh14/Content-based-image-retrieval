import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainApp(QMainWindow):
    width = 900
    height = 500
    window_Title = "Image Retrieval"

    def __init__(self):
        super().__init__()

        self.window_Title = "Image Retrieval"
        self.width = 900
        self.height = 500

        self.InitWindow()

    def InitWindow(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.window_Title)

        #Ảnh Query
        self.query_image = QLabel(self)
        self.query_image.move(100, 100)
        pixmap = QPixmap('cat.jpg')
        self.query_image.resize(pixmap.width(), pixmap.height())
        self.query_image.setPixmap(pixmap)

        #Button chọn ảnh
        self.browser_button = QPushButton('Browse Image', self)
        self.browser_button.setToolTip('This is an example button')
        self.browser_button.move(int(self.width/2.5), int(self.height/1.2))
        self.browser_button.clicked.connect(self.browserImageClick)

    def browserImageClick(self):
        selected_filter = "*.png *.jpg *.bmp"
        filename=QFileDialog.getOpenFileName(self,'Query Image',filter=selected_filter)
        imagePath = filename[0]
        pixmap = QPixmap(imagePath)
        self.query_image.resize(pixmap.width(), pixmap.height())
        self.query_image.setPixmap(pixmap)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())