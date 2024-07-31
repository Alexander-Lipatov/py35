from abc import ABC
from typing import List, Dict
from config import PAYMENT, TOPPING_PORTION
import statemanager as sm


class Topping:
    
    name:str
    price:float
    percent:float
    count:float


    def __new__(cls, *args, **kwargs):
        instance = super(Topping, cls).__new__(cls, *args, **kwargs)
        cls.count -=TOPPING_PORTION[cls.__name__]
    


class Pizza:
    def  __init__(self) -> None:
        self.toppings: List[Topping]= []



class App:

    def __init__(self) -> None:
        self.data = {
            'toppings':[],
            'menu': [],
            'kassa':[],
            'storage': {}
        }

        try:
            self.load()
        except:
            self.load_default()

    def load(self):
        self.data = sm.load(self.data)

    def load_default(self):
        data = {
            'toppings':[],
            'menu': [],
            'kassa':[],
            'storage': {}
        }
        self.save(data)
        self.load()

    def save(self):
        sm.save(self.data)

        
    
class Console:
    pass