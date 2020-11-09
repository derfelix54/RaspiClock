"""
@author: Felix Reichling
"""



from PyQt5.QtWidgets import QApplication
from gui import MainWindow
import sys
import requests
from bs4 import BeautifulSoup


"""
Main function to start the gui
"""

if __name__ == "__main__":


    app = QApplication(sys.argv)
    screen_res = app.desktop().screenGeometry()
    height = screen_res.height()
    width = screen_res.width()

    result = requests.get('https://www.bible.com/verse-of-the-day')
    page = result.text
    soup = BeautifulSoup(page, 'html.parser')
    verse = soup.find('div', class_ = 'verse-wrapper').text

    window = MainWindow(width, height, verse)


    sys.exit(app.exec_())
