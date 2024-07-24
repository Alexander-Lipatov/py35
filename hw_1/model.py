from abc import ABC
from statemanager import load, save

class Product(ABC):
    _data = {}
    
    def __init__(self, *args, **kwargs):
        try:
            self._data = load()
        except:
            self._data = {}
            self.save()

    type = None

    def save(self):
        save(self._data)

    def all(self):
        return self._data

    @staticmethod
    def create(cls, vendor, category, size, color, price):
        if cls.type not in ['Men', 'Woman']:
            raise ValueError("Invalid shoe type. Must be 'Men' or 'Woman'.")

        data = {
            'vendor': vendor,
            'category': category,
            'size': size,
            'color': color,
            'price': price
        }
        return cls(**data)
        

class ShoesModel(Product):
    def __init__(self, vendor, category, size, color, price):
        super().__init__()
        self.vendor = vendor
        self.category = category
        self.size = size
        self.color = color
        self.price = price

        if self.type not in self._data:
            self._data[self.type] = []

        self._data[self.type].append(self.get_data())
        self.save()

    def get_data(self):
        return {
            'vendor': self.vendor,
            'category': self.category,
            'size': self.size,
            'color': self.color,
            'price': self.price
        }


class MenShoes(ShoesModel):
    type = 'Men'


class WomanShoes(ShoesModel):
    type = 'Woman'


# # Пример использования статического метода
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# men_shoes_data = Product.create(MenShoes, vendor="Nike", category="Sneakers", size=42, color="Black", price=100)
# woman_shoes_data = Product.create(WomanShoes, vendor="Adidas", category="Heels", size=38, color="Red", price=150)

# # Доступ ко всем данным
# model = Product()
# print(model.all())
