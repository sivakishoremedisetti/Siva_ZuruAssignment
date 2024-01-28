import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import maya.cmds as cmds

class getSelectedList(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Maya Tools'
        self.initUI()
  
    def initUI(self):
        self.setWindowTitle(self.title)
        button = QPushButton('Get Asset Names', self)
        button.setToolTip('Get selected asset names')
        button.move(100,70)
        button.clicked.connect(self.get_asset_names)
        self.show()

    def get_asset_names(self):
        #pass
        selList = cmds.ls(sl = True)
        if len(selList) == 0:
            print("Please select the object.")
        for item in selList:
            print(item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = getSelectedList()
    sys.exit(app.exec_())