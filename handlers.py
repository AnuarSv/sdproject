from aiogram import Router, F
from aiogram.filters import Command
from commands import StartCommand, HelpCommand, HistoryCommand, DeleteHistoryCommand
from strategies import HistoryResponseStrategy, GPTResponseStrategy

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

@router.message(F.text)
async def cmd_text(message: Message):
    history = await rq.get_history(message.from_user.id)
    strategy = GPTResponseStrategy() if "question" in message.text.lower() else HistoryResponseStrategy()
    response = await strategy.generate_response(message, history)
    await message.answer(response)
    await rq.save_history(message.from_user.id, f'{message.text}\n{response}')