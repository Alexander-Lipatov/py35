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


# Adapter pattern
class ModernNotificationService:
    def send_notification(self, message):
        print(f"Sending modern notification: {message}")

class LegacySMSService:
    def send_sms(self, text):
        print(f"Sending SMS: {text}")

class SMSAdapter(ModernNotificationService):
    def __init__(self, legacy_sms_service):
        self.legacy_sms_service = legacy_sms_service

    def send_notification(self, message):
        self.legacy_sms_service.send_sms(message)

# Client code
if __name__ == "__main__":
    modern_notification = ModernNotificationService()
    legacy_sms = LegacySMSService()
    sms_adapter = SMSAdapter(legacy_sms)

    modern_notification.send_notification("Hello, modern world!")
    sms_adapter.send_notification("Hello, legacy system!")



# Decorator pattern


class DataSource:
    def writeData(self, data):
        pass
    def readData(self):
        pass

class FileDecorator(DataSource):
    
    def writeData(self, data):
        pass
    def readData(self):
        pass





