from abc import ABC, abstractmethod
from app.views.parent.parent_view import ParentView
"""

"""
class AbstractUI(ABC):
    def __init__(self, app_data):
        self.app_data = app_data
        self.pv = ParentView()

    def run(self):
        self.pv.present('fullscreen')
        self.pv.wait_modal()