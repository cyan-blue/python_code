#!/usr/bin/python
# coding=utf-8
import time,datetime  
import urllib2 
def chk_qq(qqnum):
  chkurl = 'http://wpa.paipai.com/pa?p=1:'+`qqnum`+':17'
  a = urllib2.urlopen(chkurl)  
  length=a.headers.get("content-length")  
  a.close()  
  print datetime.datetime.now()
  print length 
  if length=='2348':  
    return 'Online'
  elif length=='2205':  
    return 'Offline'
  else:  
    return 'Unknown Status!'
def writestate(statenow):
  f=open(str(qq),'a')
  m=str(datetime.datetime.now())+"===state===="+statenow+"\n\r"
  f.write(m)
  f.close()
qq = 907790764

if __name__=='__main__':
  while 1:
    stat = chk_qq(qq)
    writestate(stat)
    time.sleep(10) ##多长时间测一次
    print `qq` + ' is ' + stat
