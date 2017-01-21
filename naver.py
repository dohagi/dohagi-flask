#from flask import (
#        Flask,
#)
import json
import os
import sys
import urllib.request
Naver_CL_ID = "cHvFt2qeZlFUEs1Cwkew"
Naver_CL_SEC = "jcyxUbZffT"
""" If we use flask,
>>> def add_routes(app):
...     app.route("/api/searchNotebook/")(searchNotebook)
...     app.route("/api/searchSmartphone/")(searchSmartphone)
"""
def searchNotebook():
    encText = urllib.parse.quote("노트북")
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=100"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", Naver_CL_ID)
    request.add_header("X-Naver-Client-Secret", Naver_CL_SEC)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        #print(response_body.decode('utf-8'))
        result = []
        names = []
        items = json.loads(response_body.decode('utf-8'))['items']
        for item in items:
            d = {}
            name = item['title'].replace('<b>','')
            name = name.replace('</b>','')
            if name in names:
                continue
            names.append(name)
            d['name'] = name
            d['brand'] = name.split()[0]
            d['lprice'] = item['lprice']
            d['image'] = item['image']
            result.append(d)

        return result
    else:
        print("Error Code:" + rescode)

def searchSmartphone():
    encText = urllib.parse.quote("스마트폰")
    url = "https://openapi.naver.com/v1/search/shop?query=" + encText + "&display=100"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", Naver_CL_ID)
    request.add_header("X-Naver-Client-Secret", Naver_CL_SEC)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        result = []
        names = []
        items = json.loads(response_body.decode('utf-8'))['items']
        for item in items:
            d = {}
            name = ""
            tmp = item['title'].replace('<b>','')
            tmp = tmp.replace('</b>','')
            idx = tmp.find('[')
            if idx == 0:
                continue

            if idx > 0:
                tmp = tmp[:idx-1]
            tmp = tmp.split()
            if tmp[0] == "애플":
                name = tmp[1] + " " + tmp[2]
            else:
                name = tmp[-1]
            if name in names:
                continue

            names.append(name)
            d['name'] = name
            d['brand'] = tmp[0]
            d['image'] = item['image']
            result.append(d)
        return result
    else:
        print("Error Code:" + rescode)
""" Test code
>>> # items = searchSmartphone()
>>> items = searchNotebook()
>>> for item in items:
...     print(item)
"""
