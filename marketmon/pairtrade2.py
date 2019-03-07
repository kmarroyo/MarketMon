#!/usr/bin/python3.5
# 
#

import json, requests
import tkinter as tki   #gui
import tkinter.font  #gui
import threading
import socket
from pygame import mixer
#mixer.init()
#alert=mixer.Sound('/home/pi/Downloads/Bell.wav')

TIC1 = 0
TIC2 = 1
SUMCLS = 2
CLS1 = 3
xxx2 = 4
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

["SPY", "QQQ", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["SPY", "XLK", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SPY", "XLY", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SPY", "USMV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
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

["QQQ", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],

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

["IWM", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IWM", "IWF", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["IWM", "XLY", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],

["IEMG", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["IEMG", "VEU", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["IEMG", "MCHI", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["IEMG", "EWY", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],


["VEA", "VGK", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["VEA", "EZU", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["VEA", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VEA", "VT", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VEA", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VEA", "EWG", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["VEA", "EWU", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["VEA", "EWJ", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],




#["XOP", "XLE", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["XOP", "OIH", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],



["VWO", "MCHI", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["VWO", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["VWO", "VEU", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],

["JNK", "SJNK", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],


["XLK", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["XLK", "IVV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],

["XLK", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLK", "VTI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLK", "VOO", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLK", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLK", "VT", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLK", "DIA", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLK", "XLY", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["XLI", "DIA", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["XLI", "VTI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLI", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLI", "IVV", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLI", "VTV", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLI", "VOO", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],

["XLI", "IWD", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLI", "VT", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["XLI", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],


["IEFA", "VEU", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["IEFA", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["IEFA", "VGK", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["IEFA", "EZU", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["IEFA", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["IEFA", "EWG", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IEFA", "VT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IEFA", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IEFA", "EWU", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IEFA", "EWJ", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],



["XLV", "VTV", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["XLV", "VOO", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["XLV", "IVV", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["XLV", "USMV", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["XLV", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["XLV", "VTI", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["EWJ", "SCHF", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["EWJ", "VEU", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["SCHF", "VGK", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["SCHF", "EZU", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["SCHF", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["SCHF", "VT", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["SCHF", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SCHF", "EWG", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["SCHF", "EWU", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],

["EZU", "VGK", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["EZU", "EWG", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["EZU", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["EZU", "VEU", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["EZU", "EWU", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],


["XLY", "IWF", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["XLY", "VTI", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLY", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLY", "IVV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLY", "VOO", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["XLY", "VT", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["XLY", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["XLY", "DIA", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],


["IVV", "DIA", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["IVV", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["IVV", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["IVV", "ACWI", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["IVV", "VT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["IVV", "IWD", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["IVV", "USMV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["IVV", "IJR", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["ACWI", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["ACWI", "VTI", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["ACWI", "VOO", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["ACWI", "IWF", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["ACWI", "DIA", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["ACWI", "VEU", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["ACWI", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["ACWI", "VTV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["ACWI", "IWD", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["ACWI", "IJR", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["VGK", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["VGK", "EWG", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["VGK", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VGK", "VEU", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VGK", "EWU", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VGK", "VT", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["IJR", "VTI", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IJR", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["IJR", "VT", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],
["IJR", "VOO", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["IEF", "BND", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],
["IEF", "TLT", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["USMV", "VTV", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["USMV", "IWD", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["USMV", "SPLV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["USMV", "VOO", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["USMV", "DIA", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["USMV", "VTI", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["USMV", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],

["VEU", "VT", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["VEU", "FEZ", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["VEU", "EWG", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],
["VEU", "EWU", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["DIA", "VOO", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["DIA", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["DIA", "VTI", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["DIA", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["DIA", "IWD", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["DIA", "VT", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],
["DIA", "IWF", 0.0, 0.0, 0.0, 0.0, 0.95, 0.22, 0.0, 0.0],

["FEZ", "EWG", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["FEZ", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["FEZ", "EWU", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["VTI", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["VTI", "VT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["VTI", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["VTI", "IWD", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],


["IWD", "VOO", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["IWD", "ITOT", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["IWD", "VT", 0.0, 0.0, 0.0, 0.0, 0.93, 0.30, 0.0, 0.0],
["IWD", "IWF", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["VOO", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["VOO", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["VOO", "VT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],

["EWG", "ACWX", 0.0, 0.0, 0.0, 0.0, 0.92, 0.34, 0.0, 0.0],

["ACWX", "VT", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],
["ACWX", "EWU", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],

["ITOT", "IWF", 0.0, 0.0, 0.0, 0.0, 0.98, 0.10, 0.0, 0.0],
["ITOT", "VT", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],
["ITOT", "VTV", 0.0, 0.0, 0.0, 0.0, 0.97, 0.14, 0.0, 0.0],


["VT", "IWF", 0.0, 0.0, 0.0, 0.0, 0.96, 0.18, 0.0, 0.0],
["VT", "VTV", 0.0, 0.0, 0.0, 0.0, 0.94, 0.26, 0.0, 0.0],


["XLC", "IWF", 0.0, 0.0, 0.0, 0.0, 0.9, 0.42, 0.0, 0.0],

["IWF", "VTV", 0.0, 0.0, 0.0, 0.0, 0.91, 0.38, 0.0, 0.0],

    
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




win.title("Pair Trader 2")
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

NORMAL = 0
ISSUED_CLOSE = 1
stateUDP = NORMAL



def getMovAveData():
    keepGoing = True
    doOnce = True
    global pairArr

    for pa in pairArr:
        webSite = "https://api.iextrading.com/1.0/stock/" + pa[TIC1] + "/chart/3m"
        try:
            url_1 = requests.get(webSite,timeout=7)
        except:
            try:
                url_1 = requests.get(webSite,timeout=7)
            except:
                keepGoing = False
                break
        if (keepGoing and (len(url_1.text) > 20)  and (url_1.text[0]== '[')): # 20 is arbitrary.  Here to catch invalid symbol
            text = json.loads(url_1.text)
            webSite = "https://api.iextrading.com/1.0/stock/" + pa[TIC2] + "/chart/3m"
            try:
                url_2 = requests.get(webSite,timeout=7)
            except:
                try:
                    url_2 = requests.get(webSite,timeout=7)
                except:
                    keepGoing = False
                    break
        else:
            keepGoing = False
            print(pa[TIC1], pa[TIC2])
            break
        if (keepGoing and (len(url_2.text) > 20)  and (url_2.text[0]== '[')): # 20 is arbitrary.  Here to catch invalid symbol
            text2 = json.loads(url_2.text)

            if ((len(text2) >= 50) and (len(text)>= 50)):
                sumCloses = 0.0
                idx2 = len(text2) - 49
                for idx in range(len(text) - 49,len(text)):
                    sumCloses += text[idx]["close"] / text2[idx2]["close"]
                    idx2 += 1
                pa[SUMCLS] = sumCloses


                    
#                    if doOnce:
#                        print (pa[TIC1], text[idx]["close"],pa[TIC2], text2[idx]["close"])
#                if doOnce:
#                    print (sumCloses)
#                    doOnce = False
#                for tx in text[(len(text) - 49):]:
#                    sumCloses += tx["close"]
#                pa[SUMCLS]= sumCloses   
                if (len(text2) != len(text)):
                    print(pa[TIC1], pa[TIC2], len(text), len(text2))
                    
            else:
                keepGoing = False
                print(pa[TIC1], pa[TIC2], len(text), len(text2))
                break
        else:
            keepGoing = False
            print(pa[TIC1], pa[TIC2])
            break
    return keepGoing



doneGettingMovingAve = False


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
    global doneGettingMovingAve

    if not firstTimeThrough:
        keepGoing = True
        if not doneGettingMovingAve:
          
            keepGoing = getMovAveData()
            doneGettingMovingAve = keepGoing
            
        if keepGoing:
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
    #            else:
    #                print("Cashed")
             
                    
                    
                    
                if (keepGoing and (len(url_1.text) > 20)  and (url_1.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
                    if not foundInCache:
                        cachedTics = cachedTics + [[pa[TIC1], url_1]]
                    text = json.loads(url_1.text)
                    pa[CLS1] = text['iexRealtimePrice']
                    if (not (isinstance(pa[CLS1], int) or isinstance(pa[CLS1], float))) or pa[CLS1] == 0:
                        pa[CLS1] = text['open']
                    
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
                            pa[CLS2] = text['open']
                        curRatio = pa[CLS1]/pa[CLS2]
                        movingAvg = (curRatio + pa[SUMCLS]) / 50
                        if curRatio > movingAvg:
                            pa[DELT] = curRatio/movingAvg
                        else:
                            pa[DELT] = movingAvg / curRatio
                                     
                    else:
                        keepGoing = False
                        break
                    
    #            print (pa[TIC1], pa[OPN1], pa[CLS1], pa[TIC2], pa[OPN2], pa[CLS2])

        if keepGoing:
            labelRightTop["bg"] = "#001F3F"
            labelLeftTop["bg"] = "#001F3F"
            labelRightTop["text"] = ""
            pairArr.sort(key=lambda row: row[DELT:], reverse=True)         
#            pprint.pprint(pairArr)
          
            leftStr = ""
            rightStr = ""
            count = 0
    
            for pa in pairArr:
                sDelta = ("{:.3f}".format(round(pa[DELT],3)))
                sThre = ("{:.2f}".format(round(pa[THRE],2)))
                
                if count < 20:
                    
                    leftStr = leftStr + " " + pa[TIC1] + " " + pa[TIC2] + " " + sThre + " " + sDelta + "\n"
                else:
                    if count < 40:
                        rightStr = rightStr + " " + pa[TIC1] + " " + pa[TIC2] + " " + sThre + " " + sDelta + "\n"
                    
                count += 1
               
#            rightStr = "OVER RATIO: " + str(countOver)  + " / " + str(len(pairArr)) + "\n" + rightStr      
#            if foundAnOverThres:  
#                labelLeftTop["fg"] = "OrangeRed2"
#                alert.play()
#            else:
#                labelLeftTop["fg"] = "OliveDrab1" 
            
            labelLeftTop["text"] = leftStr
            labelRightTop["text"] = rightStr
                

                    
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



