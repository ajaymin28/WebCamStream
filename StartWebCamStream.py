from utils.SocketWebCamServer import SocketWebCamServer

WebServer = SocketWebCamServer(PORT=4545)
WebServer.start_server()