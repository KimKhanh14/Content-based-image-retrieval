import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from matplotlib import *
from main import retrieval

class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.imagePath = None
        self.window_Title = "Image Retrieval"
        self.width = 900
        self.height = 500

        self.imageWidth=150
        self.imageHeight = 200
        self.InitWindow()

    def InitWindow(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(self.width,self.height)
        self.setWindowTitle(self.window_Title)
        #Ảnh kết quả
        self.result_image=QLabel(self)
        self.result_image.setStyleSheet(" border: 4px dashed #aaa;")
        self.result_image.resize(670, 480)
        self.result_image.move(10, 10)
        #Ảnh Query
        self.query_image = QLabel(self)
        self.query_image.setStyleSheet(" border: 4px dashed #aaa;")
        self.query_image.resize(self.imageWidth,  self.imageHeight)
        self.query_image.move(self.width-200, 10)
        #Button chọn ảnh
        self.browser_button = QPushButton('Browse Image', self)
        self.browser_button.setToolTip('Click This To Choose Your Image')
        self.browser_button.resize(155,20)
        self.browser_button.move(self.width-200, 230)
        self.browser_button.clicked.connect(self.browserImageClick)
        #Button Query
        self.query_button = QPushButton('Query Image', self)
        self.query_button.setToolTip('Retrieval Similar Images')
        self.query_button.resize(155, 20)
        self.query_button.move(self.width-200, 260)
        self.query_button.clicked.connect(self.retrievalImage)
        # Button Clear
        self.clear_button = QPushButton('Clear', self)
        self.clear_button.setToolTip('Clear Contents')
        self.clear_button.resize(155, 20)
        self.clear_button.move(self.width - 200, 290)
        self.clear_button.clicked.connect(self.clear)

    def browserImageClick(self):
        selected_filter = "*.png *.jpg *.bmp"
        filename=QFileDialog.getOpenFileName(self,'Query Image',filter=selected_filter)
        self.imagePath = filename[0]

        brImg_pixmap = QPixmap(self.imagePath)

        brImg_pixmap=brImg_pixmap.scaled(self.imageWidth,self.imageHeight)
        self.query_image.resize(brImg_pixmap.width(), brImg_pixmap.height())
        self.query_image.setPixmap(brImg_pixmap)

    def retrievalImage(self):
        if( self.imagePath == None):
            dlg = CustomDialog()
            dlg.exec()
        else:
            result_pixmap=retrieval(self.imagePath)
            result_pixmap = result_pixmap.scaled(670, 480)
            self.result_image.resize(result_pixmap.width(), result_pixmap.height())
            self.result_image.setPixmap(result_pixmap)

    def clear(self):
        self.imagePath = None
        self.query_image.clear()
        self.result_image.clear()

#Custom Dialog
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Empty Image")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel("Please Choose Your Image?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())