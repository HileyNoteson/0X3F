import time
import random
import os
import secrets
import sys
import hashlib
import os.path
import getpass
from os import listdir
from os.path import isfile,join
from termcolor import colored, cprint
from shutil import copyfile
from datetime import datetime
os.system('cls')
token = open("D:\Documents\pythonos\login.token",'r')
tolken = token.read()
login = input("login: ")
password = getpass.getpass()
loginfo = bytearray(login+password,'utf-8')
password = ""
login = ""
newhash = hashlib.sha224(loginfo).hexdigest()
loginfo=""
token.close()
if newhash == tolken:
    print("login successful")
    storedhash = ""
    tolken = ""
    token = ""
    os.system('cls')
    userinput = ""
    commandlist = ["!update","!start","!clear","!addons"]
    loadseq = ["[        ]","[#       ]","[##      ]","[###     ]","[####    ]","[#####   ]","[######  ]","[####### ]","[########]"]
    loadnum = 0
    while 1==1:
        tempinput = input("input:")
        if tempinput == commandlist[1]:
            os.system('cls') 
                #while loadnum <= 8:
               #print(loadseq[loadnum])
                #time.sleep(random.randint(0, 1))
                #os.system('cls')
                #loadnum = loadnum + 1
            loadnum=0 
            exec(open('D:\Documents\pythonos\\app\\appinit.py').read())
        if tempinput == commandlist[0]:
                filesystem = r"D:\Documents\pythonos"
                begin = input(colored("do you want to try to install/update the core filesystem?", "cyan") + "   [y or n]")
                if begin == "y":
                    if not os.path.exists(filesystem):
                        os.makedirs(filesystem)
                    copyfile(__file__,"D:\Documents\pythonos\\boot.py")
                if begin == "n":
                    print("cancelled!")