import paho.mqtt.client as mqtt;
import PIL
import PIL.Image as pilimg
from PIL import Image
import datetime

publish.single("mydata/whoareyou/request", "videostreaming", hostname="ec2-52-78-81-16.ap-northeast-2.compute.amazonaws.com")


# on_connect는 subscriber가 브로커에 연결하면서 호출할 함수, rc가 0이면 정상 연결이 됐다는 의미
def on_connect(client, userdata, flags, rc):
    print("connect.." + str(rc));
    if rc == 0: # 0이 정상 연결 -> 구독신청
        client.subscribe("mydata/whoareyou/getimage"); # Topic명
    else:
        print("연결 실패");

# 메시지가 도착됐을 때 처리할 일들 - 여러가지 장비 제어하기, 값을 MongoDB에 저장 (ex) led on/off, 문 개폐
def on_message(client, userdata, msg):
    now = datetime.datetime.now()
    filename = '%s.jpg' % now
    f = open(filename, "wb");
    f.write(msg.payload);
    f.close();
    im = Image.open(filename);
    image_bytes2 = im.tobytes()
    new_image = pilimg.frombytes("RGB", (im.width, im.height), image_bytes2)
    new_image.show()

# callback함수 : 이벤트가 발생했을 때 실행할 메소드

mqttClient = mqtt.Client();
mqttClient.on_connect = on_connect; # 브로커에 연결이 되면 on_connect라는 함수가 실행되도록 등록 (핸들러함수(콜백) 등록)
mqttClient.on_message = on_message; # 브로커에서 메시지가 전달되면 내가 등록해놓은 on_message함수가 실행
mqttClient.connect("ec2-52-78-81-16.ap-northeast-2.compute.amazonaws.com", 1883, 60); # 브로커에 연결하기 # 연결 # keepalive : 브로커와 통신할 최대 시간
mqttClient.loop_forever(); # 토픽이 전달될 때 까지 수신 대기