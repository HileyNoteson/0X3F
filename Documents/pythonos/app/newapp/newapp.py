import os
from shutil import copyfile
commandlist = ["!install","!start","!clear"]
print("hi")
print(__file__)
while 1==1:
    tempinput = input("newappinput:")
    if tempinput == commandlist[0]:
        input("if you run !install from an app launched through the appinit script it will be overwritten with it.\nyou must run apps manually to install/fix filesystem. press any key to continue")
        dir1 = r"D:\Documents\pythonos\app\newapp\subdir"
        try:
            os.makedirs(dir1)
        except:
            print()
        finally:
            copyfile(__file__,"D:\\Documents\\pythonos\\app\\newapp\\newapp.py")
    if tempinput == commandlist[2]:
        os.system("cls") 
    if tempinput == commandlist[3]:
        exec(open('D:\Documents\pythonos\\boot.py').read())
