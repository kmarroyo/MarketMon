#test code. do not run


##import socket
##def get_ip():
##    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
##    try:
##        # doesn't even have to be reachable
##        s.connect(('10.255.255.255', 1))
##        IP = s.getsockname()[0]
##    except:
##        IP = '127.0.0.1'
##    finally:
##        s.close()
##    return IP
##s = get_ip()
##
##s = "255.255.255.255"
##list =  (s.split('.'))
##lStr = list[0] + '.' + list[1]
##print (lStr)
##rStr = list[2] + '.' + list[3]
##print (rStr)
##if (len(rStr)) < 7:
##    rStr = '.' + rStr
##print (rStr)
##print (len(rStr))  
    
    









##from threading import Thread
##import time
##
##global cycle
##cycle = 0.0
##
##class Hello5Program:  
##    def __init__(self):
##        self._running = True
##
##    def terminate(self):  
##        self._running = False  
##
##    def run(self):
##        global cycle
##        while self._running:
##            time.sleep(5) #Five second delay
##            cycle = cycle + 1.0
##            print ("5 Second Thread cycle+1.0 - ", cycle)
##
##class Hello2Program:  
##    def __init__(self):
##        self._running = True
##
##    def terminate(self):  
##        self._running = False  
##
##    def run(self):
##        global cycle
##        while self._running:
##            time.sleep(2) #Five second delay
##            cycle = cycle + 0.5
##            print ("5 Second Thread cycle+1.0 - ", cycle)
##
###Create Class
##FiveSecond = Hello5Program()
###Create Thread
##FiveSecondThread = Thread(target=FiveSecond.run) 
###Start Thread 
##FiveSecondThread.start()
##
###Create Class
##TwoSecond = Hello2Program()
###Create Thread
##TwoSecondThread = Thread(target=TwoSecond.run) 
###Start Thread 
##TwoSecondThread.start()
##
##
##Exit = False #Exit flag
##while Exit==False:
## cycle = cycle + 0.1 
## print ("Main Program increases cycle+0.1 - ", cycle)
## time.sleep(1) #One second delay
## if (cycle > 5): Exit = True #Exit Program
##
##TwoSecond.terminate()
##FiveSecond.terminate()
##print ("Goodbye :)")




#UDP_IP = "192.168.1.22"
#UDP_PORT = 5005
#Message = "Hello, World"

#print ("UDP target IP:", UDP_IP)
#print ("UDP target port:", UDP_PORT)
#print ("message:", Message)

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
#sock.sendto(b'Message' ,(UDP_IP, UDP_PORT))

##UDP_IP = "192.168.1.168"
##UDP_PORT = 5005
##
##sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
##sock.bind((UDP_IP, UDP_PORT))
##
##while True:
##    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
##    print ("received message:", data)
##
##
##
##print (round(80,1))
##print (101/96)
##print (str(round(((101/96-1)*100), 2)))
##
##print (100/95.05703422053232)
##string = (str(round(((100/95.05703422053232-1)*100), 2)))
##print (len(string))
##string2 =("{:.2f}".format(1.5))
##print (string2)
















##quote = 51
##pClose = 50
##print ('======')
##chg = quote / pClose
##if chg < 1:
##    neg = True
##    percent = (1.0 - chg) * 100
##else:
##    neg = False
##    percent = (chg - 1.0) * 100
##if percent < 10:
##    sPercent = ("{:.2f}".format(round(percent,2)))
##else:
##    if percent < 100:  
##        sPercent = ("{:.1f}".format(round(percent,1)))
##    else:
##        sPercent = "BIG"
##if (neg == True):
##    sPercent = "-" + str(sPercent) + "%"
##else:
##    sPercent = "+" + str(sPercent) + "%"
##    
##print (sPercent)
##diff = abs(quote - pClose)
##if diff < 1000:
##    sDiff = ("{:.2f}".format(round(diff,2)))
##else:
##    sDiff = "BIG"
##print (sDiff)
##
##yo = 6
##if isinstance(yo, int):
##    print("ture")

#chg = quote / pClose
#TypeError: unsupported operand type(s) for /: 'NoneType' and 'float'
    
    

        
