from model import Product
from view import MainWindow, CreateProductWindow


class Controller:
    def __init__(self, model:Product, view:MainWindow):
        self.model = model
        self.view = view
        self.view.btn.config(command=self.add_product)

        self.update_view()
        
    def update_view(self):
        data = self.model.all()
        for i in data:
            self.view.table.insert("", 'end', values=(
                i.vendor, 
                i.category,
                i.size,
                i.color,
                i.price,
                i.sex
            ))

    

    def add_product(self):

        def read_data():
            vendor = window.vendor.get()
            category = window.category.get()
            size = window.size.get()
            color = window.color.get()
            price = window.price.get()
            sex = window.sex.get()
            model = self.model.create(vendor, category, size, color, price, sex)
            print(model.__dict__)
            self.view.table.insert("", 'end', values=(
                model.vendor, 
                model.category,
                model.size,
                model.color,
                model.price,
                model.sex
            ))

        window = CreateProductWindow()
        window.add_btn.config(command=read_data)
        

        

        
        # vendor = self.view.vendor_entry.get()
        # category = self.view.category_entry.get()
        # size = self.view.size_entry.get()
        # color = self.view.color_entry.get()
        # price = self.view.price_entry.get()
        # sex = self.view.sex_entry.get()

    #    model = self.model.create('Nike', 'Sneakers', 42, 'Black', 100, 'men')
    #    self.view.table.insert("", 'end', values=(
    #             model.vendor, 
    #             model.category,
    #             model.size,
    #             model.color,
    #             model.price,
    #             model.sex
    #         ))
       
    
       
    