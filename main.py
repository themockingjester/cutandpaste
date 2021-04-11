from datetime import time

from kivy.properties import ObjectProperty
from kivy.uix.behaviors import DragBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from qrmaker import QrMake
from image_processing import ImageProcessing
class CameraWindow(BoxLayout):
    camera = ObjectProperty(None)
class MainWindow(BoxLayout):
    pass
class ShowQr(BoxLayout):
    qr = ObjectProperty(None)
class uiApp(MDApp):
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
    def mainscreen_to_camerascreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'camerascreen'
    def camerascreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'mainscreen'
    def mainscreen_to_qrscreen(self):
        self.screen_manager.transition.direction = 'down'
        self.screen_manager.current = 'qrscreen'
        obj = QrMake()
        obj.make("7879.56",'5645')
    def qrscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'up'
        self.screen_manager.current = 'mainscreen'
uiApp().run()