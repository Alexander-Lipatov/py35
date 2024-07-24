import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MVC Example")
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
        