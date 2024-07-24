import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MVC Example")
        ttk.Label(self, text='text main window')
        self.geometry("1000x400")
        self.table = self.create_table()
        self.btn = self.create_button()

    
    def create_button(self):
        button = ttk.Button(text='Добавить товар')
        button.pack()
        return button


    def create_table(self):
        columns = ("vendor", "category", "size", 'color', 'price')
        table = ttk.Treeview(columns=columns, show='headings')
        table.pack()

        # определяем заголовки
        table.heading("vendor", text="Производитель")
        table.heading("category", text="Категория")
        table.heading("size", text="Размер")
        table.heading("color", text="Цвет")
        table.heading("price", text="Цена")
        return table
    

    def add_product_window(self):
        window = tk.Tk()
        window.title("Новое окно")
        window.geometry("250x200")
        # label=ttk.Label(window, text="Принципиально новое окно")
        # label.pack(anchor='center', expand=1)
        return window
    
    


class CreateProductWindow(tk.Tk):

    
        

    def __init__(self):
        super().__init__()
        self.title("MVC Example1")
        self.geometry("300x200")

        self.vendor = self.create_input('Vendor')
        self.category = self.create_input('category')
        self.size = self.create_input('size')
        self.color = self.create_input('color')
        self.price = self.create_input('price')
        self.sex = self.create_input('sex')
        self.add_btn = self.create_button('Добавить')

    def create_button(self, text):
        button = ttk.Button(self, text=text)
        button.pack()
        return button

    
    def create_input(self, label):
        label=ttk.Label(self, text=label)
        label.pack()
        input_vendor = tk.Entry(self)
        input_vendor.pack()
        return input_vendor
    
    
        
        
        

