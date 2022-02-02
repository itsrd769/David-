from os import startfile
from time import sleep
from pyautogui import click
from keyboard import press
from keyboard import write

def WhatsappMsg(name,message):

    click(x=671, y=879)

    sleep(20)

    click(x=452, y=226)

    sleep(1)

    write(name)

    sleep(1)

    click(x=414, y=375)

    sleep(1)

    click(x=825, y=735)

    sleep(1)

    write(message)

    press('enter')

def WhatsCall(name):
   
    click(x=671, y=879)

    sleep(20)

    click(x=452, y=226)

    sleep(1)

    write(name)

    sleep(1)

    click(x=414, y=375)

    sleep(1)

    click(x=825, y=735)

    sleep(1)

    click(x=1156, y=183)

def WhatsChat(name):
    
    click(x=671, y=879)

    sleep(20)

    click(x=452, y=226)

    sleep(1)

    write(name)

    sleep(1)

    click(x=414, y=375)

    sleep(1)

    click(x=825, y=735)

    sleep(1)

