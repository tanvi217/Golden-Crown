class UniverseView(object):

    @staticmethod
    def show_ruler_allies(ruler_kingdom):
        if ruler_kingdom:
            print(ruler_kingdom.realm, end=" ")
            print(*ruler_kingdom.allies)
        else:
            print("NONE")
