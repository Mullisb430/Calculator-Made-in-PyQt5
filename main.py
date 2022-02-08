import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QGridLayout, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 600)

        calculator = QWidget(self)
        gridLayout = QGridLayout()
        self.setCentralWidget(calculator)
        calculator.setLayout(gridLayout)
        numberButtons = list()

        self.calculationBox = QLineEdit()
        self.calculationBox.setFixedHeight(30)
        gridLayout.addWidget(self.calculationBox, 0, 0, 1, 4)

        buttonZero = QPushButton()
        numberButtons.append(buttonZero)
        gridLayout.addWidget(buttonZero, 5, 1, 1, 1)

        buttonOne = QPushButton()
        numberButtons.append(buttonOne)
        gridLayout.addWidget(buttonOne, 2, 0, 1, 1)

        buttonTwo = QPushButton()
        numberButtons.append(buttonTwo)
        gridLayout.addWidget(buttonTwo, 2, 1, 1, 1)

        buttonThree = QPushButton()
        numberButtons.append(buttonThree)
        gridLayout.addWidget(buttonThree, 2, 2, 1, 1)

        buttonFour = QPushButton()
        numberButtons.append(buttonFour)
        gridLayout.addWidget(buttonFour, 3, 0, 1, 1)

        buttonFive = QPushButton()
        numberButtons.append(buttonFive)
        gridLayout.addWidget(buttonFive, 3, 1, 1, 1)

        buttonSix = QPushButton()
        numberButtons.append(buttonSix)
        gridLayout.addWidget(buttonSix, 3, 2, 1, 1)

        buttonSeven = QPushButton()
        numberButtons.append(buttonSeven)
        gridLayout.addWidget(buttonSeven, 4, 0, 1, 1)

        buttonEight = QPushButton()
        numberButtons.append(buttonEight)
        gridLayout.addWidget(buttonEight, 4, 1, 1, 1)

        buttonNine = QPushButton()
        numberButtons.append(buttonNine)
        gridLayout.addWidget(buttonNine, 4, 2, 1, 1)

        # Setting the text for the number buttons
        for number in range(0, 10):
            numberButtons[number].setText(str(number))
        
        buttonPlus = QPushButton()
        buttonPlus.setText("+")
        gridLayout.addWidget(buttonPlus, 2, 3, 1, 1)
        
        buttonMinus = QPushButton()
        buttonMinus.setText("-")
        gridLayout.addWidget(buttonMinus, 3, 3, 1, 1)
        
        buttonTimes = QPushButton()
        buttonTimes.setText("*")
        gridLayout.addWidget(buttonTimes, 4, 3, 1, 1)
        
        buttonDivide = QPushButton()
        buttonDivide.setText("/")
        gridLayout.addWidget(buttonDivide, 5, 3, 1, 1)
        
        buttonDecimal = QPushButton()
        buttonDecimal.setText(".")
        gridLayout.addWidget(buttonDecimal, 5, 0, 1, 1)
        
        buttonModulus = QPushButton()
        buttonModulus.setText("%")
        gridLayout.addWidget(buttonModulus, 1, 2, 1, 1)

        buttonDel = QPushButton()
        buttonDel.setText("Delete")
        gridLayout.addWidget(buttonDel, 1, 3, 1, 1)
        
        buttonEqual = QPushButton()
        buttonEqual.setText("=")
        gridLayout.addWidget(buttonEqual, 5, 2, 1, 1)

        buttonOne.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "1")))
        buttonTwo.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "2")))
        buttonThree.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "3")))
        buttonFour.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "4")))
        buttonFive.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "5")))
        buttonSix.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "6")))
        buttonSeven.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "7")))
        buttonEight.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "8")))
        buttonNine.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "9")))

        buttonPlus.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "+")))
        buttonMinus.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "-")))
        buttonTimes.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "*")))
        buttonDivide.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "/")))
        buttonDecimal.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + ".")))
        buttonModulus.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text() + "%")))

        buttonDel.pressed.connect(lambda : self.calculationBox.setText(str(self.calculationBox.text()[0:-1])))

        buttonEqual.pressed.connect(lambda : self.calculationBox.setText(str(eval(self.calculationBox.text()))))


        




app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()