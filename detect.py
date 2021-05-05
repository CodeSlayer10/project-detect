import cv2
# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
import requests
import time
from multiprocessing import Process

class Api1:
    def __init__(self, first, second=None, third=None):
        self.first = first
        self.second = second
        self.third = third

    def Show(self):
        link = "https://codeslayer67.pythonanywhere.com/{}".format(self.first)  # link that is going to be used
        resp = requests.get(link)
        if resp.status_code != 200:
            print(resp.status_code)
        else:
            str_content = resp.content.decode()
            #  print(str_content)
            return str_content

    def UpdateBool(self):
        link = "https://codeslayer67.pythonanywhere.com/{}/{}/{}".format(self.first, self.second, self.third)  # link that is going to be used
        resp = requests.get(link)
        if resp.status_code != 200:
            print(resp.status_code)

        else:
            str_content = resp.content.decode()
            #  print(str_content)
            return str_content




class v1():
    def __init__(self, boolz, times):
        self.boolz = boolz
        self.times = int(times)

    def update(self, new):
        self.boolz = new







item12 = Api1("SB")
item = item12.Show()
boolz = item[10]
boolz = int(boolz)
item_v1 = v1(boolz, 10)
item13 = Api1("SID")
item1 = item13.Show()
id = "".join(item1[8:-3])
item10 = Api1("ID", id, "is_human_there = 0")
item11 = Api1("ID", id, "is_human_there = 1")
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame1 = video_capture.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray1, 1.3, 5)
    print(len(faces), "hhh")
    if len(faces) == 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 250), 2)
            #cv2.putText(frame1, item_v1.boolz, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        if item_v1.boolz != 1:
            new = item11.UpdateBool()
            time.sleep(10)
            print(new[47], "hi")
            item_v1.update(int(new[47]))

    else:
        if item_v1.boolz == 1:
            new = item10.UpdateBool()
            time.sleep(10)
            print(new[47], "hi")
            item_v1.update(int(new[47]))
    time.sleep(10)
    print(item_v1.boolz)





    #cv2.imshow('video', frame1)
    #if cv2.waitKey(1) & 0xff == ord('q'):
     #   break
#video_capture.release()
#cv2.destroyAllWindows()






# def detector_v1(num):
#     start_time = time.time()
#     for i in range(1, num):
#         item = item12.Show()
#         boolz = item[10]
#         item_v1.update(boolz)
#         print(boolz)
#         time.sleep(60.0 - ((time.time() - start_time) % 60.0))
