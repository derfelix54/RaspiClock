"""
@author: Felix Reichling
"""



from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication
from gui import Crawler, MainWindow
import sys
import schedule
from bs4 import BeautifulSoup


"""
Main function to start the gui
"""

if __name__ == "__main__":


    app = QApplication(sys.argv)
    
    
    w = MainWindow()

    crawler = Crawler()
    crawler.verseChanged.connect(w.set_verse)

    schedule.every().day.at("12:45").do(crawler.start)

    dt = 1000
    schedule_timer = QTimer(interval = dt, timeout = schedule.run_pending)
    schedule_timer.start()
    schedule.run_pending()

    w.showMaximized()


    app.exec_()
