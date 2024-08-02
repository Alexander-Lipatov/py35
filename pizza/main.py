from abc import ABC
from typing import List, Dict

import statemanager as sm
from mixins import StorageMixin
from model import Pizza, Order
    





class App(StorageMixin):

    def __init__(self) -> None:

        self.data = {
            'toppings':[],
            'menu': [],
            'kassa':[],
            'storage': {},
        }
        self.order = []

        self.load_default()     
        if self.first_load:
            self._generate_pizza()
            self._generate_toppings()

       
    def _generate_pizza(self)-> List:
        list_pizzas = [Pizza(name=f'pizza_{_+1}') for _ in range(5)]
        self.data['menu'] = list_pizzas
        self.save()
        return list_pizzas
    
    def _generate_toppings(self)-> List:
        list_toppings = [Pizza(name=f'topping_{_+1}') for _ in range(5)]
        self.data['toppings'] = list_toppings
        self.save()
        return list_toppings
    
    
    
    # def create_order(self, pizza):
    #     order = Order()
    #     order.pizzas.append(pizza)
    #     self.order.append()
    #     return self.order


    
    

        
    
class Console:
    pass


if __name__ == '__main__':
    app = App()
    print(app.__dict__)