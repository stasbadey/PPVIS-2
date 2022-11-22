from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication
from view.design import profile, design, registration, choose, entry, action, change, changeprofile, create, delete, \
    myrecipe, recipe, recipelist, recovery1, recovery2


class View_of_windows:
    def __init__(self, controller):
        self.controller = controller

    def entry_method(self):
        self.controller.entry()

    def check_login_and_password(self):
        self.controller.check_login_and_password()

    def lost_password(self):
        self.controller.lost_password()

    def add_recipe(self):
        self.controller.add_recipe()

    def delete_recipe(self, id: int):
        self.controller.delete_recipe()

    def show_available_recipe(self):
        self.controller.show_available_recipe()

    class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_recipelist_window)
            self.pushButton_2.clicked.connect(self.show_profile_window)
            self.pushButton_3.clicked.connect(self.show_action_window)
            self.pushButton_4.clicked.connect(QCoreApplication.instance().quit)

        def show_recipelist_window(self):
            if self.w is None:
                self.w = View_of_windows.RecipeListWindow()
            self.w.show()
            self.close()

        def show_profile_window(self, checked):
            if self.w is None:
                self.w = View_of_windows.ProfileApp()
            self.w.show()
            self.close()

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

    class ProfileApp(QtWidgets.QMainWindow, profile.Ui_Profile):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_changeprofile_window)
            self.pushButton_2.clicked.connect(View_of_windows.show_available_recipe)
            self.pushButton_3.clicked.connect(self.show_main_window)

        def show_myrecipe_window(self):
            if self.w is None:
                self.w = View_of_windows.MyrecipeWindow()
            self.w.show()
            self.close()

        def show_changeprofile_window(self):
            if self.w is None:
                self.w = View_of_windows.ChangeProfileWindow()
            self.w.show()
            self.close()

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

    class RegistraionWindow(QtWidgets.QMainWindow, registration.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_main_window)

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

    class EntryWindow(QtWidgets.QMainWindow, entry.Ui_MainWindow):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_main_window)
            self.pushButton_2.clicked.connect(View_of_windows.check_login_and_password)

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

        def show_recovery_window(self):
            if self.w is None:
                self.w = View_of_windows.Recovery1Window()
            self.w.show()
            self.close()

    class ActionWindow(QtWidgets.QMainWindow, action.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_vision_window)
            self.pushButton_2.clicked.connect(self.show_create_window)
            self.pushButton_3.clicked.connect(self.show_delete_window)
            self.pushButton_4.clicked.connect(self.show_change_window)
            self.pushButton_5.clicked.connect(self.show_myrecipe_window)

        def show_vision_window(self):
            if self.w is None:
                self.w = View_of_windows.RecipeWindow()
            self.w.show()
            self.close()

        def show_create_window(self):
            if self.w is None:
                self.w = View_of_windows.CreateWindow()
            self.w.show()
            self.close()

        def show_delete_window(self):
            if self.w is None:
                self.w = View_of_windows.DeleteWindow()
            self.w.show()
            self.close()

        def show_change_window(self):
            if self.w is None:
                self.w = View_of_windows.ChangeWindow()
            self.w.show()
            self.close()

        def show_myrecipe_window(self):
            if self.w is None:
                self.w = View_of_windows.MyrecipeWindow()
            self.w.show()
            self.close()

    class ChangeWindow(QtWidgets.QMainWindow, change.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_action_window)
            self.pushButton_2.clicked.connect(self.show_action_window)

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

    class ChangeProfileWindow(QtWidgets.QMainWindow, changeprofile.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_main_window)

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

    class CreateWindow(QtWidgets.QMainWindow, create.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(View_of_windows.add_recipe)
            self.pushButton_2.clicked.connect(self.show_action_window)

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

    class DeleteWindow(QtWidgets.QMainWindow, delete.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(View_of_windows.delete_recipe)
            self.pushButton_2.clicked.connect(self.show_action_window)

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

    class MyrecipeWindow(QtWidgets.QMainWindow, myrecipe.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_recipe_window)
            self.pushButton_2.clicked.connect(self.show_recipe_window)
            self.pushButton_3.clicked.connect(self.show_recipe_window)
            self.pushButton_4.clicked.connect(self.show_recipe_window)
            self.pushButton_5.clicked.connect(self.show_recipe_window)
            self.pushButton_6.clicked.connect(self.show_action_window)
            self.pushButton_7.clicked.connect(self.show_profile_window)

        def show_recipe_window(self):
            if self.w is None:
                self.w = View_of_windows.RecipeWindow()
            self.w.show()
            self.close()

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

        def show_profile_window(self):
            if self.w is None:
                self.w = View_of_windows.ProfileApp()
            self.w.show()
            self.close()

    class RecipeWindow(QtWidgets.QMainWindow, recipe.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_action_window)
            self.pushButton_2.clicked.connect(self.show_action_window)

        def show_action_window(self):
            if self.w is None:
                self.w = View_of_windows.ActionWindow()
            self.w.show()
            self.close()

    class RecipeListWindow(QtWidgets.QMainWindow, recipelist.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_recipe_window)
            self.pushButton_2.clicked.connect(self.show_recipe_window)
            self.pushButton_3.clicked.connect(self.show_recipe_window)
            self.pushButton_4.clicked.connect(self.show_recipe_window)
            self.pushButton_5.clicked.connect(self.show_recipe_window)
            self.pushButton_6.clicked.connect(self.show_main_window)

        def show_recipe_window(self):
            if self.w is None:
                self.w = View_of_windows.RecipeWindow()
            self.w.show()
            self.close()

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

    class Recovery1Window(QtWidgets.QMainWindow, recovery1.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_recovery2_window)

        def show_recovery2_window(self):
            if self.w is None:
                self.w = View_of_windows.Recovery2Window()
            self.w.show()
            self.close()

    class Recovery2Window(QtWidgets.QMainWindow, recovery2.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_main_window)

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

    class ChooseWindow(QtWidgets.QMainWindow, choose.Ui_choose):
        def __init__(self):
            super().__init__()
            self.w = None
            self.setupUi(self)
            self.pushButton.clicked.connect(self.show_registraion_window)
            self.pushButton_2.clicked.connect(self.show_entry_window)
            self.pushButton_3.clicked.connect(self.show_main_window)
            self.pushButton_4.clicked.connect(QCoreApplication.instance().quit)

        def show_main_window(self):
            if self.w is None:
                self.w = View_of_windows.MainWindow()
            self.w.show()
            self.close()

        def show_registraion_window(self):
            if self.w is None:
                self.w = View_of_windows.RegistraionWindow()
            self.w.show()
            self.close()

        def show_entry_window(self):
            if self.w is None:
                self.w = View_of_windows.EntryWindow()
            self.w.show()
            self.close()
