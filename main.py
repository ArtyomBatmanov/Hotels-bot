import database.create_bd
from loader import bot
import handlers # noqa
from telebot.custom_filters import StateFilter
from utils.set_bot_commands import set_default_commands



if __name__ == "__main__":
    database.create_bd.create_table()
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
