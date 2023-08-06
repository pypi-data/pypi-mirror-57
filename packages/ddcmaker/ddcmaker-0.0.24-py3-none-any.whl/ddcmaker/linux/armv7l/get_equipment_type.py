import os
import ddcmaker


def get_eq_type():
    path_dict = {"/home/pi/human": 0, "/home/pi/Car": 1, "/home/pi/human_code": 2, "/home/pi/spider": 3}
    for key in path_dict.keys():
        if os.path.exists(key):
            return path_dict[key]
    return -1


def get_maker_name():
    maker_list = {-1: "", 0: "机器人", 1: "无人车", 2: "机器人", 3: "六足蜘蛛"}
    makername = maker_list[get_eq_type()]
    return makername


def init_human():
    r = ddcmaker.Robot()
    r.init_head()
    r.init_body()


def init_spider():
    s = ddcmaker.Spider()
    s.init_head()
    s.init_body()


def init_car():
    c = ddcmaker.Car()
    c.stop()


def get_init_func():
    if get_eq_type()in [0, 2]:
        init_human()
    elif get_eq_type() == 3:
        init_spider()
    elif get_eq_type() == 1:
        init_car()
