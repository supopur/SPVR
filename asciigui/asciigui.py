from art import *
from os import popen

def artg(text : str):
    thing = text2art(text)
    print(thing)
    thing = art("gimme", 10)
    print(thing)

def clear():
    popen('clear')

if __name__ == "__main__":
    artg('Zmackni    tlacitko \nA \nna \nmicrobitu')
