
from typing import List, Dict
from config import PAYMENT, TOPPING_PORTION


class Pizza:
    def  __init__(self, name) -> None:
        self.toppings: List[Topping]= []
        self.name = name

    def __repr__(self) -> str:
        return f'{self.name}'
    
    @staticmethod
    def custom_pizza():
        return Pizza("Custom Pizza")
    
class Order:
    def __init__(self) -> None:
        self.pizzas: List[Pizza]= []
        self.total_price: float = 0


class Topping:
    
    name:str
    price:float
    percent:float
    count:float


    