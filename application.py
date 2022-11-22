from view.view_dao import View_class
from controller.controller_dao import Controller
from model.model_dao import Model


class Application:
    def __init__(self, view: View_class, controller: Controller, model: Model):
        self.view = view
        self.controller = controller
        self.model = model


if __name__ == "__main__":
    controller = Controller()
    view = View_class(controller)
    Recipe = list()
    Users = list()
    model = Model(Recipe, Users)
    app = Application(view, controller, model)
    app.view.build()
