try:
    import checkfiles as check

    #print('Checking folders...')
    check.checktree()

    print('Checking file integrity...')
    check.checkfiles()
except:
    print('ERROR FAILED TO IMPORT LETHAL MODULES CHECK YOUR FILES')
    print('LAUNCH REQUIRED.SH IF THAT DOESNT FIX IT DOWNLOAD THIS FILE:')
    print('https://raw.githubusercontent.com/supopur/SPVR/main/checkfiles.py')
    print('AND PUT IT IN THE MAIN DIRECTORY')
    print('MODULES POTENTIALY MISSING:')
    print('checkfile.py')
import configparser
from datetime import datetime
#import pyjokes
from googletrans import Translator as translator
#import random
import linecache
from os.path import exists
from colorama import Fore, Style
from os import popen
from sys import path
#import the gui:
path.insert(0, 'asciigui/')
import asciigui as gui
import voicestuff as vs
import signal
#import keyboard

def main(vtipn : float = 0):
    #settings stuff
    conf = configparser.ConfigParser()
    conf.read('conf.ini')
    
    if not exists('conf.ini'):
        print(Fore.RED + "[EXCEPTION]: Config file doesn't. Please download it from: https://raw.githubusercontent.com/supopur/SPVR/main/conf.ini", Style.RESET_ALL)
        download = input("Do you want to download it Y/n: ")
        download = download.lower()
        if download == '' or download == 'y':
            print(popen("wget https://raw.githubusercontent.com/supopur/SPVR/main/conf.ini").read())
            #return 0
        else:
            return 0

    

    
    jokefile = conf['jokes']['jokefile']
    joken = conf['jokes']['jokenumber']
    joken = int(joken)
    
    rlang = conf['recognizer']['lang']
    ambient = conf['recognizer']['adjust_ambient']
    ambient = float(ambient)
    
    ttslang = conf['tts']['deflang']
    ttsdir = conf['tts']['dirname']

    

    
    #confsoup = [jokefile, joken, rlang, ambient, ttslang, ttsdir, ttsncache]
    #print(confsoup)
    gui.clear()
    gui.artg('Mluv    do  microfonu')
    text = vs.recognize()
    gui.clear()
    gui.wait('Cekej...')
    print('Toto je print z funkce "main"', str(text))
    print(text)
    if 'se máš' in text:
        print('main: "jak se máš" recognized')
        output = 'mám se, dobře a co ty'
        print('Input: ', text, ' Output: ', output)
        
        vs.TTS(output, output, ttslang, ttsdir)
    elif 'funguješ' in text:
        print('main: "fungujes" recognized')
        output = 'když zmáčkneš tlačítko tak se do počítače pošle signál aby poslouchal, počítač nahraje zvukovou stopu a pak ji pošle do serverů googlu aby se řeč převedla na text, Pak google pošle zpět text (string), program se podívá jestli je tento text v databázi, Pokud je tak přes google překladač převede odpověď z textu do zvuku, A pak ten převedený text přehraje'
        print('Input: ', text, ' Output: ', output)
        vs.TTS(output, 'jak fungujes')
    elif 'čas' in text or 'hodin' in text or 'minut' in text:
        print('main: "cas" recognized')
        timed = datetime.now()
        time = timed.strftime("právě je %H hodin a %M minut")
        vs.TTS(time, 'time')
    elif 'slyšíš' in text:
        print('main: "slysis" recognized')
        vs.TTS('Ano pořád tě poslouchám, ha, ha, ha, pořád tě slyším')
    elif 'jmenuješ' in text:
        print('main: "jmenujes" recognized')
        vs.TTS('jmenuji se, aah, no, hele, já ani nevím')
    elif "atrakce" in text or "zábava" in text or "projekty" in text or "projekt" in text:
        print('main: "atrakce" recognized')
        with open('projekty.txt', 'r') as f:
            projekty = f.read()
            print(projekty, 'projekty')
        vs.TTS(projekty, 'projekty')
    elif 'vtip' in text:
        print('main: "vtip" recognized')
        try:
            vtipn
        except NameError:
            print("Setting joke number to 1...")
            vtipn = 1
        else:
            if not vtipn == 14:
                vtipn += 1
                print('Adding 1 to vtipn')
            else:
                print('Resetting jokenumber...')
                vtipn = 1
                

        print(vtipn)
        vtip = linecache.getline('vtipy.txt', vtipn)
        print(vtip)
        agree = input(f'Chose this joke: number: {vtipn}, {vtip} \n press Enter to continue or write jokenumber: ')
        if agree == '':
            pass
        elif not agree == '':
            agree = int(agree)
            vtipn = agree
            vtip = linecache.getline('vtipy.txt', vtipn)
        vs.TTS(vtip, 'joke')
        return vtipn
    elif 'stop' in text:
        print('main: "Stop" recognized')
        try:
            print('Stopping')
            return 'stop'
        except:
            print('Stopping failed...')
            
    elif 'co je' in text:
        print('main: "co je" recognized')
        if 'google' in text:
            vs.TTS('Google je google')
        elif 'databáze' in text:
            vs.TTS('databáze je list hodnot')
        elif 'string' in text or 'spring' in text or 'strike' in text or 'strange' in text or 'stream' in text:
            vs.TTS('String je hodnota textu v počítačovém programu')
        else:
            vs.TTS('Jak já to mám vědět')
    elif 'zajímavé' in text:
        vs.TTS('velmi')
    elif 'umíš' in text:
        vs.TTS('Všechny příkazy: vtip, jaké jsou tady projekty, jak se jmenuješ,jak se máš, kolik je hodin, jak funguješ', 'commands')
    elif 'mám' in text and 'dobře' in text:
        vs.TTS('tak to je dobře')
    elif 'mám' in text and 'blbě' in text:
        vs.TTS('tak to je špatně, a proč')
    elif 'to je dobré' in text or 'to je super' in text or 'to je docela dobré' in text or 'to je docela super' in text:
        vs.TTS('To teda je')
    elif 'nevím' in text:
        vs.TTS('To já také ne')
    elif 'co jsi' in text:
        vs.TTS('Já jsem hlasový asistent')
    else:
        vs.TTS('Omlouvám se ale nerozumněl jsem, Nebo tato věta není v mé databázy')

if __name__ == '__main__':
    try:
        vtip = 0
        while True:
            #keyboard.on_press_key("r", lambda _:main(1))
            vtip = main(vtip)
            if vtip == 'stop': break
    except:
        gui.clear()
        gui.error("OOOPS    NECO   SE    POKAZILO")