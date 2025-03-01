import ui
from datetime import datetime

print('start', datetime.now())
pv = ui.View()
pv.present('fullscreen')
print('waiting', datetime.now())
pv.wait_modal()
print('finished', datetime.now())
