from ddcmaker.public.advanced_mode import ad_mode


class sonar(ad_mode):
    def __init__(self):
        super().__init__()
        self.name = "sonar.py"

    def sonar(self):
        print("自动避障")
        super().run()


class cv_color(ad_mode):
    def __init__(self):
        super().__init__()
        self.list = ["cv_color_stream.py", "cv_track_stream.py", "cv_color_tracking.py",
                     "hexapod_balance.py", "cv_linefollow.py"]

    def identifying(self):
        print("识别颜色")
        self.name = self.list[0]
        super().run()

    def tracking(self):
        print("云台追踪")
        self.name = self.list[1]
        super().run()

    def follow(self):
        print("机体跟随")
        self.name = self.list[2]
        super().run()

    def balance(self):
        print("自动平衡")
        self.name = self.list[3]
        super().run()

    def linefollow(self):
        print("自动巡线")
        self.name = self.list[4]
        super().run()
