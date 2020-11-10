# -*- coding: utf-8 -*-
"""
MainWindow
Window where Clock and Date should appear


@author: Felix Reichling
"""

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QLCDNumber
from PyQt5.QtCore import QDate, QTime, QTimer, Qt
import datetime


class MainWindow(QMainWindow):

    def __init__(self, width, height, verse, *args,**kwargs):
        
        
        
        super(MainWindow, self).__init__(*args, **kwargs)
       
        self.initUI(width, height, verse)
        print('successfully built initUI...')
        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()
        self.showDate()
        print('successfully showed lcd...')

        
    def initUI(self, width, height, verse):
        self.lcd = QLCDNumber(self)
        self.lcdDate = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.lcdDate.setDigitCount(10)
        
        self.label = QLabel(self)
        self.label.setText(verse)
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
        """
        date = QDate.currentDate()
        textDate = date.toString(format = Qt.ISODate)
        self.lcdDate.display(textDate)
        """
        date = QDate.currentDate()
        date.toString(Qt.ISODate)
        final = date.toString('dd.MM.yyyy')

        self.lcdDate.display(final)

        