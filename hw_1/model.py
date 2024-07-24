from abc import ABC
from statemanager import load, save
from typing import List
class Product:
    uid = 0
    
    def __init__(self, *args, **kwargs):
        try:
            self._data:List[ShoesModel] = load()
        except:
            self._data:List[ShoesModel] = []
            self.save()

    def save(self):
        save(self._data)

    def all(self):
        return self._data

    def create(self, vendor, category, size, color, price, sex):
        uid = Product.uid + 1
        model :ShoesModel = ShoesModel(uid, vendor, category, size, color, price, sex)
        self._data.append(model)
        self.save()
        return model

    def delete(self, uid):
        for model in self._data:
            if model.uid == uid:
                self._data.remove(model)
                self.save()
                break
    
    def get(self, uid):
        for model in self._data:
            if model.uid == uid:
                return model
        return None
        

class ShoesModel:

    def __init__(self, uid, vendor, category, size, color, price, sex):
        self.uid = uid
        self.vendor = vendor
        self.category = category
        self.size = size
        self.color = color
        self.price = price
        self.sex = sex



    

# model = Product()
# model.create('safsd','asdasd',10, 'asdasd', 2000, 'men')


# # Пример использования статического метода
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# woman_shoes_data = Product.create(WomanShoes, vendor="Adidas", category="Heels", size=38, color="Red", price=150)

# # Доступ ко всем данным
# model = Product()
# print(model.all())
