import tkinter as tk
from tkinter import ttk
from controller import Controller

class MainWindow(tk.Tk):
    def __init__(self, controller:Controller):
        super().__init__()
        self.controller = controller

        self.title("MVC Example")
        # self.geometry("1000x400")

        # Создаем таблицу
        self.table = self.create_table()
        self.bind('<<TreeviewSelect>>', self.get_selected_row)
        

        # Кнопка для создания товара
        self.btn = self.create_button('Добавить')
        self.btn.config(command=self.open_create_product)
        
        # Кнопка удаления товара
        self.btn_delete = self.create_button('Удалить')
        self.btn_delete.config(state='disabled')

        # Кнопка изменения товара
        self.btn_update = self.create_button('Изменить')
        self.btn_update.config(state='disabled')

        


        self.refresh_table()
    
    def get_selected_row(self, event):
        selected_items = self.table.selection()

        if selected_items:  # Получаем идентификатор выделенной строки
            selected_item = selected_items[0]
            item = self.table.item(selected_item)  # Получаем данные строки
            self.btn_delete.config(state='normal', command=lambda: self.delete_product(item['values'][0]))
            self.btn_update.config(state='normal', command=lambda: self.update_product())

    def update_product(self):
        selected_items = self.table.selection()
        if selected_items:
            selected_item = selected_items[0]
            item = self.table.item(selected_item)  # Получаем данные выделенной строки
            modal = UpdateProductWindow(master=self, values=item['values'], uid=item['values'][0])
            self.wait_window(modal)
            self.btn_update.config(state='disabled')
            self.refresh_table()

    def delete_product(self,uid):
        selected_items = self.table.selection()
        if selected_items:
            self.table.delete(selected_items[0])
            self.btn_delete.config(state='disabled')
            self.btn_update.config(state='disabled')
            self.controller.delete_product(uid)

    def create_button(self, text: str):
        button = ttk.Button(text=text)
        button.pack()
        return button

    def create_table(self):
        self.columns = ("uuid", "vendor", "category", "size", 'color', 'price', 'sex')
        table = ttk.Treeview(columns=self.columns, show='headings')

        for c in self.columns:
            if c == "uuid":
                table.column(c, stretch=tk.NO,  width=0)
                table.heading(c, text=c)
                continue
            table.column(c, stretch=tk.NO, anchor=tk.CENTER, width=100)
            table.heading(c, text=c)

        table.pack()
        return table
    
    def open_create_product(self):
        modal = CreateProductWindow(self, self.controller)
        self.wait_window(modal)
        self.refresh_table()

    def open_update_product(self):
        pass
    
    def refresh_table(self):
        # Очищаем таблицу
        for row in self.table.get_children():
            self.table.delete(row)
        
        # Получаем данные от контроллера и добавляем в таблицу
        data = self.controller.get_all_product()
        print(data[0].get_tuple_values())
        for product in data:
            self.table.insert('', 'end', values=product.get_tuple_values())
    
    


class MenuFrame(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        pass


class CreateProductWindow(tk.Toplevel):

    def __init__(self, master:MainWindow = None, controller:Controller=None):
        super().__init__(master)
        self.controller = controller

        self.title("MVC Example1")
        self.geometry("300x400")
        self.transient(master)
        self.grab_set()
        self.data = {}

        self.root = master

        self.vendor = self.create_input('vendor')
        self.category = self.create_input('category')
        self.size = self.create_input('size')
        self.color = self.create_input('color')
        self.price = self.create_input('price')
        self.sex = self.create_input('sex')
        self.add_btn = self.create_button('Добавить')

    def add_product(self):
        vendor = self.vendor.get()
        category = self.category.get()
        size = self.size.get()
        color = self.color.get()
        price = self.price.get()
        sex = self.sex.get()
        
        if self.controller.add_product(vendor, category, size, color, price, sex):
            self.root.table.insert('', 'end', values=(vendor, category, size, color, price, sex))
            self.destroy()
        
        


    def create_button(self, text):
        button = ttk.Button(self, text=text, command=self.add_product)
        button.pack()
        return button

    
    def create_input(self, label):
        label=ttk.Label(self, text=label)
        label.pack()
        input_vendor = tk.Entry(self)
        input_vendor.pack()
        return input_vendor
    
    

class UpdateProductWindow(tk.Toplevel):

    def __init__(
            self, 
            uid,
            values,
            master:MainWindow = None, 
        ):
        super().__init__(master)

        self.root = master
        self.controller = master.controller

        self.title("Update data")
        self.geometry("300x400")
        self.transient(master)
        self.grab_set()

        
        for index, col_item in enumerate(self.root.columns):
            if col_item == 'uuid':
                continue
            setattr(self, col_item, self.create_input(col_item.title(), values[index]))

        self.uid = uid

        self.add_btn = self.create_button('Добавить')
        

    def create_button(self, text):
        button = ttk.Button(self, text=text, command=self.update_product)
        button.pack()
        return button

    def create_input(self, label, value):
        label=ttk.Label(self, text=label)
        label.pack()
        input = tk.Entry(self)
        input.insert(0, value)
        input.pack()
        return input
    
    def update_product(self):
        vendor = self.vendor.get()
        category = self.category.get()
        size = self.size.get()
        color = self.color.get()
        price = self.price.get()
        sex = self.sex.get()
        if self.controller.update_product(self.uid, vendor, category, size, color, price, sex):
            self.destroy()
    
    
        
        
        

