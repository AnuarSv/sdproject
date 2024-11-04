from aiogram import Router, F
from aiogram.filters import Command
from commands import StartCommand, HelpCommand, HistoryCommand, DeleteHistoryCommand

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await StartCommand().execute(message)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await HelpCommand().execute(message)

@router.message(Command("history"))
async def cmd_history(message: Message):
    await HistoryCommand().execute(message)

@router.message(Command("del_history"))
async def cmd_del_history(message: Message):
    await DeleteHistoryCommand().execute(message)