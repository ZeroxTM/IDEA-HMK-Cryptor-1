# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecureTransmission7.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time

from server.socket import Socket

custom_key = None
file_path = None
soc = None

def send_text(text, soc):
    while text != '':
        soc.sender.send(text[:8])
        text = text[8:]

class Ui_DataView(object):
    def setupUi(self, DataView):
        DataView.setObjectName("DataView")
        DataView.resize(671, 499)
        self.centralwidget = QtWidgets.QWidget(DataView)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 211, 431))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 71, 31))
        self.label.setObjectName("label")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(230, 40, 211, 431))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 71, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(450, 40, 211, 431))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setReadOnly(True)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 10, 71, 31))
        self.label_3.setObjectName("label_3")
        DataView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DataView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 22))
        self.menubar.setObjectName("menubar")
        DataView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DataView)
        self.statusbar.setObjectName("statusbar")
        DataView.setStatusBar(self.statusbar)

        self.retranslateUi(DataView)
        QtCore.QMetaObject.connectSlotsByName(DataView)
        DataView.setFixedSize(DataView.size())
        DataView.setWindowModality(QtCore.Qt.ApplicationModal)
        #***************************************************
        # displaying the Sender File  contents on gui
        if file_path == None:
            file = QtCore.QFile("files/receiver_decrypted.txt")
        else:
            file = QtCore.QFile(file_path)
        if not file.open(QtCore.QIODevice.ReadOnly):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(file.errorString())
            x = msg.exec_()
        stream = QtCore.QTextStream(file)
        self.textEdit.setText(stream.readAll())
        file.close()
        #***************************************************
        # displaying the Server  File  contents on gui
        # change the path to the actual path of the server(socket)
        file1 = QtCore.QFile("files/socket_data.txt")
        if not file1.open(QtCore.QIODevice.ReadOnly):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(file1.errorString())
            x = msg.exec_()
        stream = QtCore.QTextStream(file1)
        self.textEdit_2.setText(stream.readAll())
        file1.close()
        #***************************************************
        # displaying the receiver File  contents on gui
        # change the path to the actual path of the server(socket)
        file2 = QtCore.QFile("files/receiver_decrypted.txt")
        if not file2.open(QtCore.QIODevice.ReadOnly):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(file2.errorString())
            x = msg.exec_()
        stream = QtCore.QTextStream(file2)
        self.textEdit_3.setText(stream.readAll())
        file2.close()
        #***************************************************

    def retranslateUi(self, DataView):
        _translate = QtCore.QCoreApplication.translate
        DataView.setWindowTitle(_translate("DataView", "Encryption"))
        self.label.setText(_translate("DataView", "Sender"))
        self.label_2.setText(_translate("DataView", "Server"))
        self.label_3.setText(_translate("DataView", "Receiver"))


