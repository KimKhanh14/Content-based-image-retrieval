import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from main import retrieval

class MainApp(QMainWindow):
    width = 900
    height = 500
    window_Title = "Image Retrieval"

    def __init__(self):
        super().__init__()

        self.window_Title = "Image Retrieval"
        self.width = 900
        self.height = 500
        self.imagePath=None
        self.InitWindow()

    def InitWindow(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.window_Title)

        #Ảnh Query
        self.query_image = QLabel(self)
        self.query_image.setStyleSheet(" border: 4px dashed #aaa;")
        self.query_image.resize(150, 130)
        self.query_image.move(450, 350)
        #Button chọn ảnh
        self.browser_button = QPushButton('Browse Image', self)
        self.browser_button.setToolTip('This is an example button')
        self.browser_button.move(300, 350)
        self.browser_button.clicked.connect(self.browserImageClick)
        #Button Query
        self.query_button = QPushButton('Query Image', self)
        self.query_button.setToolTip('This is an example button')
        self.query_button.move(600, 350)
        self.query_button.clicked.connect(self.retrievalImage)
    def browserImageClick(self):
        selected_filter = "*.png *.jpg *.bmp"
        filename=QFileDialog.getOpenFileName(self,'Query Image',filter=selected_filter)
        self.imagePath = filename[0]

        pixmap = QPixmap(self.imagePath)
        self.query_image.resize(pixmap.width(), pixmap.height())
        self.query_image.setPixmap(pixmap)

    def retrievalImage(self):
        retrieval(self.imagePath)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())