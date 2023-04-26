from PyQt5.QtWidgets import *
beta = QApplication([])
from time import sleep
def function1():
    pass
def function2():
    pass
def end():
    huh.hide()
def question_box(assets, functions = [function1, function2]):
    global huh
    a = 0
    huh = QDialog()
    huh.setFixedHeight(200)
    huh.setFixedWidth(400)
    huh.setWindowTitle(assets[0])
    buttons = []
    for thing in assets:
        if a <= 0:
            a +=1
            pass
        else:
            buttons.append(QPushButton(thing))
            
    count = 0
    hline = QHBoxLayout()
    for button in buttons:
        hline.addWidget(button)
    for func in functions:
        if count == len(buttons):
            break
        else:
            buttons[count].clicked.connect(func)
            count +=1


    huh.setLayout(hline)
    huh.move(1850, 1400)
    huh.show()





    sleep(10)
fr = QWidget()
fr.show()
beta.exec_()