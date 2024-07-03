import datetime

# Adapter pattern
class LogToFile:
    def __init__(self, filename) -> None:
        self.filename = filename

    def log(self, *args):
        with open(self.filename, 'a') as file:
            file.write(str(datetime.datetime.now()) + ': '+ ', '.join(map(str, args)) + '\n')

class LogToDisplay:
    def log(self, *args):
        print('log to display', *args)


class LoggerAdapter:
    def __init__(self, logObject:LogToDisplay|LogToFile) -> None:
        self.logObject = logObject

    def log(self,*args):
        self.logObject.log(*args)


logger = LoggerAdapter(LogToFile('log.txt'))
class Calc:
    def __init__(self) -> None:
        self.log('__________start______________')
        self.x = 0

    def add(self,x ):
        self.log(self.x, 'adkmfdgkdmkdfmd', x)
        self.x += x

    def log(self, *args):
        logger.log(*args)



# c1 = Calc()

# c1.add(5)
# c1.add(10)
# c1.add(100)