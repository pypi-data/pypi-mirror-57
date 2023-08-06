import socket #line:1
import requests #line:2
import re #line:3
import time #line:4
import json #line:5
def get_mac_address ():#line:7
    import uuid #line:8
    O0O00OO0000O0OO00 =uuid .UUID (int =uuid .getnode ()).hex [-12 :].upper ()#line:9
    return '%s:%s:%s:%s:%s:%s'%(O0O00OO0000O0OO00 [0 :2 ],O0O00OO0000O0OO00 [2 :4 ],O0O00OO0000O0OO00 [4 :6 ],O0O00OO0000O0OO00 [6 :8 ],O0O00OO0000O0OO00 [8 :10 ],O0O00OO0000O0OO00 [10 :])#line:10
def get_ip ():#line:13
    try :#line:14
        OOO0OO0O0000OOOOO =socket .socket (socket .AF_INET ,socket .SOCK_DGRAM )#line:15
        try :#line:16
            OOO0OO0O0000OOOOO .connect (('www.baidu.com',0 ))#line:17
        except :#line:18
            print ("无法连接到外网！")#line:19
        OO0OOO0O0OO0O0OO0 =OOO0OO0O0000OOOOO .getsockname ()[0 ]#line:21
    except :#line:22
        OO0OOO0O0OO0O0OO0 ="x.x.x.x"#line:23
    finally :#line:24
        OOO0OO0O0000OOOOO .close ()#line:25
    return OO0OOO0O0OO0O0OO0 #line:26
def get_extranetip ():#line:29
    try :#line:30
        O0OO0O0OOOO0O000O =requests .get ("http://"+str (time .localtime ().tm_year )+".ip138.com/ic.asp",timeout =2 )#line:31
        O000OOO0O0O0OOO00 =re .search (r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",O0OO0O0OOOO0O000O .content .decode (errors ='ignore')).group (0 )#line:32
        if len (str (O000OOO0O0O0OOO00 ))>7 :#line:33
            return O000OOO0O0O0OOO00 #line:34
    except Exception as O0OO0OO00OOO0O000 :#line:35
        try :#line:36
            OO000OO0OOOO0OOO0 =requests .get ("http://txt.go.sohu.com/ip/soip",timeout =2 ).text #line:37
            O000OOO0O0O0OOO00 =re .findall (r'\d+.\d+.\d+.\d+',OO000OO0OOOO0OOO0 )[0 ]#line:38
            if len (str (O000OOO0O0O0OOO00 ))>7 :#line:39
                return O000OOO0O0O0OOO00 #line:40
        except Exception as O0OO0OO00OOO0O000 :#line:41
            O000OOO0O0O0OOO00 =requests .get ("http://members.3322.org/dyndns/getip",timeout =3 ).text .strip ()#line:42
            if len (str (O000OOO0O0O0OOO00 ))>7 :#line:44
                return O000OOO0O0O0OOO00 #line:45
    print ("暂时无法发出外网请求！")#line:46
def getipadress ():#line:50
    O0OO0OO0OOO0OOOOO =get_ip ()#line:51
    O0OOO0O000O0OO00O =get_mac_address ()#line:52
    OOOO000O00OO00O0O =get_extranetip ()#line:53
    return O0OO0OO0OOO0OOOOO ,O0OOO0O000O0OO00O ,OOOO000O00OO00O0O #line:54
def postaddress (O00O000OOOO0OOO0O ,O00OO0OOOO0000000 ,OO0OO0O0OO00OOO00 ,O00O00O0OOO0OO00O ,O0O0O00O0OOOOOO0O ):#line:57
    OOOO0000OOO000OO0 =json .dumps ({'inIp':O00O000OOOO0OOO0O ,'macAddr':O00OO0OOOO0000000 ,'exIp':OO0OO0O0OO00OOO00 ,'type':O0O0O00O0OOOOOO0O })#line:59
    OO0OO0OO0O0O00O00 ={'content-type':'application/json;charset=UTF-8'}#line:60
    print (OOOO0000OOO000OO0 )#line:61
    O000OOO0OOOOO0O0O =requests .post (O00O00O0OOO0OO00O ,OOOO0000OOO000OO0 ,headers =OO0OO0OO0O0O00O00 )#line:62
    print (O000OOO0OOOOO0O0O )#line:63
    if O000OOO0OOOOO0O0O .status_code ==200 :#line:64
        return O00O000OOOO0OOO0O #line:65
    elif O000OOO0OOOOO0O0O .status_code ==504 :#line:66
        print ("当前服务器接口不通")#line:67
        time .sleep (15 )#line:68
    else :#line:69
        time .sleep (15 )#line:70
        return postaddress (O00O000OOOO0OOO0O ,O00OO0OOOO0000000 ,OO0OO0O0OO00OOO00 ,O00O00O0OOO0OO00O ,O0O0O00O0OOOOOO0O )#line:71
