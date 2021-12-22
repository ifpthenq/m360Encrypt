import sys
import os
from pathlib import Path
#from ahCrypto import ahCrypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import urllib.parse
import base64
import ctypes
from PyQt5 import QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtGui import QColor
from PyQt5.QtGui import * 
from Labels import Labels
from PyQt5.QtWidgets import QApplication
from howToGuide import howToGuide


from win32api import GetSystemMetrics


from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QWidget, QDialog
)

from PyQt5.uic import loadUi

from funky_screen_ui import Ui_MainWindow as funky_MainWindow
from fw import FunkyWindow

from m360Encrypt_ui import Ui_MainWindow
#from main_window_ui import Ui_MainWindow
from gen_keys_ui import Ui_GenKeysWindow
from instruction_window_ui  import Ui_InstructionWindow

class instructionWindow(QMainWindow, Ui_InstructionWindow):
    def __init__(self, parent=None):
       #print("dbg: init Instructions")
        super().__init__(parent)
        self.setupUi(self)
        self.textEdit.setText("test")
class genKeys(QMainWindow, Ui_GenKeysWindow):
    def __init__(self, parent):
        #print("dbg: init genKeysWindow")
        
        super().__init__(parent)
        
        self.setupUi(self)
        self.parenty = parent
        #self.parenty.textEdit.setText("test")
        self.lineEditFileLocation.setText("C:\Temp")
        stringPath = self.lineEditFileLocation.text()
        pathpath = '/'.join(stringPath.split('\\'))
        self.save_folder = Path(pathpath)
        #print("dbg: stringPath is {}".format(pathpath))
        
    def browseFiles(self):
        #print("dbg: yes i do have a browsefiles()")
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.Directory)
        #self.lineEditFileLocation = ""
        if(dialog.exec()):
            dir = dialog.selectedFiles()
       
            self.lineEditFileLocation.setText(dir[0])
        if len(self.lineEditFileLocation.text()) == 0:
            return None
        stringPath = self.lineEditFileLocation.text()
        pathpath = '/'.join(stringPath.split('\\'))
        self.save_folder = Path(pathpath)
        self.lineEditFileLocation.setText(str(self.save_folder))
        #print("dbg: finished BrowseFiles and Save folder is: {} / {}".format(type(self.save_folder), self.save_folder))
        
        
    def generateKeys(self): 
        #print("dbg: now i have a generate keys()")
        ctypes.windll.user32.MessageBoxW(0, 'This will cause the program to freeze \n for a couple of minutes' , 'Warning', 0)
        doSaveFiles = self.checkBox.isChecked()
        doLoadPrivateKey = self.checkBox_2.isChecked()
        doLoadPublicKey = self.checkBox_3.isChecked()
        doSaveSSH = self.checkBox_4.isChecked()
        
        filePrefix = self.filenamePrefix.text()
        pubFile = os.path.join(self.save_folder, filePrefix + "_public_key.PEM")
        pubSSH = os.path.join(self.save_folder, filePrefix + "_pub_id_rsa.pub")
        privFile = os.path.join(self.save_folder, filePrefix + "_private_key.PEM")
        #privSSH = os.path.join(self.save_folder, filePrefix + "_priv_id_rsa")
        
        key_pair = RSA.generate(2048)
        #pubkey = key_pair.publickey()
        
        if(doSaveFiles):
            try:
                with open(privFile, "wb") as f:

                    f.write(key_pair.exportKey('PEM'))
                f.close()
                
                        
                pubkey = key_pair.publickey()
            
                with open(pubFile,"wb") as f:
                    f.write(pubkey.exportKey('PEM'))
                f.close()
                    
                if(doSaveSSH):
                    with open(pubSSH, "wb") as f2:
                        f2.write(pubkey.exportKey('OpenSSH'))
                    f2.close()
             
                ctypes.windll.user32.MessageBoxW(0, 'Successfully wrote files' , 'Files Created', 0)
            
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(0, str(e) , 'Error', 0)
        
        
        if(doLoadPrivateKey):
            self.parenty.textEdit.setText(key_pair.exportKey('PEM').decode())
            
        if(doLoadPublicKey):
            self.parenty.textEdit_3.setText(pubkey.exportKey('PEM').decode())
       
        if(doLoadPublicKey or doLoadPrivateKey):
            self.parenty.loadKeys()
        
        self.close()
    def enableGenBrowseFiles(self):
        #print("dBG: enableGenBrowseFiles")
        if self.checkBox.isChecked():
            self.pushButtonBrowse.setEnabled(True)
            self.label.setEnabled(True)
            self.lineEditFileLocation.setEnabled(True)
            self.label_5.setEnabled(True)
            self.filenamePrefix.setEnabled(True)
            self.checkBox_4.setEnabled(True)
            self.label_7.setEnabled(True)
            
        else:
            self.pushButtonBrowse.setEnabled(False)
            self.label.setEnabled(False)
            self.lineEditFileLocation.setEnabled(False)
            self.label_5.setEnabled(False)
            self.filenamePrefix.setEnabled(False)
            self.checkBox_4.setEnabled(False)
            self.label_7.setEnabled(False)
    
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #call setupUi in your ui file
        self.setupUi(self) 
        #call your event handler function
        self.connectSignalsSlots()
        self.public_key_fname = ""
        self.private_key_fname = ""
        #self.mainAhCrypto = ahCrypto()
        self.loadedPublicKey = "No Key Set"
        self.loadedPrivateKey = "No Key Set"
        self.sharedPassword = "No PW Set"
        self.public_key_loaded = False
        self.private_key_loaded = False
        screenWidth = GetSystemMetrics(0)
        screenHeight = GetSystemMetrics(1)
        print("DBG: This is funky window")
        self.labels = Labels() 
        self.howTos = howToGuide()
        self.howToSize = 9
        self.selectHowTo()
        self.toggleDPI = 0
    def connectSignalsSlots(self):
    #all of your event listeners go in here
        #self.action_Exit.triggered.connect(self.close)
        print("DBG: enteredConnectSignalSlots")
        #self.actionInstructions.triggered.connect(self.displayInstructions)
        #self.actionGenerate_New_Key_Pair.triggered.connect(self.genKeyPair)
       
    def messageDecrypt(self):
        #print("DBG: messageDecrypt()")
        #check if password is empty
        if len(self.lineEdit_2.text()) < 1:
            self.popError('Error', 'Password cannot be blank', 0)
            return None
        sharedPassword = self.lineEdit_2.text()
        if self.sharedPassword and (self.sharedPassword != "No PW set"):
            source = self.textEdit_7.toPlainText()
            source = base64.b64decode(source.encode("latin-1"))
            key = self.sharedPassword.encode()
            key = SHA256.new(key).digest()
            IV = source[:AES.block_size]
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            data = decryptor.decrypt(source[AES.block_size:])
            padding = data[-1]
            if data [-padding:] != bytes([padding]) * padding:
                raise ValueError("Invalid Padding")
            data = data[:-padding]
            #decoded = base64.b64encode(data).decode("latin-1")
            #decoded = str(data)
            decoded = data.decode()
            self.textEdit_7.setText(str(decoded))
            
    def messageEncrypt(self):
        #print("DBG: messageEncrypt()")
        #check if password is empty
        if len(self.lineEdit_2.text()) < 1:
            self.popError('Error', 'Password cannot be blank', 0)
            return None
        sharedPassword = self.lineEdit_2.text()
        #first check if shared password exists
        if self.sharedPassword and (self.sharedPassword != "No PW set"):
            #print("DBG: beginning encrypt message")
            key = self.sharedPassword.encode()
            source = self.textEdit_7.toPlainText().encode()
            key = SHA256.new(key).digest()
            IV = Random.new().read(AES.block_size)
            encryptor = AES.new(key, AES.MODE_CBC, IV)
            padding = AES.block_size - len(source) % AES.block_size
            source += bytes([padding]) * padding
            data = IV + encryptor.encrypt(source)
            decoded = base64.b64encode(data).decode("latin-1") 
            self.textEdit_7.setText(str(decoded))
            
        
    def loadSharedPassword(self):
        #print("DBG: loadSharedPassword()")
        self.sharedPassword = self.textEdit_4.toPlainText()
        self.statuspassloaded.setText("Yes")
    def loadSharedPasswordDec(self):
        #print("DBG: loadSharedPassword()") 
        
        self.sharedPassword = self.textEdit_6.toPlainText()
        self.statuspassloaded.setText("Yes")
        #print("DBG: self.sharedPassword here is {}".format(self.sharedPassword))
    def RSADecrypt(self):
        try:
            #check that private key is loaded
            if not self.private_key_loaded:
                self.popError('Error', 'You must load a private key \n before you can decrypt a passphrase.', 0)
                return None
    
            #print("DBG: RSADecrypt()")
            rsa_object = PKCS1_v1_5.new(self.private_key)
            #print("DBG: starting decrypt")
            encrypt_byteAsString = self.textEdit_4.toPlainText()
            #encrypt_byteAsHex = ''.join([str(hex(ord(i)))[2:4] for i in encrypt_byteAsString])
        
            encrypt_byteAsBytes = bytes.fromhex(encrypt_byteAsString)
            encrypt_byte = encrypt_byteAsBytes
            allowed_length = 1024
            my_length = len(encrypt_byte)
            if my_length < allowed_length:
                decipher_text = rsa_object.decrypt(encrypt_byte, "failure")
                self.lineEdit_5.setText(decipher_text.decode())
            else: 
            #offset = 0
            #res = []
            #while my_length - offset > 0:
            #    if my_length - offset > allowed_length:
            #        res.append(rsa_object.decrypt(encrypt_byte[offset: offset + allowed_length], 'failure'))
            #    else:
            #        res.append(rsa_object.decrypt(encrypt_byte[offset:], 'failure'))
            #    offset += allowed_length
            #decrypt_byte = b''.join(res)
                self.popError('Error', 'The text your trying to decrypt \n exceeds the maximum length \n for a password', 0)
        except ValueError as ve:
            self.popError('Error', 'This text is not a valid cipher', 0)
        except Exception as e:
            self.popError('Error', 'Cannot decrypt this with the private \n key you have loaded', 0)
    
    
    def RSAEncrypt(self):
        try: 
            #print("DBG: RSAEncrypt()")
            check = self.lineEdit_3.text()
            #check if public key is loaded
            if not self.public_key_loaded:
                self.popError('No public key', 'You must load a public Key \n before you can encrypt a passphrase', 0)
                return None
            #check if it's empty
            if (check == ""):
                self.popError('Blank Field', 'Cannot encrypt an empty field',0)
                return None
            #check if short
            if (len(check) < 16):
                self.popError('Warning', 'Warning: This is a short passphrase. \n A longer passphrase would be more secure.', 0)
            #check if too long
            if(len(check) > 117):
                self.popError('Sorry', 'The passphrase needs to be under 117 characters.', 0)
                return None
            #create an RSA objec using the public key
            
            rsa_object = PKCS1_v1_5.new(self.public_key)
            message = self.lineEdit_3.text()
            #returns bytes
            cipher_textAsBytes = rsa_object.encrypt(message.encode()) 
        
            #convert bytes to hex
            cipher_textAsHex = cipher_textAsBytes.hex()
            #print(str(cipher_textAsHex) )
            #convert to readable string
            #cipher_textAsString = ''.join(chr(int(cipher_textAsHex[i:i+2], 16)) for i in range(0, len(cipher_textAsHex), 2))
            
            self.textEdit_2.setText(cipher_textAsHex)
        except ValueError as ve: 
            if ve == "Plaintext is too long":
                self.popError('Error', 'Your password must be less than 117 characters', 0)
            else:
                self.popError('Error', 'There\'s something wrong with the password you selected. Try a different one', 0)
    def loadKeys(self):
        #print("DBG: loadKeys")
        #this function takes whatever is in the window
        #turns it into keys, and loads them into globals
        
        pubKeyAsString = self.textEdit_3.toPlainText()
        if not pubKeyAsString:
            self.popError('Warning', 'Warning: No Public Key Selected', 0)
        else:
            try:
                self.public_key = RSA.importKey(pubKeyAsString)
                #self.statuspubloaded.setText("Yes")
                self.public_key_loaded = True
               
            except ValueError as ve:
                self.popError('Error', 'The public key you entered \n is not the correct format. \n No public key loaded', 0)
        
        privKeyAsString = self.textEdit.toPlainText()
        if not privKeyAsString:
            self.popError('Warning', 'Warning: No Private Key Selected', 0)
        else:
            try:
                self.private_key = RSA.importKey(privKeyAsString)
                #self.statusprivloaded.setText("Yes")
                self.private_key_loaded = True
            except ValueError as ve:
                self.popError('Error', 'The private key you entered \n is not the correct format. \n No private key loaded', 0)
        
        if self.public_key_loaded:
            self.popError('Public Key Loaded', 'Public Key loaded successfully', 0)
       
            
        if self.private_key_loaded: 
            self.popError('Private Key Loaded', 'Private Key loaded successfully', 0)
        #check to make sure
        
        #checkRSA = self.public_key.exportKey("PEM")
        #checkString = checkRSA.decode("utf-8")
        #print(checkString)
          
    def selectPublicKey(self):
        #print("DBG: selectPublicKey")
        pkeyFile = QFileDialog.getOpenFileName(self, 'Select Public Key',
                   'c:\\')
        public_key_path = pkeyFile[0]
        try: 
        
            public_key = RSA.importKey(open(public_key_path, 'r').read())
            pubKeyAsBytes = public_key.exportKey("PEM") # rsa to bytes
            pubKeyAsString = pubKeyAsBytes.decode("utf-8") #bytes to string
            #to convert from string to key again use
            # private_key = RSA.importKey(privKeyAsString)
            self.textEdit_3.setText(str(pubKeyAsString))
        except ValueError as ve:
            self.popError('Error', 'This is not a valid KEY file', 0)
        except FileNotFoundError as f:
            self.popError('Error', 'No file selected', 0)
    def savePassword(self):
        #print("DBG: savePassword")
        return None
    def generateKeyPair(self):
        #print("DBG: generateKeyPair")
         #self.dialog.show()
        self.dialog = genKeys(self)
        self.dialog.show()
    def selectPrivateKey(self):
        #print("DBG: selectPrivateKey")
        pkeyFile = QFileDialog.getOpenFileName(self, 'Select Private Key',
                   'c:\\')
        private_key_path = pkeyFile[0]
        try: 
        
            private_key = RSA.importKey(open(private_key_path, 'r').read())
            privKeyAsBytes = private_key.exportKey("PEM") # rsa to bytes
            privKeyAsString = privKeyAsBytes.decode("utf-8") #bytes to string
            #to convert from string to key again use
            # private_key = RSA.importKey(privKeyAsString)
            self.textEdit.setText(str(privKeyAsString))
        except ValueError as ve:
            self.popError('Error', 'This is not a valid KEY file', 0)
        except FileNotFoundError as f:
            self.popError('Error', 'No file selected', 0)
        
    def popError(self, title, text, style):
        ##  Styles:
        ##  0 : OK
        ##  1 : OK | Cancel
        ##  2 : Abort | Retry | Ignore
        ##  3 : Yes | No | Cancel
        ##  4 : Yes | No
        ##  5 : Retry | Cancel 
        ##  6 : Cancel | Try Again | Continue
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    def notesDecrypt(self):
        #print("DBG: notesDecrypt")
        #check password is not blank
        if (len(self.lineEdit.text()) < 1):
            self.popError('Error', 'Password cannot be blank', 0)
            return None
        try:
            myPassword = self.lineEdit.text()
            source = self.textEdit_9.toPlainText()
       
        
            source = base64.b64decode(source.encode("latin-1"))
            key = myPassword.encode()
            key = SHA256.new(key).digest()
            IV = source[:AES.block_size]
            decryptor = AES.new(key, AES.MODE_CBC, IV)
            data = decryptor.decrypt(source[AES.block_size:])
            padding = data[-1]
            if data [-padding:] != bytes([padding]) * padding:
                raise ValueError("Invalid Padding")
            data = data[:-padding]
                #decoded = base64.b64encode(data).decode("latin-1")
                #decoded = str(data)
            decoded = data.decode()
            self.textEdit_9.setText(str(decoded))
        except Exception as e:
            self.popError('Error', 'Unable to decrypt note with given password', 0)
            #print(e)
        
        
    def loadEncryptedFile(self):
        #print("DBG: loadEncryptedFile()")
        try:
            filename = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(filename[0], 'r')
            note = file.read()
            self.textEdit_9.setText(note)
        except:
            return None
    def revealNotesPW(self):
        #print("DBG: revealNotesPW")
        currentState = self.lineEdit.echoMode()
        if (currentState == 2):
            self.lineEdit.setEchoMode(0)
        else:
            self.lineEdit.setEchoMode(2)
    def revealPWSender(self):
        #print("DBG: revealPWSender")
        currentState = self.lineEdit_3.echoMode()
        if (currentState == 2):
            self.lineEdit_3.setEchoMode(0)
        else:
            self.lineEdit_3.setEchoMode(2)
    def revealPSReceiver(self):
        #print("DBG: revealPWReceiver")
        currentState = self.lineEdit_5.echoMode()
        if (currentState == 2):
            self.lineEdit_5.setEchoMode(0)
        else:
            self.lineEdit_5.setEchoMode(2)
    def revealPWMessage(self):
        #print("DBG: revealPWMessage")
        currentState = self.lineEdit_2.echoMode()
        if (currentState == 2):
            self.lineEdit_2.setEchoMode(0)
        else:
            self.lineEdit_2.setEchoMode(2)
    def encryptAndSave(self):
        #check that pw field isn't blank
        if(len(self.lineEdit.text()) < 1):
            self.popError('Error', 'Password field cannot be blank',0)
            return None
        #make sure note is not blank
        if(len(self.textEdit_9.toPlainText()) )< 1 : 
            self.popError('Error', 'Note appears to be blank', 0)
            return None
        #encrypt it
        
        #first check if shared password exists
        mypassword = self.lineEdit.text()
        key = mypassword.encode()
        source = self.textEdit_9.toPlainText().encode()
        key = SHA256.new(key).digest()
        IV = Random.new().read(AES.block_size)
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        padding = AES.block_size - len(source) % AES.block_size
        source += bytes([padding]) * padding
        data = IV + encryptor.encrypt(source)
        decoded = base64.b64encode(data).decode("latin-1") 
        self.textEdit_9.setText(str(decoded))
        
        #then save to file
        try: 
            filename = QFileDialog.getSaveFileName(self, 'Save File')
            file = open(filename[0], 'w')
            text = self.textEdit_9.toPlainText()
            file.write(text)
            file.close()
            self.popError('Success', 'Successfully saved encrypted file',0)
        except Exception as e:
            self.popError('Error', str(e), 0)
        #print("DBG: encryptAndSave")
    
    def useHighDPI(self):
        #print("DBG: USe High DPI")
        self.label_15.setText(self.labels.loadKeyPairMain(8,8))
        self.textEdit_8.setHtml(self.labels.setFaq(8, 8,6))
        self.textEdit_5.setHtml(self.labels.setBitcoin(7.25))
        self.label_17.setText(self.labels.setLabel17(7))
        self.label_18.setText(self.labels.setLabel18(7))
        self.label_3.setText(self.labels.setLabel3(7))
        self.label_10.setText(self.labels.setLabel10(7))
        self.label_11.setText(self.labels.setLabel11(7))
        self.label_19.setText(self.labels.setLabel19(10, 7))
        self.label_23.setText(self.labels.setLabel23(7))
        self.label_33.setText(self.labels.setLabel33(7))
        self.label_34.setText(self.labels.setLabel34(7))
        self.howToSize = 7
        self.selectHowTo()
        self.toggleDPI = 1
    def useLowDPI(self):
        #print("DBG: Use Low DPI") 
        if(self.toggleDPI):
            #self.textEdit_5.setHtml(self.labels.loadKeyPairMain(10,10))
            self.label_15.setText(self.labels.loadKeyPairMain(10,10))
            self.textEdit_8.setHtml(self.labels.setFaq(10,10, 8))
            self.textEdit_5.setHtml(self.labels.setBitcoin(8.25))
            self.label_17.setText(self.labels.setLabel17(9))
            self.label_18.setText(self.labels.setLabel18(9))
            self.label_3.setText(self.labels.setLabel3(9))
            self.label_10.setText(self.labels.setLabel10(9))
            self.label_11.setText(self.labels.setLabel11(9))
            self.label_19.setText(self.labels.setLabel19(12, 9))
            self.label_23.setText(self.labels.setLabel23(9))
            self.label_33.setText(self.labels.setLabel33(9))
            self.label_34.setText(self.labels.setLabel34(9))
            self.howToSize = 9
            self.selectHowTo()
            self.toggleDPI = 0
        else:
            self.useHighDPI()
            
        
    def selectHowTo(self):
        soptions = []
        selectedIndex = self.comboBox.currentIndex()
        if selectedIndex == 0:
            
            self.comboBox_2.clear()
            self.comboBox_2.setEnabled(False)
            self.textEdit_6.setHtml(self.howTos.sendMessage(self.howToSize))
            
        elif selectedIndex == 1:
            self.textEdit_6.clear()
            self.comboBox_2.setEnabled(True)
            self.comboBox_2.clear()
            soptions = [
                "** Choose your role ",
                "When You Are the Sender",
                "When You Are the Receiver"
            ]
            self.comboBox_2.addItems(soptions)
            self.comboBox_2.currentIndexChanged.connect(self.youAreSender)  
            
    def youAreSender(self):
        selectedIndex = self.comboBox_2.currentIndex()
        if selectedIndex == 0:
            self.textEdit_6.clear()
        elif selectedIndex == 1:
            self.textEdit_6.setHtml(self.howTos.exchangePasswordSender(self.howToSize))
        else:
            self.textEdit_6.setHtml(self.howTos.exchangePasswordReceiver(self.howToSize))
        
