from PyQt5 import QtWidgets


class test(QtWidgets.QApplication):
    def __init__(self):
        super().__init__([])
        self.window = QtWidgets.QWidget(windowTitle='SetMax ans SetMin')
        self.layout = QtWidgets.QVBoxLayout()
        self.window.setLayout(self.layout)
        self.label = QtWidgets.QLabel(self.window, toolTip='without any restrictions', text='Without any restrictions')
        self.entry1 = QtWidgets.QLineEdit(self.window, toolTip='Entry', clearButtonEnabled=True)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.entry1)
        self.label2 = QtWidgets.QLabel(self.window, toolTip='With Restrictions', text='With some size restrictions')
        self.entry2 = QtWidgets.QLineEdit(self.window, toolTip='Entry', clearButtonEnabled=True)
        self.entry2.setMaximumWidth(500)
        self.entry2.setMinimumWidth(200)
        print(self.entry2.width(), self.entry2.height(), self.entry1.maximumHeight(),
              self.entry2.maximumSize())  # to get attributes   (in pixels)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.entry2)
        self.window.show()


test().exec()
