"""
Author: Jaimin Bhoi(ajaymin28)
Date: 4/4/2022

Github: https://github.com/ajaymin28/WebCamStream

Do whatever you want with this code. Just keep the Author same.

"""


import socket
import cv2
from utils.Helpers import Helpers

HelpersObj = Helpers()

class SocketWebCamServer:

    def __init__(self, PORT=4545, webcam=0):
        self.port = PORT
        self.socket_server = socket.socket()
        self.socket_server.bind(("",self.port))
        self.cap = cv2.VideoCapture(webcam)
        self.run_server = True

    def close_server(self):
        self.run_server = False

    def start_server(self):

        self.socket_server.listen(5)
        print("websocker server running {}".format(self.socket_server.getsockname()))
        while self.run_server:

            base64Image = None
            c, addr = self.socket_server.accept()

            ret, frame = self.cap.read()
            if ret:
                base64Image = HelpersObj.get_img_from_array(frame)
                if base64Image is not None:
                    c.send(base64Image.encode())
                else:
                    c.send("Invalid Image".encode())
            else:
                c.send("error getting frame".encode())

            c.close()
