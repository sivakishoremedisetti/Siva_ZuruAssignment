import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import maya.cmds as cmds

class question_two(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Maya Tools'
        self.initUI()
  
    def initUI(self):
        self.setWindowTitle(self.title)
        moveX = QPushButton('Move X by 2', self)
        moveX.setToolTip('Move Selected object in X by 2')
        moveX.move(100,30)
        moveX.clicked.connect(self.moveXbyTwo)

        moveY = QPushButton('Move Y by 2', self)
        moveY.setToolTip('Move Selected object in Y by 2')
        moveY.move(100,60)
        moveY.clicked.connect(self.moveYbyTwo)

        moveFace = QPushButton('Faces outwards by 4', self)
        moveFace.setToolTip('Move one of the faces of the object outwards by 4')
        moveFace.move(100,90)
        moveFace.clicked.connect(self.moveFacebyFour)

        self.show()

    def moveXbyTwo(self):
        selList = cmds.ls(sl = True)
        if len(selList) == 0:
            print("Please select the object.")
        for item in selList:
            getX = cmds.getAttr(item+".translateX")
            cmds.setAttr(item+".translateX",getX+2)

    def moveYbyTwo(self):
        selList = cmds.ls(sl = True)
        if len(selList) == 0:
            print("Please select the object.")
        for item in selList:
            getX = cmds.getAttr(item+".translateY")
            cmds.setAttr(item+".translateY",getX+2)

    def moveFacebyFour(self): 
        selList = cmds.ls(sl = True)
        if len(selList) == 0:
            print("Please select the object.")
        face1 = selList[0]+'.f[1]'
        cmds.select(face1)
        cmds.move(2, 2, 0, relative=True, objectSpace=True) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = question_two()
    sys.exit(app.exec_())