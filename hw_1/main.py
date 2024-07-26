from model import Product
from view import MainWindow
from controller import Controller

class App:
    model = Product()
    controller = Controller(model)
    view = MainWindow(controller)

    @staticmethod
    def run():
        App.view.mainloop()

if __name__ == '__main__':
    App.run()
    