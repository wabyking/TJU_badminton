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
            count++
            book("2014216003","123456","03","21","00029","2019")#00026是下午4：00~5：00那场吗？
            book("2014216003","123456","03","21","00029","2018")
            book("2014216103","123456","03","21","00030","2018")
            book("2014216103","123456","03","21","00030","2018")
            continue
        if(cmp(now,end)>0):
            return 0;
        


if __name__ == "__main__":
    if autoBook()==0:
        print "over"
