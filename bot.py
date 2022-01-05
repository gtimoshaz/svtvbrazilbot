from aiogram import Bot, Dispatcher, executor, types
import os
import textwrap


API_TOKEN = os.environ["API_TOKEN"]

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это бот, чтобы рисовать картинку, где Светов на другом конце планеты говорит что-то о России или СНГ. Пришлите мне флаг с текстом твитта Светова, и я их совмещу")

@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Пожалуйста, пришлите текст с картинкой-флагом")

@dp.message_handler(content_types=['photo'])
async def handle_image(message: types.Message):
    if not message.caption:
        await message.reply("Пожалуйста пришлите эту же картинку, но с текстом")
        return
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
