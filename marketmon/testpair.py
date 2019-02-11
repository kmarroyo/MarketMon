#!/usr/bin/python3.5
# 
#

import json, requests
import socket


TIC1 = 1

mTic = "IWF"
 
pairArr = [


[0.98,"IGM"],
[0.98,"GSLC"],
[0.98,"SPHQ"],
[0.98,"XLG"],
[0.98,"IYW"],
[0.98,"VV"],
[0.98,"SCHX"],
[0.98,"SPLG"],
[0.98,"IWV"],
[0.98,"VTI"],
[0.98,"MGC"],
[0.98,"IWB"],
[0.98,"ROM"],
[0.98,"DSI"],
[0.98,"SCHB"],
[0.98,"ITOT"],
[0.98,"SPTM"],
[0.98,"FTEC"],
[0.98,"OEF"],
[0.98,"VGT"],
[0.98,"PXLG"],
[0.98,"RPG"],
[0.98,"IVV"],
[0.98,"VONE"],
[0.98,"IYY"],
[0.98,"UPRO"],
[0.98,"SSO"],
[0.98,"SCHK"],
[0.98,"SPY"],
[0.98,"MTUM"],
[0.98,"VOO"],
[0.98,"SPXL"],
[0.98,"TECL"],
[0.98,"XLK"],
[0.98,"FTC"],
[0.98,"PWB"],
[0.97,"FLGE"],
[0.97,"CSM"],
[0.97,"QQEW"],
[0.97,"TMFC"],
[0.97,"VOT"],
[0.97,"IXN"],
[0.97,"QUAL"],
[0.97,"AIEQ"],
[0.97,"FPX"],
[0.97,"SKYY"],
[0.97,"IWP"],
[0.97,"QQQE"],
[0.97,"PDP"],
[0.97,"ESGU"],
[0.96,"JHML"],
[0.96,"XNTK"],
[0.96,"FV"],
[0.96,"IWL"],
[0.96,"FDN"],
[0.96,"RYT"],
[0.96,"FEX"],
[0.96,"ACWI"],
[0.96,"TDIV"],
[0.96,"SUSA"],
[0.96,"FDIS"],
[0.96,"URTH"],
[0.96,"LRGF"],
[0.96,"IOO"],
[0.96,"FVC"],
[0.96,"VT"],
[0.96,"JKH"],
[0.96,"IYC"],
[0.96,"VO"],
[0.95,"DGRW"],
[0.95,"SPHB"],
[0.95,"VCR"],
[0.95,"FTCS"],
[0.95,"SECT"],
[0.95,"QUS"],
[0.95,"XLY"],
[0.95,"VTHR"],
[0.95,"VBK"],
[0.95,"FNY"],
[0.95,"IWR"],
[0.95,"DIA"],
[0.95,"AOA"],
[0.95,"VXF"],
[0.95,"XT"],
[0.94,"DDM"],
[0.94,"IPAY"],
[0.94,"UDOW"],
[0.94,"FXL"],
[0.94,"JKD"],
[0.94,"RSP"],
[0.94,"ROUS"],
[0.94,"SCHM"],
[0.94,"FVAL"],
[0.94,"PXMG"],
[0.94,"PNQI"],
[0.94,"RXI"],
[0.94,"CRBN"],
[0.94,"TILT"],
[0.94,"IGV"],
[0.94,"QDF"],
[0.94,"SHE"],
[0.94,"JHMM"],
[0.94,"JPUS"],
[0.94,"FNDX"],
[0.93,"AOR"],
[0.93,"QTEC"],
[0.93,"FNX"],
[0.93,"CWB"],
[0.93,"FXH"],
[0.93,"DEUS"],
[0.93,"GVIP"],
[0.93,"VB"],
[0.93,"PRF"],
[0.93,"ARKW"],
[0.93,"RWL"],
[0.93,"IWO"],
[0.93,"DGRO"],
[0.93,"FDRR"],
[0.93,"RYH"],
[0.93,"IJK"],
[0.93,"IYJ"],
[0.93,"RDVY"],
[0.93,"CFA"],
[0.92,"FDLO"],
[0.92,"MDYG"],
[0.92,"VLUE"],
[0.92,"IVOG"],
[0.92,"VTWG"],
[0.92,"EQAL"],
[0.92,"ACWF"],
[0.92,"FYC"],
[0.92,"EUSA"],
[0.92,"SCHA"],
[0.92,"COWZ"],
[0.92,"VIG"],
[0.92,"GSEW"],
[0.92,"FFTY"],
[0.92,"USMF"],
[0.92,"VOX"],
[0.92,"FINX"],
[0.92,"FTLS"],
[0.92,"DLN"],
[0.91,"ACIM"],
[0.91,"SPSM"],
[0.91,"MVV"],
[0.91,"IWM"],
[0.91,"TNA"],
[0.91,"URTY"],
[0.91,"FHLC"],
[0.91,"UWM"],
[0.91,"PKW"],
[0.91,"MOAT"],
[0.91,"VHT"],
[0.91,"VTV"],
[0.91,"IJH"],
[0.91,"MDY"],
[0.91,"MIDU"],
[0.91,"CATH"],
[0.91,"IHI"],
[0.91,"VTWO"],
[0.91,"IVOO"],
[0.91,"DWAS"],
[0.91,"XSW"],
[0.91,"MGV"],
[0.91,"AOM"],
[0.91,"ICVT"],
[0.91,"PSJ"],
[0.91,"SIZE"],
[0.91,"FNGU"],
[0.91,"SPMD"],
[0.91,"XITK"],
[0.91,"IYH"],
[0.90,"FNDA"],
[0.90,"CIBR"],
[0.90,"IXP"],
[0.90,"FYX"],
[0.90,"SMLF"],
[0.90,"PRFZ"],
[0.90,"QYLD"],
[0.90,"IJT"],
[0.90,"JKG"],
[0.90,"SLYG"],
[0.90,"ACWV"],
[0.90,"RXL"],
[0.90,"VOE"],
[0.90,"VIS"],
[0.90,"XLC"],
[0.90,"VIOG"],
[0.90,"HACK"],
[0.90,"IWD"],
[0.90,"VUSE"],







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
"UPRO",
"IEMG",
"VEA",
"XOP",
"VWO",
"JNK",
"XLK",
"XLI",
"SSO",
"SPXL",
"GUSH",
"ERX",
"IEFA",
"GDXJ",
"XLV",
"EWJ",
"OIH",
"KRE",
"IYR",
"SCHF",
"EZU",
"TQQQ",
"MCHI",
"XLY",
"IVV",
"ACWI",
"VGK",
"IJR",
"IEF",
"USMV",
"VEU",
"DIA",
"FEZ",
"VTI",
"IWD",
"VOO",
"EWG",
"ACWX",
"SPLV",
"ITOT",
"VT",
"XLC",
"EWU",
"IWF",

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
