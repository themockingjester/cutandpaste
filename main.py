from datetime import time
import random
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from wireless import WirelessConnection
from qrmaker import QrMake
from image_processing import ImageProcessing

class ImageButton(ButtonBehavior, Image):
    pass
class CameraWindow(BoxLayout):
    camera = ObjectProperty(None)


class MainWindow(BoxLayout):
    pass
class ShowQr(BoxLayout):
    qr = ObjectProperty(None)
class Qrreader(BoxLayout):
    zbarcam=ObjectProperty(None)
class uiApp(MDApp):
    portused={}
    def build(self):
        self.screen_manager = ScreenManager()

        self.builderscreen = MainWindow()
        screen = Screen(name='builderscreen')
        screen.add_widget(self.builderscreen)
        self.screen_manager.add_widget(screen)

        self.camerascreen = CameraWindow()
        screen = Screen(name='camerascreen')
        screen.add_widget(self.camerascreen)
        self.screen_manager.add_widget(screen)

        self.qrscreen = ShowQr()
        screen = Screen(name='qrscreen')
        screen.add_widget(self.qrscreen)
        self.screen_manager.add_widget(screen)

        self.qrreasderscreen = Qrreader()
        screen = Screen(name='qrreasderscreen')
        screen.add_widget(self.qrreasderscreen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''


        self.camerascreen.camera.export_to_png("temp.png")
        print("Captured")
        obj = ImageProcessing()
        obj.removeBackground()
    def portNumberGenerator(self):
        port = None
        while True:
            port = random.randrange(30000, 50000, 1)
            if port not in uiApp.portused:
                uiApp.portused[port] = True
                break
        return port
    def mainscreen_to_camerascreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'camerascreen'
    def camerascreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'builderscreen'
    def mainscreen_to_qrscreen(self):
        try:
            self.qrscreen.qr.reload()
        except:
            print("can't refresh qr")
        obj1 = WirelessConnection()
        ip = obj1.ipfinder()
        port = self.portNumberGenerator()
        obj2 = QrMake()
        obj2.make(ip,port)
        self.screen_manager.transition.direction = 'down'
        self.screen_manager.current = 'qrscreen'
        obj1.server(ip,port)

    def qrscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'builderscreen'
    def mainscreen_to_receivescreen(self):

        self.screen_manager.transition.direction = 'down'
        self.screen_manager.current = 'qrreasderscreen'
    def getrecievedqr(self):
        k = ', '.join([str(symbol.data) for symbol in self.qrreasderscreen.zbarcam.symbols])
        print(k)
        print("ok")
    def receivescreen_to_mainscreen(self):
        self.getrecievedqr()
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'builderscreen'
uiApp().run()