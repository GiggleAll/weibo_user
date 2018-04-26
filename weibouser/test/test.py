# -*- coding: utf-8 -*-
# import requests
# import time
# # url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page=1&lefnav=0"
# # url = "https://weibo.com"
url = "https://weibo.com/aj/v6/comment/big?ajwvr=6&id=4222889714121544&page=1&filter=all&filter_tips_before=1&from=singleWeiBo"
# url = "https://ynuf.alipay.com/service/um.json"
# url = "https://log.mmstat.com/y.gif?logtype=0&title=&pre=https%3A%2F%2Fweibo.com%2F&cache=b8eb3f0&scr=1680x1050&cna=xcUvE92ba2YCAW/GGDiiL8tG&spm-cnt=0.0.0.0.5f710z6S0z6So0&category=&userid=&aplus&yunid=&7eebe1e18e57e&trid=0bfa917715223179298013918e&asid=AQAAAABpurxaTvhWCAAAAACyIcNpRur1BA==&p=1&o=linux&b=chrome64&s=1680x1050&w=webkit&ism=other&lver=8.3.8&jsver=aplus_std&pver=0.3.14&tag=1&stag=-1&lstag=-1"
# url = "https://sbeacon.sina.com.cn/a.gif?V=2.2.4.20141125&CI=sz:1680x1050|dp:24|ac:Mozilla|an:Netscape|cpu:undefined|pf:Linux%20x86_64|jv:1.3|ct:unkown|lg:zh-CN|tz:-8|fv:undefined|ja:0&PI=pid:0-9999-0-0-1|st:0|et:2|ref:https%3A//passport.weibo.com/visitor/visitor%3Fentry%3Dminiblog%26a%3Denter%26url%3Dhttps%253a%252f%252fweibo.com%252f%26domain%3D.weibo.com%26ua%3Dphp-sso_sdk_client-0.6.23%26_rand%3D1522317928.2563|hp:unkown|PGLS:|ZT:|MT:|keys:|dom:920|ifr:1|nld:747|drd:102|bp:0|url:&UI=vid:4661687872336.988.1522317929794|sid:4661687872336.988.1522317929794|lv::1:1:1|un:|uo:|ae:|su:0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFGbbjnXo4MpW75iedxJrZO&EX=ex1:WEIBO-V6|ex2:&gUid_1522317929803"
# url = "https://login.taobao.com/member/login.jhtml?from=wbfast&style=wbfast&goto=http%3A%2F%2Fweibo.com%2Fa%2Fbind%2Flogin%3Fentry%3Dtaobao%26sid%3D014c610096183a8b5a2cf21ae26cab75"
# url = "https://weibo.com/aj/v6/top/topnavthird?ajwvr=6&url=https%253A%252F%252Fweibo.com%252F&uid=&lang=zh-cn&islogin=0&_t=1&_v=STK_15223179286751"
# # url = "https://log.mmstat.com/y.gif?logtype=0&title=&pre=https%3A%2F%2Fweibo.com%2F&cache=4f136cc&scr=1680x1050&cna=xcUvE92ba2YCAW/GGDiiL8tG&spm-cnt=0.0.0.0.5f718vuh8vuhu2&category=&userid=&aplus&yunid=&7eebe1e18e57e&trid=0bb3a67415223179287992401e&asid=AQAAAABourxad5U6fwAAAAA0/8JJbdJoHg==&p=1&o=linux&b=chrome64&s=1680x1050&w=webkit&ism=other&lver=8.3.8&jsver=aplus_std&pver=0.3.14&tag=1&stag=-1&lstag=-1"
# url = "https://login.taobao.com/member/login.jhtml?from=wbfast&style=wbfast&goto=http%3A%2F%2Fweibo.com%2Fa%2Fbind%2Flogin%3Fentry%3Dtaobao%26sid%3D014c610096183a8b5a2cf21ae26cab75"
# url = "https://login.taobao.com/member/login.jhtml?from=wbfast&style=wbfast&goto=http%3A%2F%2Fweibo.com%2Fa%2Fbind%2Flogin%3Fentry%3Dtaobao%26sid%3D014c610096183a8b5a2cf21ae26cab75"
# url = "https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.19)&_=1522319136023"
# headers = {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     "Cache-Control": "max-age=0",
#     "Content-Type":"application/x-www-form-urlencoded",
#     # "Connection": "keep-alive",
#     # "Host": "weibo.com",
#     # "Cookie":"TC-Ugrow-G0=968b70b7bcdc28ac97c8130dd353b55e",
#     # "Cookie":"SUB=_2AkMt55wbf8NxqwJRmPESyG7laoV2yg3EieKbu23AJRMxHRl-yj9jqkAYtRB6Bmey9CWu_MUs2geyiqXMf_w4OKjPlMDc",
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
# }
# import json
# import time
# from cookielib import LWPCookieJar
# r = requests.session()
# a = r.get(url=url, headers=headers)
# print a.status_code, a.cookies.get_dict()
# s = requests.get(url=url, headers=headers)
# print s.status_code, s.cookies.get_dict()
#
#
#
# # r.cookies = LWPCookieJar()
# # r.headers = headers
# # a = r.get(url=url)
# #
# # a.cookies.save(filename="test.txt", ignore_discard=True, ignore_expires=True)
# # print a.status_code
# # data = json.loads(a.text)
# # print data["data"]

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# option = Options()
# # option.add_argument("--headless")
# # option.add_argument("--disable-gpu")
# driver = webdriver.Chrome(executable_path="/home/hjliang/下载/chromedriver1", chrome_options=option)
# driver.get(url=url)
# import time
# time.sleep(10)
# print driver.get_cookies()
# print driver.get_cookie("SUB").get
# driver.quit()
import json
import pickle
a = json.loads(u'{"login": "8948961dff729de4991669d2adb9e7a4", "SUB": "_2AkMtnUeMf8NxqwJRmPkWzm3rZI9zyAvEieKbwbZXJRMyHRl-yD9jqkZZtRB6Bh1pY3OUwLjlXAA89P06CTxYmrepBgUb", "SUBP": "0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdTb81ZeCK8snOErWefUhP"}', encoding="utf-8")
print a, a.__class__
