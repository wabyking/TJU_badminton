# -*- coding: utf-8 -*-
import time
from book import *


start="11-58-59"
end="12-01-01"
count=0
def autoBook():
    while(1):
        now=time.strftime('%H-%M-%S',time.localtime(time.time()))
        print now        
        if (cmp(start,now)<0 and cmp(now,end)<0):
            print "第"+str(count)+"次尝试："+now
            count+=1
            book("username1","psw1","03","21","00029","2019")#00029是下午4：00~5：00那场吗？
            book("username1","psw1","03","21","00029","2018")
            book("username2","psw2","03","21","00030","2018")#00029是时间编号，00017是早上最早的一场
            book("username2","psw2","03","21","00030","2019")#2019是19号场地
            continue
        if(cmp(now,end)>0):
            return 0;
        


if __name__ == "__main__":
    if autoBook()==0:
        print "over"
