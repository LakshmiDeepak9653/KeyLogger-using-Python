from cryptography.fernet import Fernet
keys_information_e = "Key-log_E.txt"
system_information_e = "system_E.txt"
clipboard_information_e = "clipboard_E.txt"
keys_information ="Key-log.txt"
system_information = "system-info.txt"
clipboard_information = "clipboard.txt"
Cryptokey = "KEY.txt"

filepath = "//home//kali//Desktop//WW mk1//"
with open(filepath+Cryptokey,'rb') as f:
    key=f.read()
    fernet=Fernet(key)

def Decrypt_file(files_E,files_D):
    files_E1 = filepath+files_E
    files_D1 = filepath+files_D
    with open(files_E1,'rb') as f:
        encrypted = f.read()
    decrypted=fernet.decrypt(encrypted)
    with open(files_D1,'wb') as f:
        f.write(decrypted)
    print("Decrypted 👍",files_E,"\tTO\t",files_D)


Decrypt_file(keys_information_e,keys_information)
Decrypt_file(system_information_e,system_information)
Decrypt_file(clipboard_information_e,clipboard_information)
