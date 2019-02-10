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
OPN1 = 2
CLS1 = 3
OPN2 = 4
CLS2 = 5
CORR = 6
THRE = 7
DELT = 8
DDIVT= 9 # |delt(Delta)| divided by thre(Threshold)
#    tic1   tic2  opn1  cls1  opn2  cls2  corr   thre  delt   ddivt  
pairArr = [

["SPY", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["SPY", "DIA", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["SPY", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["SPY", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["SPY", "VT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["SPY", "IWD", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["SPY", "TQQQ", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["SPY", "QQQ", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["SPY", "XLK", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SPY", "XLY", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SPY", "USMV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SPY", "TNA", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["SPY", "IWM", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["SPY", "XLI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["SPY", "IJR", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["SPY", "XLV", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["EEM", "MCHI", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["EEM", "FXI", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["EEM", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["EEM", "VEU", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["EEM", "EWY", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["XLF", "IWD", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["XLF", "VTV", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],

["QQQ", "XLK", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["QQQ", "VTI", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["QQQ", "UPRO", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["QQQ", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["QQQ", "SPXL", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["QQQ", "IVV", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["QQQ", "VOO", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["QQQ", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["QQQ", "VT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["QQQ", "XLY", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["QQQ", "XLC", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["QQQ", "DIA", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],

["GDX", "GDXJ", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],

["EFA", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["EFA", "VGK", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["EFA", "EZU", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["EFA", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["EFA", "VT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["EFA", "EWG", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["EFA", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["EFA", "EWU", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["EFA", "EWJ", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],


["FXI", "MCHI", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["FXI", "VWO", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["FXI", "IEMG", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],

["HYG", "JNK", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["HYG", "SJNK", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],

["AMLP", "AMJ", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],

["IWM", "VTI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IWM", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IWM", "VT", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["IWM", "IVV", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IWM", "VOO", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IWM", "SPXL", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IWM", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IWM", "IWF", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["IWM", "XLY", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],




    
##    ["SPY", "QQQ", 0.0,  0.0,  0.0,  0.0,  0.96,  0.40, 0.0, 0.0],
##    ["SPY", "IWM", 0.0,  0.0,  0.0,  0.0,  0.92,  0.40, 0.0, 0.0],
##    ["QQQ", "IWM", 0.0,  0.0,  0.0,  0.0,  0.89,  0.40, 0.0, 0.0],
##    ["HYG", "JNK", 0.0,  0.0,  0.0,  0.0,  0.98,  0.10, 0.0, 0.0],
##    ["XLI", "DIA", 0.0,  0.0,  0.0,  0.0,  0.93,  0.40, 0.0, 0.0],
##    ["VEU", "EFA", 0.0,  0.0,  0.0,  0.0,  0.98,  0.16, 0.0, 0.0],
##    ["VT",  "EFA", 0.0,  0.0,  0.0,  0.0,  0.94,  0.20, 0.0, 0.0],
]

#pairArr[order(pairArr[:,7], decreasing = TRUE),]
#pairArr.sort(key=lambda row: row[6:], reverse=True)
import pprint 
#pprint.pprint(pairArr)



# start gui
win = tki.Tk()
#########




win.title("Pair Trader")
myFont = tkinter.font.Font(family = 'Piboto Condensed', size = 24, weight = "bold")

labelLeftTop = tki.Label(win,justify="left", width="25", height = "10",bg = "#001F3F",fg = "OliveDrab1")
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

NORMAL = 0
ISSUED_CLOSE = 1
stateUDP = NORMAL






timerCount = 1
def TimerPopped():
    global timerCount
    global timer
    global sName
    
    global serverSock
    global ReadUDP
    global UDP_IP_ADDRESS
    global stateUDP
    global ISSUED_CLOSE
    global NORMAL

    global firstTimeThrough
    global pairArr

    if not firstTimeThrough:

    
        keepGoing = True
    #    print ('refreshing')

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
                    keepGoing = False
                    break
#            else:
#                print("Cashed")
         
                
                
                
            if (keepGoing and (len(url_1.text) > 20)  and (url_1.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
                if not foundInCache:
                    cachedTics = cachedTics + [[pa[TIC1], url_1]]
                text = json.loads(url_1.text)
                pa[CLS1] = text['iexRealtimePrice']
                if (not (isinstance(pa[CLS1], int) or isinstance(pa[CLS1], float))) or pa[CLS1] == 0:
                    pa[CLS1] = text['open']
                pa[OPN1] = text['open']
                if (pa[CLS1] < pa[OPN1]):
                    first = -((1 - (pa[CLS1]/pa[OPN1]))*100)
                else:
                    first = (((pa[CLS1]/pa[OPN1])-1)*100)
            else:
                keepGoing = False
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
                        keepGoing = False
                        break
                    
                if (keepGoing and (len(url.text) > 20)  and (url.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
                    if not foundInCache:
                        cachedTics = cachedTics + [[pa[TIC2], url]]

                    text = json.loads(url.text)
                    pa[CLS2] = text['iexRealtimePrice']
                    if (not (isinstance(pa[CLS2], int) or isinstance(pa[CLS2], float))) or pa[CLS2] == 0:
                        pa[CLS2] = text['open']
                    pa[OPN2] = text['open']
                    if (pa[CLS2] < pa[OPN2]):
                        second = -((1 - (pa[CLS2]/pa[OPN2]))*100)
                    else:
                        second = (((pa[CLS2]/pa[OPN2])-1)*100)
                    pa[DELT] = (first - second)
                    pa[DDIVT] = abs(pa[DELT])/pa[THRE]
                else:
                    keepGoing = False
                
#            print (pa[TIC1], pa[OPN1], pa[CLS1], pa[TIC2], pa[OPN2], pa[CLS2])

        if keepGoing:
            labelRightTop["bg"] = "#001F3F"
            labelLeftTop["bg"] = "#001F3F"
            labelRightTop["text"] = ""
            pairArr.sort(key=lambda row: row[DDIVT:], reverse=True)         
#            pprint.pprint(pairArr)
            foundAnOverThres = False
            leftStr = ""
            for pa in pairArr:
                prtStr = ""
                if pa[DDIVT] > 1.0:
                    foundAnOverThres = True
                sDelta = ("{:.2f}".format(round(abs(pa[DELT]),2)))
                sThre = ("{:.2f}".format(round(pa[THRE],2)))
                leftStr = leftStr + " " + pa[TIC1] + " " + pa[TIC2] + " " + sThre + " " + sDelta + "\n"
                
                    
            if foundAnOverThres:  
                labelLeftTop["fg"] = "OrangeRed2"
                alert.play()
            else:
                labelLeftTop["fg"] = "OliveDrab1" 
            
            labelLeftTop["text"] = leftStr
            
                

                    
#                print(prtStr, pa[TIC1], pa[TIC2], pa[THRE], abs(pa[DELT]))
                    
                
                       
           





    
        
##        webSite = "https://api.iextrading.com/1.0/stock/" + sName + "/quote"
##                
##        try:
##            url = requests.get(webSite,timeout=7)
##        except:
##            keepGoing = False
###            print("requests.get failed")
##                
##        if (keepGoing and (len(url.text) > 20)  and (url.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
##                
##            text = json.loads(url.text)
##
##        #    labelLeftTop["text"] = "1234567\n45\n1234567"
##            quote = text['iexRealtimePrice']
##
##            pClose = text['previousClose']
##            if (not (isinstance(quote, int) or isinstance(quote, float))) or quote == 0:
##                pClose = text['close']
##                quote = pClose
##            chg = quote / pClose
##            if chg < 1:
##                neg = True
##                percent = (1.0 - chg) * 100
##            else:
##                neg = False
##                percent = (chg - 1.0) * 100
##            if percent < 10:
##                sPercent = ("{:.2f}".format(round(percent,2)))
##            else:
##                if percent < 100:  
##                    sPercent = ("{:.1f}".format(round(percent,1)))
##                else:
##                    sPercent = "BIG"
##
##            # print (sPercent)
##
##            diff = abs(quote - pClose)
##            if diff < 1000:
##                sDiff = ("{:.2f}".format(round(diff,2)))
##            else:
##                if diff < 10000:
##                    sDiff = ("{:.1f}".format(round(diff,1)))
##                else:
##                    sDiff = "BIG"
##
##            if (neg == True):
##                labelRightTop["fg"] = "OrangeRed2"
##                labelLeftTop["fg"] = "OrangeRed2"
##                sPercent = "-" + str(sPercent) + "%"
##                sDiff = "-" + str(sDiff)
##            else:
##                labelRightTop["fg"] = "OliveDrab1"
##                labelLeftTop["fg"] = "OliveDrab1"
##                sPercent = "+" + str(sPercent) + "%"
##                sDiff = "+" + str(sDiff)
##            labelRightTop["bg"] = "#001F3F"
##            labelLeftTop["bg"] = "#001F3F"
##
##
##
##            
##            quoteStr = str(quote)
##        #    print (len(quoteStr))
##            if (len(quoteStr) > 1) and (len(quoteStr) < 8):
##                labelRightTop["text"] = quoteStr +  "\n" + sDiff + "\n" + sPercent     
##                dlStr = text['symbol']
##                labelLeftTop["text"] = dlStr + "\nCHANGE\n% CHG"
##        else:
##            labelLeftTop["bg"] = "purple1"
##            dlStr = sName
##            labelLeftTop["text"] = dlStr + "\nCHANGE\n% CHG"
##            labelRightTop["text"] = "0\n0\n0"
##            
##        
##
##
##                
##        if not keepGoing:
##            
##            labelRightTop["bg"] = "purple1"


        if not keepGoing:
           
            labelRightTop["bg"] = "purple1"
            labelLeftTop["bg"] = "purple1"

            
    if timerCount == 3 or stateUDP != NORMAL:
            timerCount = 0
            if stateUDP == NORMAL:
                ip=get_ip()
                if ip != UDP_IP_ADDRESS:
                    ReadUDP.terminate()
                    try:
                         serverSock.shutdown(socket.SHUT_RD)
                    except:
                         Oops = 0  # Dont do anything  
                
                    serverSock.close()
                    stateUDP = ISSUED_CLOSE

            else:
                if stateUDP == ISSUED_CLOSE:
                    UDP_IP_ADDRESS = get_ip()
                    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) 
                    ReadUDP =   ReadUDP_Port()
                    ReadUDPthread = threading.Thread(target=ReadUDP.run) 
                    ReadUDPthread.start()
                    stateUDP = NORMAL


            
    
    timer = threading.Timer(6, TimerPopped) #web site isnt that real time
                                            #Its about 15 to 30 seconds behind
                                            #Less than 6 seconds won't help you
                                            #And it lets others use the website
                                            #without bogging it down.
    timer.start()
    timerCount += 1
        




labelLeftTop.bind("<Configure>", resize_lt)  #what about right top? 


UDP_PORT_NO = 60066
UDP_IP_ADDRESS = get_ip()

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))



def Checkname(s):
    for char in s:
        if (char < 'a' or char > 'z') and (char < 'A' or char > 'Z') and char != '.':
            return False
    return True
        
        
class ReadUDP_Port:
    
    def __init__(self):
        self._running = True

    def terminate(self):  
        self._running = False  

    def run(self):
        global sName
        global firstTimeThrough
        while self._running:

            data, addr = serverSock.recvfrom(256)

 #           serverSock.close()
 
            if len(data) > 0 and len(data) < 7:
                if Checkname(str(data, 'utf-8','ignore')):
                    sName = str(data, 'utf-8','ignore')
                    firstTimeThrough = False

            
ReadUDP =   ReadUDP_Port()
ReadUDPthread = threading.Thread(target=ReadUDP.run) 
ReadUDPthread.start()


TimerPopped()













def close():
    timer.cancel()

    win.destroy()
    
    ReadUDP.terminate()
    serverSock.close()

win.protocol("WM_DELETE_WINDOW", close)







win.mainloop()



