from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from Gemini import gpt
from texts import help, welcome
import requestsDB as rq
import keyboard as kb
from data import data_gemini


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(welcome, reply_markup=kb.reply_kb)


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(help, reply_markup=kb.reply_kb)


@router.message(Command('history'))
async def cmd_get_history(message: Message):
    history = await rq.get_history(message.from_user.id)
    await message.reply(history, reply_markup=kb.reply_kb)


@router.message(Command('del_history'))
async def cmd_del_history(message: Message):
    del_history = await rq.delete_history(message.from_user.id)
    await message.reply(del_history, reply_markup=kb.reply_kb)


@router.message(F.text == 'Help❔️')
async def cmd_answer(message: Message):
    await message.answer(help, reply_markup=kb.reply_kb)


@router.message(F.text == 'My History🗒️')
async def cmd_answer(message: Message):
    history = await rq.get_history(message.from_user.id)
    await message.reply(history, reply_markup=kb.reply_kb)


@router.message(F.text == 'Delete my history 🗑️')
async def cmd_answer(message: Message):
    del_history = await rq.delete_history(message.from_user.id)
    await message.reply(del_history, reply_markup=kb.reply_kb)


@router.message(F.text)
async def cmd_answer(message: Message):
    history = await rq.get_history(message.from_user.id)
    response = await gpt(message.text, history, data_gemini)
    await message.reply(response)
    await rq.save_history(message.from_user.id, f'{message.text}\n{response}')
