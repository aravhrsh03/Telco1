from dataclasses import dataclass

@dataclass
class Notification:
    def send(self, msg):
        raise NotImplementedError

@dataclass
class SMSNotification(Notification):
    def send(self, msg):
        print(f"SMS: {msg}")

@dataclass
class EmailNotification(Notification):
    def send(self, msg):
        print(f"Email: {msg}")

@dataclass
class WhatsAppNotification(Notification):
    pass

@dataclass
class NotificationService:
    strategy: Notification
    
    def send(self, msg):
        self.strategy.send(msg)
    
service = NotificationService(WhatsAppNotification())
print(service.strategy)
service.send("Message Sent")