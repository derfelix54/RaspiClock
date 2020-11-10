# -*- coding: utf-8 -*-
"""
MainWindow
Window where Clock and Date should appear


@author: Felix Reichling
"""

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QLCDNumber
from PyQt5.QtCore import QDate, QTime, QTimer, Qt, QUrl, QCoreApplication
from PyQt5 import QtNetwork
import requests
from bs4 import BeautifulSoup



class MainWindow(QMainWindow):

    def __init__(self, width, height, *args,**kwargs):
        
        
        
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI(width, height)
        print('successfully built initUI...')
        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)

        updateVerse = QTimer(self)
        updateVerse.timeout.connect(self.redraw_Verse)
        QTimer.singleShot(0, self.redraw_Verse)
        updateVerse.start(60000*555) #update every 6 hours

        self.showlcd()
        self.showDate()
        print('successfully showed lcd...')

        
    def initUI(self, width, height):
        self.lcd = QLCDNumber(self)
        self.lcdDate = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcdDate.setDigitCount(10)
        
        self.label = QLabel(self)
        self.label.setFont(QFont('Times', 70, QFont.Bold))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        

        

        self.setGeometry(0,0,width,height)
        self.setWindowTitle('RaspiClock')

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)
        layout.addWidget(self.lcdDate)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
        self.show()


    def showlcd(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.lcd.display(text)

    def showDate(self):
        date = QDate.currentDate()
        date.toString(Qt.ISODate)
        final = date.toString('dd.MM.yyyy')

        self.lcdDate.display(final)


    def redraw_Verse(self):
        result = requests.get('https://www.bible.com/verse-of-the-day')
        page = result.text
        soup = BeautifulSoup(page, 'html.parser')
        self.verse = soup.find('div', class_ = 'verse-wrapper').text

        self.verse = self.verse.replace(".", ". ")
        self.label.setText(self.verse)

 


    




    

        