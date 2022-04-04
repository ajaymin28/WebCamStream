"""
Author: Jaimin Bhoi(ajaymin28)
Date: 4/4/2022

Do whatever you want with this code. Just keep the Author same.

"""

import threading
import socket       
import base64
from PIL import Image
from io import BytesIO
import numpy as np


class SocketWebCamStream:

    def __init__(self, SOCKET_IP,PORT, frame_queue_size=1, isthreaded=True):
        self.SOCKET_IP = SOCKET_IP
        self.PORT = PORT
        self.frame_queue = []
        self.frame_queue_size = frame_queue_size
        self.frame_queue_lock = threading.Lock()
        self.isthreaded = isthreaded

        if self.isthreaded:
            self.t1 = threading.Thread(target=self.start_get_stream)
            self.t1.setName("Socket webcam Stream Thread")
            self.runThread = True
            self.t1.start()
            print("thread started")

    def getFrame(self):

        Frame = None
        if self.isthreaded:
            self.frame_queue_lock.acquire()
            if len(self.frame_queue)>=self.frame_queue_size:
                try:
                    Frame = self.frame_queue.pop(0)
                except:
                    pass
            self.frame_queue_lock.release()
        else:
            self.frame_queue_lock.acquire()
            Frame = self.getImageFromSocket()
            self.frame_queue_lock.release()

        return Frame

    def __del__(self):
        if self.isthreaded:
            self.t1.join() 

    def getImageFromSocket(self):

        base64Data = ''
        opencvimage = None
        s = socket.socket()    
        try: 
            s.connect((self.SOCKET_IP, self.PORT))
            while True:
                temp = s.recv(1).decode()
                if temp!="":
                    base64Data += temp
                else:
                    break
        except:
            pass
        finally:
            s.close()

        del s

        try:
            imgdata = base64.b64decode(base64Data)
            pilimage = Image.open(BytesIO(imgdata)).convert('RGB')
            opencvimage = np.ascontiguousarray(pilimage)
        except:
            pass

        return opencvimage

    def exit_thread(self):
        if self.isthreaded:
            self.runThread = False
            self.__del__()

    def start_get_stream(self):

        while self.runThread:

            opencvimage = None
            try:    
                opencvimage = self.getImageFromSocket()
            except Exception as e:
                print(e)
                pass

            self.frame_queue_lock.acquire()
            self.frame_queue.append(opencvimage)
            self.frame_queue_lock.release()

            if self.runThread==False:
                break