from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot("6156300300:AAFCz6Sic4gcvMddmYyrZIDtRexuJaCnPO0", parse_mode="html") #
dp = Dispatcher(bot, storage=MemoryStorage())