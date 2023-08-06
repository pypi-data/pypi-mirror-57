#!/usr/bin/python
from ddcmaker.linux.armv7l import get_equipment_type as ge  # line:4

if ge.get_eq_type() == 3 or ge.get_eq_type() == 2:  # line:6
    import serial  # line:7
    import pigpio  # line:8
    import time  # line:9
    import ctypes  # line:10

    LOBOT_SERVO_FRAME_HEADER = 0x55  # line:12
    LOBOT_SERVO_MOVE_TIME_WRITE = 1  # line:13
    LOBOT_SERVO_MOVE_TIME_READ = 2  # line:14
    LOBOT_SERVO_MOVE_TIME_WAIT_WRITE = 7  # line:15
    LOBOT_SERVO_MOVE_TIME_WAIT_READ = 8  # line:16
    LOBOT_SERVO_MOVE_START = 11  # line:17
    LOBOT_SERVO_MOVE_STOP = 12  # line:18
    LOBOT_SERVO_ID_WRITE = 13  # line:19
    LOBOT_SERVO_ID_READ = 14  # line:20
    LOBOT_SERVO_ANGLE_OFFSET_ADJUST = 17  # line:21
    LOBOT_SERVO_ANGLE_OFFSET_WRITE = 18  # line:22
    LOBOT_SERVO_ANGLE_OFFSET_READ = 19  # line:23
    LOBOT_SERVO_ANGLE_LIMIT_WRITE = 20  # line:24
    LOBOT_SERVO_ANGLE_LIMIT_READ = 21  # line:25
    LOBOT_SERVO_VIN_LIMIT_WRITE = 22  # line:26
    LOBOT_SERVO_VIN_LIMIT_READ = 23  # line:27
    LOBOT_SERVO_TEMP_MAX_LIMIT_WRITE = 24  # line:28
    LOBOT_SERVO_TEMP_MAX_LIMIT_READ = 25  # line:29
    LOBOT_SERVO_TEMP_READ = 26  # line:30
    LOBOT_SERVO_VIN_READ = 27  # line:31
    LOBOT_SERVO_POS_READ = 28  # line:32
    LOBOT_SERVO_OR_MOTOR_MODE_WRITE = 29  # line:33
    LOBOT_SERVO_OR_MOTOR_MODE_READ = 30  # line:34
    LOBOT_SERVO_LOAD_OR_UNLOAD_WRITE = 31  # line:35
    LOBOT_SERVO_LOAD_OR_UNLOAD_READ = 32  # line:36
    LOBOT_SERVO_LED_CTRL_WRITE = 33  # line:37
    LOBOT_SERVO_LED_CTRL_READ = 34  # line:38
    LOBOT_SERVO_LED_ERROR_WRITE = 35  # line:39
    LOBOT_SERVO_LED_ERROR_READ = 36  # line:40
    pi = pigpio.pi()  # line:42
    serialHandle = serial.Serial("/dev/ttyAMA0", 115200)  # line:43


    def portInit():  # line:46
        pi.set_mode(17, pigpio.OUTPUT)  # line:47
        pi.write(17, 0)  # line:48
        pi.set_mode(27, pigpio.OUTPUT)  # line:49
        pi.write(27, 1)  # line:50


    portInit()  # line:53


    def portWrite():  # line:56
        pi.write(27, 1)  # line:57
        pi.write(17, 0)  # line:58


    def portRead():  # line:61
        pi.write(17, 1)  # line:62
        pi.write(27, 0)  # line:63


    def portRest():  # line:66
        time.sleep(0.1)  # line:67
        serialHandle.close()  # line:68
        pi.write(17, 1)  # line:69
        pi.write(27, 1)  # line:70
        serialHandle.open()  # line:71
        time.sleep(0.1)  # line:72


    def checksum(OO0O0O000OO0O0000):  # line:75
        O0000OO00O0OO0O0O = 0x00  # line:77
        for OO00O00OO0O0OOO0O in OO0O0O000OO0O0000:  # line:78
            O0000OO00O0OO0O0O += OO00O00OO0O0OOO0O  # line:79
        O0000OO00O0OO0O0O = O0000OO00O0OO0O0O - 0x55 - 0x55  # line:80
        O0000OO00O0OO0O0O = ~O0000OO00O0OO0O0O  # line:81
        return O0000OO00O0OO0O0O & 0xff  # line:82


    def serial_serro_wirte_cmd(id=None, w_cmd=None, dat1=None, dat2=None):  # line:85
        portWrite()  # line:87
        O000O00OO0OOOO0OO = bytearray(b'\x55\x55')  # line:88
        O000O00OO0OOOO0OO.append(id)  # line:89
        if dat1 is None and dat2 is None:  # line:91
            O000O00OO0OOOO0OO.append(3)  # line:92
        elif dat1 is not None and dat2 is None:  # line:93
            O000O00OO0OOOO0OO.append(4)  # line:94
        elif dat1 is not None and dat2 is not None:  # line:95
            O000O00OO0OOOO0OO.append(7)  # line:96
        O000O00OO0OOOO0OO.append(w_cmd)  # line:98
        if dat1 is None and dat2 is None:  # line:100
            pass  # line:101
        elif dat1 is not None and dat2 is None:  # line:102
            O000O00OO0OOOO0OO.append(dat1 & 0xff)  # line:103
        elif dat1 is not None and dat2 is not None:  # line:104
            O000O00OO0OOOO0OO.extend([(0xff & dat1), (0xff & (dat1 >> 8))])  # line:105
            O000O00OO0OOOO0OO.extend([(0xff & dat2), (0xff & (dat2 >> 8))])  # line:106
        O000O00OO0OOOO0OO.append(checksum(O000O00OO0OOOO0OO))  # line:108
        serialHandle.write(O000O00OO0OOOO0OO)  # line:110


    def serial_servo_read_cmd(id=None, r_cmd=None):  # line:113
        portWrite()  # line:114
        OOOO0OO00O0O00OOO = bytearray(b'\x55\x55')  # line:115
        OOOO0OO00O0O00OOO.append(id)  # line:116
        OOOO0OO00O0O00OOO.append(3)  # line:117
        OOOO0OO00O0O00OOO.append(r_cmd)  # line:118
        OOOO0OO00O0O00OOO.append(checksum(OOOO0OO00O0O00OOO))  # line:119
        serialHandle.write(OOOO0OO00O0O00OOO)  # line:120
        time.sleep(0.00034)  # line:121


    def serial_servo_get_rmsg(OOO0000000OO0000O):  # line:124
        serialHandle.flushInput()  # line:125
        portRead()  # line:126
        time.sleep(0.005)  # line:127
        OOO0O00OO0OO0O0O0 = serialHandle.inWaiting()  # line:128
        if OOO0O00OO0OO0O0O0 != 0:  # line:129
            O0OOO0O00O00OOOO0 = serialHandle.read(OOO0O00OO0OO0O0O0)  # line:130
            if O0OOO0O00O00OOOO0[0] == 0x55 and O0OOO0O00O00OOOO0[1] == 0x55 and O0OOO0O00O00OOOO0[
                4] == OOO0000000OO0000O:  # line:132
                OO00O0OOOO000O00O = O0OOO0O00O00OOOO0[3]  # line:134
                serialHandle.flushInput()  # line:135
                if OO00O0OOOO000O00O == 4:  # line:136
                    return O0OOO0O00O00OOOO0[5]  # line:137
                elif OO00O0OOOO000O00O == 5:  # line:138
                    O0O0O00O00OO0OO00 = 0xffff & (
                                O0OOO0O00O00OOOO0[5] | (0xff00 & ((O0OOO0O00O00OOOO0[6]) << 8)))  # line:139
                    return ctypes.c_int16(O0O0O00O00OO0OO00).value  # line:140
                elif OO00O0OOOO000O00O == 7:  # line:141
                    OOO00000OOO000000 = 0xffff & (
                                O0OOO0O00O00OOOO0[5] | (0xff00 & ((O0OOO0O00O00OOOO0[6]) << 8)))  # line:142
                    O0OOO000OO0OOO00O = 0xffff & (
                                O0OOO0O00O00OOOO0[7] | (0xff00 & ((O0OOO0O00O00OOOO0[8]) << 8)))  # line:143
                    return ctypes.c_int16(OOO00000OOO000000).value, ctypes.c_int16(O0OOO000OO0OOO00O).value  # line:144
            else:  # line:145
                return None  # line:146
        else:  # line:147
            serialHandle.flushInput()  # line:148
            return None  # line:150
