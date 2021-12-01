import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from os.path import exists
from colorama import Fore, Style
from os import mkdir

r = sr.Recognizer()

def TTS(text : str = 'oops žádný vstup textu', filename : str = '', lang : str = 'cs', play : bool = True, ctx : str = ''):
    print(ctx)
    if not exists("sound"):
        try:
            mkdir("sound")
        except:
            print("VoiceStuff: Error could not make directory sound")
    if filename == '':
        filename = text
        print(f'VoiceStuff: Chagin filename to {filename}.mp3')
    else:
        print(f'VoiceStuff: Filename is {filename}.mp3')
    tts = gTTS(text, lang = lang)
    if True:
        try:
            if filename == 'joke' or filename == 'jak fungujes' or filename == 'commands':
                raise Exception("File doesn't exist")
            else:
                location = 'sound' + '/' + filename + '.mp3'
                playsound(location)
        except:
            print('VoiceStuff: Plaing sound from cache failed')
            try:
                location = 'sound' + '/' + filename + '.mp3'
                print('VoiceStuff: Saving speech to: ' + location)
                tts.save(location)
                print('VoiceStuff: Plaing speech from: ' + location)
                playsound(location)
            except:
                print(Fore.RED + '[EXCEPTION]VoiceStuff: Unable to save and play the speech', Style.RESET_ALL)
                pass
        else:
            print('VoiceStuff: Plaing sound from cache was successful')

            


def recognize():
    with sr.Microphone() as source2:
        
        #noise canceling
        r.adjust_for_ambient_noise(source2, duration = 0.5)

        audio2 = r.listen(source2)

        text = r.recognize_google(audio2, language = 'cs-CZ')
        text = text.lower()
        print('Google recongized you said:', text)
        text = str(text)
        return text

if __name__ == '__main__':
    recognize()