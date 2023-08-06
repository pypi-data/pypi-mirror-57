import os


def get_eq_type():
    if os.path.exists("/home/pi/human"):
        return 0
    elif os.path.exists("/home/pi/Car"):
        return 1
    elif os.path.exists("/home/pi/human_code"):
        return 2
    elif os.path.exists("/home/pi/spider"):
        return 3
    else:
        return -1
