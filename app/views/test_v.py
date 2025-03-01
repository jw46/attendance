import ui

class TestView(ui.View):
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
        button.action = button_tapped
        self.add_subself(button)
        self.present('sheet')
        self.wait_modal()