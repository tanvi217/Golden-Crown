
import pathlib
import sys

from src.main.models.cover import Cover
from src.main.models.kingdom import Kingdom 
from src.main.controller.kingdom_to_emblem import get_emblem

class SenderKingdom(Kingdom):

    def __init__(self, realm, messages_file_path):
        super().__init__(realm)
        self.messages_file_path = messages_file_path
        self.allies = list()

    def __add_ally(self, ally):
        if ally not in self.allies and ally != self.realm:
            self.allies.append(ally)

    def send_messages(self):
        is_file = pathlib.Path(self.messages_file_path).exists()

        if is_file:
            input_file = open(self.messages_file_path, 'r')
            for line in input_file:
                try:
                    destination_kingdom, secret_message = line.split(" ", 1)
                    self.send_message(secret_message, destination_kingdom)

                except ValueError:
                    print("Message parameter is missing in line {}".format(line))

            input_file.close() 

        else:
            raise FileNotFoundError("Could not read file - {}".format(self.messages_file_path))

    def send_message(self, secret_message, destination_kingdom):
        destination_emblem = get_emblem(destination_kingdom)
        if destination_emblem:
            cover = Cover(secret_message, destination_emblem)
            if cover.is_destination_emblem_in_message():
                self.__add_ally(destination_kingdom)
        else:
            print("{} kingdom does not exist.".format(destination_kingdom))
