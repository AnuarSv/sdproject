from aiogram.types import Message
from aiogram import Router

router = Router()

class StartCommand:
    async def execute(self, message: Message):
        await message.answer("Hello! I am Astana IT University Bot")

class HelpCommand:
    async def execute(self, message: Message):
        help_text = '''🤖 Astana IT University Chatbot Help
        How to Use the Bot:
        - Start: Type "Hello!" to begin the conversation.
        - Ask Questions on topics such as Admission requirements, Scholarship applications, etc.
        '''
        await message.answer(help_text)

class HistoryCommand:
    async def execute(self, message: Message):
        history = await rq.get_history(message.from_user.id)
        await message.answer(history if history else "No history available.")

class DeleteHistoryCommand:
    async def execute(self, message: Message):
        await rq.delete_history(message.from_user.id)
        await message.answer("History deleted successfully.")
