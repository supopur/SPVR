#NO DO NOT TOUCH THIS IT WORKS AND THAT IS FINE OK
#IF YOU DARE TOUCH THIS CODE YOU WILL GO TO HELL
import os
import pathlib
def main():
    path = pathlib.Path('main.py').parent.absolute()
    #we shall store all the file names in this list
    filelist = []
    files2 = ['/main.py', '/voicestuff.py', '/vtipy.txt', '/projekty.txt', '/conf.ini', '/MBinteract/mbinteract.py', '/MBinteract/strwash.py', '/gui/gui.py', '/gui/activate.jpg', '/gui/reloading.jpg', '/gui/yn.jpg', '/gui/wait.svg', ]
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
                if miss in ['gui.py', 'activate.jpg', 'reloading.jpg', 'wait.svg', 'yn.jpg']:
                    command = 'wget https://raw.githubusercontent.com/supopur/SPVR/main/gui/' + miss
                elif miss in ['mbinteract.py', 'strwash.py']:
                    command = 'wget https://raw.githubusercontent.com/supopur/SPVR/main/MBinteract/' + miss
                elif miss in files2:
                    command = 'wget https://raw.githubusercontent.com/supopur/SPVR/main/' + miss
                else:
                    run = False
                if run:
                    print(os.popen(command).read())
