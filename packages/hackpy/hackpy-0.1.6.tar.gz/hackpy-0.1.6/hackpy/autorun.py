from os import remove, environ, getenv
from os import path as os_path
from hackpy.settings import *

class autorun:
    def __init__(self, path):
        self.path = os_path.dirname(os_path.realpath(path))
        self.file = path.split('\\')[-1]
        self.name = self.file.split('.')[0]
        self.autorunDirPath = (environ['SystemDrive'] + '\\Users\\' + getenv('USERNAME') + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        self.autorunBatPath = (module_location  + '\\tempdata\\' + self.name + '.cmd')
        self.autorunVbsPath = (self.autorunDirPath + '\\' + self.name + '.vbs')
    
    # Add file to startup
    def install(self):
        if os_path.isfile(self.path + '\\' + self.file):
            if (self.file.endswith('.py') or self.file.endswith('.pyw')):
                execute = 'python '
            else:
                execute = 'start \"\" '
            # Write batch script
            with open(self.autorunBatPath, 'w', encoding = "utf8", errors = 'ignore') as tempfile:
                tempfile.write(
                    '@echo off'       + '\n' +
                    'chcp 65001'      + '\n' +
                    'cd ' + self.path + '\n' +
                    ''    + execute   + self.file
                )
            # Write VBS script
            with open(self.autorunVbsPath, 'w', encoding = "utf8", errors = 'ignore') as tempfile:
                tempfile.write(
                    'wscript.createobject(\"WScript.shell\")' + 
                    '.run(\"' + self.autorunBatPath + '\"), 0, true'
                )

            print(self.autorunVbsPath)
            print(self.autorunBatPath)
            return os_path.exists(self.autorunVbsPath and self.autorunBatPath)
        else:
            return False

    # Delete file from startup
    def uninstall(self):
        try:
            remove(self.autorunVbsPath)
            remove(self.autorunBatPath)
        except:
            return False
        return not os_path.exists(self.autorunBatPath and self.autorunVbsPath)