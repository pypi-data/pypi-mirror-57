from os              import remove
from random          import randint
from subprocess      import call
from hackpy.info     import *
from hackpy.settings import *

class command:
    ##|
    ##| Execute system command : hackpy.command.system('command')
    ##| Execute system command : hackpy.command.hiddenSystem('command')
    ##| Execute nircmdc command: hackpy.command.nircmdc('command')
    ##|
    def system(recived_command):
        return call(recived_command, shell = True)

    def hiddenSystem(recived_command):
    	vbs_path = module_location + r'\tempdata\systemCommand-' + str(randint(1, 99999)) + '.vbs'
    	with open(vbs_path, 'w') as file:
    		file.write('''
set ws = wscript.createobject(\"WScript.shell\")
ws.run(\"''' + recived_command + '''\"), 0, true''')
    	command.system(vbs_path)
    	remove(vbs_path)

    def nircmdc(recived_command):
        return command.system(module_location + r'\executable\nircmd.exe ' + recived_command + devnull)

