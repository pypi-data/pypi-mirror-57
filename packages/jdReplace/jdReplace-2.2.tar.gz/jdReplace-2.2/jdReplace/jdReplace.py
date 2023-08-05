#!/usr/bin/env python3
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QLabel, QPlainTextEdit, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QCheckBox, QProgressBar, QFileDialog
from PyQt5.QtCore import QDir, QLocale, Qt, QThread, pyqtSignal
from jdTranslationHelper import jdTranslationHelper
from PyQt5.QtGui import QFont, QIcon
import webbrowser
import sys
import os

version = "2.2"

texts = jdTranslationHelper(lang=QLocale.system().name())
currentDir = os.path.dirname(os.path.realpath(__file__))
texts.loadDirectory(os.path.join(currentDir,"translation"))

def showMessageBox(title,text):
    messageBox = QMessageBox()
    messageBox.setWindowTitle(title)
    messageBox.setText(text)
    messageBox.setStandardButtons(QMessageBox.Ok)
    messageBox.exec_()

class AboutWindow(QWidget):
    def setup(self):
        self.titleLabel = QLabel("jdReplace Version " + version)
        self.descriptionLabel = QLabel(texts.translate("about.description"))
        self.copyrightLabel = QLabel("Copyright © 2019 JakobDev")
        self.licenseLabel = QLabel(texts.translate("about.license"))
        self.viewSourceButton = QPushButton(texts.translate("about.viewSource"))
        self.closeButton = QPushButton(texts.translate("about.close"))
        
        self.closeButton.setIcon(QIcon.fromTheme("window-close"))

        self.titleLabelFont = QFont()
        self.titleLabelFont.setBold(True)
        self.titleLabelFont.setPointSize(16)

        self.legalFont = QFont()
        self.legalFont.setPointSize(8)

        self.titleLabel.setFont(self.titleLabelFont)
        self.copyrightLabel.setFont(self.legalFont)
        self.licenseLabel.setFont(self.legalFont)

        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)
        self.copyrightLabel.setAlignment(Qt.AlignCenter)
        self.licenseLabel.setAlignment(Qt.AlignCenter)

        self.viewSourceButton.clicked.connect(self.viewSourceAction)
        self.closeButton.clicked.connect(self.closeAction)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.viewSourceButton)
        self.buttonLayout.addWidget(self.closeButton)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.descriptionLabel)
        self.mainLayout.addWidget(self.copyrightLabel)
        self.mainLayout.addWidget(self.licenseLabel)
        self.mainLayout.addLayout(self.buttonLayout)
        
        self.setLayout(self.mainLayout)
        self.setWindowTitle(texts.translate("about.title"))
        
    def viewSourceAction(self):
        webbrowser.open("https://gitlab.com/JakobDev/jdReplace")

    def closeAction(self):
        self.close()

class ReplaceThread(QThread):
    count = pyqtSignal("int")
    progress = pyqtSignal("int")
    text = pyqtSignal("QString")
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def setup(self,recursive,path,searchText,replaceText,skipHidden,followSymlinks):
        self.recursive = recursive
        self.path = path
        self.searchText = searchText
        self.replaceText = replaceText
        self.skipHidden = skipHidden
        self.followSymlinks = followSymlinks

    def listFiles(self,path): 
        self.text.emit(texts.translate("progressbar.searching") % path)
        try:  
            for f in os.listdir(path):
                if f.startswith(".") and self.skipHidden:
                    continue
                filename = os.path.join(path,f)
                if os.path.islink(filename) and not self.followSymlinks:
                    continue
                if os.path.isdir(filename):
                    if self.recursive:
                        self.listFiles(filename)
                else:
                    self.filelist.append(filename)
        except:
            print("Could not read " + path)

    def run(self):
        self.filelist = []
        self.listFiles(self.path)
        self.count.emit(len(self.filelist))
        progressCount = 0
        for filename in self.filelist:
            try:
                with open(filename, 'r') as file :
                    filedata = file.read()
                if filedata.find(self.searchText) != -1:
                    filedata = filedata.replace(self.searchText,self.replaceText)
                    with open(filename, 'w') as file:
                        file.write(filedata)
            except:
                print(texts.translate("replace.error").replace("{}",filename))
            progressCount += 1
            self.progress.emit(progressCount)

