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


from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog, QWidget, QDialog
)

from PyQt5.uic import loadUi

from m360Encrypt_ui import Ui_MainWindow
#from main_window_ui import Ui_MainWindow
from gen_keys_ui import Ui_GenKeysWindow
from instruction_window_ui  import Ui_InstructionWindow

class instructionWindow(QMainWindow, Ui_InstructionWindow):
    def __init__(self, parent=None):
        print("dbg: init Instructions")
        super().__init__(parent)
        self.setupUi(self)
        self.textEdit.setText("test")
class genKeys(QMainWindow, Ui_GenKeysWindow):
    def __init__(self, parent):
        print("dbg: init genKeysWindow")
        
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
        print("dbg: yes i do have a browsefiles()")
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
        print("dbg: now i have a generate keys()")
        self.label_6.setText("** Working")
        doSaveFiles = self.checkBox.isChecked()
        doLoadPrivateKey = self.checkBox_2.isChecked()
        doLoadPublicKey = self.checkBox_3.isChecked()
        
        filePrefix = self.filenamePrefix.text()
        pubFile = os.path.join(self.save_folder, filePrefix + "_public_key.PEM")
        privFile = os.path.join(self.save_folder, filePrefix + "_private_key.PEM")
        key_pair = RSA.generate(2048)
        pubkey = key_pair.publickey()
        
        if(doSaveFiles):
            try:
                with open(privFile, "wb") as f:

                    f.write(key_pair.exportKey('PEM'))
                    f.close()
                
                pubkey = key_pair.publickey()
            
                with open(pubFile,"wb") as f:
                    f.write(pubkey.exportKey('OpenSSH'))
                    f.close()
             
             
                ctypes.windll.user32.MessageBoxW(0, 'Files Created' , 'Successfully wrote files', 0)
            
            except Exception as e:
                popError('Error', e, 0)
        
        
        if(doLoadPrivateKey):
            self.parenty.textEdit.setText(key_pair.exportKey('PEM').decode())
            
        if(doLoadPublicKey):
            self.parenty.textEdit_3.setText(pubkey.exportKey('PEM').decode())
       #self.keys = ahCrypto()
        #self.keys.generateKeyPair()
        
        #reset path, incase someone just typed it in and hit generate
        #stringPath = self.lineEditFileLocation.text()
        #pathpath = '/'.join(stringPath.split('\\'))
        #self.save_folder = Path(pathpath)
        
        
        #private_key_fname = (os.path.join(self.save_folder, "private_key.txt"))
        #public_key_fname = (os.path.join(self.save_folder, "public_key.txt"))
       # print("dbg: in genkeys and save folder is : {} / {}".format(type(self.save_folder), self.save_folder))
       # with open(private_key_fname, 'w') as write_file:
        #    print("dbg: Writing private key")
         #   write_file.write(str(self.keys.private_key))
          #  write_file.close()
        #with open(public_key_fname, 'w') as write_file:
         #   print("dbg: Writing public key")
          #  write_file.write(str(self.keys.public_key))
           # write_file.close()
           
        #here we're sending in the keys not the serialized key bytes
        #self.keys.save_file_private(self.keys.private_key, private_key_fname)
        #self.keys.save_file_public(self.keys.public_key, public_key_fname)
        self.close()
    def enableGenBrowseFiles(self):
        print("dBG: enableGenBrowseFiles")
        if self.checkBox.isChecked():
            self.pushButtonBrowse.setEnabled(True)
            self.label.setEnabled(True)
            self.lineEditFileLocation.setEnabled(True)
            self.label_5.setEnabled(True)
            self.filenamePrefix.setEnabled(True)
        else:
            self.pushButtonBrowse.setEnabled(False)
            self.label.setEnabled(False)
            self.lineEditFileLocation.setEnabled(False)
            self.label_5.setEnabled(False)
            self.filenamePrefix.setEnabled(False)
    
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
        #self.dialog = genKeys(self)
        #bc1qndzd3fdyjzklvefxz9rch6rk7wnep9t87440tq
        #bc: bc1qndzd3fdyjzklvefxz9rch6rk7wnep9t87440tq
        #eth: 0x5f879Ef9D9680675A51110DD231481faBdd32d6b
        #eth: 0x5f879Ef9D9680675A51110DD231481faBdd32d6b
        #dg: DF7Yq9nayLb34ctEAcQT5TCuDvyVT1dSqy
        #dg: DF7Yq9nayLb34ctEAcQT5TCuDvyVT1dSqy
        
        #self.dialog.show()
        #self.keys = ahCrypto()
        #test = self.keys.generateKeyPair()
        #print(self.keys.private_key)
        
    def connectSignalsSlots(self):
    #all of your event listeners go in here
        #self.action_Exit.triggered.connect(self.close)
        print("DBG: enteredConnectSignalSlots")
        #self.actionInstructions.triggered.connect(self.displayInstructions)
        #self.actionGenerate_New_Key_Pair.triggered.connect(self.genKeyPair)
       
    def messageDecrypt(self):
        print("DBG: messageDecrypt()")
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
        print("DBG: messageEncrypt()")
        #check if password is empty
        if len(self.lineEdit_2.text()) < 1:
            self.popError('Error', 'Password cannot be blank', 0)
            return None
        sharedPassword = self.lineEdit_2.text()
        #first check if shared password exists
        if self.sharedPassword and (self.sharedPassword != "No PW set"):
            print("DBG: beginning encrypt message")
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
        print("DBG: loadSharedPassword()")
        self.sharedPassword = self.textEdit_4.toPlainText()
        self.statuspassloaded.setText("Yes")
    def loadSharedPasswordDec(self):
        print("DBG: loadSharedPassword()") 
        
        self.sharedPassword = self.textEdit_6.toPlainText()
        self.statuspassloaded.setText("Yes")
        print("DBG: self.sharedPassword here is {}".format(self.sharedPassword))
    def RSADecrypt(self):
        #check that private key is loaded
        if not self.private_key_loaded:
            self.popError('Error', 'You must load a private key \n before you can decrypt a passphrase.', 0)
            return None
    
        print("DBG: RSADecrypt()")
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
            
    
    
    def RSAEncrypt(self):
        try: 
            print("DBG: RSAEncrypt()")
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
        print("DBG: loadKeys")
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
        print("DBG: selectPublicKey")
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
        print("DBG: savePassword")
    def generateKeyPair(self):
        print("DBG: generateKeyPair")
         #self.dialog.show()
        self.dialog = genKeys(self)
        self.dialog.show()
    def selectPrivateKey(self):
        print("DBG: selectPrivateKey")
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
        print("DBG: notesDecrypt")
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
            print(e)
        
        
    def loadEncryptedFile(self):
        print("DBG: loadEncryptedFile()")
        try:
            filename = QFileDialog.getOpenFileName(self, 'Open File')
            file = open(filename[0], 'r')
            note = file.read()
            self.textEdit_9.setText(note)
        except:
            return None
    def revealNotesPW(self):
        print("DBG: revealNotesPW")
        currentState = self.lineEdit.echoMode()
        if (currentState == 2):
            self.lineEdit.setEchoMode(0)
        else:
            self.lineEdit.setEchoMode(2)
    def revealPWSender(self):
        print("DBG: revealPWSender")
        currentState = self.lineEdit_3.echoMode()
        if (currentState == 2):
            self.lineEdit_3.setEchoMode(0)
        else:
            self.lineEdit_3.setEchoMode(2)
    def revealPSReceiver(self):
        print("DBG: revealPWReceiver")
        currentState = self.lineEdit_5.echoMode()
        if (currentState == 2):
            self.lineEdit_5.setEchoMode(0)
        else:
            self.lineEdit_5.setEchoMode(2)
    def revealPWMessage(self):
        print("DBG: revealPWMessage")
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
        print("DBG: encryptAndSave")
    def browseFiles(self):
        print("DBG: browseFiles")
      
 
        
    
    
    def old_genKeyPair(self):
        #get a file location
        
        print("dbg: genkeypair")
        #self.dialog.show()
        self.dialog = genKeys(self)
        self.dialog.show()
        
        com='''
        
        '''
    def old_displayInstructions(self):
        self.dialog2 = instructionWindow(self)
        self.dialog2.show()
        
    def old_setPublicKey(self):
        print("set public key button pressed")
        pkeyFile = QFileDialog.getOpenFileName(self, 'Select Public Key',
                    'c:\\')
        #pkeyFile.setFileMode(QRileDialog.AnyFile)
        #pkeyFile.setFilter("Text Files (*.txt)")
        self.public_key = pkeyFile[0]
        filename = pkeyFile[0]
        print(filename)
        try:
            with open(filename, 'r', encoding='utf-8') as kFile:
                lines = kFile.readlines()
                print(lines)
                print("I just printed the file")
                self.textEditPublicKey.clear()
                self.textEditPublicKey.append("Loading Key File: {}".format(str(filename)))
                for line in lines:
                    self.textEditPublicKey.append(line)
            print("dbg: Line 144 - trying to load from file")
            self.loadedPublicKey = self.mainAhCrypto.load_key_public(filename)
            #test
            
            print("dbg: I just set loadedPublicKey. Type  is {}".format(type(self.loadedPublicKey)))
        except Exception as e:
            print(e)
    
    def old_setPrivateKey(self):
        print("dbg: setPrivateKey")
        pkeyFile = QFileDialog.getOpenFileName(self, 'Select Private Key',
                   'c:\\')
        #this is the text version of the key for displaying
        self.private_key = pkeyFile[0]
        filename = pkeyFile[0]
        try: 
            with open(filename, 'r', encoding='utf-8') as kFile:
                lines = kFile.readlines()
                self.textEditPrivateKey.clear()
                self.textEditPrivateKey.append("Loading Key File: {}".format(str(filename)))
                for line in lines:
                    self.textEditPrivateKey.append(line)
            #this is the bytes version of the key
            self.loadedPrivateKey = self.mainAhCrypto.load_key_private(filename)
            print("DBG: I HAVE LOADED THE PRIVATE KEY AND IT IS A {}".format(type(self.loadedPrivateKey)))
         
        except Exception as e:
            print(e)
        
    def old_encryptMainWindo(self):
        print("dbg: encryptMainWindo")
        
        encryptedMessage = self.mainAhCrypto.encrypt(self.loadedPublicKey, self.textEditEncrypt.toPlainText())
        self.textEditEncrypt.setText(str(encryptedMessage))
        
    def old_decryptMainWindo(self):
        print("dbg: decryptMainWindo")
        
        decryptedMessage = self.mainAhCrypto.decrypt(self.loadedPrivateKey, self.textEditEncrypt.toPlainText())
        self.textEditEncrypt.setText(str(decryptedMessage))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    #generate = genKeys()
    #this.generateWindow = generate
    win.show()
    #generate.show()
    sys.exit(app.exec())