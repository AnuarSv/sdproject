class Observer:
    def update(self, message):
        raise NotImplementedError

class UserObserver(Observer):
    def __init__(self, telegram_adapter, user_id):
        self.telegram_adapter = telegram_adapter
        self.user_id = user_id

    async def update(self, message):
        await self.telegram_adapter.send_message(self.user_id, message)

class NotificationService:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    async def notify(self, message):
        for observer in self._observers:
            await observer.update(message)
