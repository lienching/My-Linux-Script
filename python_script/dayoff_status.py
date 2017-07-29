#!/usr/bin/python
#coding=utf8
import sys
if not sys.version_info[0]==3:
    print( "Error, You need python3" )
    exit(1)

from urllib.request import urlopen
import ssl
import lxml.html

BASE_URL="http://www.dgpa.gov.tw"
PAGE_URL="/nds.html"

def main():
    html_string=''
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response=urlopen("https://www.dgpa.gov.tw", context=ctx)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
        html=lxml.html.fromstring(html_string)
        tb1=[]
        rows = html.cssselect("tr")
        for row in rows:
            tb1.append([])
            for td in row.cssselect("td"):
                tb1[-1].append(td.text_content())
        del tb1[0:5];
        tb1.pop()
        for n in tb1:
            for j in n:
                if u"地區" in j:
                    n.remove(j)
        while True:
            try:
                print("輸入縣市(輸入exit 結束程式):")
                user=input()
                finded=False
                if user is "exit" or "exit" in user:
                    break
                for n in tb1:
                    if user in n[0]:
                        print(n[1])
                        finded=True
                        break
                if not finded:
                    print(user + " no find!\n")
                print("\n")
            except KeyboardInterrupt:
                break
        print("Program Ended!")
    except Exception as e:
        print(str(e))

main()
