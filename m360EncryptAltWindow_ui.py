# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'm360EncryptAltWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 844)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 120, 651, 541))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 632, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 611, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_2.setEnabled(False)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 60, 611, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_6.setGeometry(QtCore.QRect(80, 100, 611, 521))
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 150, 471, 141))
        self.textEdit.setObjectName("textEdit")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(20, 10, 471, 81))
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(30, 100, 371, 31))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(30, 360, 471, 141))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_18 = QtWidgets.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(30, 300, 381, 41))
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(420, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 320, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(360, 540, 141, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(510, 30, 21, 21))
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap(":/images/help.png"))
        self.label_21.setScaledContents(True)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(510, 110, 21, 21))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap(":/images/help.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.label_28 = QtWidgets.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(510, 320, 21, 21))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/images/help.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_11.setGeometry(QtCore.QRect(560, 20, 171, 41))
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 681, 81))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 681, 31))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 180, 221, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_20 = QtWidgets.QLabel(self.tab)
        self.label_20.setGeometry(QtCore.QRect(380, 20, 21, 21))
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap(":/images/help.png"))
        self.label_20.setScaledContents(True)
        self.label_20.setObjectName("label_20")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 150, 671, 20))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 220, 671, 91))
        self.textEdit_2.setObjectName("textEdit_2")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(20, 319, 721, 31))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(20, 350, 681, 81))
        self.label_11.setObjectName("label_11")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 440, 671, 91))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 540, 221, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(20, 580, 671, 20))
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab)
        self.pushButton_5.setGeometry(QtCore.QRect(700, 150, 21, 21))
        self.pushButton_5.setAutoFillBackground(True)
        self.pushButton_5.setStyleSheet("")
        self.pushButton_5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/images/eye.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab)
        self.pushButton_7.setGeometry(QtCore.QRect(700, 580, 21, 21))
        self.pushButton_7.setAutoFillBackground(True)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(20, 20, 681, 81))
        self.label_19.setObjectName("label_19")
        self.textEdit_7 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_7.setGeometry(QtCore.QRect(80, 140, 641, 421))
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(140, 570, 161, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(500, 570, 161, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(70, 100, 71, 20))
        self.label_23.setObjectName("label_23")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 100, 541, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(-310, 530, 47, 13))
        self.label_24.setObjectName("label_24")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_12.setGeometry(QtCore.QRect(700, 100, 21, 21))
        self.pushButton_12.setAutoFillBackground(True)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setText("")
        self.pushButton_12.setIcon(icon)
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_33 = QtWidgets.QLabel(self.tab_8)
        self.label_33.setGeometry(QtCore.QRect(20, 10, 291, 101))
        self.label_33.setObjectName("label_33")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_9.setGeometry(QtCore.QRect(20, 120, 751, 481))
        self.textEdit_9.setObjectName("textEdit_9")
        self.label_34 = QtWidgets.QLabel(self.tab_8)
        self.label_34.setGeometry(QtCore.QRect(290, 10, 91, 21))
        self.label_34.setObjectName("label_34")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_8)
        self.lineEdit.setGeometry(QtCore.QRect(390, 10, 341, 20))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_10.setGeometry(QtCore.QRect(360, 50, 91, 71))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_13.setGeometry(QtCore.QRect(510, 50, 81, 71))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_14.setGeometry(QtCore.QRect(660, 50, 81, 71))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_15.setGeometry(QtCore.QRect(740, 10, 21, 21))
        self.pushButton_15.setAutoFillBackground(True)
        self.pushButton_15.setStyleSheet("")
        self.pushButton_15.setText("")
        self.pushButton_15.setIcon(icon)
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 10, 771, 611))
        self.textEdit_8.setReadOnly(True)
        self.textEdit_8.setObjectName("textEdit_8")
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 0, 81, 61))
        self.textBrowser_3.setAutoFillBackground(True)
        self.textBrowser_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(320, 0, 321, 111))
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 61, 41))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/images/modulus.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(670, 10, 151, 21))
        self.label_12.setObjectName("label_12")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 151, 16))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(690, 40, 101, 71))
        self.pushButton_16.setObjectName("pushButton_16")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 854, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "How To : Send Encrypted Messages"))
        self.comboBox.setItemText(1, _translate("MainWindow", "How To : Securely Exchange a Password"))
        self.comboBox.setItemText(2, _translate("MainWindow", "How To : Generate a New Key Pair"))
        self.comboBox.setItemText(3, _translate("MainWindow", "How To : Keep Encrypted Notes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "How To Guide"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Load Key Pairs</span></p><p><span style=\" font-size:7pt;\">You can use an existing Key Pair or generate a new one.<br/>These keys are used to encrypt and decrypt the shared password. </span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Copy and paste your own </span><span style=\" font-size:7pt; font-weight:600; text-decoration: underline;\">private</span><span style=\" font-size:7pt; font-weight:600;\"> key here or click on the button to load it from a file</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600;\">Copy and paste your partner\'s </span><span style=\" font-size:7pt; font-weight:600; text-decoration: underline;\">public</span><span style=\" font-size:7pt; font-weight:600;\"> key here or click on the button to load it from a file</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Select File"))
        self.pushButton_3.setText(_translate("MainWindow", "Select File"))
        self.pushButton_4.setText(_translate("MainWindow", "LOAD KEYS"))
        self.label_21.setToolTip(_translate("MainWindow", "<html><head/><body><p>-- Before you can exchange messages, you and your partner need to agree on a password. <br/>( If you have already agreed on a password, you can skip this step )</p><p>-- Key Pairs will help you exchange the password in an encrypted format, so no one else can read it. </p><p>-- If you don\'t already have key files, click on the \'Generate Key Pair&quot; button and generate new keys.</p><p>-- When you\'re finished, &quot;Load&quot; your private key and your partner\'s public key. This program will use the loaded keys to encrypt or decrypt the shared password. </p></body></html>"))
        self.label_22.setToolTip(_translate("MainWindow", "<html><head/><body><p>You can either paste your private key in here, or you can load it from a file. This program will use your private key to decrypt a password that your partner has sent to you. </p></body></html>"))
        self.label_28.setToolTip(_translate("MainWindow", "<html><head/><body><p>You can either paste your partner\'s public key, or you can load it from a file. This key will be used to encrypt a password that only your partner can decrypt </p></body></html>"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "If you don\'t already have one"))
        self.pushButton_11.setText(_translate("MainWindow", "Generate New Key Pair"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Load Key Pairs"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600; text-decoration: underline;\">Sender</span></p><p><span style=\" font-size:7pt;\">Use RSA to encrypt a shared password. </span></p><p><span style=\" font-size:7pt;\">Prerequisites to Encrypt: You must have your communication partner\'s public key. </span></p><p><span style=\" font-size:7pt;\"><br/><br/></span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt;\">What password do you want to share with your partner?</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Encrypt"))
        self.label_20.setToolTip(_translate("MainWindow", "<html><head/><body><p>-- Before you can exchange messages, you and your partner need to agree on a password. </p><p>-- This section lets you choose a password and encrypt it. Only your partner can decrypt it. <br/><br/>1. Load the public key of the person you\'re sending the password to<br/>2. Type a long secure passphrase or password that\'s less than 117 characters long<br/>3. Press the Encrypt button<br/>4. Share the encrypted password with your partner any way you want (chat, email, etc)</p><p><br/></p></body></html>"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Type your password or passphrase here."))
        self.textEdit_2.setPlaceholderText(_translate("MainWindow", "Your encrypted passphrase will appear here."))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; font-weight:600; text-decoration: underline;\">Receiver</span></p><p><span style=\" font-size:7pt;\">Use RSA to decrypt a shared password. </span></p><p><span style=\" font-size:7pt;\">Prerequisites to Decrypt: You must have been sent a password encrypted with your public key. </span></p><p><span style=\" font-size:7pt;\"><br/><br/></span></p></body></html>"))
        self.textEdit_4.setPlaceholderText(_translate("MainWindow", "Paste the sender\'s encrypted password here."))
        self.pushButton_6.setText(_translate("MainWindow", "Decrypt"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Your decrypted passphrase will appear here."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Password Exchange"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Encrypt/Decrypt Message</span></p><p>Messages in this window will be encrypted or decrypted using the given password.<br/></p><p><br/><br/></p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "Encrypt"))
        self.pushButton_9.setText(_translate("MainWindow", "Decrypt"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>Password</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Messages"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:7pt; text-decoration: underline;\">Encrypted Notes</span></p><p><span style=\" font-size:7pt;\">On the fly encryption for text notes.<br/>Requires password to unlock.<br/>No plain text copies ever written to hard drive</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "Password: "))
        self.pushButton_10.setText(_translate("MainWindow", "Load \n"
" Encrypted \n"
" File"))
        self.pushButton_13.setText(_translate("MainWindow", "Decrypt"))
        self.pushButton_14.setText(_translate("MainWindow", "Encrypt \n"
" && Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Encrypted Notes"))
        self.textEdit_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">Frequently Asked Questions </span><span style=\" font-size:7pt;\"><br /></span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:7pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> <span style=\" font-weight:600;\">What encryption algorithms are used?</span> <br />RSA is used for the password exchange. The passphrase is limited to 117 characters to accomdate keys generated by other programs. The Message and Notes use AES with SHA-256 as the hash algorithm. </li>\n"
"<li style=\" font-size:7pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\"> Can we agree on a password and manually type it in?</span><br />Yes. </li>\n"
"<li style=\" font-size:7pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\"> Can messages or notes be recovered if I lost my password?</span><br />No. That\'s the whole point. No password = no message. Without the password it\'s impossible to decrypt the notes. There are no backdoors built into this software. </li>\n"
"<li style=\" font-size:7pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Is this software legal?</span><br />Yes. At the time this software is created there are no US regulations against users ensuring their own privacy. This software does not automatically update, so if that law changes there is no way to retroactively invalidate this software. However, Modulus360\'s intent is to comply with all U.S. laws and regulations, so, should the law change to disallow private encryption, please consider your software license revoked and voluntarily destroy your copy of this software. Please do not use this software to plan, coordinate, or perpetrate crime. Please do not use this software in any of the countries expressly prohibited by US law. Use at your own risk. </li></ul></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "FAQ"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">m360Encrypt</span></p></body></html>"))
        self.textEdit_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:600;\">We Support Privacy and Civil Liberty<br /></span><span style=\" font-size:6pt;\">Consider helping us out!</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt; font-weight:600;\">BC:</span><span style=\" font-size:6pt;\"> bc1qndzd3fdyjzklvefxz9rch6rk7wnep9t87440tq<br /></span><span style=\" font-size:6pt; font-weight:600;\">ETH:</span><span style=\" font-size:6pt;\"> 0x5f879Ef9D9680675A51110DD231481faBdd32d6b<br /></span><span style=\" font-size:6pt; font-weight:600;\">DOGE</span><span style=\" font-size:6pt;\">: DF7Yq9nayLb34ctEAcQT5TCuDvyVT1dSqy</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "Font size too big or too small?"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Version 2.0.2_ld</p></body></html>"))
        self.pushButton_16.setText(_translate("MainWindow", "Change \n"
" Resolution"))
import resources_rc
