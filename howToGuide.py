
class howToGuide():
    def __init__(self, parent=None):
        self.initiated = True
        
    def sendMessage(self, size):
        smallerSize = size - 1
        body = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
p,ul,li {{ font-size:{0}pt; font-weight:normal; margin:0,0,0,0; -qt-block-indent:0; text-indent:0px; white-space: pre-wrap; }}
.question {{font-weight:600; font-size: {0}pt;margin-top:12px;}} 
.answer {{font-size: {1}pt; margin-top:5px; -qt-block-indent: 1; text-indent: 12pt;}}
</style></head>

<body>
<p><span style="font-weight:600;">How to Send Encrypted Messages</span>
</p>
<ul>
<li>
<p class="question"> Step One </p>
<p class="answer"> <b>You and the person you are communicating with both need to be running m360Encrypt on your computers.</b></p>
</li>

<li>
<p class="question"> Step Two </p>
<p class="answer"> <b>You and your partner need to agree on a secure password </b>
 <br />The password can be up to 117 characters and should be at least 30 characters
 <br /><i style="color:#f9faca;">Note: For help with exchanging passwords, see "How to : Securely Exchange a Password" in this guide </i>
</p>
</li>

<li>
<p class="question"> Step Three </p>
<p class="answer"> <b>On the "Messages" Tab, type or paste your password into the "Password" text field</b></p>
<p class="answer" style="color:#f9faca;"> <i>Note: This program will whatever password is in this field to encrypt and decrypt the message in the messages
 in the text box </i> </p>
</li>

<li>
<p class="question"> Step Four </p>
<p class="answer"> <b>Type your message into the text field, and press the Encrypt button</b?</p>
</li>

<li>
<p class="question"> Step Five </p>
<p class="answer"> <b>Copy the encrypted text and paste it into your email, chat, social media, or whatever software you are using to communicate with your partner </b></p>
</li>

<li>
<p class="question"> Use Any Third Party Software </p>
<p class="answer"> This software does not transmit any data or open any ports. It is
 intended for you to encrypt and decrypt messages here and then copy and paste them
 into whatever software you want to use for communication. If encrypted, your
 data will be protected from service proivders and other eavesdroppers. </p>
</li>
</ul>
</body>

