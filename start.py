# Init the program
import os, sys

def MoveFile():
    user = GetUsers()
    path = '/Users/' + user + '/'
    os.rename('./BingPicture.py', path + "BingPicture.py")
    return user, path

def GetUsers():
    import getpass
    user = getpass.getuser()
    print("Thanks for using the Script，" + user + '!')
    return user

def Crontab( user,path, FileName = 'BingPicture.py'):
    PythonPath = GetPythonPath()
    CrontabFile = "*/20 * * * * " + PythonPath + " " + path + FileName + ' >> ' + path + FileName.replace('.py', '.log') + ' 2>&1'
    with open('./.cron', 'w') as file:
        file.write(CrontabFile)
    CrontabCommand = 'sudo crontab -u ' + user + ' ./.cron'
    os.system(CrontabCommand)
    os.system('sudo crontab -u ' + user + ' -e')

def last():
    os.remove('./.cron')

def GetPythonPath():
    return sys.executable

def main():
    user ,path = MoveFile()
    Crontab(user, path)
    last()

if __name__ == '__main__':
    main()