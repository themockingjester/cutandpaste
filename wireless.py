import socket
from kivymd.toast import toast
class WirelessConnection():
    def __init__(self):
        pass
    def ipfinder(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    def client(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            toast('connected')
        except:
            s.close()

    def server(self,ip,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sendscreen.ip.text, int(self.sendscreen.port.text)
        try:
            s.bind((ip, int(port)))

        except:
            toast('something is incorrect with your data')
            s.close()

            return 0
        s.listen(1)

        toast('working')
        clientsocket, address = s.accept()

        toast(f"Connection from {address} has been established.")