</html>
""".format(size, smallerSize)
        return body
        
    def exchangePasswordSender(self, size):
        smallerSize = size - 1
        body = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
p,ul,li {{ font-size:{0}pt; font-weight:normal; margin:0,0,0,0; -qt-block-indent:0; text-indent:0px; white-space: pre-wrap; }}
.question {{font-weight:600; font-size: {0}pt;margin-top:12px;}} 
.answer {{font-size: {1}pt; margin-top:5px; -qt-block-indent: 1; text-indent: 12pt;}}
</style></head>

<body>
<p><span style="font-weight:600;">How to Securely Exchange a Password</span>
</p>
<p><span style="font-weight:600;">When you are the Sender:</span>
</p>

<ul>
<li><p class="question">Step 1</p>
<p class="answer"><b>You and your partner both need to be running m360Encrypt on your computers.
</b></p>
</li>

<li><p class="question">Step 2</p>
<p class="answer"><b>You need to get your partner's <i style="color:#f9faca">public</i> key. </b></p>
<p class="answer"> They can share their public key with you via email, chat, social media, post it on a website - 
 any way that you normally communicate. It's OK if other people see their public key. 
</p>
<p class="answer"> You can either copy the key to your clipboard by highlighting all of it, and pressing Ctrl + C on your keyboard,
 or you can save the key as a file on your computer.</p>
</li>

<li>
<p class="question">
Step 3
</p>
<p class="answer"><b>Load your Partner's Public Key</b></p>
<p class="answer">Put your partner's public key in the bottom textbox on the "Load KeyPairs" tab. </p>
<p class="answer" style="color:#f9faca">Note: If you copied the public key to your clipboard, you can paste it into the textbox by clicking
on the textbox to select it, and then pressing Ctrl + V on your keyboard</p>
<p class="answer" style="color:#f9faca">If you received the key as a file, you can click on the Select button and select the file, and
 m360Encrypt will import it for you into the textbox. 
<p class="answer" style="color:#f9faca">Note: It's OK to have the private key box (the top textbox) be blank. This field is only used to decrypt
 a password. As the Sender you are Encrypting the password. Only the recipient can decrypt it. </p>
<p class="answer"> <b>Once the Public Key appears in the box, click on the Load Keys button.</b></p>

<p class="answer" style="color:#f9faca"><i>What to do if you get an error :</i></p>
<p class="answer" style="color:#f9faca"><i> If you get an error message when you click the Load Keys button it is because the key is not the right format. 
 A public key should start with "-----BEGIN PUBLIC KEY-----" or "ssh-rsa"
 The file type will be a .txt file, .PUB, or .PEM. All of these can be opened in a text editor like Notepad
 so that you can verify the key starts with the correct header. <br />
 If the key is not able to load, try re-copying the key, or ask your partner to generate and send a new key. </i>
</p>
</li>

<li>
<p class="question">Step 4</p>
<p class="answer"><b>Create a Password</b></p>
<p class="answer"> Go to the "Password Exchange" tab. </p>
<p class="answer"> You will need to create a very long password or passphrase. It should be more than 30 characters, but less than 117. </p>
<p class="answer"> Put your password in the top text field on the PasswordExchange Tab. </p>
<p class="answer"> Click on the "Encrypt" button. 
<p class="answer"> You should now see a cipher of your password in the second text box. A cipher is encrypted text that looks
 like random unreadable characters. The cipher will always be the same size, regardless of how long or short the password is. 
</p>
</li>

<li>
<p class="question">Step 5</p>
<p class="answer"><b>You need to get the ciper to the person you are trying to communicate with.</b></p>
<p class="answer">Highlight the whole thing and press Ctrl+C to copy it. Use Ctrl + V to paste it in any software you regularly use for communication (email, chat, social media, etc), and
send it to your partner. 

</p>


</li>

<li>
<p class="question">Step 6</p>
<p class="answer"><b>Copy the plain text password into the Messages tab to use it to encrypt messages</b></p>
<p class="answer">You will need to use the <b>plain-text password</b> (not the cipher) to encrypt messages
 for your partner. </p>
<p class="answer"> Click on the eye symbol next to the password field to reveal the plain-text password. Highlight the whole thing
 and press Ctrl + C to copy it. </p>
<p class="answer">Go to the "Messages" Tab. Click into the Password field and then press Ctrl + V on your keyboard
 to paste the password into the field. </p>
</li>

<li>
<p class="question"> You are now ready to encrypt messages that only your communication partner can read </p>
<p class="answer" style="color:#f9faca"> <b>Note:</b> For detailed instructions on how to send messages see the "How To: Send Encrypted Messages" guide </p>
</li>
</ul>

</body></html>        
""".format(size, smallerSize)
        return body
        
        
        
        
    def exchangePasswordReceiver(self, size):
        smallerSize = size - 1
        body = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
p,ul,li {{ font-size:{0}pt; font-weight:normal; margin:0,0,0,0; -qt-block-indent:0; text-indent:0px; white-space: pre-wrap; }}
.question {{font-weight:600; font-size: {0}pt;margin-top:12px;}} 
.answer {{font-size: {1}pt; margin-top:5px; -qt-block-indent: 1; text-indent: 12pt;}}
</style></head>

<body>
<p><span style="font-weight:600;">How to Securely Exchange a Password</span>
</p>
<p><span style="font-weight:600;">When you are the Receiver:</span>
</p>

<ul>
<li>

</li>
<li><p class="question">Step 1</p>
<p class="answer"><b>You and your partner both need to be running m360Encrypt on your computers.</b>
</p>
</li>

