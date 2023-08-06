#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMenuBar, QAction, QWidget, QVBoxLayout, QFileDialog, QDialog, QLabel
from PySide2.QtCore import qtTrId
from mkedit.core.EditCenter import EditCenter
from mkedit.core.Dialog import Dialog as MKDialog
import os
from scheduler.PySild2QtScheduler import qtScheduler

if getattr(sys, 'frozen', False) and sys.platform == 'darwin':
    os.environ['QTWEBENGINEPROCESS_PATH'] = os.path.normpath(os.path.join(
        sys._MEIPASS, 'PySide2', 'Qt', 'lib',
        'QtWebEngineCore.framework', 'Helpers', 'QtWebEngineProcess.app',
        'Contents', 'MacOS', 'QtWebEngineProcess'
    ))


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.init()
        self.initSize()
        self.initUI()
        self.initData()
        self.updateMenuBar()

    def init(self):
        self.editCenter = EditCenter(self)
        self.editCenter.extendTabWidget = self.extendTabWidget
        self.editCenter.startInit()

    def extendTabWidget(self) -> list:
        nodes = list()
        nodes.append(('xxx',QLabel('xxxx')))
        nodes.append(('aaa',QLabel('aaa')))

        return nodes

    def initSize(self):
        desktop = QApplication.desktop()
        self.screenWidth = desktop.width() * 0.8
        self.screenHeight = desktop.height() * 1
        print("screen width is %d height is %d" % (self.screenWidth, self.screenHeight))
        self.resize(self.screenWidth, self.screenHeight)

    def initUI(self):
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout()
        self.mainWidget.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.editCenter)
        self.setCentralWidget(self.mainWidget)

    def updateMenuBar(self):
        menuBar = QMenuBar()
        winmenu = menuBar.addMenu(qtTrId("File"))
        selectProjectDirAction = QAction(qtTrId("选择工作目录"), self)
        selectProjectDirAction.triggered.connect(self.openFileDir)
        winmenu.addAction(selectProjectDirAction)

        createDirAction = QAction(qtTrId("创建目录"), self)
        createDirAction.triggered.connect(self.createDir)
        winmenu.addAction(createDirAction)

        createFileAction = QAction(qtTrId("创建文件"), self)
        createFileAction.triggered.connect(self.createFile)
        winmenu.addAction(createFileAction)
        self.setMenuBar(menuBar)

    def initData(self):
        self.editCenter.getMenusBar.setSupportFileSuffix(["txt", "md"], "md")
        self.editCenter.getMenusBar.updateWorkDir("")

    def openFileDir(self):
        print("openFileDir")
        fileDialog = QFileDialog(self)
        fileDialog.setFileMode(QFileDialog.Directory)
        ret = fileDialog.exec_()
        if ret == QDialog.Accepted:
            fileName = fileDialog.selectedFiles()
            self.editCenter.getMenusBar.updateWorkDir(fileName[0])

    def createDir(self):
        print("createDir")
        text = MKDialog().inputDirNameDialog()
        if text:
            print(text)
            self.editCenter.getMenusBar.createDir(text)

    def createFile(self):
        print("createFile")
        text = MKDialog().inputFileNameDialog()
        if text:
            print(text)
            self.editCenter.getMenusBar.createFile(text, self.editCenter.getMenusBar.getDefaultValue)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qtScheduler.initSignal()
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
