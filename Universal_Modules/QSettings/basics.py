from PyQt5 import QtCore, QtWidgets


class test:
    def __init__(self):
        self.settings = QtCore.QSettings('Testing', 'Test')  # company name and the project name
        self.setValues()
        self.getValues()

    def setValues(self):
        self.settings.setValue('color', 'orange')  # key and then value
        self.settings.setValue('indent', 6)
        self.settings.setValue('started', False)

    def getValues(self):
        print(self.settings.value('color'))
        print(self.settings.value('indent'), type(self.settings.value('indent')))
        print(self.settings.value('not here',
                                  None))  # second parameter is returned when a key is not there in the settings
        print(self.settings.value('started'),
              type(self.settings.value('started')))  # ! always use the type attribute of the value
        print(self.settings.value('started', type=bool), type(self.settings.value('started', type=bool)))
        print(self.settings.contains('not there'), self.settings.contains('color'))
        print(self.settings.allKeys())
        self.settings.sync()  # manually saves the settings
        # self.settings.clear() todo: clears all the keys


test()
