from aiogram import F, Router
from aiogram.types import Message
from commands import HelpCommand, HistoryCommand, DeleteHistoryCommand, DefaultCommand
from requestsDB import HistoryService
from Gemini import GeminiService
import keyboard as kb

router = Router()

history_service = HistoryService()
gemini_service = GeminiService()

@router.message(F.text == 'Help❔️')
async def cmd_help(message: Message):
    await HelpCommand().execute(message)

@router.message(F.text == 'My History🗒️')
async def cmd_history(message: Message):
    await HistoryCommand(history_service).execute(message)

@router.message(F.text == 'Delete my history 🗑️')
async def cmd_delete_history(message: Message):
    await DeleteHistoryCommand(history_service).execute(message)

@router.message(F.text)
async def cmd_default(message: Message):
    await DefaultCommand(gemini_service, history_service).execute(message)
