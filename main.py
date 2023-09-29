import os, asyncio

from dispatcher import dp
from aiogram import Bot
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from dotenv import load_dotenv

from web_scraping.myWeb import kun_uz_play

load_dotenv()


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer("Kun.uz eng oxirgi ma'lumotlari rasmi")
    await message.answer('Biroz kuting...')
    await kun_uz_play()
    cat = FSInputFile('news.png', filename='screenshot')
    await message.answer_photo(cat)


async def main():
    token = os.getenv('BOT_TOKEN')
    bot = Bot(token)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
