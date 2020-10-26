import sys

from src.main.models.cover import Cover
from src.main.models.kingdom import Kingdom 
from src.main.controller.kingdom_to_emblem import get_emblem

class SenderKingdom(Kingdom):

    def __init__(self, realm, messages_file_path):
        super().__init__(realm, get_emblem(realm))
        self.messages_file_path = messages_file_path
        self.allies = list()

    def __add_ally(self, ally):
        if ally not in self.allies and ally != self.realm:
            self.allies.append(ally)

    def send_messages(self):
        try:
            input_file = open(self.messages_file_path, 'r')

        except OSError:
            print("Could not read file - ", messages_file_path)
            sys.exit()

        with input_file:
            for line in input_file:
                try:
                    destination_kingdom, secret_message = line.split(" ", 1)
                    self.send_message(secret_message, destination_kingdom)

                except ValueError:
                    print("Message parameter is missing in line {}".format(line))

            input_file.close() 

    def send_message(self, secret_message, destination_kingdom):
        try:
            destination_emblem = get_emblem(destination_kingdom)
            cover = Cover(secret_message, destination_emblem)
            if cover.is_destination_emblem_in_message():
                self.__add_ally(destination_kingdom)

        except KeyError:
            print("{} kingdom does not exist.".format(destination_kingdom))
