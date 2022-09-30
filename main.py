from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboard import *

token = '5700260133:AAHAgTcy3hXt9UwTdvkkB84v51jcwHoE_rI'

bot = Bot(token=token)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Start')


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer("Привет, выбери предмет.", reply_markup=keyboard)
    await message.delete()


@dp.message_handler(commands=['ввм'])
async def command_wwm(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/84607638315?pwd=V284U0xGamxMTGZuTC8wQ1BsRVF5dz09", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['мок'])
async def command_mok(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/85661175197?pwd=WUczc2d4R2pVREJ6Y1pFZ1pWQlYyZz09#success", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['опос'])
async def command_opoc(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/88592085134?pwd=Q3BDa2E2dEVQNUJ2YXBvUlh5UDExZz09", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['тп'])
async def command_tp(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/84178888643?pwd=dXptV28xcFZYZ3U1Tk4yejJTejNVdz09", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['Філософія'])
async def command_filosofija(message: types.Message):
    await message.answer("Ідентифікатор: 699 367 1571 \nпароль: 012345", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['опос_лр'])
async def command_opoc_lr(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/82779889372?pwd=SHBIZGYwUWVRYnhJbHUwd092Y0x1dz09")
    await message.delete()


@dp.message_handler(commands=['тп_лр'])
async def command_tp_lr(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/89943133937?pwd=cHA5dmNBc1hId2l4NjVWY2YxbmM1dz09", reply_markup=keyboard_start)
    await message.delete()


@dp.message_handler(commands=['ввм_лр'])
async def command_wwm_lr(message: types.Message):
    await message.answer("https://us02web.zoom.us/j/85260722333?pwd=cjUvQ2c0dlVUWWNIM0tDbi9TY1VTUT09", reply_markup=keyboard_start)
    await message.delete()


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)