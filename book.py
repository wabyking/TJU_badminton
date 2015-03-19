# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def book(name,pwd,mouth,day,time,cdinfoid):

    #第一步登录
    payload = {'name': name, 'pwd': pwd}  
    r = requests.get("http://115.24.255.82/index.php/Book/Login/authCheck.html", params=payload)
    print r.text#输出登录成功与否

    _cookies = r.cookies
    book=requests.get("http://115.24.255.82/index.php/Book/Book/index.html",cookies=_cookies)


    #第二步 初预定获取预定编号各种信息
    #日期
    #mouth="03"
    #day="20"
    #time="00017"#  #此处是重点 早上的时间编号是00017 
    cg="01"
    #cdinfoid="2019"       #20XY，其中XY是场地编号  此处编号是17
    preBook=requests.get("http://115.24.255.82//index.php/Book/Book/index4?day=2015-"+mouth+"-"+day+"&time="+time+"&cg=01&cdinfoid="+cdinfoid,cookies=_cookies)



    #print preBook.text.encode("GBK", "ignore")  
    soup = BeautifulSoup(preBook.text)
    if len(soup.find_all("input", attrs={"type": "hidden","name":"SEQ_NO"}))==0:
        print "wait..."
        return 0
    SEQ_NO=soup.find_all("input", attrs={"type": "hidden","name":"SEQ_NO"})[0]['value']
    CELL_PHONE=soup.find_all("input", attrs={"type": "hidden","name":"CELL_PHONE"})[0]['value']
    REAL_NAME=soup.find_all("input", attrs={"type": "hidden","name":"REAL_NAME"})[0]['value']
    __hash__=soup.find_all("input", attrs={"type": "hidden","name":"__hash__"})[0]['value']
    print REAL_NAME
    print CELL_PHONE
    print SEQ_NO
    print __hash__

    data={
        '__hash__':__hash__,
	'CELL_PHONE':CELL_PHONE,
	'REAL_NAME':REAL_NAME,
	'CGINFO_ID':'02',
	'CDINFO_ID':cdinfoid,
	'SEQ_NO':SEQ_NO,
	'PRICE':'5',
	'DISCOUNT':'1',
	'PRICE_FINAL':'5',

    }

    #第三步  确认预定 
    realBook=requests.post("http://115.24.255.82//index.php/Book/Book/order.html",cookies=_cookies,data=data)

    print realBook.text.encode("GBK", "ignore")  




if __name__ == "__main__":
    book("yourusername","yourpassword","03","22","00017","2019")





    
