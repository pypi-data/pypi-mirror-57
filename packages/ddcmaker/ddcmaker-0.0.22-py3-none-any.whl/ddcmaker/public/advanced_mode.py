"""高级模式"""
import ddcmaker
import subprocess


class ad_mode(object):

    def __init__(self, timeout=30):
        self.__version__ = ddcmaker.__version__
        self.Xpath = "python3 /home/pi/hexapod/"
        self.sleeptime = timeout
        self.name = ""
        # self.list = ["sonar.py", "cv_color_stream.py", "cv_track_stream.py", "cv_color_tracking.py", "hexapod_balance.py", "cv_linefollow.py"]
        self.list = []

    def run(self):
        # os.system(self.Xpath+self.name)
        # print("抢夺舵机控制权限…………")
        from ddcmaker.public import killprocess
        # for s in self.list:
        #     killprocess.kill_process(s)
        cmd = self.Xpath + self.name
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            try:
                proc.communicate(timeout=self.sleeptime)
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        # time.sleep(self.sleeptime)
        finally:
            killprocess.kill_process(self.name)
