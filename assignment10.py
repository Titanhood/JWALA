#question_1
import time
day=time.asctime()
print(day)
#question_2
import webbrowser
url = 'https://www.youtube.com/'
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
#question_3
import os
z=os.listdir()
for i in range(1,len(z)-1):
    z[i],ext=os.path.splitext(z[i])
    os.rename(z[i]+'.txt',z[i]+'(new).jpg')
print(z)
