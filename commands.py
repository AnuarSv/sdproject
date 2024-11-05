from aiogram.types import Message
from base import BaseCommand
from Gemini import GeminiService
from requestsDB import HistoryService
from texts import help
from keyboard import reply_kb

class HelpCommand(BaseCommand):
    async def execute(self, message: Message):
        await message.answer(help, reply_markup=reply_kb)


class HistoryCommand(BaseCommand):
    def __init__(self, history_service: HistoryService):
        self.history_service = history_service

    async def execute(self, message: Message):
        history = await self.history_service.get_history(message.from_user.id)
        await message.answer(history or "No history found.", reply_markup=reply_kb)

class DeleteHistoryCommand(BaseCommand):
    def __init__(self, history_service: HistoryService):
        self.history_service = history_service

    async def execute(self, message: Message):
        await self.history_service.delete_history(message.from_user.id)
        await message.answer("History deleted.", reply_markup=reply_kb)

class DefaultCommand(BaseCommand):
    def __init__(self, gemini_service: GeminiService, history_service: HistoryService):
        self.gemini_service = gemini_service
        self.history_service = history_service

    async def execute(self, message: Message):
        history = await self.history_service.get_history(message.from_user.id)
        response = await self.gemini_service.get_response(message.text, history)
        await self.history_service.save_history(message.from_user.id, f"USER: {message.text}\nGemini: {response}")
        # print(f"{message.text}\n{response}")
        await message.reply(response)