if __name__ == "__main__":
    
    
    #os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "0"
    #QApplication.setAttribute(QtCore.Qt.AA_Use96Dpi)
    #QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling)
    app = QApplication(sys.argv)
    #app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    #app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
    #app.setAttribute(QtCore.Qt.AA_Use96Dpi)
    QApplication.setStyle("Fusion")
    #
    
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, QtCore.Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.ToolTipText, QtCore.Qt.white)
    dark_palette.setColor(QPalette.Text, QtCore.Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, QtCore.Qt.white)
    dark_palette.setColor(QPalette.BrightText, QtCore.Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, QColor(35, 35, 35))
    dark_palette.setColor(QPalette.Active, QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.Disabled, QPalette.ButtonText, QtCore.Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.WindowText, QtCore.Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.Text, QtCore.Qt.darkGray)
    dark_palette.setColor(QPalette.Disabled, QPalette.Light, QColor(53, 53, 53))
    QApplication.setPalette(dark_palette)
    screenWidth = GetSystemMetrics(0)
    screenHeight = GetSystemMetrics(1)
    print("DBG: res: {} x {}".format(screenWidth, screenHeight))
    if (screenWidth / screenHeight) < 1.7:
        print ("this is a funky screen size. changing UI to fit")
             
        #fwin = FunkyWindow()
        #fwin.show()
        win = Window()
        win.show()
    else:
        #fwin = FunkyWindow()
        #fwin.show()
        win = Window()
        win.show()
    #generate.show()
    sys.exit(app.exec())