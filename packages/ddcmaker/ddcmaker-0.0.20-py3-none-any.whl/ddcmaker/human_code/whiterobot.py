
from ddcmaker.human_code.__init__ import *

class robot(object):

    def up(self, step=1):
        lsc.RunActionGroup(0, step)
        # lsc.WaitForFinish(5000)
        time.sleep(1.2)
        print("机器人站立")

    def down(self, step=1):
        lsc.RunActionGroup(14, step)
        # lsc.WaitForFinish(5000)
        time.sleep(1)
        print("机器人蹲下")

    def check(self, step=1):
        lsc.RunActionGroup(188, step)
        # lsc.WaitForFinish(5000)
        time.sleep(1)
        print("机器人自检")

    def forward(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(1, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(2)
            print("机器人前进")

    def backward(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(2, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(2)
            print("机器人后退")

    def left(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(3, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(2)
            print("<---机器人左转")

    def right(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(4, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(2)
            print("机器人右转--->")


    def nod(self, step=1):
        for i in range(step):
            PWMServo.setServo(1, 1800, 200)
            time.sleep(0.3)
            PWMServo.setServo(1, 1200, 200)
            time.sleep(0.3)
            PWMServo.setServo(1, 1500, 100)
            time.sleep(1)
            print("机器人点头")

    def shaking_head(self, step=1):
        for i in range(step):
            PWMServo.setServo(2, 1800, 200)
            time.sleep(0.4)
            PWMServo.setServo(2, 1200, 200)
            time.sleep(0.4)
            PWMServo.setServo(2, 1500, 100)
            time.sleep(1)
            print("机器人摇头")

    '''这里的动作组不再是点头摇头了，需要重新写'''
    # =======================================================
    def left_slide(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(11, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(1)
            print("<<<*****机器人左滑")

    def right_slide(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(12, 1)
            # lsc.WaitForFinish(5000)
            time.sleep(1)
            print("机器人右滑******>>>")

    def push_up(self, step=1):
        lsc.RunActionGroup(7, step)
        time.sleep(7.5)
        print("机器人俯卧撑")

    def abdominal_curl(self, step=1):
        lsc.RunActionGroup(8, step)
        time.sleep(9.8)
        print("机器人仰卧起坐")

    def wave(self, step=1):
        for i in range(step):
            lsc.RunActionGroup(9, 1)
            time.sleep(3.1)
            print("机器人挥手┏(＾0＾)┛")

    def bow(self, step=1):
        lsc.RunActionGroup(10, step)
        time.sleep(4.1)
        print("机器人鞠躬╰(￣▽￣)╭")

    def spread_wings(self, step=1):
        lsc.RunActionGroup(13, step)
        time.sleep(10.5)
        print("机器人大鹏展翅")

    def haha(self, step=1):
        lsc.RunActionGroup(15, step)
        time.sleep(8.2)
        print("机器人哈哈大笑o(*￣▽￣*)o")

    def straight_boxing(self, step=1):
        lsc.RunActionGroup(30, step)
        time.sleep(1.9)
        print("机器人直拳连击")

    def lower_hook_combo(self, step=1):
        lsc.RunActionGroup(31, step)
        time.sleep(2.8)
        print("机器人下勾拳连击")

    def left_hook(self, step=1):
        lsc.RunActionGroup(32, step)
        time.sleep(1.7)
        print("机器人左勾拳")

    def right_hook(self, step=1):
        lsc.RunActionGroup(33, step)
        time.sleep(1.4)
        print("机器人右勾拳")

    def punching(self, step=1):
        lsc.RunActionGroup(34, step)
        time.sleep(2)
        print("机器人攻步冲拳")

    def crouching(self, step=1):
        lsc.RunActionGroup(35, step)
        time.sleep(3)
        print("机器人八字蹲拳")

    def yongchun(self, step=1):
        lsc.RunActionGroup(36, step)
        time.sleep(2.5)
        print("机器人咏春拳")

    def beat_chest(self, step=1):
        lsc.RunActionGroup(37, step)
        time.sleep(7)
        print("机器人捶胸")

    def left_side_kick(self, step=1):
        lsc.RunActionGroup(50, step)
        time.sleep(1.5)
        print("机器人左侧踢")

    def right_side_kick(self, step=1):
        lsc.RunActionGroup(51, step)
        time.sleep(2)
        print("机器人右侧踢")

    def left_foot_shot(self, step=1):
        lsc.RunActionGroup(52, step)
        time.sleep(1.5)
        print("机器人左脚射门")

    def right_foot_shot(self, step=1):
        lsc.RunActionGroup(53, step)
        time.sleep(1.5)
        print("机器人右脚射门")

    def show_poss(self, step=1):
        print("机器人摆拍poss")
        lsc.RunActionGroup(60, step)
        time.sleep(60)

    def inverted_standing(self, step=1):
        lsc.RunActionGroup(101, step)
        time.sleep(5)
        print("机器人前倒站立")

    def rear_stand_up(self, step=1):
        lsc.RunActionGroup(102, step)
        time.sleep(5)
        print("机器人后倒站立")


'''
你好呀，为什么要打开这个文件
'''
