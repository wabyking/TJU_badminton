# -*- coding: utf-8 -*-
import time,httplib
import threading
def getBeijinTime():
     try:
         conn = httplib.HTTPConnection("www.beijing-time.org")
         conn.request("GET", "/time.asp")
         response = conn.getresponse()
         print response.status, response.reason
         if response.status == 200:
             result = response.read()
             data = result.split("\r\n")
             year = data[1][len("nyear")+1 : len(data[1])-1]
             month = data[2][len("nmonth")+1 : len(data[2])-1]
             day = data[3][len("nday")+1 : len(data[3])-1]
             #wday = data[4][len("nwday")+1 : len(data[4])-1]
             hrs = data[5][len("nhrs")+1 : len(data[5])-1]
             minute = data[6][len("nmin")+1 : len(data[6])-1]
             sec = data[7][len("nsec")+1 : len(data[7])-1]

             beijinTimeStr = "%s/%s/%s %s:%s:%s" % (year, month, day, hrs, minute, sec)
             beijinTime = time.strptime(beijinTimeStr, "%Y/%m/%d %X")
             return beijinTime
     except:
         return None

def syncLocalTime():
     """
     同步本地时间
     """
     beijinTime = getBeijinTime()
     if beijinTime is None:
         timer = threading.Timer(30.0, syncLocalTime)
         timer.start()
     else:
         tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec = beijinTime[:6]
         import os
         os.system("date %d-%d-%d" % (tm_year, tm_mon, tm_mday))     #设置日期
         os.system("time %d:%d:%d.0" % (tm_hour, tm_min, tm_sec))    #设置时间

if __name__=='__main__':
    while True:
        syncLocalTime()
        time.sleep(30)
#该代码片段来自于: http://www.sharejs.com/codes/python/8508