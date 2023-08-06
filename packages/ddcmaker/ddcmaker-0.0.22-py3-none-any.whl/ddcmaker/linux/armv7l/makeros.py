from ddcmaker .server .__init__ import *#line:1
def linux_maker (OOO0O0O00OOOOOO00 ,settime =50 ,offline_running =False ):#line:4
    O0O0OOO0OO0O00OO0 ={"msg":"","code":1 ,"data":{}}#line:5
    OOO0O0O00OOOOOO00 =str (OOO0O0O00OOOOOO00 ,encoding ="u8").replace ('    ','')#line:11
    if not OOO0O0O00OOOOOO00 :#line:13
        O0O0OOO0OO0O00OO0 .update (err ="代码不能为空，请输入代码。")#line:14
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:15
    try :#line:16
        O0000OO0O0O0OO0O0 =eval (OOO0O0O00OOOOOO00 )["code"]#line:17
        O0000OO0O0O0OO0O0 =base64 .b64decode (O0000OO0O0O0OO0O0 )#line:18
        O0000OO0O0O0OO0O0 =str (O0000OO0O0O0OO0O0 ,encoding ="u8")#line:19
    except Exception as OOO0000OOO00OO000 :#line:21
        O0O0OOO0OO0O00OO0 .update (err =OOO0000OOO00OO000 )#line:23
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:25
    if O0000OO0O0O0OO0O0 =="":#line:26
        O0O0OOO0OO0O00OO0 .update (err ="代码不能为空，请输入代码。")#line:27
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:29
    if O0000OO0O0O0OO0O0 !=""and "stop"in O0000OO0O0O0OO0O0 [:15 ]:#line:30
        OO0OO0OO00OOO000O =eval (OOO0O0O00OOOOOO00 )["type"]#line:32
        if OO0OO0OO00OOO000O ==0 :#line:33
            import ddcmaker #line:34
            OOO00OOOO00OO0O0O =ddcmaker .Robot ()#line:35
            OOO00OOOO00OO0O0O .up ()#line:36
        elif OO0OO0OO00OOO000O ==1 :#line:37
            import ddcmaker #line:38
            O0O0000O0O0OOO0O0 =ddcmaker .Car ()#line:39
            O0O0000O0O0OOO0O0 .stop ()#line:40
        else :#line:41
            print ("没有对应创客设备！")#line:42
        O0O0OOO0OO0O00OO0 .update (code =666 ,msg ="动作已经终止",err ="前端请求主动中断动作，杀死运行进程。")#line:43
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:44
    OO0O00OO0000OOO0O =str (time .time ())[-6 :]+".py"#line:46
    OO0OOOO00OO0O00O0 ="resave//"+OO0O00OO0000OOO0O #line:47
    if "###offline_running=True###"in O0000OO0O0O0OO0O0 [:50 ]:#line:50
        offline_running =True #line:51
    with open (OO0OOOO00OO0O00O0 ,"w+",encoding ="u8")as O0O0O00O0O000OO0O :#line:52
        O0O0O00O0O000OO0O .write (O0000OO0O0O0OO0O0 )#line:54
        O0O0O00O0O000OO0O .close ()#line:55
    OOOOOOOOO00O00O00 ="python3  "+OO0OOOO00OO0O00O0 #line:59
    if offline_running !=True :#line:60
        O0OO0OO0O00O0OO0O =open (OO0OOOO00OO0O00O0 ,"r",encoding ="u8")#line:62
        O00000OOOOOOO0OO0 =O0OO0OO0O00O0OO0O .readlines ()#line:63
        O0O00O000OO00000O ="os"#line:65
        for OOO0O0OOOO0OOOOO0 in O00000OOOOOOO0OO0 :#line:66
            O0000O0O00O0OO0OO =OOO0O0OOOO0OOOOO0 .split ("import")#line:67
            if len (O0000O0O00O0OO0OO )>1 :#line:68
                OO0O00O0000O0OO0O =O0000O0O00O0OO0OO [1 ].split (O0O00O000OO00000O )#line:69
                if len (OO0O00O0000O0OO0O )>1 :#line:70
                    O0O0OOO0OO0O00OO0 .update (code =555 ,msg ="安全检查未通过",err ="代码中引入了"+O0O00O000OO00000O +"库，违反了机器人第三定律，终止运行，请检查代码后重新运行")#line:72
                    os .remove (OO0OOOO00OO0O00O0 )#line:73
                    return json .dumps (O0O0OOO0OO0O00OO0 )#line:74
        try :#line:78
            OOOOOO0O0OO00O00O =subprocess .Popen (OOOOOOOOO00O00O00 ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,shell =True )#line:79
        except Exception as OOO0000OOO00OO000 :#line:80
            O0O0OOO0OO0O00OO0 .update (err =OOO0000OOO00OO000 )#line:81
            return json .dumps (O0O0OOO0OO0O00OO0 )#line:83
        try :#line:85
            O000O00O0OOO000O0 ,OO00O0OO0OOOO00O0 =OOOOOO0O0OO00O00O .communicate (timeout =settime )#line:86
        except Exception as OOO0000OOO00OO000 :#line:87
            print ("捕捉错误",OOO0000OOO00OO000 )#line:88
            OOOOOO0O0OOO0O0OO =""#line:90
            if ge .get_eq_type ()==0 or ge .get_eq_type ()==2 :#line:91
                from ddcmaker .public import killprocess #line:92
                killprocess .kill_process (OO0O00OO0000OOO0O )#line:93
                OOOOOO0O0OOO0O0OO ="机器人"#line:94
            if ge .get_eq_type ()==1 :#line:95
                from ddcmaker .public import killprocess #line:96
                killprocess .kill_process (OO0O00OO0000OOO0O )#line:97
                import ddcmaker #line:98
                O000O0O0OO0O00000 =ddcmaker .Car ()#line:99
                O000O0O0OO0O00000 .stop ()#line:100
                OOOOOO0O0OOO0O0OO ="无人车"#line:101
            if ge .get_eq_type ()==3 :#line:102
                from ddcmaker .public import killprocess #line:103
                killprocess .kill_process (OO0O00OO0000OOO0O )#line:104
                OOOOOO0O0OOO0O0OO ="六足蜘蛛"#line:105
            O0O0OOO0OO0O00OO0 .update (code =233 ,msg ="超时主动中断",err ="运行超时，中断"+OOOOOO0O0OOO0O0OO +"操作，"+OOOOOO0O0OOO0O0OO +"一次最长允许运行动作"+str (settime )+"秒")#line:107
        else :#line:109
            if OO00O0OO0OOOO00O0 :#line:110
                O0O0OOO0OO0O00OO0 .update (err =OO00O0OO0OOOO00O0 .decode ("u8"))#line:111
            else :#line:112
                O0O0OOO0OO0O00OO0 .update (code =0 ,msg ="执行成功",data ={"moduleData":[O000O00O0OOO000O0 .decode ("u8")],"printData":O000O00O0OOO000O0 .decode ("u8"),})#line:116
        finally :#line:117
            os .remove (OO0OOOO00OO0O00O0 )#line:119
        print (O0O0OOO0OO0O00OO0 )#line:120
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:121
    else :#line:122
        print ("当前设备脱机运行，不再受到平台约束！")#line:123
        O0O0OOO0OO0O00OO0 .update (code =777 ,msg ="高级模式脱机运行",err ="警告：当前模式为高级模式，设备将执行脱机命令，设备将不会超时中断动作！\n请谨慎使用，仅限教师或者工程师调试使用！！\n若要停止，请等待设备运行结束或者关闭设备电源")#line:125
        def O00000OOOOOO0OOO0 ():#line:127
            try :#line:128
                O0O0O0OO0OO0O0OO0 =subprocess .Popen (OOOOOOOOO00O00O00 ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,shell =True )#line:129
                O0O0O0OO0OO0O0OO0 .communicate (timeout =1000 )#line:130
            except Exception as OO0O0O00OOOO00000 :#line:131
                print (OO0O0O00OOOO00000 )#line:132
            finally :#line:133
                os .remove (OO0OOOO00OO0O00O0 )#line:134
        import threading #line:135
        O00OO000OO0000OO0 =threading .Thread (target =O00000OOOOOO0OOO0 )#line:136
        O00OO000OO0000OO0 .setDaemon (True )#line:137
        O00OO000OO0000OO0 .start ()#line:138
        return json .dumps (O0O0OOO0OO0O00OO0 )#line:139
