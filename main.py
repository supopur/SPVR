import voicestuff as vs
from datetime import datetime
#import pyjokes
from googletrans import Translator as translator
import random
import linecache


def main(vtipn : float = 0):
    text = vs.recognize()
    print('Toto je print z funkce "main"', str(text))
    print(text)
    if 'se máš' in text:
        print('main: "jak se máš" recognized')
        output = 'mám se, dobře a co ty'
        print('Input: ', text, ' Output: ', output)
        vs.TTS(output)
    elif 'funguješ' in text:
        print('main: "fungujes" recognized')
        output = 'když zmáčkneš tlačítko tak se do počítače pošle signál aby poslouchal, počítač nahraje zvukovou stopu a pak ji pošle do serverů googlu aby se řeč převedla na text, Pak google pošle zpět text (string), program se podívá jestli je tento text v databázi, Pokud je tak přes google překladač převede odpověď z textu do zvuku, A pak ten převedený text přehraje'
        print('Input: ', text, ' Output: ', output)
        vs.TTS(output, 'jak fungujes')
    elif 'čas' in text or 'hodin' in text or 'minut' in text:
        print('main: "cas" recognized')
        time = datetime.now()
        hrs = time.strftime("%H")
        min = time.strftime("%M")
        output = f'Právě je {hrs} hodin a {min} minut'
        vs.TTS(output, 'time')
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
            if not vtipn == 10:
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
        vs.TTS('Já jsem halsový asistent')
    else:
        vs.TTS('Omlouvám se ale nerozumněl jsem, Nebo tato věta není v mé databázy')

if __name__ == '__main__':
    vtip = 0
    while True:
        try:
            vtip = main(vtip)
            if vtip == 'stop':
                break
        except:
            break