class Ui_Cryptology(object):
    def __init__(self):
        self.soc = None

    def setupUi(self, Cryptology):
        Cryptology.setObjectName("Cryptology")
        Cryptology.resize(738, 494)
        self.centralwidget = QtWidgets.QWidget(Cryptology)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 421, 441))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 151, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(460, 30, 231, 81))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(20, 20, 171, 18))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 50, 191, 18))
        self.radioButton_2.setObjectName("radioButton_2")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(518, 200, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setVisible(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(518, 160, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(458, 230, 231, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 20, 171, 18))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 50, 191, 18))
        self.radioButton_4.setObjectName("radioButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(450, 340, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(528, 380, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(648, 340, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(598, 440, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(478, 440, 91, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(448, 320, 181, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(478, 130, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(480, 110, 101, 16))
        self.label_3.setObjectName("label_3")
        Cryptology.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Cryptology)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 738, 22))
        self.menubar.setObjectName("menubar")
        Cryptology.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Cryptology)
        self.statusbar.setObjectName("statusbar")
        Cryptology.setStatusBar(self.statusbar)

        self.retranslateUi(Cryptology)
        QtCore.QMetaObject.connectSlotsByName(Cryptology)

        Cryptology.setFixedSize(Cryptology.size())
        self.radioButton_2.setChecked(True)
        self.radioButton_3.setChecked(True)
        self.pushButton.clicked.connect(self.progress)
        self.pushButton_3.clicked.connect(self.browse_a_file)
        # Disable EVERYTHING!
        self.groupBox_2.setVisible(False)
        self.label_2.setVisible(False)
        self.lineEdit.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_5.setVisible(False)
        # self.orig_stdout = sys.stdout
        # Encrypt Button Event
        self.pushButton_2.clicked.connect(self.start_encryption)
        # Reset Button Event
        self.pushButton_4.clicked.connect(self.reset_everything)
        # View Data
        self.pushButton_5.clicked.connect(self.data_view)

    def open_log(self):
        self.f = open('files/temp.txt', 'w')
        sys.stdout = self.f

    def close_log(self):
        self.f.close()

    def read_log(self):
        self.f = open('files/temp.txt', 'r')
        line = self.f.readline()
        while line:
            self.textEdit.append(line)
            line = self.f.readline()
        self.f.close()

    # (don't touch)
    def data_view(self):
        self.DataView = QtWidgets.QMainWindow()
        self.ui = Ui_DataView()
        self.ui.setupUi(self.DataView)
        self.DataView.show()

    # Reset Button Event (don't touch)
    def reset_everything(self):
        self.radioButton.setChecked(True)
        self.pushButton.setEnabled(True)
        self.pushButton.setText("Secure")
        self.radioButton_3.setChecked(True)
        self.groupBox_2.setVisible(False)
        self.label_2.setVisible(False)
        self.lineEdit.clear()
        self.lineEdit.setVisible(False)
        self.pushButton_3.setVisible(False)
        self.pushButton_2.setVisible(False)
        self.pushButton_4.setVisible(False)
        self.pushButton_5.setVisible(False)
        self.radioButton.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        global file_path
        file_path = None
        self.progressBar.reset()
        self.textEdit.clear()

    # Encryption Button Event
    def start_encryption(self):
        self.open_log()
        mode = 0
        # if the user chose to enter a message manually
        if self.radioButton_3.isChecked():
            send_text(self.lineEdit.text()+'\n', self.soc)###
            self.pushButton_5.setVisible(False)
            #self.soc.close_connection()
        # the user chose to encrypt a file
        else:
            # displaying file contents on gui
            file = QtCore.QFile(file_path)
            if not file.open(QtCore.QIODevice.ReadOnly):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText(file.errorString())
                x = msg.exec_()
                mode = 1

            self.soc.sender.send_file(file_path) ###
            self.soc.close_connection()
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(False)
            self.pushButton_5.setVisible(True)

        if mode == 0:
            self.pushButton_4.setVisible(True)
        self.close_log()
        self.read_log()

    # Secure button Event
    def progress(self):
        global custom_key
        self.open_log()
        # if custom key is chosen
        if self.radioButton.isChecked():
            if self.lineEdit_2.text() != "":

                custom_key = str(self.lineEdit_2.text())
                if len(custom_key) == 32:
                    try:
                        custom_key = int(custom_key, 16)
                        self.soc = Socket(custom_key)
                        self.label.setVisible(True)
                        self.progressBar.setVisible(True)
                        self.completed = 0.0
                        while self.completed < 100:
                            self.completed += 0.0001
                            self.progressBar.setValue(self.completed)
                        time.sleep(1)
                        self.progressBar.setVisible(False)
                        self.pushButton.setText("Secured!")
                        self.pushButton.setDisabled(True)
                        self.groupBox_2.setVisible(True)
                        self.label_2.setVisible(True)
                        self.lineEdit.setVisible(True)
                        self.pushButton_2.setVisible(True)
                        self.radioButton.setEnabled(False)
                        self.radioButton_2.setEnabled(False)
                        self.lineEdit_2.setEnabled(False)
                    except:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Invalid 32 digit HEX key!")
                        x = msg.exec_()
                        self.lineEdit_2.clear()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Invalid 32 digit HEX key!")
                    x = msg.exec_()
                    self.lineEdit_2.clear()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Insert 32 digit HEX Key!")
                x = msg.exec_()
                self.lineEdit_2.clear()
        # Random IDEA Key is chosen
        else:
            self.progressBar.setVisible(True)
            self.completed = 0.0
            while self.completed < 100:
                self.completed += 0.0001
                self.progressBar.setValue(self.completed)
            time.sleep(1)
            self.label.setVisible(True)
            self.progressBar.setVisible(False)
            self.pushButton.setText("Secured!")
            self.pushButton.setDisabled(True)
            self.groupBox_2.setVisible(True)
            self.label_2.setVisible(True)
            self.lineEdit.setVisible(True)
            self.pushButton_2.setVisible(True)
            self.radioButton.setEnabled(False)
            self.radioButton_2.setEnabled(False)
            ##############
            self.soc = Socket()
        self.close_log()
        self.read_log()

    def browse_a_file(self):
        global file_path
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py);;Text Files (*.txt)",
            options=options)
        if fileName:
            self.lineEdit.setText(fileName)
            file_path = fileName

    def retranslateUi(self, Cryptology):
        show_key = lambda: self.lineEdit_2.show() or self.label_3.show()
        hide_key = lambda: self.lineEdit_2.hide() or self.label_3.hide()
        browse_file_radio = lambda: self.label_2.setText(_translate("Cryptology", "Browse your file")) or (
            self.pushButton_3.show())
        enter_message_radio = lambda: self.label_2.setText(_translate("Cryptology", "Enter your message")) or (
            self.pushButton_3.hide())
        _translate = QtCore.QCoreApplication.translate
        Cryptology.setWindowTitle(_translate("Cryptology", "Cryptology"))
        self.label.setText(_translate("Cryptology", "Console :"))
        self.groupBox.setTitle(_translate("Cryptology", "Encryption Key"))
        self.radioButton.setText(_translate("Cryptology", "Custom Encryption Key"))
        self.radioButton_2.setText(_translate("Cryptology", "Random IDEA Encryption Key"))
        self.pushButton.setText(_translate("Cryptology", "Secure"))
        self.groupBox_2.setTitle(_translate("Cryptology", "Encrypt Message"))
        self.radioButton_3.setText(_translate("Cryptology", "Enter a message to cipher"))
        self.radioButton_4.setText(_translate("Cryptology", "Browse for a file to encrypt"))
        self.pushButton_2.setText(_translate("Cryptology", "Encrypt"))
        self.pushButton_3.setText(_translate("Cryptology", "Browse"))
        self.pushButton_4.setText(_translate("Cryptology", "Reset"))
        self.pushButton_5.setText(_translate("Cryptology", "View Data"))
        self.label_2.setText(_translate("Cryptology", "Enter your message"))
        self.label_3.setText(_translate("Cryptology", "Enter Key"))
        self.radioButton.toggled.connect(show_key)
        self.radioButton_2.toggled.connect(hide_key)
        self.radioButton_3.toggled.connect(enter_message_radio)
        self.radioButton_4.toggled.connect(browse_file_radio)


if __name__ == "__main__":
    import sys
    soc = 0
    app = QtWidgets.QApplication(sys.argv)
    Cryptology = QtWidgets.QMainWindow()
    ui = Ui_Cryptology()
    ui.setupUi(Cryptology)
    Cryptology.show()
    sys.exit(app.exec_())
