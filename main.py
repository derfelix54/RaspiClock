"""
@author: Felix Reichling
"""



from PyQt5.QtWidgets import QApplication
from gui import MainWindow
import sys



"""
Main function to start the gui
"""

if __name__ == "__main__":


    app = QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    height = screen_res.height()
    width = screen_res.width()

    window = MainWindow(width, height)


    sys.exit(app.exec_())
