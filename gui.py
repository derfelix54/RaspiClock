# -*- coding: utf-8 -*-
"""
MainWindow
Window where Clock and Date should appear


@author: Felix Reichling
"""

from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLCDNumber
from PyQt5.QtCore import QTime, QTimer
import sys

class MainWindow(QMainWindow):
    




    def __init__(self, width, height,*args,**kwargs):
        
        
        
        super(MainWindow, self).__init__(*args, **kwargs)
       
        self.initUI(width, height)

        timer = QTimer(self)
        timer.timeout.connect(self.showlcd)
        timer.start(1000)
        self.showlcd()

        
        

        

    def initUI(self, width, height):
        self.lcd = QLCDNumber(self)
        self.lcd.setDigitCount(8)
        self.setGeometry(0,0,width,height)
        self.setWindowTitle('RaspiClock')

        layout = QVBoxLayout()
        layout.addWidget(self.lcd)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


        self.show()


    def showlcd(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.lcd.display(text)
 
        