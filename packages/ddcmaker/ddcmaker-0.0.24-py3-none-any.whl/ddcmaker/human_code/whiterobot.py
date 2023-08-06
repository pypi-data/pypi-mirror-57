from ddcmaker.linux.armv7l import get_equipment_type as ge
from ddcmaker.human_code.human_ssr import serial_human
from ddcmaker.public.basic_mode import ba_mode

if ge.get_eq_type() == 2:

    class robot(ba_mode):
        def __init__(self):
            super().__init__()
            self.name = "机器人"
            self.SSR = serial_human()
            self.sleeptime = 1
            self.nodid = 1
            self.shakingid = 2
            self.Interval_time = 200
            self.homing_angle = 1500
            self.start_angle = 1800
            self.end_angle = 1200

        def init_body(self):
            self.run_action("0")

        def up(self, step):
            self.run_action("0", step, "站立")

        def down(self, step):
            self.run_action("14", step, "蹲下")

        def check(self, step):
            self.run_action("188", step, "自检")

        def forward(self, step):
            self.run_action("1", step, "前进")

        def backward(self, step):
            self.run_action("2", step, "后退")

        def left(self, step):
            self.run_action("3", step, "左转")

        def right(self, step):
            self.run_action("4", step, "右转")

        def left_slide(self, step):
            self.run_action("11", step, "左滑")

        def right_slide(self, step):
            self.run_action("12", step, "右滑")

        def push_up(self, step=1):
            self.run_action("7", step, "俯卧撑")

        def abdominal_curl(self, step=1):
            self.run_action("8", step, "仰卧起坐")

        def wave(self, step):
            self.run_action("9", step, "挥手┏(＾0＾)┛")

        def bow(self, step):
            self.run_action("10", step, "鞠躬╰(￣▽￣)╭")

        def spread_wings(self, step):
            self.run_action("13", step, "大鹏展翅")

        def haha(self, step):
            self.run_action("15", step, "哈哈大笑o(*￣▽￣*)o")

        def straight_boxing(self, step):
            self.run_action("30", step, "直拳连击")

        def lower_hook_combo(self, step):
            self.run_action("31", step, "下勾拳连击")

        def left_hook(self, step):
            self.run_action("32", step, "左勾拳")

        def right_hook(self, step):
            self.run_action("33", step, "右勾拳")

        def punching(self, step):
            self.run_action("34", step, "攻步冲拳")

        def crouching(self, step):
            self.run_action("35", step, "八字蹲拳")

        def yongchun(self, step):
            self.run_action("36", step, "咏春拳")

        def beat_chest(self, step):
            self.run_action("37", step, "捶胸")

        def left_side_kick(self, step):
            self.run_action("50", step, "左侧踢")

        def right_side_kick(self, step):
            self.run_action("51", step, "右侧踢")

        def left_foot_shot(self, step):
            self.run_action("52", step, "左脚射门")

        def right_foot_shot(self, step):
            self.run_action("53", step, "右脚射门")

        def show_poss(self, step):
            self.run_action("60", step, "摆拍poss")

        def inverted_standing(self, step):
            self.run_action("101", step, "前倒站立")

        def rear_stand_up(self, step):
            self.run_action("102", step, "后倒站立")


'''
我喜欢吃蒸鲈鱼，虾鲍鳝，蝴蝶翅
'''
