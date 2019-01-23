import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui


print ('hello world')
url = requests.get('https://api.iextrading.com/1.0/stock/aapl/book')
# todo see what url.status_code is
text = json.loads(url.text)
print (text)
print ('\n')
print (text['quote']['close'])

# start gui
win = tki.Tk()
win.title("Market Monitor")
myFont = tkinter.font.Font(family = 'Piboto Condensed', size = 24, weight = "bold")
#myFont = tkinter.font.Font(family = 'Helvetica', size = 24, weight = "bold")
#myFont = tkinter.font.Font = ( size = 24, weight = "bold")
#listbox = tki.Listbox(win,font = myFont)
#listbox.pack(fill = tki.BOTH, expand=1)
#listbox.insert(tki.END, "Hello World")
#listbox.insert(tki.END, text['quote']['close'])
#     20      3
labelLeftTop = tki.Label(win,justify="right", width="7", height = "3",bg = "#001F3F")
#labelLeftTop.pack()
#labelLeftMid = tki.Label(win, width="10", height = "3",bg = "midnight blue")
#labelLeftBot = tki.Label(win, width="10", height = "3",bg = "blue")
labelRightTop = tki.Label(win, width="7", height = "3",bg = "#001F3F")
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

labelLeftTop["text"] = "1234567\n   45\n1234567"
labelRightTop["text"] = "1234567\n   45\n1234567"
def resize_lt(event):
    print("In lt",event.height, event.x, event.y)
   
    if event.height != 46:
#        labelLeftTop['text']= "Goodbye"
        labelLeftTop['fg'] = "OliveDrab1"
        myFont['size'] = round(event.height/(5))
        print(round(event.height/(5)))
        labelLeftTop['font'] = myFont
        labelRightTop['font'] = myFont
#        labelLeftTop["text"] = "1234567890\n   45\n1234567"

        
def resize(event):
    print (event.height, event.x, event.y) 
    print ("Resize invoked")
 
win.bind("<Configure>", resize)

labelLeftTop.bind("<Configure>", resize_lt)


def close():
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)
print ("bye")
win.mainloop()


