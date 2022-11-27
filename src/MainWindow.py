from PyQt5 import QtCore, QtGui, QtWidgets
from ListWindow import Ui_listWindow  #call the ListWindow from other file to summon it with openWindow function 
from datetime import datetime
from pathlib import Path
import winsound

class Ui_mainWindow(object):

    l = Ui_listWindow()         #placeholder for self parameter
    fileName = Ui_listWindow.fileName       #borrow the variable from ListWindow
    filePath = Ui_listWindow.filePath
    
    def isFileExists(self):         #If the file didn't exist, create new file
        if (Ui_listWindow.findFile(self.l, self.fileName, self.filePath) == None): #borrow the function from ListWindow
            file = open(self.fileName, "x")
        else:
            return

    believes = ["Atheist", "Buddhism", "Christianity", "Hinduism", "Islam", "Jainism", "Judaism", "Neo-Paganism", "Shinto", "Sikhism", "Other"]
    possibleYear = []

    for i in range(datetime.today().year, 1900, -1): #find all possible birthYear to add in combobox
        possibleYear.append(str(i))

    def loadUp(self):       #Clear out the empty line in file and rewrite the file
        fileRead = open(Ui_listWindow.findFile(self.l, self.fileName, self.filePath), "r")
        data = fileRead.read()
        fileRead.close()
        if (data == ""):
            return
        people = data.splitlines()
        actualPeople = self.deFrag(people, "")
        fileWrite = open(Ui_listWindow.findFile(self.l, self.fileName, self.filePath), "w")
        for i in actualPeople:
            person = i.split()
            for info in person:
                fileWrite.write(info)
                if not info == person[len(person) -1]:
                    fileWrite.write(" ")
            fileWrite.write("\n")
        fileWrite.close()

    def deFrag(self, lists, val):     #Filter out certain value in all of the set
        return [value for value in lists if value != val]

    def getID(self):                  #read file to continue from the latest ID
        people = Ui_listWindow.readFile(self.l)
        if len(people) == 0:
            return 0
        for i in people:
            person = i.split()
        return int(person[0])

    def getData(self):      #retrive data from input boxes
        id = "{0:04d}".format(self.getID() + 1) #count list of people and add 1 to assign current person ID and format it to 4digits number
        name = self.firstName.text()
        lastName = self.lastName.text()
        birthYear = self.birthYear.currentText()
        believes = self.believesBox.currentText()
        if (self.maleButton.isChecked()):
            sex = "Male"
        elif (self.femaleButton.isChecked()):
            sex = "Female"
        tel = self.tel.text()
        if (self.checkData(name, lastName, birthYear, tel)):
            age = datetime.today().year - (int(birthYear))
            person = str(id + " " + name.capitalize() + " " + lastName.capitalize() + " " + str(age) + " " + sex + " " + believes + " " + tel)
            self.register(person)

    def checkData(self, name, lastName, birthYear, tel):
        if (len(name) == 0 or len(lastName) == 0 or len(birthYear) == 0 or len(tel) == 0):  #force user to only fill in all the boxes
            self.resultText.setText("You must fill in all the information!")
            return False
        if (not name.isalpha() or not lastName.isalpha()):      #force user to only fill in letters
            self.resultText.setText("The name must contain only letters!")
            return False
        if (not tel.isnumeric()):   #force user to only fill in number
            self.resultText.setText("Telephone number must contain only numbers!")
            return False
        if (not len(tel) == 10):    #force user to only fill exactly 10 digits of telephone number
            self.resultText.setText("Telephone number must have exactly 10 digits!")
            return False
        return True

    def clearBoxes(self):    #clear input boxes 
        self.firstName.clear()
        self.lastName.clear()
        self.tel.clear()

    def register(self, person):     #write data on file
        file = open(Ui_listWindow.findFile(self.l, self.fileName, self.filePath),"a")
        for i in person:
            file.write(str(i))
        file.write("\n")
        file.close()
        self.resultText.setText("Data saved successfully.")  
        self.clearBoxes()

    def openWindow(self): #function to open list window
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_listWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(488, 286)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("appIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(488, 286))
        mainWindow.setMaximumSize(QtCore.QSize(488, 286))
        mainWindow.setBaseSize(QtCore.QSize(488, 286))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.firstName = QtWidgets.QLineEdit(self.centralwidget)
        self.firstName.setGeometry(QtCore.QRect(98, 30, 133, 20))
        self.firstName.setObjectName("firstName")
        self.believesBox = QtWidgets.QComboBox(self.centralwidget)
        self.believesBox.setGeometry(QtCore.QRect(98, 129, 100, 20))
        self.believesBox.setObjectName("believesBox")
        self.believesBox.addItems(self.believes)   #add Religions list to the combobox
        self.believesBox.setCurrentIndex(1) # set Buddism as a default choice
        self.maleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.maleButton.setGeometry(QtCore.QRect(99, 179, 45, 17))
        self.maleButton.setObjectName("maleButton")
        self.maleButton.setChecked(True) #check Male Radiobox as default
        self.femaleButton = QtWidgets.QRadioButton(self.centralwidget)
        self.femaleButton.setGeometry(QtCore.QRect(150, 179, 57, 17))
        self.femaleButton.setObjectName("femaleButton")
        self.tel = QtWidgets.QLineEdit(self.centralwidget)
        self.tel.setGeometry(QtCore.QRect(285, 79, 133, 20))
        self.tel.setObjectName("tel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(42, 30, 50, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(255, 30, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(31, 79, 64, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(190, 79, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(51, 129, 39, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(71, 179, 22, 16))
        self.label_6.setObjectName("label_6")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(60, 230, 75, 23))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(lambda: [self.getData(), winsound.MessageBeep(winsound.MB_OK)]) #call the function to collect data in boxes and make beep sound
        self.lastName = QtWidgets.QLineEdit(self.centralwidget)
        self.lastName.setGeometry(QtCore.QRect(310, 30, 133, 20))
        self.lastName.setObjectName("lastName")
        self.resultText = QtWidgets.QLabel(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(150, 230, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.resultText.setFont(font)
        self.resultText.setText("")
        self.resultText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.resultText.setObjectName("resultText")
        self.viewButton = QtWidgets.QToolButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(440, 230, 25, 25))
        self.viewButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("viewButtonIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.viewButton.setIcon(icon)
        self.viewButton.setObjectName("viewButton")
        self.viewButton.clicked.connect(lambda: self.openWindow()) #call the function to open window when clicked
        self.birthYear = QtWidgets.QComboBox(self.centralwidget)
        self.birthYear.setGeometry(QtCore.QRect(98, 79, 71, 20))
        self.birthYear.setObjectName("birthYear")
        self.birthYear.addItems(self.possibleYear)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionView_Lists = QtWidgets.QAction(mainWindow)
        self.actionView_Lists.setObjectName("actionView_Lists")
        self.label.setBuddy(self.firstName)
        self.label_2.setBuddy(self.lastName)
        self.label_3.setBuddy(self.birthYear)
        self.label_4.setBuddy(self.tel)
        self.label_5.setBuddy(self.believesBox)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.firstName, self.lastName)
        mainWindow.setTabOrder(self.lastName, self.birthYear)
        mainWindow.setTabOrder(self.birthYear, self.tel)
        mainWindow.setTabOrder(self.tel, self.believesBox)
        mainWindow.setTabOrder(self.believesBox, self.maleButton)
        mainWindow.setTabOrder(self.maleButton, self.femaleButton)
        mainWindow.setTabOrder(self.femaleButton, self.saveButton)
        mainWindow.setTabOrder(self.saveButton, self.viewButton)

        self.isFileExists()
        self.loadUp()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Registration Form"))
        self.maleButton.setText(_translate("mainWindow", "Male"))
        self.femaleButton.setText(_translate("mainWindow", "Female"))
        self.label.setText(_translate("mainWindow", "First name"))
        self.label_2.setText(_translate("mainWindow", "Last name"))
        self.label_3.setText(_translate("mainWindow", "Year of birth"))
        self.label_4.setText(_translate("mainWindow", "Telephone Number"))
        self.label_5.setText(_translate("mainWindow", "Believes"))
        self.label_6.setText(_translate("mainWindow", "Sex:"))
        self.saveButton.setText(_translate("mainWindow", "Save"))
        self.actionView_Lists.setText(_translate("mainWindow", "View Lists"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
