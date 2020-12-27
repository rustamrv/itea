import json
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def inline_kb_from_iterable(
        tag,
        text_field):
    json_data = json.dumps({
        'tag': tag
    })
    but = InlineKeyboardButton(
        text=text_field,
        callback_data=json_data
    )
    kb = InlineKeyboardMarkup()
    kb.add(but)
    return kb
