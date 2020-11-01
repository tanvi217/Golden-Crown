from config import KINGDOM_TO_EMBLEM

def get_emblem(kingdom):
    try:
        emblem = KINGDOM_TO_EMBLEM[kingdom]
        return emblem
    except KeyError:
        return None