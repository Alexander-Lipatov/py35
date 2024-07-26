from abc import ABC
from statemanager import load, save
from typing import List
import uuid
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
        uid = uuid.uuid4()
        model :ShoesModel = ShoesModel(uid, vendor, category, size, color, price, sex)
        self._data.append(model)
        self.save()
        print(model.__dict__)
        return model
    
    def update(self, uid, vendor, category, size, color, price, sex):
        for model in self._data:
            if str(model.uid) == uid:
                model.vendor = vendor
                model.category = category
                model.size = size
                model.color = color
                model.price = price
                model.sex = sex
                self.save()
                break

    def delete(self, uid: str):
        for model in self._data:
            if str(model.uid) == uid:
                self._data.remove(model)
                self.save()
                break
    
    def get(self, uid):
        for model in self._data:
            if model.uid is uid:
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

    def get_tuple_values(self)-> tuple:
        return [value for value in self.__dict__.values()]



    

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
