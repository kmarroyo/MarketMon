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
myFont = tkinter.font.Font(family = 'Helvetica', size = 24, weight = "bold")
#myFont = tkinter.font.Font = ( size = 24, weight = "bold")
#listbox = tki.Listbox(win,font = myFont)
#listbox.pack(fill = tki.BOTH, expand=1)
#listbox.insert(tki.END, "Hello World")
#listbox.insert(tki.END, text['quote']['close'])
labelLeftTop = tki.Label(win, width="20", height = "3",bg = "midnight blue")
labelLeftMid = tki.Label(win, width="20", height = "3",bg = "midnight blue")
labelLeftBot = tki.Label(win, width="20", height = "3",bg = "blue")
labelRightTop = tki.Label(win, width="20", height = "3",bg = "midnight blue")
labelRightMid = tki.Label(win, width="20", height = "3",bg = "midnight blue")
labelRightBot = tki.Label(win, width="20", height = "3",bg = "midnight blue")

labelLeftTop.grid(row =0 ,column=0,sticky='nsew')
labelLeftMid.grid(row =1 ,column=0,sticky='nsew')
labelLeftBot.grid(row =2 ,column=0,sticky='nsew')
labelRightTop.grid(row =0 ,column=1,sticky='nsew')
labelRightMid.grid(row =1 ,column=1,sticky='nsew')
labelRightBot.grid(row =2 ,column=1,sticky='nsew')

win.grid_columnconfigure(0,weight=1)
win.grid_columnconfigure(1,weight=1)
win.grid_rowconfigure(0,weight=1)
win.grid_rowconfigure(1,weight=1)
win.grid_rowconfigure(2,weight=1)


labelLeftTop["text"] = "Hello"
def resize(event):
    print ("Resize invoked")
 
win.bind("<Configure>", resize)




def close():
    win.destroy()

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
