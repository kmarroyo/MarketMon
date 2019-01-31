#!/usr/bin/python3.5
import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui
import threading
import socket


print ('hello world')
#url = requests.get('https://api.iextrading.com/1.0/stock/aapl/book')
#url = requests.get('https://api.iextrading.com/1.0/stock/aapl/quote')

# todo see what url.status_code is
#text = json.loads(url.text)
#print (text)
#print ('\n')
#print (text['quote']['close'])
#print (text['close'])

# start gui
win = tki.Tk()
#########




win.title("Market Monitor")
myFont = tkinter.font.Font(family = 'Piboto Condensed', size = 24, weight = "bold")
#myFont = tkinter.font.Font(family = 'Helvetica', size = 24, weight = "bold")
#myFont = tkinter.font.Font = ( size = 24, weight = "bold")
#listbox = tki.Listbox(win,font = myFont)
#listbox.pack(fill = tki.BOTH, expand=1)
#listbox.insert(tki.END, "Hello World")
#listbox.insert(tki.END, text['quote']['close'])
#     20      3
labelLeftTop = tki.Label(win,justify="left", width="7", height = "3",bg = "#001F3F",fg = "OliveDrab1")
labelLeftTop.pack()
#labelLeftMid = tki.Label(win, width="10", height = "3",bg = "midnight blue")
#labelLeftBot = tki.Label(win, width="10", height = "3",bg = "blue")
labelRightTop = tki.Label(win,justify="right", width="7", height = "3",bg = "#001F3F",fg = "OliveDrab1")

#labelRightMid = tki.Label(win, width="10", height = "3",bg = "midnight blue")
#labelRightBot = tki.Label(win, width="10", height = "3",bg = "midnight blue")

#labelLeftTop.grid_propagate(True)
#labelRightTop.grid_propagate(True)


labelLeftTop.grid(row =0 ,column=0,sticky='nsew')
#labelLeftMid.grid(row =1 ,column=0,sticky='nsew')
#labelLeftBot.grid(row =2 ,column=0,sticky='nsew')
labelRightTop.grid(row =0 ,column=1,sticky='nsew')
#labelRightMid.grid(row =1 ,column=1,sticky='nsew')
#labelRightBot.grid(row =2 ,column=1,sticky='nsew')

win.grid_columnconfigure(0,weight=1)
win.grid_columnconfigure(1,weight=1)
win.grid_rowconfigure(0,weight=1)
#win.grid_rowconfigure(1,weight=1)
#win.grid_rowconfigure(2,weight=1)
#print (tkinter.font.families())
#print (tkinter.font.names())

labelLeftTop["text"] = "\nUDPport\nticker"
labelRightTop["text"] = "\n60066\n<Enter>"
firstTimeThrough = True

oldHeight = 0
def resize_lt(event):
    print("In lt",event.height, event.x, event.y)
    global FirstTimeInresize
    global oldHeight
    if FirstTimeInresize == False:

        myFont['size'] = round(event.height/(5))
        print(round(event.height/(5)))
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
        
        print (ord(event.char))
        if ord(event.char) == 13:
            print ("Enter Key pressed")
            print (stockName)
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

##prevtimerCount = 0
##def DeadManTimer():
##    global dtimer
##    global timer
##    global prevtimerCount
##    global  serverSock
##    global ReadUDP
##    global UDP_IP_ADDRESS
##    global stateUDP
##    global ISSUED_CLOSE
##    global NORMAL
##    
##
##    if prevtimerCount == timerCount:
##        timer = threading.Timer(3, TimerPopped) # Call this same routine in first parameter seconds
##        timer.start()
##    
##    if stateUDP == NORMAL:
##        ip=get_ip()
##        if ip != UDP_IP_ADDRESS:
##            ReadUDP.terminate()
##            try:
##                serverSock.shutdown(socket.SHUT_RD)
##            except:
##                print("Error UDP shutdown")
##            
##            serverSock.close()
##            stateUDP = ISSUED_CLOSE
##            print(" IP changed")
##    else:
##        if stateUDP == ISSUED_CLOSE:
##            UDP_IP_ADDRESS = get_ip()
##            serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##            serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) 
##            ReadUDP =   ReadUDP_Port()
##            ReadUDPthread = threading.Thread(target=ReadUDP.run) 
##            ReadUDPthread.start()
##            stateUDP = NORMAL
##            print("restarted UDP thread")
##        
##        
##    
##    
##    prevtimerCount = timerCount
##    dtimer = threading.Timer(120, DeadManTimer) # 2 minutes
##    dtimer.start()





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
                        print("Error UDP shutdown")
                
                    serverSock.close()
                    stateUDP = ISSUED_CLOSE
                    print(" IP changed")
            else:
                if stateUDP == ISSUED_CLOSE:
                    UDP_IP_ADDRESS = get_ip()
                    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO)) 
                    ReadUDP =   ReadUDP_Port()
                    ReadUDPthread = threading.Thread(target=ReadUDP.run) 
                    ReadUDPthread.start()
                    stateUDP = NORMAL
                    print("restarted UDP thread") 

            
    
    timer = threading.Timer(3, TimerPopped) # Call this same routine in first parameter seconds
    timer.start()
    timerCount += 1
        


#DeadManTimer()
#dtimer = threading.Timer(120, DeadManTimer) # 2 minutes
#dtimer.start()


        
#def resize(event):
#    print (event.height, event.x, event.y) 
#    print ("Resize invoked")
 
#win.bind("<Configure>", resize)

labelLeftTop.bind("<Configure>", resize_lt)  #what about right top? 


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
print (get_ip())

UDP_PORT_NO = 60066
UDP_IP_ADDRESS = get_ip()

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))


#while True:
 #   data, addr = serverSock.recvfrom(1024)
#    print ("Message: ", data)
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
            print ("ReadUDP before recv")
            data, addr = serverSock.recvfrom(256)
            print ("Out of recvfrom")
 #           serverSock.close()
            print(data)
            if len(data) > 0 and len(data) < 7:
                if Checkname(str(data, 'utf-8','ignore')):
                    sName = str(data, 'utf-8','ignore')
                    firstTimeThrough = False
                print(sName)
        
        print ("ReadUDP thread running")
            
ReadUDP =   ReadUDP_Port()
ReadUDPthread = threading.Thread(target=ReadUDP.run) 
ReadUDPthread.start()


TimerPopped()













def close():
    timer.cancel()
#    dtimer.cancel()
    win.destroy()
    
    ReadUDP.terminate()
    serverSock.close()

win.protocol("WM_DELETE_WINDOW", close)






print ("bye")
win.mainloop()
print ("bye after  main")


