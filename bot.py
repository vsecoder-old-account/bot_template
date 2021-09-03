# -*- coding: utf-8 -*-

# AIOGRAM
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.utils.exceptions import Throttled
from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode, reply_keyboard
from aiogram.utils import executor
import aiogram.utils
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.executor import start_webhook
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# DB models
from models import db_session
from models.users import User

# Admin panel
import threading
def web():
    import web
x = threading.Thread(target=web)
x.start()

# Logging
from scripts.checks import print_log

# Time
import datetime

db_session.global_init('database.db')

bot_token = '1409551099:AAH7dlcOfAwITtbWnMsn0HB1mDhP_XXuLG0' # token

bot = Bot(token=bot_token)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

class States(Helper):
    mode = HelperMode.snake_case

    STATE_0 = ListItem()

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer("👮 Слишком много запросов, просим подождать!")

# /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
	session = db_session.create_session()
	iduser = message.from_user.id
	user_all = session.query(User).all()
	T = True
	for all in user_all:
		if all.id == iduser:
			T = False

	if T == True:
		# добавить нового юзера
		session = db_session.create_session()
		name = message.from_user.first_name
		url = message.from_user.username
		iduser = message.from_user.id
		message.from_user.last_name = '-'
		if message.from_user.last_name != None:
			fullname = message.from_user.last_name
        
		now = datetime.datetime.now()
		user = User(
			id=iduser,
			name=name,
            fullname=fullname,
			data='[{}]',
            work=now.strftime("%d-%m-%Y %H:%M")
		)
		session.add(user)
		session.commit()
		await bot.send_message(message.chat.id, '''text''', parse_mode="HTML")
		print_log(f"New user ID:{iduser} {name}", 'INFO', 'BOT')
	else:
		await bot.send_message(message.chat.id, 'text')

@dp.message_handler(content_types=["text"])
@dp.throttled(anti_flood, rate=2)
async def check(message: types.Message):
	try:
		if message.text == 'text':
			state = dp.current_state(user=message.from_user.id)
			await state.set_state(States.all()[0])
	except BaseException as e:
		await bot.send_message(1218845111, 'В системе ошибка...\n<code>' + str(e) + '</code>', parse_mode='html')
		await bot.send_message(message.chat.id, 'Упс, ошибка...')
		print_log(f"Error: {e}", 'ERROR', 'BOT')

@dp.message_handler(state=States.STATE_0)
async def state_case_met1(message: types.Message):
	await bot.send_message(message.chat.id, 'text')

	state = dp.current_state(user=message.from_user.id)
	await state.reset_state()

async def ad_send(text):
	session = db_session.create_session()
	user_all = session.query(User).all()
	have = 0
	try:
		for all in user_all:
			await bot.send_message(all.id, text, parse_mode='HTML')
			have = have + 1
	except Exception:
		pass
	print_log(f"Ad sending {have}!", 'INFO', 'BOT')
	return have

if __name__ == "__main__":
	print_log(f"Bot starting", 'INFO', 'BOT')
	executor.start_polling(dp)
	print_log(f"Bot stoping", 'INFO', 'BOT')