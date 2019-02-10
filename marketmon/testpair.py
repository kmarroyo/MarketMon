#!/usr/bin/python3.5
# 
#

import json, requests
import socket


TIC1 = 1

mTic = "IWM"
 
pairArr = [

[0.98,"VTWG"],
[0.98,"FNX"],
[0.98,"SMLF"],
[0.98,"IJS"],
[0.98,"SLYV"],
[0.98,"FYC"],
[0.98,"VBR"],
[0.98,"IJH"],
[0.98,"MIDU"],
[0.98,"IWN"],
[0.98,"MDY"],
[0.97,"IVOO"],
[0.97,"VIOV"],
[0.97,"VBK"],
[0.97,"MVV"],
[0.97,"IWC"],
[0.97,"SCHM"],
[0.97,"IJK"],
[0.97,"EZM"],
[0.97,"EES"],
[0.97,"MDYG"],
[0.97,"IVOG"],
[0.96,"GSSC"],
[0.96,"RWK"],
[0.96,"VTWV"],
[0.96,"CSML"],
[0.96,"RZG"],
[0.96,"JHMM"],
[0.96,"IWR"],
[0.96,"VO"],
[0.96,"IJJ"],
[0.95,"DES"],
[0.95,"DWAS"],
[0.95,"FNY"],
[0.95,"MDYV"],
[0.95,"VUSE"],
[0.95,"IWP"],
[0.95,"JKH"],
[0.95,"FEX"],
[0.95,"IVOV"],
[0.95,"VOT"],
[0.94,"DEUS"],
[0.94,"RWJ"],
[0.94,"AIEQ"],
[0.94,"EQAL"],
[0.94,"IWV"],
[0.94,"CFA"],
[0.94,"ROUS"],
[0.94,"VTI"],
[0.94,"RSP"],
[0.94,"SPTM"],
[0.94,"SCHB"],
[0.94,"COWZ"],
[0.94,"PSCT"],
[0.94,"ITOT"],
[0.94,"LRGF"],
[0.93,"SPHB"],
[0.93,"IYY"],
[0.93,"DON"],
[0.93,"TILT"],
[0.93,"SCHK"],
[0.93,"FVC"],
[0.93,"FRLG"],
[0.93,"VOE"],
[0.93,"EUSA"],
[0.93,"IWB"],
[0.93,"FV"],
[0.93,"GSLC"],
[0.93,"VONE"],
[0.93,"CSM"],
[0.93,"SPLG"],
[0.93,"IWS"],
[0.93,"PSCH"],
[0.93,"SCHX"],
[0.93,"QQEW"],
[0.93,"VT"],
[0.93,"SECT"],
[0.93,"FXR"],
[0.93,"ONEQ"],
[0.92,"RDVY"],
[0.92,"PSCI"],
[0.92,"FVAL"],
[0.92,"VV"],
[0.92,"JHML"],
[0.92,"SMLV"],
[0.92,"DSI"],
[0.92,"JKG"],
[0.92,"FTC"],
[0.92,"SPY"],
[0.92,"JPUS"],
[0.92,"VLUE"],
[0.92,"FXD"],
[0.92,"PKW"],
[0.92,"IVV"],
[0.92,"XT"],
[0.92,"QQQE"],
[0.92,"FDIS"],
[0.92,"VCR"],
[0.92,"VOO"],
[0.92,"UPRO"],
[0.92,"SPXL"],
[0.92,"ACWI"],
[0.92,"FPX"],
[0.92,"RPG"],
[0.92,"SSO"],
[0.92,"JKL"],
[0.92,"PRF"],
[0.92,"SCHG"],
[0.92,"AIRR"],
[0.92,"VUG"],
[0.91,"AOA"],
[0.91,"GSEW"],
[0.91,"IWF"],
[0.91,"VONG"],
[0.91,"FNDX"],
[0.91,"MGC"],
[0.91,"IYJ"],
[0.91,"PDP"],
[0.91,"IUSG"],
[0.91,"URTH"],
[0.91,"QUAL"],
[0.91,"QDF"],
[0.91,"USMF"],
[0.91,"PXMG"],
[0.91,"XTL"],
[0.91,"SHE"],
[0.91,"VIS"],
[0.91,"XLY"],
[0.91,"DGRW"],
[0.91,"RWL"],
[0.91,"CRBN"],
[0.91,"SUSA"],
[0.91,"PWB"],
[0.91,"SPHQ"],
[0.91,"IYC"],
[0.91,"TMFC"],
[0.91,"FIDU"],
[0.91,"FIW"],
[0.90,"IVW"],
[0.90,"AOR"],
[0.90,"RYT"],
[0.90,"VOOG"],
[0.90,"SPYG"],
[0.90,"MGK"],
[0.90,"OEF"],
[0.90,"VTHR"],
[0.90,"CWB"],
[0.90,"RXI"],
[0.90,"FXH"],
[0.90,"FTA"],
[0.90,"FXO"],
[0.90,"ESGU"],
[0.90,"ROBO"],
[0.90,"CFO"],
[0.90,"FLGE"],
[0.90,"IWY"],
[0.90,"RPV"],
[0.90,"RGI"],
[0.90,"PXLG"],
[0.90,"JKE"],



]


ai = ["SPY",
"EEM",
"XLF",
"QQQ",
"GDX",
"EFA",
"FXI",
"USO",
"HYG",
"AMLP",
"IWM",
]


keepGoing = True

for pa in pairArr:
    webSite = "https://api.iextrading.com/1.0/stock/" + pa[TIC1] + "/quote"
         
    try:
        url = requests.get(webSite,timeout=7)
    except:
        keepGoing = False
        break
    if (keepGoing and (len(url.text) > 20)  and (url.text[0]== '{')): # 20 is arbitrary.  Here to catch invalid symbol
        text = json.loads(url.text)
        total = text['avgTotalVolume']
        if total > 3000000:
            if pa[0] ==  0.90:
                thresh = "0.42"
            elif pa[0] ==  0.91:
                thresh = "0.38"
            elif pa[0] ==  0.92:
                thresh = "0.34"
            elif pa[0] ==  0.93:
                thresh = "0.30"
            elif pa[0] ==  0.94:
                thresh = "0.26"
            elif pa[0] ==  0.95:
                thresh = "0.22"
            elif pa[0] ==  0.96:
                thresh = "0.18"
            elif pa[0] ==  0.97:
                thresh = "0.14"
            elif pa[0] ==  0.98:
                thresh = "0.10"
            else:
                print ("ERROR")
                keepGoing = False
                break    

            if pa[TIC1] not in ai:
                print ("[\"" + mTic  + "\", " + "\"" + pa[1] + "\""
                       + ", 0.0, 0.0, 0.0, 0.0, " + str(pa[0]) + ", " + thresh
                       + ", " + "0.0, 0.0],")

                
if not (keepGoing):
    print("ERROR------------------------ERROR")
