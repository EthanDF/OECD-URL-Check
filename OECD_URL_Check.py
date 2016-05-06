__author__ = 'fenichele'

import urllib
from urllib import request
from urllib import error

urlFiles = 'OECD_URLs.txt'

def readURLList():

    uL = []
    with open(urlFiles, 'r') as x:
        urlList = x.readlines()
        for u in urlList:
            uL.append(u.strip('\n'))

    return uL

def checkURL(url):

    checkText = 'You or your institution have access to this content'
    try:
        with urllib.request.urlopen(url) as r:
            if checkText in r.read().decode('utf-8'):
                pass
            else:
                print("\turl problem with\n"+url)
    except error.HTTPError:
        print("\turl problem with\n" + url)

def runIt():

    counter = 0
    urls = readURLList()
    for u in urls:
        counter += 1
        print('record: '+str(counter))
        checkURL(u)

    print ('done!')

runIt()
