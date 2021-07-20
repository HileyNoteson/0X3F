import hashlib
login = input("login")
password = input("password")
loginfo = bytearray(login+password,'utf-8')
password = ""
login = ""
newhash = hashlib.sha224(loginfo).hexdigest()
print(newhash)
loginfo = ""
newhash = ""