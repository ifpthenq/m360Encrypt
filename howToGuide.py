
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
<p class="answer"> You and the person you are communicating with both need to be running m360Encrypt on your computers. </p>
</li>

<li>
<p class="question"> Step Two </p>
<p class="answer"> You and your partner need to agree on a secure password
 <br />&nbsp; &nbsp; &nbsp;The password can be up to 117 characters and should be at least 30 characters
 <br />&nbsp; &nbsp; &nbsp; <b>Note:</b> For help with exchanging passwords, see "How to : Securely Exchange a Password" in this guide 
</p>
</li>

<li>
<p class="question"> Step Three </p>
<p class="answer"> On the "Messages" Tab, type or paste your password into the "Password" text field</p>
</li>

<li>
<p class="question"> Step Four </p>
<p class="answer"> Type your message into the text field, and press the Encrypt button</p>
</li>

<li>
<p class="question"> Step Five </p>
<p class="answer"> Copy the encrypted text and paste it into your email, chat, social media, or whatever software you are using to communicate with your partner</p>
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
<p class="answer">You and the person you are communicating with both need to be running m360Encrypt on your computers.
</p>
</li>

<li><p class="question">Step 2</p>
<p class="answer">You need to get your partner's <b>public</b> key. </p>
<p class="answer"> They can share their public key with you via email, chat, social media, post it on a website - 
any way that normally communicate. It's OK if other people see their public key. 
</p>
</li>

<li>
<p class="question">
Step 3
</p>
<p class="answer">Put your partner's public key in the bottom textbox on the "Load KeyPairs" tab. </p>
<p class="answer">If you copied the public key to your clipboard, you can paste it into the textbox</p>
<p class="answer">If you received the key as a file, you can click on the Select button and select the file, and
m360Encrypt will import it for you into the textbox. 
<p class="answer">It's OK to have the private key box (the top textbox) be blank. You don't need it</p>
<p class="answer">Once the Public Key appears in the box, click on the Load Keys button </p>

<p class="answer"><b>Troubleshooting</b><br />
If you get an error message when you click the Load Keys button it is because the key is not the right format. 
A public key should start with "-----BEGIN PUBLIC KEY-----" or "ssh-rsa"
The file type will be a .txt file, .PUB, or .PEM. All of these can be opened in a text editor like Notepad
so that you can verify the key starts with the correct header. <br />
If the key is not able to load, try re-copying the key, or ask your partner to generate and send a new key. 
</p>
</li>

<li>
<p class="question">Step 4</p>
<p class="answer"> Go to the "Password Exchange" tab. </p>
<p class="answer"> You will need to create a very long password or passphrase. It should be more than 30 characters, but less than 117. </p>
<p class="answer"> Put your password in the top text field on the PasswordExchange Tab. </p>
<p class="answer"> Click on the "Encrypt" button. 
<p class="answer"> You should now see a cipher of your password in the second text box. A cipher is encrypted text that looks
like random unreadable characters. The cipher will always have 1024 characters, regardless of how long or short the password is. 
</p>
</li>

<li>
<p class="question">Step 5</p>
<p class="answer">You need to get the ciper to the person you are trying to communicate with.</p>
<p class="answer">Highlight the whole thing and press Ctrl+C to copy it. Use Ctrl + V to paste it in any software you regularly use for communication (email, chat, social media, etc), and
send it to your partner. 

</p>

</li>

<li>
<p class="question">Step 6</p>
<p class="answer">You will need to use the <b>plain-text password</b> (not the cipher) to encrypt messages
for your partner. </p>
<p class="answer"> Click on the eye symbol next to the password field to reveal the plain-text password. Highlight the whole thing
and press Ctrl + C to copy it. </p>
<p class="answer">Go to the "Messages" Tab. Click into the Password field and then press Ctrl + V on your keyboard
to paste the password into the field. </p>
</li>

<li>
<p class="question"> You are now ready to encrypt messages that only your communication partner can read </p>
<p class="answer"> <b>Note:</b> For detailed instructions on how to send messages see the "How To: Send Encrypted Messages" guide </p>
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

</ul>

</body></html>        
""".format(size, smallerSize)
        return body