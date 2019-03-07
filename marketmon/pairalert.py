#!/usr/bin/python3.5
# 
#

import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui
import threading
import socket
from pygame import mixer
mixer.init()
alert=mixer.Sound('/home/pi/Downloads/Bell.wav')

TIC1 = 0
TIC2 = 1
SHARES1 = 2
PRICE1 = 3
CLS1 = 4
SHARES2 = 5
PRICE2 = 6
CLS2 = 7
THRE = 8  # Threshold price 


#    tic1   tic2  SHARES1 PRICE1 CLS1 SHARES2 PRICE2 CLS2 THRE
pairArr = [

["EEM", "MCHI", 293, 42.715, 0.0, -200, 62.35, 0.0, -10.00],

]

#pairArr[order(pairArr[:,7], decreasing = TRUE),]
#pairArr.sort(key=lambda row: row[6:], reverse=True)
import pprint 
#pprint.pprint(pairArr)



# start gui
win = tki.Tk()
#########




win.title("Pair Alert")
#myFont = tkinter.font.Font(family = 'Piboto Condensed', size = 24, weight = "bold")
myFont = tkinter.font.Font(family = 'Liberation Mono', size = 24, weight = "bold")

labelLeftTop = tki.Label(win,justify="right", width="25", height = "10",bg = "#001F3F",fg = "OliveDrab1")
labelLeftTop.pack()
labelRightTop = tki.Label(win,justify="right", width="25", height = "10",bg = "#001F3F",fg = "OliveDrab1")

labelLeftTop['font'] = myFont
labelRightTop['font'] = myFont

labelLeftTop.grid(row =0 ,column=0,sticky='nsew')

labelRightTop.grid(row =0 ,column=1,sticky='nsew')


win.grid_columnconfigure(0,weight=1)
win.grid_columnconfigure(1,weight=1)
win.grid_rowconfigure(0,weight=1)


NoIP = True

def get_ip():
    global NoIP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        NoIP = False
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


s = get_ip()
if NoIP:
    lStr = "NO IP"
    rStr = "ADDRESS"
else:
    list =  (s.split('.'))
    lStr = list[0] + '.' + list[1]
    rStr = list[2] + '.' + list[3]
    if (len(rStr)) < 7:
        rStr = '.' + rStr
 




labelLeftTop["text"] = lStr + "\nUDPport\nticker"
labelRightTop["text"] = rStr + "\n60066\n<Enter>"
firstTimeThrough = True

oldHeight = 0
def resize_lt(event):
    x=0  #nothing
##    global FirstTimeInresize
##    global oldHeight
##    if FirstTimeInresize == False:
##
##        myFont['size'] = round(event.height/(5))
##        
##        if round(event.height/(5)) != oldHeight:
##            
##            oldHeight = round(event.height/(5))
##            labelLeftTop['font'] = myFont
##            labelRightTop['font'] = myFont
##        
##        
##    else:
##        oldHeight = round(event.height/(5))
##        FirstTimeInresize = False
##FirstTimeInresize = True # For some reason, first time threw causes main window to grow past physical screen size        
sName = "SPY"
stockName = "" 
def keystroke(event):
    global stockName
    global sName
    global firstTimeThrough
    if len(event.char) == 1:
        
        
        if ord(event.char) == 13: #Enter Key pressed 
            
            if len(stockName):
                if Checkname(stockName):
                    sName = stockName
                    firstTimeThrough = False
            stockName = ""
        else:
            if len(stockName) < 7:
                stockName += event.char

win.bind("<Key>", keystroke)






