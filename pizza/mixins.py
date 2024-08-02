import statemanager as sm


class StorageMixin:

    def load(self):
        sm.load(self.data)

    def save(self):      
        sm.save(self.data)
        

    def load_default(self):
        self.first_load = False


        try:
            self.load()
        except:
            print('No such file')
            self.first_load = True
        self.save()
        

    
