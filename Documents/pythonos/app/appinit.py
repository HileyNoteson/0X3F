from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("D:\\Documents\\pythonos\\app") if isfile(join("D:\\Documents\\pythonos\\app", f))]
while 1==1:
    print(onlyfiles)
    apptolaunch = input("what app do you want to launch?  ")
    print(apptolaunch)
    try:
        exec(open('D:\\Documents\\pythonos\\app'+'\\'+ apptolaunch).read())
        exit
    except:
        print("app not found")