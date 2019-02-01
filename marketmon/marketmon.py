#!/usr/bin/python3.5
# Version 0.1   2-1-2019
#

import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui
import threading
import socket


# start gui
win = tki.Tk()
#########




win.title("Market Monitor")
myFont = tkinter.font.Font(family = 'Piboto Condensed', size = 24, weight = "bold")

labelLeftTop = tki.Label(win,justify="left", width="7", height = "3",bg = "#001F3F",fg = "OliveDrab1")
labelLeftTop.pack()
labelRightTop = tki.Label(win,justify="right", width="7", height = "3",bg = "#001F3F",fg = "OliveDrab1")



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

    global FirstTimeInresize
    global oldHeight
    if FirstTimeInresize == False:

        myFont['size'] = round(event.height/(5))
        
        if round(event.height/(5)) != oldHeight:
            
            oldHeight = round(event.height/(5))
            labelLeftTop['font'] = myFont
            labelRightTop['font'] = myFont
        
        
    else:
        oldHeight = round(event.height/(5))
        FirstTimeInresize = False
FirstTimeInresize = True # For some reason, first time threw causes main window to grow past physical screen size        
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

    if not firstTimeThrough:

    
        keepGoing = True
    #    print ('refreshing')
        
        webSite = "https://api.iextrading.com/1.0/stock/" + sName + "/quote"
                
        try:
            url = requests.get(webSite,timeout=7)
        except:
            keepGoing = False
#            print("requests.get failed")
                
        if (keepGoing and (len(url.text) > 20)  and (url.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
                
            text = json.loads(url.text)

        #    labelLeftTop["text"] = "1234567\n45\n1234567"
            quote = text['iexRealtimePrice']

            pClose = text['previousClose']
            if (not (isinstance(quote, int) or isinstance(quote, float))) or quote == 0:
                pClose = text['close']
                quote = pClose
            chg = quote / pClose
            if chg < 1:
                neg = True
                percent = (1.0 - chg) * 100
            else:
                neg = False
                percent = (chg - 1.0) * 100
            if percent < 10:
                sPercent = ("{:.2f}".format(round(percent,2)))
            else:
                if percent < 100:  
                    sPercent = ("{:.1f}".format(round(percent,1)))
                else:
                    sPercent = "BIG"

            # print (sPercent)

            diff = abs(quote - pClose)
            if diff < 1000:
                sDiff = ("{:.2f}".format(round(diff,2)))
            else:
                if diff < 10000:
                    sDiff = ("{:.1f}".format(round(diff,1)))
                else:
                    sDiff = "BIG"

            if (neg == True):
                labelRightTop["fg"] = "OrangeRed2"
                labelLeftTop["fg"] = "OrangeRed2"
                sPercent = "-" + str(sPercent) + "%"
                sDiff = "-" + str(sDiff)
            else:
                labelRightTop["fg"] = "OliveDrab1"
                labelLeftTop["fg"] = "OliveDrab1"
                sPercent = "+" + str(sPercent) + "%"
                sDiff = "+" + str(sDiff)
            labelRightTop["bg"] = "#001F3F"
            labelLeftTop["bg"] = "#001F3F"



            
            quoteStr = str(quote)
        #    print (len(quoteStr))
            if (len(quoteStr) > 1) and (len(quoteStr) < 8):
                labelRightTop["text"] = quoteStr +  "\n" + sDiff + "\n" + sPercent     
                dlStr = text['symbol']
                labelLeftTop["text"] = dlStr + "\nCHANGE\n% CHG"
        else:
            labelLeftTop["bg"] = "purple1"
            dlStr = sName
            labelLeftTop["text"] = dlStr + "\nCHANGE\n% CHG"
            labelRightTop["text"] = "0\n0\n0"
            
        


                
        if not keepGoing:
            
            labelRightTop["bg"] = "purple1"

            
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


            
    
    timer = threading.Timer(3, TimerPopped) #web site isnt that real time
                                            #Its about 15 to 30 seconds behind
                                            #Less than 3 seconds won't help you
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



