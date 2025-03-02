import ui
import app.apputil.config as config

class OptionsView:
    def __init__(self):
        pass

    def get_sc(self):
        sc = ui.SegmentedControl()
        sc.segments = config.OPTIONS
        sc.background_color = 'white'
        sc.width = 300
        sc.heigh = 70
        return sc

