#NO DO NOT TOUCH THIS IT WORKS AND THAT IS FINE OK
#IF YOU DARE TOUCH THIS CODE YOU WILL GO TO HELL
import os
import pathlib

def checktree(reqdir : list = ['gui', 'MBinteract', 'assets']):
    print('Checking directory tree...')
    required_dir = reqdir
    directories = os.listdir()
    missing = []
    
    for dir in required_dir:
        if not dir in directories:
            print(f'Missing file: {dir}')
            missing.append(dir)
        else:
            print(f'{dir} ok...')
    if not missing == []:
        print(missing)
        yn = input('Folders are missing do you want to make them? (Y/n): ')
        yn = yn.lower()
        if yn == '' or 'y':
            print('Downloading files...')
            for miss in missing:
                os.popen(f'mkdir {miss}')

def checkfiles():
    path = pathlib.Path('main.py').parent.absolute()
    #we shall store all the file names in this list
    filelist = []
    #you can touch this list "files2"
    files2 = ['/main.py', '/voicestuff.py', '/vtipy.txt', '/projekty.txt', '/conf.ini', '/MBinteract/mbinteract.py', '/MBinteract/strwash.py', '/gui/gui.py', '/gui/activate.jpg', '/gui/reloading.jpg', '/gui/yn.jpg', '/gui/wait.svg', ]
    #NOW DONT TOUCH ANYTHING
    missing = []

    filelist2 = []

    for root, dirs, files in os.walk(path):
        for file in files:
            #append the file name to the list
            
            filelist.append(os.path.join(root,file))

    for file in filelist:
        file = file.replace(str(path), '')
        filelist2.append(file)

    for list in files2:
        if not list in filelist2:
            print(f"Missing file {list}")
            missing.append(list)
        else:
            print(f"{list} ok...")
                    
    if not missing == []:
        print(missing)
        yn = input('Files are missing do you want to donwload them? (Y/n): ')
        yn = yn.lower()
        if yn == '' or 'y':
            print('Downloading files...')
            for miss in missing:
                run = True
                print(miss)
                if miss in ['/gui/gui.py', '/gui/activate.jpg', '/gui/reloading.jpg', '/gui/wait.svg', '/gui/yn.jpg']:
                    print('File is in gui folder')
                    command = 'wget -P gui/ https://raw.githubusercontent.com/supopur/SPVR/main' + miss
                    print(command)
                elif miss in ['/MBinteract/mbinteract.py', '/MBinteract/strwash.py']:
                    print("File is in MBInteract folder")
                    command = 'wget -P MBinteract/ https://raw.githubusercontent.com/supopur/SPVR/main' + miss
                elif miss in files2:
                    print(f"File is in the main folder")
                    command = 'wget https://raw.githubusercontent.com/supopur/SPVR/main/' + miss
                else:
                    run = False
                if run:
                    print(os.popen(command).read())
if __name__ == '__main__':
    checktree()
    checkfiles()