from ddcmaker.public.advanced_mode import ad_mode


class cv_mode(ad_mode):
    def __init__(self):
        super().__init__()
        self.Xpath = "python3 /home/pi/human_code/"
        self.list = ["cv_find_stream.py", "cv_color_stream.py", "cv_find_hand.py", "cv_line_patrol.py", "cv_track_stream.py"]

    def automatic_shot(self):
        print("自动射门")
        self.name = self.list[0]
        super().run()

    def identifying(self):
        print("颜色识别")
        self.name = self.list[1]
        super().run()

    def find_hand(self):
        print("手势识别")
        self.name = self.list[2]
        super().run()

    def linefollow(self):
        print("自动巡线")
        self.name = self.list[3]
        super().run()

    def tracking(self):
        print("云台追踪")
        self.name = self.list[4]
        super().run()
