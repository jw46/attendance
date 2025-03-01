import ui
from app.views.super_v import SuperView

class TestView(SuperView):
    def __init__(self, model):
        self.model = model


    def button_tapped(self, sender):
        self.close()

    def show(self):
        self.name = 'Test self'
        self.background_color = 'white'
        button = ui.Button(title='Tap me!')
        button.center = (self.width * 0.5, self.height * 0.5)
        button.flex = 'LRTB'
        button.action = self.button_tapped
        self.add_subview(button)
        self.present('fullscreen')
        self.wait_modal()