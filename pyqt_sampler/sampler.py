""" This is my first foray into PyQt6 Initial set up code comes from
https://coderslegacy.com/python/pyqt6-create-basic-window/

Other links:
Icons from https://icon-icons.com/pack/Miscellany-Web-icons/692

"""

from PyQt6.QtWidgets import (QApplication, QVBoxLayout, QHBoxLayout,
                             QWidget, QLabel)
from PyQt6.QtGui import QIcon, QFont, QFontDatabase, QPixmap
from PyQt6.QtCore import Qt
import sys, os

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.dir_path = os.getcwd()
        self.load_fonts()
        self.UI()

    def load_fonts(self):
        """ I get my fonts as a ttf from fonts.google.com and download
        the to the resources folder. Be sure to include the license.

        Hint: you will need to make sure you get the name correct from
        Google fonts."""
        title_font_path = (
                self.dir_path +
                "/pyqt_sampler/resources/LibreBaskerville-Bold.ttf"
            )
        text_font_path = (
                self.dir_path +
                "/pyqt_sampler/resources/Montserrat-Regular.ttf"
        )
        id = QFontDatabase.addApplicationFont(
                title_font_path
            )
        id2 = QFontDatabase.addApplicationFont(
            text_font_path
        )

        # test to make sure both loaded correctly
        # addApplicationFont will return a -1 if there
        # is an error.
        if id < 0 or id2 < 0:
            print("Error")
            print(f"id = {id} and id2 = {id2}")

    def UI(self):
        # Initialize GUI components
        app_title = QLabel("Title of App")
        app_title.setAlignment(Qt.AlignmentFlag.AlignTop)
        app_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        app_title.setFont(QFont("Libre Baskerville", 20))
        
        app_description = QLabel("Description goes here.")
        app_description.setAlignment(Qt.AlignmentFlag.AlignTop)
        app_description.setFont(QFont("Montserrat", 12))
        
        search_label = QLabel("Search: ")
        # Set Layout
        vbox = QVBoxLayout()

        self.resize(300, 300)
        self.setWindowTitle("App Title")
        self.setWindowIcon(QIcon("icon.jpg"))
 
        layout = QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(app_title)
        layout.addWidget(app_description)

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
