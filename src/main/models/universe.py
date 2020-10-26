import os

from config import MIN_ALLIES
from src.main.models.sender_kingdom import SenderKingdom

class Universe:

    def __init__(self, sender_kingdom, secret_messages_file_path):
        self.sender_kingdom = SenderKingdom(sender_kingdom, secret_messages_file_path)
        self.ruler_kingdom = None

    def get_ruler_kingdom(self):
        """
        checks if sender king is the ruler
        """
        if len(self.sender_kingdom.allies) >= MIN_ALLIES:
            self.ruler_kingdom = self.sender_kingdom
        return self.ruler_kingdom
