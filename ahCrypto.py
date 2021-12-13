
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
from pathlib import Path


class ahCrypto():

    def __init__(self):
        print("DBG: init crypto class")
        self.key = "Not set yet"
        self.public_key = "not set yet"
        self.private_key = "not set yet"
        #print(crypto.__file__)
        
    
    
    def generateKeyPair(self, keypath):
        #keypath should be a string
        locgtg = False; 
        if isinstance(keypath, str):
           #keypath = '/'.join(keypath.split('\\'))
           locgtg = True; 
           
        else:
            print("DBG: keypath needs to be a string. Not a {}".format(type(keypapth)))
            
        if locgtg:
            print("DBG: generating KeyPair")
            key_pair = RSA.generate(2048)
            keypath = Path(keypath)
            privateKeyFileName = keypath / "private_key.PEM"
            with open(privateKeyFileName, "wb") as f:
                f.write(key_pair.exportKey('PEM'))
                f.close()
            
            pubkey = key_pair.publickey()
            publicKeyFileName = keypath / "public_key.PEM"
            with open(publicKeyFileName, "wb") as f:
                f.write(pubkey.exportKey('OpenSSH'))
                f.close()
        else: 
            print("DBG: a gtg was not met in generateKeyPair()")
            print("DBG: locgtg is {}".format(str(locgtg)))
              
            
    
    def encrypt(self, message, publicKeyFileName):
        locgtg = False; 
        #check that public key exists
        if Path(publicKeyFileName).is_file():
            locgtg = True; 
        else:
            print("DBG: The public key file {} does not exist".format(publicKeyFileName))
        
        if locgtg:
            public_key = RSA.importKey(open(publicKeyFileName, 'r').read())
            print("DBG: Imported public key from file")
            rsa_object = PKCS1_v1_5.new(public_key)
            print("DBG: Created public key opbject")
            cipher_text = rsa_object.encrypt(message.encode())
            print("DBG: Encrypted message to cipher_text")
            return cipher_text
            
        else:
            print("DBG: a gtg was not met in encrypt()")
            print("DBG: locgtg is {}".fomrat(str(locgtg)))
       
    def decrypt(self, cipher_text, privateKeyFileName):
        #the cipher_text is encoded then encrypted
        locgtg = False; 
        #check if private key file exists
        if Path(privateKeyFileName).is_file():
            locgtg = True; 
        else: 
            print("DBG: The private key file {} does not exist".format(privateKeyFileName))
            
        if locgtg: 
            private_key = RSA.importKey(open(privateKeyFileName, 'r').read())
            print("DBG: Imported private key from file")
            rsa_object = PKCS1_v1_5.new(private_key)
            print("DBG: Created private key object")
            encrypt_byte = cipher_text
            #allowed longth must be set to the key size / 8
            allowed_length = 256
            message_length = len(encrypt_byte)
            if message_length < 256:
                decipher_text = rsa_object.decrypt(encrypt_byte, "Failed to decrypt message")
            else:
                offset = 0
                res = []
                while message_length - offset > 0:
                    if message_length - offset > allowed_length:
                        res.append(rsa_object.decrypt(encrypt_byte[offset: offset + allowed_length], "Failed in decrypt A"))
                    else:
                        res.append(rsa_object.decrypt(encrypt_byte[offset:], "Failed in decrypt B"))
                    offset += allowed_length
                decrypt_byte = b''.join(res)
            decipher_text = decrypt_byte.decode()
            return decipher_text
            
        else:
            print("DBG: a gtg was not met in decrypt()")
            print("DBG: locgtg is {}".format(str(locgtg)))
        
    
    
    
    
    
        
        