""" ==========================================

ラズパイ側に搭載するプログラム
time.sleepで待機しながら、2秒ごとにカメラで取得した画像情報を送信し続ける
ip_idr, port_num は適宜変更する必要あり。

========================================== """

import socket
import cv2
import time

ip_adr = "192.168.128.111"
port_num = 5000

while True:
    time.sleep(2)    
    ret, frame = cv2.VideoCapture(0).read()
    _, buffer = cv2.imencode('.jpg', frame)
    img_as_bytes = buffer.tobytes()
    #camera_image = camera_image.tobytes()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((ip_adr, 5000))
        client_socket.sendall(img_as_bytes)
        print("Image sent to the server.")