class StartWindow(QWidget):
    def setup(self):
        self.about = AboutWindow()
        self.about.setup()
        self.thread = ReplaceThread()

        self.directoryLabel = QLabel(texts.translate("label.directory"))
        self.directoryEdit = QLineEdit()
        self.directoryButton = QPushButton(texts.translate("button.browse"))
        self.inputTextLabel = QLabel(texts.translate("label.searchFor"))
        self.inputTextEdit = QPlainTextEdit()
        self.outputTextLabel = QLabel(texts.translate("label.replaceWith"))
        self.outputTextEdit = QPlainTextEdit()
        self.subdirCheckBox = QCheckBox(texts.translate("checkbox.searchSubdirectories"))
        self.hiddenCheckBox = QCheckBox(texts.translate("checkbox.skipHidden"))
        self.symlinkCheckBox = QCheckBox(texts.translate("checkbox.followSymlinks"))
        self.progressBar = QProgressBar()
        self.aboutButton = QPushButton(texts.translate("button.about"))
        self.okButton = QPushButton(texts.translate("button.ok"))

        self.directoryButton.setIcon(QIcon.fromTheme("folder"))
        self.aboutButton.setIcon(QIcon.fromTheme("help-about"))

        self.directoryEdit.setText(QDir.currentPath())
        self.inputTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.outputTextEdit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.directoryButton.clicked.connect(self.browse)
        self.aboutButton.clicked.connect(self.showAbout)
        self.okButton.clicked.connect(self.replaceFiles)
        self.thread.count.connect(self.setMax)
        self.thread.progress.connect(self.setProgress)
        self.thread.text.connect(self.setBarText)
        self.thread.finished.connect(self.threadFinish)
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setFormat("0")

        self.directoryLayout = QHBoxLayout()
        self.directoryLayout.addWidget(self.directoryLabel)
        self.directoryLayout.addWidget(self.directoryEdit)
        self.directoryLayout.addWidget(self.directoryButton)
        
        self.checkBoxLayout = QHBoxLayout()
        self.checkBoxLayout.addWidget(self.subdirCheckBox)
        self.checkBoxLayout.addWidget(self.hiddenCheckBox)
        self.checkBoxLayout.addWidget(self.symlinkCheckBox)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.aboutButton)
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.okButton)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.directoryLayout)
        self.mainLayout.addWidget(self.inputTextLabel)
        self.mainLayout.addWidget(self.inputTextEdit)
        self.mainLayout.addWidget(self.outputTextLabel)
        self.mainLayout.addWidget(self.outputTextEdit)
        self.mainLayout.addLayout(self.checkBoxLayout)
        self.mainLayout.addWidget(self.progressBar)
        self.mainLayout.addLayout(self.buttonLayout)
        
        self.setLayout(self.mainLayout)
        self.resize(650, 550)
        self.setWindowTitle("jdReplace")
        self.show()

    def browse(self):
        path = self.directoryEdit.text()
        if not os.path.isdir(path):
            path = QDir.currentPath()
        directory = QFileDialog.getExistingDirectory(self, texts.translate("filedialog.title"),path)

        if directory:
            self.directoryEdit.setText(directory)
    
    def showAbout(self):
        self.about.show()

    def setMax(self,count):
        self.progressBar.setMaximum(count)
        self.filecount = count

    def setProgress(self,count):
        self.progressBar.setValue(count)
        self.progressBar.setFormat(str(count) + "/" + str(self.filecount))

    def setBarText(self,text):
        self.progressBar.setFormat(text)

    def threadFinish(self):
        self.okButton.setEnabled(True)
        showMessageBox(texts.translate("messagebox.finished.title"),texts.translate("messagebox.finished.text"))
        
    def replaceFiles(self):
        path = self.directoryEdit.text()
        if not os.path.isdir(path):
            showMessageBox(texts.translate("messagebox.nodirectory.title"),texts.translate("messagebox.nodirectory.text") % path)
            return
        searchText = self.inputTextEdit.toPlainText()
        if searchText == "":
            showMessageBox(texts.translate("messagebox.nosearchtext.title"),texts.translate("messagebox.nosearchtext.text"))
            return
        replaceText = self.outputTextEdit.toPlainText()
        self.okButton.setEnabled(False)
        self.progressBar.setValue(0)
        self.thread.setup(bool(self.subdirCheckBox.checkState()),path,searchText,replaceText,bool(self.hiddenCheckBox.checkState()),bool(self.symlinkCheckBox.checkState()))
        self.thread.start()

def main():
    app = QApplication(sys.argv)
    w = StartWindow()
    w.setup()
    sys.exit(app.exec_())