def windows_maker (OO000OOO00OOOOO0O ):#line:141
    OO0O0000O00O0000O ={"msg":"","code":1 ,"data":{}}#line:142
    OO000OOO00OOOOO0O =str (OO000OOO00OOOOO0O ,encoding ="u8").replace ('    ','')#line:147
    print (OO000OOO00OOOOO0O )#line:148
    try :#line:149
        OOOO0OOOO000OO0O0 =eval (OO000OOO00OOOOO0O )["code"]#line:150
        OOOO0OOOO000OO0O0 =base64 .b64decode (OOOO0OOOO000OO0O0 )#line:151
        OOOO0OOOO000OO0O0 =str (OOOO0OOOO000OO0O0 ,encoding ="u8")#line:152
        print ("取出传入的值",OOOO0OOOO000OO0O0 )#line:153
    except Exception as O0O00OOO00000000O :#line:154
        print (O0O00OOO00000000O )#line:155
        OO0O0000O00O0000O .update (err =O0O00OOO00000000O )#line:156
        return json .dumps (OO0O0000O00O0000O )#line:158
    if OOOO0OOOO000OO0O0 =="":#line:159
        OO0O0000O00O0000O .update (err ="代码不能为空，请输入代码。")#line:160
        return json .dumps (OO0O0000O00O0000O )#line:162
    if OOOO0OOOO000OO0O0 !=""and "stop"in OOOO0OOOO000OO0O0 [:15 ]:#line:163
        print ("终止机器人运动")#line:165
        OO0O0000O00O0000O .update (code =666 ,msg ="动作已经终止",err ="前端请求主动中断动作，杀死运行进程。")#line:166
        return json .dumps (OO0O0000O00O0000O )#line:167
    O0OOOO0OO0OO0O000 =str (time .time ())[-6 :]+".py"#line:169
    print (O0OOOO0OO0OO0O000 )#line:170
    with open (O0OOOO0OO0OO0O000 ,"w+",encoding ="u8")as OO0000000OO0O000O :#line:171
        OO0000000OO0O000O .write (OOOO0OOOO000OO0O0 )#line:173
        OO0000000OO0O000O .close ()#line:174
    O00O00OOOO0OOO0OO ="python "+O0OOOO0OO0OO0O000 #line:177
    print (O00O00OOOO0OOO0OO )#line:178
    try :#line:179
        O0O0OOO0OO0OOO0O0 =subprocess .Popen (O00O00OOOO0OOO0OO ,stdout =subprocess .PIPE ,stderr =subprocess .PIPE ,encoding ="u8",shell =False )#line:180
    except Exception as O0O00OOO00000000O :#line:181
        print (O0O00OOO00000000O )#line:182
        OO0O0000O00O0000O .update (err =O0O00OOO00000000O )#line:183
        return json .dumps (OO0O0000O00O0000O )#line:185
    try :#line:186
        O00OOO000OOO0OOOO ,OO00000O0000OOO0O =O0O0OOO0OO0OOO0O0 .communicate (timeout =60 )#line:187
    except subprocess .TimeoutExpired :#line:188
        O0O0OOO0OO0OOO0O0 .kill ()#line:189
        OO0O0000O00O0000O .update (code =233 ,msg ="机器运行超时，中断机器人链接。")#line:190
    else :#line:191
        if OO00000O0000OOO0O :#line:192
            OO0O0000O00O0000O .update (err =OO00000O0000OOO0O )#line:193
        else :#line:194
            OO0O0000O00O0000O .update (code =0 ,data ={"moduleData":[O00OOO000OOO0OOOO ],"printData":O00OOO000OOO0OOOO ,})#line:198
    finally :#line:199
        os .remove (O0OOOO0OO0OO0O000 )#line:201
    return json .dumps (OO0O0000O00O0000O )#line:202
def Mac_maker ():#line:205
    OOOOOO00OO0OO0OO0 ={"msg":"","code":1 ,"data":{}}#line:206
    OOOOOO00OO0OO0OO0 .update (err ="当前系统为Mac,暂时不支持此系统！")#line:207
    return json .dumps (OOOOOO00OO0OO0OO0 )#line:208
def other_maker ():#line:211
    O0O0OO000OO000O0O ={"msg":"","code":1 ,"data":{}}#line:212
    O0O0OO000OO000O0O .update (err ="你这是啥系统呀，暂时不支持哟！")#line:213
    return json .dumps (O0O0OO000OO000O0O )#line:214
