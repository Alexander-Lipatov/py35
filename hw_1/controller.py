from model import Product, MenShoes
from view import MainWindow


class Controller:
    def __init__(self, model:Product, view:MainWindow):
        self.model = model
        self.view = view
        self.view.btn.config(command=self.add_product)

        self.update_view()
        
    def update_view(self):
        data = self.model.all()
        for i in data['Men']:
            self.view.table.insert('', 'end', values=(i['vendor'], i['category'], i['size'], i['color'], i['price']))

    def add_product(self):
        self.model.create(MenShoes, 'asdsadasd', 'asdadssad', 30, 'red', 100)
        self.update_view()