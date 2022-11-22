class Recipe:
    def __init__(self, name: str, ingridients: str, action: str, availability: bool, id: int):
        self.name = name
        self.ingridients = ingridients
        self.actions = list()
        self.actions.append(action)
        self.__availability = availability
        self.__id = id
