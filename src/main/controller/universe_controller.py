from src.main.models.universe import Universe
from src.main.views.show_ruler_allies import UniverseView

class UniverseController(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def send_messages(self):
        self.model.sender_kingdom.send_messages()

    def show_ruler(self):
        ruler = self.model.get_ruler_kingdom()
        self.view.show_ruler_allies(ruler)