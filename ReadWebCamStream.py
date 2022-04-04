import cv2
from utils.SocketWebCamStream import SocketWebCamStream

sockWeb = SocketWebCamStream(SOCKET_IP="127.0.0.1", PORT=4545)

WindowName = "Socket WebCam"
cv2.namedWindow(WindowName)

while True:

    frame = sockWeb.getFrame()
    
    if frame is not None:
        cv2.imshow(WindowName, frame)

    if cv2.waitKey(1) == ord('q'):
        sockWeb.exit_thread()
        break