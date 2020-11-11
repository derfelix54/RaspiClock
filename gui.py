# -*- coding: utf-8 -*-
"""
MainWindow
Window where Clock and Date should appear


@author: Felix Reichling
"""
import sys
import threading

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QLCDNumber
from PyQt5.QtCore import QDate, QTime, QTimer, Qt, QUrl, QCoreApplication, QObject, pyqtSignal
from PyQt5 import QtNetwork
import requests
from bs4 import BeautifulSoup

class Crawler(QObject):
    
        

    verseChanged = pyqtSignal(str)

    def start(self):
        threading.Thread(target = self._execute, daemon=True).start()


    def _execute(self):
        """
        docstring
        """
        result = requests.get('https://www.bible.com/verse-of-the-day')
        page = result.text
        soup = BeautifulSoup(page, 'html.parser')
        verse = soup.find('div', class_ = 'verse-wrapper').text

        verse = verse.replace(".", ". ")
        self.verseChanged.emit(verse)   

class MainWindow(QMainWindow):

    def __init__(self, width, height, parent = None):
        
        
        
        super(MainWindow, self).__init__(parent)

        self.initUI(width, height)

        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)

        self.showlcd()
        self.showDate()

        
    def initUI(self, width, height):
        self.lcd = QLCDNumber(digitCount=8)
        self.lcdDate = QLCDNumber(digitCount=10)

        
        self.label = QLabel(alignment = Qt.AlignCenter, wordWrap = True, text = "I Love you my child! -God")
        self.label.setFont(QFont('Times', 70, QFont.Bold))

        self.setGeometry(0, 0, width, height)
        

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.lcdDate)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        

    def showlcd(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.lcd.display(text)

    def showDate(self):
        date = QDate.currentDate()
        date.toString(Qt.ISODate)
        final = date.toString('dd.MM.yyyy')
        self.lcdDate.display(final)


    def set_verse(self, verse):
        self.label.setText(verse)

 


    




    

        