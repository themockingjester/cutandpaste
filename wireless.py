import socket
class WirelessConnection():
    def __init__(self):
        pass
    def ipfinder(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            s.bind((self.sendersip, int(self.sendersport)))
            self.sendscreen.indicator.opacity = 1
        except:
            print('something is incorrect with your data')
            s.close()
            self.sendscreen.indicator.opacity = 0
            return 0
        s.listen(4)
        # time.sleep(0.001)
        print('working')

