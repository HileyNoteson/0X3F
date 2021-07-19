import time
import random
import os
import secrets
import sys
from termcolor import colored, cprint
from shutil import copyfile
from datetime import datetime
os.system('cls')
userinput = ""
commandlist = ["!stop","!start","!clear","!addons"]
loadseq = ["[        ]","[#       ]","[##      ]","[###     ]","[####    ]","[#####   ]","[######  ]","[####### ]","[########]"]
loadnum = 0
while 1==1:
    tempinput = input("input:")
    if tempinput == commandlist[0]:
        print("ok")
    if tempinput == commandlist[1]:
        os.system('cls') 
        while loadnum <= 8:
            print(loadseq[loadnum])
            time.sleep(random.randint(0, 1))
            os.system('cls')
            loadnum = loadnum + 1
        loadnum=0 
        begin = input("do you want to begin? [y or n]") 
        if begin == "y":
            os.system('cls')
            baseoptions = ["!install","!login"]
            print("##########################")
            print(colored("Welcome to the 0x3F System","green"))
            print("")
            print("You can use the following commands. Most require a login token.")
            print(baseoptions)
            loadtoken = open("D:\Documents\pythonos\login.token", "r")
            auth = list(loadtoken.read())
            loadtoken.close()
            user = input(colored("enter your id:","blue"))
            key = input(colored("enter log-off key:","blue"))
            auth = loadtoken
            print("")
            time.sleep(1)
            print("logging in")
            print(colored("generating next logoff key","cyan"))
            nextkey = secrets.token_hex(8)
            print(nextkey)
            time.sleep(1)
            input(colored("have you recorded your logoff key in a secure location?","red") + "   [any key(s)]")
            os.system('cls')
            nextkey = ""
            token = [datetime.now().time(),user,key,nextkey]
            loadtoken = open("D:\Documents\pythonos\login.token", "w")
            loadtoken.write(str(token))
            loadtoken.close()
            print(colored("done","green"))
            time.sleep(1)
            os.system('cls')
            print("cleaning login process")
            begin = ""
            login = ""
            key = ""
            print(colored("done","green"))
            time.sleep(1)
            print(colored("generating next logoff key","cyan"))
            nextkey = secrets.token_hex(8)
            print(nextkey)
            time.sleep(1)
            input(colored("have you recorded your logoff key in a secure location?","red") + "   [any key(s)]")
            os.system('cls')
            nextkey = ""
            time.sleep(1)
            filesystem = r"D:\Documents\pythonos"
            begin = input(colored("do you want to try to install/update the core filesystem?", "cyan") + "   [y or n]")
            if begin == "y":
                if not os.path.exists(filesystem):
                    os.makedirs(filesystem)
                copyfile(__file__,"D:\Documents\pythonos\source.py")
