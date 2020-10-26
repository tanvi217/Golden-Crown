from config import SECRET_KEY
from collections import Counter

class Cover:
    
    def __init__(self, secret_message, destination_emblem):
        self.secret_message = secret_message
        self.destination_emblem = destination_emblem

    def __emblem_hash(self):
        return Counter(self.destination_emblem.upper())

    def is_destination_emblem_in_message(self):
        """
        checks if emblem is present in secret message
        """
        emblem_len = len(self.destination_emblem)
        message_len = len(self.secret_message)
        emblem_hash = self.__emblem_hash()

        if message_len < emblem_len:
            return False
        for char in self.secret_message:
            if not emblem_hash:
                return True
            if not char.isupper():
                continue
            decoded_index = (ord(char) - ord('A') - emblem_len + len(SECRET_KEY)) % len(SECRET_KEY)
            decoded_char = SECRET_KEY[decoded_index]
            if decoded_char in emblem_hash.keys():
                emblem_hash[decoded_char] -= 1
                if emblem_hash[decoded_char] == 0:
                    del emblem_hash[decoded_char]
        return False