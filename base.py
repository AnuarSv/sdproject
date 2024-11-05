from aiogram.types import Message
from abc import ABC, abstractmethod

class BaseCommand(ABC):
    @abstractmethod
    async def execute(self, message: Message):
        pass

