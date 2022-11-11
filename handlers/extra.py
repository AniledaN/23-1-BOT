from aiogram import Dispatcher, types
from config import bot, dp


# @dp.message_handler()
async def echo(message: types.Message):
    bad_words = ['java', 'html', 'css', 'дурак', 'доопарас']
    username = f"@{message.from_user.username}" if message.from_user.username is not None \
        else message.from_user.full_name

    for word in bad_words:
        if word in message.text.lower():
            await bot.delete_message(message.chat.id, message.message_id)
            await bot.send_message(
                message.chat.id,
                f"Не матерись {username} "
                f"сам ты {word}!"
            )

    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.text == 'dice':
        a = await bot.send_dice(message.chat.id, emoji='🎲')
        # print(a.dice.value)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
