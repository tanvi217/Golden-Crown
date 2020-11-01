from collections import Counter

from src.main.controller.kingdom_to_emblem import get_emblem
class Kingdom:
    
    def __init__(self, realm):
        self.realm = realm
        self.emblem = get_emblem(realm).upper()

    
