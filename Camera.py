from picamera import PiCamera
from time import sleep
import datetime


class Camera():
    def __init__(self):
        # ���Ϸ� �����ϱ�
        super().__init__()
        self.camera = PiCamera()
        # ������ 180�� ȸ���ؼ� ����Ѵ�.
        self.camera.rotation = 180
        self.camera.start_preview()
        sleep(1)

    def takepicture(self):
        now = datetime.datetime.now()
        filename = '/home/pi/Pictures/%s.jpg' % now
        self.camera.capture(filename)
        return filename

    def stop(self):
        self.camera.stop_preview() # �̸����� ȭ�� ����
