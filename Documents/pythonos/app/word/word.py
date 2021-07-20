import time
import random
import os
import secrets
import sys
from termcolor import colored, cprint
from shutil import copyfile
from datetime import datetime
from typing import Collection
commandlist = ["!install","!start","!clear","!exit"]
print("hi")
print(__file__)
while 1==1:
    tempinput = input("readerinput:")
    if tempinput == commandlist[0]:
        input("if you run !install from an app launched through the appinit script it will be overwritten with it.\nyou must run apps manually to install/fix filesystem. press any key to continue")
        dir1 = r"D:\Documents\pythonos\app\word"
        try:
            os.makedirs(dir1)
        except:
            print()
        finally:
            copyfile(__file__,"D:\\Documents\\pythonos\\app\\word\\word.py")
    if tempinput == commandlist[2]:
        os.system("cls") 
    if tempinput == commandlist[1]:
        print(colored("starting file reader","cyan"))
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir('D:\Documents\pythonos\\virtual drives\documents') if isfile(join('D:\Documents\pythonos\\virtual drives\documents', f))]
        print(onlyfiles)
        filetoopen = input("what file do you want to open?  ")
        print("opening ",filetoopen)
        time.sleep(1)
        os.system('cls')
        try:
            f = open('D:\Documents\pythonos\\virtual drives\documents'+'\\'+ filetoopen, "r")
            for x in f:
                print(x) 
        except:
            print("file not found")
        finally:
            f.close
    if tempinput == commandlist[3]:
        exec(open('D:\Documents\pythonos\\boot.py').read())