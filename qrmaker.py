import qrcode
import random
class QrMake():
    portused={}
    def __init__(self):
        pass
    def make(self,ip):
        port = None
        while True:
            port = random.randrange(30000,50000,1)
            if port not in QrMake.portused:
                QrMake.portused[port]=True
                break

        msg = str(ip) + "@@@" + str(port)
        img = qrcode.make(msg)
        img.save('qr.png')
