# Run As root
# Setting Bing Picture As Desktop Picture!
import os
import time
import urllib.request
import json

def DownloadPicuture():
    ImageUrl, FilePath = GetImageUrl()
    with open(FilePath, 'wb') as file:
        try:
            ReqImage = urllib.request.Request(ImageUrl)
            Responseimage = urllib.request.urlopen(ReqImage).read()
        except TimeoutError:
            print(time.ctime() + ' TimeOut')
        except:
            exit(0)
        file.write(Responseimage)
    print(time.ctime() + "  The picuture has been saved to " + FilePath)
    return FilePath

def MakeFileFolder():
    path = os.environ['HOME'] + '/Pictures/Bing_Pictures/'
    try:
        os.mkdir(path)
        print(time.ctime() + "  The file folder \"" + path + "\" has been set up!")
    except FileExistsError:
        pass
    return path

def GetImageUrl():
    path = MakeFileFolder()
    url = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=' + str(time.time()).replace('.', '')[:13] + '&pid=hp&ensearch=1&FORM=BEHPTB&video=1&quiz=1&fav=1'
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req).read().decode("utf-8")
    ImageUrl = 'http://www.bing.com' + json.loads(response)['images'][0]['url']
    FilePath = path + ImageUrl.split('/')[-1]
    return ImageUrl, FilePath

def SetDesktop():
    FilePath = DownloadPicuture()
    command = 'osascript -e "tell application \\\"Finder\\\" to set desktop picture to POSIX file \\\"' + FilePath + '\\\"\"'
    try:
        os.system(command)
        print(time.ctime() + "  The desktop picture has been set up!")
    except:
        print(time.ctime() + '  There is something wrong!')
        exit(0)

if __name__ == '__main__':
    SetDesktop()