import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui
import threading

print ('hello world')
#url = requests.get('https://api.iextrading.com/1.0/stock/aapl/book')
url = requests.get('https://api.iextrading.com/1.0/stock/aapl/quote')

# todo see what url.status_code is
text = json.loads(url.text)
print (text)
print ('\n')
#print (text['quote']['close'])
print (text['close'])

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
#labelRightTop.pack()
#labelRightMid = tki.Label(win, width="10", height = "3",bg = "midnight blue")
#labelRightBot = tki.Label(win, width="10", height = "3",bg = "midnight blue")

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

labelLeftTop["text"] = "1234567\n45\n1234567"
labelRightTop["text"] = "1234567\n45\n1234567"

def resize_lt(event):
    print("In lt",event.height, event.x, event.y)
    global FirstTimeInresize   
    if FirstTimeInresize == False:
        myFont['size'] = round(event.height/(5))
        print(round(event.height/(5)))
        labelLeftTop['font'] = myFont
        labelRightTop['font'] = myFont
    else:
        FirstTimeInresize = False
FirstTimeInresize = True # For some reason, first time threw causes main window to grow past physical screen size        


def TimerPopped():
    global timer
#    print ('refreshing')
    url = requests.get('https://api.iextrading.com/1.0/stock/ibm/quote')
    text = json.loads(url.text)

#    labelLeftTop["text"] = "1234567\n45\n1234567"
    quote = text['iexRealtimePrice']
    quoteStr = str(quote)
#    print (len(quoteStr))
    if (len(quoteStr) > 1) and (len(quoteStr) < 8):
        labelRightTop["text"] = quoteStr + "\n\n"
    
    if (len(text['symbol']) > 1) and (len(text['symbol']) < 8):
        pClose = text['previousClose']
        chg = quote / pClose
        if chg < 1:
            negPer = (1.0 - chg) * 100
            if negPer < 100
                if neg
        else
            posPer = (chg - 1.0) * 100
        if (perct < 100):
            if perct >= 10:
            
                
                if 
            
        
        dlStr = text['symbol'] + "   "+"\n       " + "\n        "
        labelLeftTop["text"] = dlStr
    
    timer = threading.Timer(2, TimerPopped) # Call this same routine in first parameter seconds
    timer.start()
TimerPopped()        

        
#def resize(event):
#    print (event.height, event.x, event.y) 
#    print ("Resize invoked")
 
#win.bind("<Configure>", resize)

labelLeftTop.bind("<Configure>", resize_lt)  #what about right top? 


def close():
    timer.cancel()
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)
print ("bye")
win.mainloop()


