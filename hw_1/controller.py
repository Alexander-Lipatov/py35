from model import Product
from tkinter import messagebox


class Controller:
    def __init__(self, model:Product):
        self.model = model
        
    def get_all_product(self):
        return self.model.all()
    
    def delete_product(self, uid):
        return self.model.delete(uid)

    def add_product(self, vendor, category, size, color, price, sex):
        if not self.validate_product_data(vendor,category, size, color,price,sex):
            return False
        
        return self.model.create(
            vendor,
            category,
            size,
            color,
            price,
            sex
        )
    
    def update_product(self, uid, vendor, category, size, color, price, sex):
        if not self.validate_product_data(vendor, category, size, color, price, sex):
            print('invalid')
            return False
        self.model.update(uid, vendor, category, size, color, price, sex)
        return True
    

    def validate_product_data(self, vendor, category, size, color, price, sex):
        if not vendor:
            messagebox.showerror("Ошибка валидации", "Пожалуйста, введите название производителя.")
            return False
        if not category:
            messagebox.showerror("Ошибка валидации", "Пожалуйста, введите категорию.")
            return False
        if not size.isdigit():
            messagebox.showerror("Ошибка валидации", "Размер должен быть числом.")
            return False
        if not color:
            messagebox.showerror("Ошибка валидации", "Пожалуйста, введите цвет.")
            return False
        try:
            price_value = float(price)
            if price_value <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка валидации", "Цена должна быть положительным числом.")
            return False
        if sex not in ("M", "F"):
            messagebox.showerror("Ошибка валидации", "Пол должен быть 'M' или 'F'.")
            return False

        return True 


        
        

        

        
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
       
    
       
    