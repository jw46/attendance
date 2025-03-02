import ui
from abc import ABC, abstractmethod

class SuperView(ui.View):
    def __init__(self, model):
        self.model = model

    def button_tapped(self, sender):
        self.close()

    def show(self):
        self.background_color = 'white'
        self.present('fullscreen')
        self.wait_modal()