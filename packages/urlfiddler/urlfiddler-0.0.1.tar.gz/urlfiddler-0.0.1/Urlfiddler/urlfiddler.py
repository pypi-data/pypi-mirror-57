
import urllib, base64
import ssl
import json
import time
import base64

import requests

import urllib3
import random
import os

import pyperclip

urllib3.disable_warnings()
from urllib.parse import quote,unquote

ssl._create_default_https_context = ssl._create_unverified_context
import sys
 

class urlwithfiddlerclass():

  def my_change(self,text): #切割

    if text[0:4]=='POST':#post请求
        urltype='POST'
        text=text[5:]  #切post

    elif text[0:3]=='GET':#get
        urltype='GET'
        text=text[4:]  #切get

        ##print 'urltype=\n',urltype

    fo1=text.find(' ')#切URL
    url=text[0:fo1]  
    ##print 'url=\n',url

    fo1=text.find('\n') #切掉HTTP/1.1
    text=text[fo1+1:]

    fo1=text.find('\n\n') #切掉Head
    head=text[0:fo1]  
    ##print 'head=\n',head

    body=text[fo1+2:]   #切出body
    ##print 'body=\n',body

    return  urltype,url,self.my_change_head(head),body


  def my_change_head(self,head): #处理head
    #print head
    texthead='{'
    while(1):
        fo1=head.find('\n') #切掉Head
        if fo1==-1:
            maohao=head.find(':') #冒号
            texthead=texthead+'\"'+head[0:maohao]+'\":\"'+head[maohao+2:]+'\",'+'\n'
            #print head[maohao+1:]
            break
        ##print 'fo1=\n',fo1
        head2=head[0:fo1]
        head=head[fo1+1:]
        #texthead=
        #print 'head2=\n',head2
        #print 'head=\n',head
        maohao=head2.find(':') #冒号

        texthead=texthead+'\"'+head2[0:maohao]+'\":\"'+head2[maohao+2:]+'\",'+'\n'

    s1=list(texthead)                  #将字符串转换为列表
    s1[-2]='}'
    texthead=''.join(s1)

    #print texthead
    
    aaa=eval(texthead)   #字符串转list

    try:                             #切不必要元素
        del aaa["Content-Length"]
    except:
        pass
    try:
        del aaa["Accept-Encoding"]
    except:
        pass
    try:
        del aaa["Accept-Language"]
    except:
        pass


    #print aaa
    return aaa

  def urlreplace(self,content,textfirst=0,textend=-1,replace=""):  #替换元素
    #print type(3)==type(1)
    if type(textfirst)!=type(1) and type(textfirst)!=type(1.0):                #非数字
        maohao=content.find(textfirst)+len(textfirst)
    else:
        maohao=textfirst

    if type(textend)!=type(1) and type(textend)!=type(1.0):  
        maohao2=content.find(textend)
    else :
        if int(textend)==-1:#默认-1时
            maohao2=len(content)                     ################
        else :
            maohao2=textend

    key1=content[0:int(maohao)]
    key2=content[int(maohao2):]

    key=key1+replace+key2
    return key

  def urlslect(content,textfirst=0,textend=-1):  #找出指定元素
    if type(textfirst)!=type(1) and type(textfirst)!=type(1.0):                #非数字
        maohao=content.find(textfirst)+len(textfirst)
    else:
        maohao=textfirst

    content=content[maohao:] #切无用的头部
    
    if type(textend)!=type(1) and type(textend)!=type(1.0):  
        maohao2=content.find(textend)
    else :
        if int(textend)==-1:#默认-1时
            maohao2=len(content)                     ################
        else :
            maohao2=textend
            
    key=content[:int(maohao2)]

    return key



  def urlwith_raw_getorpost(self,text,cookie=''):       #使用url 的简单getorpost 需要扩展包 raw
    a,b,c,d=self.my_change(text) #urltype,url,self.my_change_head(head),body
    if cookie!='':
        c["Cookie"]=cookie
        
    if a=='GET':
        r = requests.get(b,headers=c, verify=False)
    elif a=='POST':
        r = requests.post(b, data=d,headers=c, verify=False)
    print("status_code:",r.status_code)
    return r.text