<li><p class="question">Step 2</p>
<p class="answer"><b>(optional) Generate a new Key Pair. </b></p>
<p class="answer" style="color:#f9faca"><b>When to use this option:</b></p>
<p class="answer" style="color:#f9faca"> If you already have a key pair you can skip this step. </p>
<p class="answer" style="color:#f9faca"> You will need a public key to share with your partner, so if you do not have 
 one already that you'd like to use, then go ahead and generate a new one. For more detailed instructions
 you can review "How To: Generate a New Key Pair" in this guide.</p>
<p class="answer"> To generate a new key pair, select the "Load Key Pairs" tab, and click on the Generate New Key Pair button.<br/>
 In the new window that appears, click on "Save my keys as files on my hard drive."<br/><i> For added security, you could choose to 
 load your keys without saving them to your hard drive, and instead use different keys for every conversation. </i>
 <br/> If you choose to save the keys to your hard drive for later use, select the save location, and in the next 
 text field choose a name to append to your keys so you can identify them later. Select the options to load the keys
  into your session, and then click on the Generate button. </p>
</li>

<li><p class="question">Alternate Step 2</p>
<p class="answer"><b>(optional) Load a Key from a file </b></p>
<p class="answer" style="color:#f9faca"><b>When to use this option:</b></p>
<p class="answer" style="color:#f9faca"> You may want to use this option if you have a key that you've already dissemintated, or that
 others are already using. </p>
<p class="answer"> Click on the top "Select" button and navigate to your
 existing private key file. <br /> Click on the botton "Select" button and navigate to your existing private key file. 
</p>
</li>

<li><p class="question">Load Keys </p>
<p class="answer"> With your key fields populated, click on the Load Keys button. <br />
 This will instruct the software to use these keys to encrypt and decrypt the password 
</p>
<p class="answer" style="color:#f9faca"><i>Note: As the Reciever of the password, you will not need to 
 encrypt it. Only the Sender needs to encrypt and send the password. The Receiver only needs to Decrypt it. 
 As such, it is OK for the public key field to be blank. </i>
</li>

<li><p class="question">Send your partner your <i style="color:#f9faca">public</i> key </p>
<p class="answer"> Anyone with your public key can encrypt a short message that only you can decrypt. Therefore, 
 you can share your public key insecurely. Send it to your partner however you'd like (email, chat, social media, posted on a website, etc). 
 It doesn't matter who intercepts it, because it can only be used to encrypt messages, not to decrypt them.
</p>
</li>

<li><p class="question">SECURITY WARNING: Keep your <i style="color:#f9faca">private</i> key safe! </p>
<p class="answer"> Anyone who gets a hold of your private key and also your partner's encrypted password could decrypt the password. 
 Do NOT share your PRIVATE key with anyone. If you plan to keep it long term, consider storing it as an encrypted note. 
</p>
</li>

<li><p class="question">Step 3</p>
<p class="answer"><b>Receive a copy of the encrypted password</b> </p>
<p class="answer">Your communication partner must send you the encrypted password. You may receive it as an email,
 text message, or social media post. Copy the encrypted password, or Cipher, from whereever it's posted by highlighting
 it and pressing ctrl+C on your keyboard. Alternatively, you can save the key as a file. </p>
<p class="answer"><b>Decrypt the Key</b></p>
<p class="answer"> In your m360Encrypt software, click on the Password Exchange tab. Paste the Cipher into the large
 bottom text box in the Receiver section. Click on the Decrypt button. The plain-text password should appear in the 
 small bottom text field. 
</p>
</li>

<li><p class="question">Step 4</p>
<p class="answer"><b>Copy the plain text password into the Messages tab to use it to encrypt messages.</b></p>
<p class="answer">With the password decrypted, use the eye econ beside the bottom field to reveal the plain-text password. Copy the plain-text password  by 
 highlighting the whole thing and pressing Ctrl + C on your keyboard. </p>
