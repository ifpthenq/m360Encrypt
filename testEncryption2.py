from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
from pathlib import Path as ahPath
from ahCrypto import ahCrypto

test = ahCrypto()
#test.generateKeyPair("C:\Temp")
print("Encrypting Text")

#encrypted = test.encrypt("This is a test of your emergency broadcast system", "C:\Temp\public_key.txt")
com = '''
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. This is a test of a really long message. This is a test of a really long message. 
This is a test of a really long message. 
'''
encrypted = test.encrypt(com, "C:\Temp\public_key.txt")




print(encrypted)
print("Decrypting Text")

decrypted = test.decrypt(encrypted, "C:\Temp\private_key.txt")
print(decrypted)