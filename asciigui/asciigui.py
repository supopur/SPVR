from art import *
from os import system


def artg(text : str):
    thing = text2art(text)
    print(thing)
    thing = art("gimme", 10)
    print(thing)
def error(text : str):
    text = text2art(text)
    print(text)
    text = art("angry troll", 10)
    print(text)
def wait(text : str):
    text = text2art(text)
    print(text)
    text = art("cassette2", 5)
    print(text)

def clear():
    system('clear')

if __name__ == "__main__":
    artg('Zmackni    tlacitko \nA \nna \nmicrobitu')