## timerCount = 1
def TimerPopped():

    global timer
    global sName
    
    global serverSock
    global ReadUDP
    global UDP_IP_ADDRESS
    global stateUDP
    global ISSUED_CLOSE
    global NORMAL


    global pairArr



    keepGoing = True
        

    cachedTics = [["a","b"]]
    for pa in pairArr:
        foundInCache = False
        for c in cachedTics:
            if pa[TIC1] == c[0]:
                url_1 = c[1]
                foundInCache = True
                break
                
                

        
        if not foundInCache:
            webSite = "https://api.iextrading.com/1.0/stock/" + pa[TIC1] + "/quote"
     
            try:
                url_1 = requests.get(webSite,timeout=7)
            except:
                try:
                    url_1 = requests.get(webSite,timeout=7)
                except:
                    keepGoing = False
                    break

     
            
            
            
        if (keepGoing and (len(url_1.text) > 20)  and (url_1.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
            if not foundInCache:
                cachedTics = cachedTics + [[pa[TIC1], url_1]]
            text = json.loads(url_1.text)
            pa[CLS1] = text['iexRealtimePrice']
            if (not (isinstance(pa[CLS1], int) or isinstance(pa[CLS1], float))) or pa[CLS1] == 0:
                pa[CLS1] = text['close']
            
        else:
            keepGoing = False
            break
        if (keepGoing):
            foundInCache = False
            for c in cachedTics:
                if pa[TIC2] == c[0]:
                    url = c[1]
                    foundInCache = True
                    break
            if not foundInCache:
            
                webSite = "https://api.iextrading.com/1.0/stock/" + pa[TIC2] + "/quote"   
                try:
                    url = requests.get(webSite,timeout=7)
                except:
                    try:
                        url = requests.get(webSite,timeout=7)
                    except:
                        keepGoing = False
                        break
                
            if (keepGoing and (len(url.text) > 20)  and (url.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
                if not foundInCache:
                    cachedTics = cachedTics + [[pa[TIC2], url]]

                text = json.loads(url.text)
                pa[CLS2] = text['iexRealtimePrice']
                if (not (isinstance(pa[CLS2], int) or isinstance(pa[CLS2], float))) or pa[CLS2] == 0:
                    pa[CLS2] = text['close']
                
                             
            else:
                keepGoing = False
                break
            

    if keepGoing:
        labelRightTop["bg"] = "#001F3F"
        labelLeftTop["bg"] = "#001F3F"
        labelRightTop["text"] = ""
#        pairArr.sort(key=lambda row: row[DELT:], reverse=True)         

      
        leftStr = ""
        rightStr = ""
        count = 0
        soundAlarm = False
        for pa in pairArr:
            if pa[SHARES1] < 0:
            
                gain = ((-(pa[SHARES1])) * pa[PRICE1]) - ((-(pa[SHARES1])) * pa[CLS1])
                + (pa[SHARES2] * pa[CLS2]) - (pa[SHARES2] * pa[CLS2])
            else:
                gain = ((-(pa[SHARES2])) * pa[PRICE2]) - ((-(pa[SHARES2])) * pa[CLS2])
                + (pa[SHARES1] * pa[CLS1]) - (pa[SHARES1] * pa[CLS1])

            if gain > pa[THRE]:
                soundAlarm = True
            sGain = ("{:.2f}".format(round(gain,2)))
            sThre = ("{:.2f}".format(round(pa[THRE],2)))
            sGain = "$" + sGain
            sThre = "$" + sThre
            
            if count < 20:
                
                leftStr = leftStr + " " + pa[TIC1] + " " + pa[TIC2] + " " + sThre + " " + sGain + "\n"
            else:
                if count < 40:
                    rightStr = rightStr + " " + pa[TIC1] + " " + pa[TIC2] + " " + sThre + " " + sDelta + "\n"
                
            count += 1
           
        if soundAlarm:
            alert.play()
            
        
        labelLeftTop["text"] = leftStr
        labelRightTop["text"] = rightStr
            

                
                
            
                   
       






    


    if not keepGoing:
       
        labelRightTop["bg"] = "purple1"
        labelLeftTop["bg"] = "purple1"

        


            
    
    timer = threading.Timer(6, TimerPopped) #web site isnt that real time
                                            #Its about 15 to 30 seconds behind
                                            #Less than 6 seconds won't help you
                                            #And it lets others use the website
                                            #without bogging it down.
    timer.start()

        




labelLeftTop.bind("<Configure>", resize_lt)  #what about right top? 


#UDP_PORT_NO = 60066
UDP_IP_ADDRESS = get_ip()

#serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))



def Checkname(s):
    for char in s:
        if (char < 'a' or char > 'z') and (char < 'A' or char > 'Z') and char != '.':
            return False
    return True
        
        
##class ReadUDP_Port:
##    
##    def __init__(self):
##        self._running = True
##
##    def terminate(self):  
##        self._running = False  
##
##    def run(self):
##        global sName
##        global firstTimeThrough
##        while self._running:
##
##            data, addr = serverSock.recvfrom(256)
##
## #           serverSock.close()
## 
##            if len(data) > 0 and len(data) < 7:
##                if Checkname(str(data, 'utf-8','ignore')):
##                    sName = str(data, 'utf-8','ignore')
##                    firstTimeThrough = False

            
#ReadUDP =   ReadUDP_Port()
#ReadUDPthread = threading.Thread(target=ReadUDP.run) 
#ReadUDPthread.start()


TimerPopped()













def close():
    timer.cancel()

    win.destroy()
    
#    ReadUDP.terminate()
#   serverSock.close()

win.protocol("WM_DELETE_WINDOW", close)







win.mainloop()