<p class="answer">Click on the Messages tab. Paste the plain-text password into the password text-field by 
 selecting the text-field and pressing Ctrl + V on your keyboard. </p>
</li>

<li>
<p class="question"> You are now ready to encrypt messages that only your communication partner can read </p>
<p class="answer" style="color:#f9faca"> <b>Note:</b> For detailed instructions on how to send messages see the "How To: Send Encrypted Messages" guide </p>
</li>
</ul>

</body></html>        
""".format(size, smallerSize)
        return body
        
    def genKeyPair(self, size):
        smallersize = size - 1
        body = """
 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
p,ul,li {{ font-size:{0}pt; font-weight:normal; margin:0,0,0,0; -qt-block-indent:0; text-indent:0px; white-space: pre-wrap; }}
.question {{font-weight:600; font-size: {0}pt;margin-top:12px;}} 
.answer {{font-size: {1}pt; margin-top:5px; -qt-block-indent: 1; text-indent: 12pt;}}
</style></head>

<body>
<p><span style="font-weight:600;">How to Generate a New Key Pair</span>
</p>
<p><span style="font=weight:350;">Key Pairs can be used if you need to exchange a password over open channels. Key Pairs generate
 a private key, and a correpsonding public key. Anyone with the public key can encrypt a message, but only the person with the private
 key can decyrpt it. However, the size of the message is limited by the size of the key. This makes Key Pairs, or Asymmetric Encryption,
 unsuitable for sharing long messages, but perfect for sharing a password over open channels. Then that password can be used
 to encrypt long messags. 
</p>
<ul>
<li><p class="question">Step 1 </p>
<p class="answer"><b>Click on the Load Key Pairs tab.</b><p>
</li>
<li><p class="question">Step 2 </p>
<p class="answer"><b>Click on the Generate Key Pair button</b></p>
</li>
<li><p class="question">Step 3 </p>
<p class="answer"><b>(optional) Click the checkbox next to "Save my Keys as files on my hard drive." </b></p>
<p class="answer" style="color:#f9faca;"><b>When to use this option : </b></p>
<p class="answer" style="color:#f9faca;">Choosing to save the files to your hard drive allows you to use them again. Often, people will choose to keep
 one key pair and use it for many things. They may make their public key available on their website, or as part of their
 email signature. This way they don't have to manage multiple keys. Anyone who wants to encrypt anything to them can use
 the single public key they provide, and only the private key holder can decrypt it. </p>
<p class="answer" style="color:#f9faca;">You may also want to save your files to your hard drive if there are long pauses or delays in the 
 converstation. Anything loaded into the current m360Encrypt session will be lost when you close the program. If you must wait 
 several hours or days for your partner to respond, you may want to save the keys to a file, 
 so that you can resume the process of exchanging a password after re-opening the software. 
<p class="answer" style="color:#f9faca;"> The drawback to saving your keys to your hard drive is that it is less secure. If your computer is stolen or 
 confiscated, someone may be able to recover and use your private key to decrypt messages that were sent to you encrypted with your 
 public key. </p>

<p class="answer"> <b>Select a save location and name</b> </p>
<p class="answer"> Use the Browse button to select a loction on your computer to save the files. In the following
 text box choose a name to append to your files so you can identify them in the future. </p>



<p class="answer"><b>(optional) Click the checkbox next to Save an SSH Foramt Copy</b> </p>
<p class="answer" style="color:#f9faca;"><b>When to use this option : </b></p>
<p class="answer" style="color:#f9faca;">Some software/services require you to authenticate by uploading your public key in SSH format. m360Encrypt 
 can use either SSH or PEM format files. The option to save as SSH is just for those wishing to use this software
 to generate keys that can be used outside this software. Check this box if you plan to use your same public key for other software
 or to authenticate to other 3rd party services.</p>
