from model.entity.recipe import Recipe


class Account:
    def __init__(self, name_of_profile: str, email: str, password: str, recipe: Recipe):
        self.name_of_profile = name_of_profile
        self.email = email
        self.password = password
        self.list_of_recipe = list()
        self.list_of_recipe.append(recipe)

    def release(self):
        pass

    def password_change(self):
        pass

    def name_change(self):
        pass

    def email_change(self):
        pass

    def add_recipe(self, availability: bool):
        pass

    def delete_recipe(self):
        pass
