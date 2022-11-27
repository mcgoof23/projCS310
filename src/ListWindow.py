from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
from pathlib import Path
import os

class Ui_listWindow(object):

    fileName = "peopleLists.txt"
    filePath = Path(__file__).parent.absolute()  #Find the directory of current file source=StackOverflow

    def findFile(self, name, path):
        for root, dirs, files in os.walk(path):  #Scan for file in given path return NoneType if not found source=StackOverflow
            if name in files:
                return os.path.join(root, name)

    def readFile(self):
        file = open(self.findFile(self.fileName, self.filePath),"r")
        data = file.read()
        people = data.splitlines()
        file.close()
        return people

    def processData(self, data):
        people = []
        for i in data:
            person = i.split()
            people.append(person)
        return people

    def sortAscension(self):
        if (self.actionAscending.isChecked() == True):
            return False
        elif (self.actionDescending.isChecked() == True):
            return True
        
    def sortType(self, person):
        if (self.actionBy_ID.isChecked() == True):
            return person[0]
        elif (self.actionBy_First_Name.isChecked() == True):
            return person[1]
        elif (self.actionBy_Last_name.isChecked() == True):
            return person[2]
        elif (self.actionBy_Age.isChecked() == True):
            return int(person[3])
        elif (self.actionBy_Sex.isChecked() == True):
            return person[4]
        elif (self.actionBy_Believe.isChecked() == True):
            return person[5]

    def loadData(self):
        people = self.processData(self.readFile())
        people.sort(reverse=self.sortAscension(), key=self.sortType)        #manually create sort function because given method can't sort age as int
        self.listTable.setRowCount(len(people))
        for row in range(len(people)):
            for column in range(len(people[row])):
                self.listTable.setItem(row, column, QtWidgets.QTableWidgetItem(people[row][column]))
                if (column in [0, 3, 4]):
                    self.listTable.item(row, column).setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        
    def setupUi(self, listWindow):
        listWindow.setObjectName("listWindow")
        listWindow.resize(950, 560)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("appIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        listWindow.setWindowIcon(icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(listWindow.sizePolicy().hasHeightForWidth())
        listWindow.setSizePolicy(sizePolicy)
        listWindow.setMinimumSize(QtCore.QSize(950, 560))
        listWindow.setMaximumSize(QtCore.QSize(950, 560))
        listWindow.setBaseSize(QtCore.QSize(950, 560))
        self.centralwidget = QtWidgets.QWidget(listWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listTable = QtWidgets.QTableWidget(self.centralwidget)
        self.listTable.setGeometry(QtCore.QRect(50, 40, 850, 450))
        self.listTable.setObjectName("listTable")
        self.listTable.setColumnCount(7)
        self.listTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.listTable.setHorizontalHeaderItem(6, item)
        self.listTable.setColumnWidth(0, 60)
        self.listTable.setColumnWidth(1, 192)
        self.listTable.setColumnWidth(2, 192)
        self.listTable.setColumnWidth(3, 50)
        self.listTable.setColumnWidth(4, 70)
        self.listTable.setColumnWidth(5, 110)
        self.listTable.setColumnWidth(6, 157)
        
        self.listTable.horizontalHeader().setSectionsClickable(False)
        self.listTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.listTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.listTable.verticalHeader().setVisible(False)
        
        
        listWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(listWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSort = QtWidgets.QMenu(self.menuFile)
        self.menuSort.setObjectName("menuSort")
        listWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(listWindow)
        self.statusbar.setObjectName("statusbar")
        listWindow.setStatusBar(self.statusbar)
        self.actionBy_ID = QtWidgets.QAction(listWindow)
        self.actionBy_ID.setCheckable(True)
        self.actionBy_ID.setChecked(True)
        self.actionBy_ID.setObjectName("actionBy_ID")
        self.actionBy_First_Name = QtWidgets.QAction(listWindow)
        self.actionBy_First_Name.setCheckable(True)
        self.actionBy_First_Name.setObjectName("actionBy_First_Name")
        self.actionBy_Last_name = QtWidgets.QAction(listWindow)
        self.actionBy_Last_name.setCheckable(True)
        self.actionBy_Last_name.setObjectName("actionBy_Last_name")
        self.actionBy_Age = QtWidgets.QAction(listWindow)
        self.actionBy_Age.setCheckable(True)
        self.actionBy_Age.setObjectName("actionBy_Age")
        self.actionBy_Sex = QtWidgets.QAction(listWindow)
        self.actionBy_Sex.setCheckable(True)
        self.actionBy_Sex.setObjectName("actionBy_Sex")
        self.actionBy_Believe = QtWidgets.QAction(listWindow)
        self.actionBy_Believe.setCheckable(True)
        self.actionBy_Believe.setObjectName("actionBy_Believe")
        self.actionAscending = QtWidgets.QAction(listWindow)
        self.actionAscending.setCheckable(True)
        self.actionAscending.setChecked(True)
        self.actionAscending.setObjectName("actionAscending")
        self.actionDescending = QtWidgets.QAction(listWindow)
        self.actionDescending.setCheckable(True)
        self.actionDescending.setObjectName("actionDescending")

        groupType = QtWidgets.QActionGroup(listWindow)  #grouped the sort type for sort
        groupType.addAction(self.actionBy_ID)
        groupType.addAction(self.actionBy_First_Name)
        groupType.addAction(self.actionBy_Last_name)
        groupType.addAction(self.actionBy_Age)
        groupType.addAction(self.actionBy_Sex)
        groupType.addAction(self.actionBy_Believe)
        groupType.triggered.connect(lambda: self.loadData())
        
        groupAscension = QtWidgets.QActionGroup(listWindow) #grouped the Ascesion option for sort
        groupAscension.addAction(self.actionAscending)
        groupAscension.addAction(self.actionDescending)
        groupAscension.triggered.connect(lambda: self.loadData())

        self.menuSort.addAction(self.actionBy_ID)
        self.menuSort.addAction(self.actionBy_First_Name)
        self.menuSort.addAction(self.actionBy_Last_name)
        self.menuSort.addAction(self.actionBy_Age)
        self.menuSort.addAction(self.actionBy_Sex)
        self.menuSort.addAction(self.actionBy_Believe)
        self.menuSort.addSeparator()
        self.menuSort.addAction(self.actionAscending)
        self.menuSort.addAction(self.actionDescending)
        self.menuFile.addAction(self.menuSort.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(listWindow)
        QtCore.QMetaObject.connectSlotsByName(listWindow)

        self.loadData()

    def retranslateUi(self, listWindow):
        _translate = QtCore.QCoreApplication.translate
        listWindow.setWindowTitle(_translate("listWindow", "Lists"))
        item = self.listTable.horizontalHeaderItem(0)
        item.setText(_translate("listWindow", "ID"))
        item = self.listTable.horizontalHeaderItem(1)
        item.setText(_translate("listWindow", "First Name"))
        item = self.listTable.horizontalHeaderItem(2)
        item.setText(_translate("listWindow", "Last Name"))
        item = self.listTable.horizontalHeaderItem(3)
        item.setText(_translate("listWindow", "Age"))
        item = self.listTable.horizontalHeaderItem(4)
        item.setText(_translate("listWindow", "Sex"))
        item = self.listTable.horizontalHeaderItem(5)
        item.setText(_translate("listWindow", "Believes"))
        item = self.listTable.horizontalHeaderItem(6)
        item.setText(_translate("listWindow", "Contact Number"))
        self.menuFile.setTitle(_translate("listWindow", "File"))
        self.menuSort.setTitle(_translate("listWindow", "Sort"))
        self.actionBy_ID.setText(_translate("listWindow", "By  ID"))
        self.actionBy_First_Name.setText(_translate("listWindow", "By First name"))
        self.actionBy_Last_name.setText(_translate("listWindow", "By Last name"))
        self.actionBy_Age.setText(_translate("listWindow", "By Age"))
        self.actionBy_Sex.setText(_translate("listWindow", "By Sex"))
        self.actionBy_Believe.setText(_translate("listWindow", "By Believe"))
        self.actionAscending.setText(_translate("listWindow", "Ascending"))
        self.actionDescending.setText(_translate("listWindow", "Descending"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listWindow = QtWidgets.QMainWindow()
    ui = Ui_listWindow()
    ui.setupUi(listWindow)
    listWindow.show()
    sys.exit(app.exec_())
