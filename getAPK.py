import glob, os
import json
from pprint import pprint
from model import Model
import time
path = './LIST1/googleplay'
data = Model()
index = 0
def checkAPK(index):
    global path
    global data
    after = data.getAppId(100,index)
    before = dict ([(f, None) for f in os.path.dirname(path)])
    added = [f for f in after if not f in before]
    return added
def downloadAPK(idApp):
    global path
    os.system("gplaycli -d "+idApp +" -f "+ path+ " --progress")

def main():
    global index
    while True:
        listAPK = checkAPK(index)
        if listAPK:
            i = 0
            for x in listAPK:
                print '////Dowloading/// ' + str(x) + ' /// ' + str(index +i)
                downloadAPK(str(x))
                i = i + 1
        index = index + 100
        time.sleep(1)

if __name__ == '__main__':
    main()
