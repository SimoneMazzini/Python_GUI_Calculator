#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:47:27 2023

@author: simonemazzini
@reference: Main Guideline: https://realpython.com/python-pyqt-gui-calculator/
            Enumerate Function: https://www.programiz.com/python-programming/methods/built-in/enumerate
            Partial Function: https://www.geeksforgeeks.org/partial-functions-python/
            
"""

# CALCULATOR GUI BASED ON PyQt.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from functools import partial #Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function. (https://www.learnpython.org/en/Partial_functions)

window_size = 235
display_height = 35
button_size = 40
error_msg = 'Error'

class PycalcWindow(QMainWindow): # Class that control the main window displayed
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python Calculator")
        self.setFixedSize(window_size, window_size)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay() # Single Pre Underscore is used for internal use(https://towardsdatascience.com/5-different-meanings-of-underscore-in-python-3fafa6cd0379)
        self._createButtons()
        
    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(display_height)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyboard = [["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", "00", ".", "+", "="]
            ]
        for row, keys in enumerate(keyboard): #The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
                for col, key in enumerate(keys):
                    self.buttonMap[key] = QPushButton(key)
                    self.buttonMap[key].setFixedSize(button_size,button_size)
                    buttonsLayout.addWidget(self.buttonMap[key], row, col)
        self.generalLayout.addLayout(buttonsLayout)
    
    def setDisplayText(self, text):
        #Set the display's text.
        self.display.setText(text)
        self.display.setFocus()

    def displayText(self):
        #Get the display's text.
        return self.display.text()

    def clearDisplay(self):
        #Clear the display.
        self.setDisplayText("")
def evaluateExpression(expression):
    #Evaluate an expression (Model).
    try:
            result = str(eval(expression, {}, {}))
    except Exception:
            result = ERROR_MSG
    return result
    
    
class PyCalc: # Class that control the calculator

    def __init__(self, model, view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    def _calculateResult(self):
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)

    def _buildExpression(self, subExpression):
        if self._view.displayText() == error_msg:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)



def main():

    pycalcApp = QApplication([])
    pycalcWindow = PycalcWindow()
    pycalcWindow.show()
    PyCalc(model=evaluateExpression, view=pycalcWindow)
    sys.exit(pycalcApp.exec())

if __name__ == "__main__":   # We use the if statement and the condition __name__ == __main__ to declare that certain Python code should only be performed when the script is run directly.
    main()
    
    