</li>



<li><p class="question">Step 4</p>
<p class="answer"><b>(optional) Check the boxes next to Load Public and Private key into m360Encrypt Session </b></p>
<p class="answer" style="color:#f9faca;"><b>When to use this option : </b></p>
<p class="answer" style="color:#f9faca;">If you plan on using your keys 
 for m360Encrypt, then you can choose to load the keys into your session. This saves you the extra step of having
 to locate and load the files you've just created. </p>
<p class="answer">Click on the checkboxes to load the public and private keys into your session </p>
</li>
<li>
<p class="question">Step 5</p>
<p class="answer"><b>Click on the Generate Keys button. </b><br />This will cause the software to generate the keys and 
(if selected) write the key files to your hard drive and (if selected) load the keys into text fields in the "Load Keys"
tab. </p>
<p class="answer">WARNING: This process can take several minutes, during which time the program will be unresponsive.</p>
</li>
</ul>
</body>
</html>       
        
""".format(size, smallersize)
        return body
        
        
    def encryptedNotes(self, size):
        smallersize = size - 1
        body = """
 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" />
<style type="text/css">
p,ul,li {{ font-size:{0}pt; font-weight:normal; margin:0,0,0,0; -qt-block-indent:0; text-indent:0px; white-space: pre-wrap; }}
.question {{font-weight:600; font-size: {0}pt;margin-top:12px;}} 
.answer {{font-size: {1}pt; margin-top:5px; -qt-block-indent: 1; text-indent: 12pt;}}
</style></head>
<body>
<p><span style="font-weight:600;">How to Create and Store Encrypted Notes</span>
</p>
<p><span style="font=weight:350;">Most encryption software works by making an encrypted copy of a file already saved on your computer. This means 
 that even if you encrypt a file, there was an un-encrypted version on your hard drive, and even if its been deleted or overwritten,
 software exists that can recover the unencrypted version. </p>
<br><p>This software allows you create notes in a window and encrypt them <b><i>before</i></b> they are written to
 your hard drive, so there is no unencrypted file that could be recovered. </p>
<p> The note can be saved as an encrypted file, and decrypted only when the correct password is in the password
 field. This can be used for your own private notes, to exchange encrypted files with someone, or to save passwords or keys that
 you might need to use again. </p>
<br><p style="color:#f9faca"><b>BE SURE TO REMEMBER THE PASSWORD</b> for your note or store it safely in a password vault. Without the correct password
your note CANNOT be recovered</p>
<br>
<p><b><u>To Create and Save an Encrypted File:</u></b></p>
<ul>
<li><p class="question">Step 1</p>
<p class="answer"><b>Click on the Encrypted Notes tab.</b> </p>
</li>
<li>
<p class="question">Step 2</p>
<p class="answer"><b>Put a password in the password text field at the top of the page. </b></p>
</li>
<li>
<p class="question">Step 3</p>
<p class="answer"><b>Type your note in the large text box.</b></p>
</li>
<li>
<p class="question"> Step 4 </p>
<p class="answer"><b>Click on the Encrypt &amp; Save button.</b></p>
<p class="answer"> When prompted, select a save location for your file.</p>
</li>
</ul>
<br>
<p><b><u>To Load an Encrypted File</u></b></p>
<ul>
<li>
<p class="question">Step 1</p>
<p class="answer"><b>Click on the Load Encrypted File button and select the file you want to load. </b></p>
<p class="answer">Your
 encrypted file contents will populate the text box<.</p>
</li>
<li>
<p class="question">Step 2</p>
<p class="answer"><b>Type the password into the password field at the top of the screen</b></p>
</li><li>
<p class="question">Step 3</p>
<p class="answer"><b>Click on the Decrypt button. </b> </p>
<p class="answer">If the password is correct, the contents of the text box window
will decrypt.</p>
</li>
</ul>


</body></html>
""".format(size,smallersize)
        return body