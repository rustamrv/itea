import telebot
from config import TOKEN
from utils import inline_kb_from_iterable
import constants
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, KeyboardButton, ReplyKeyboardMarkup
import json
from models import UserQuestionnaire
from mongoengine import NotUniqueError
from mongoengine.errors import ValidationError

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handler_start(message):
    kb = inline_kb_from_iterable(constants.questionnaire_tag, 'Заполнить анкету')
    try:
        UserQuestionnaire.objects.create(
            telegram_id=message.chat.id,
            username=getattr(message.from_user, 'username', None)
        )
    except NotUniqueError:
        pass
    bot.send_message(message.chat.id, 'День добрый! Бот-консультант готов вам помочь!', reply_markup=kb)


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.questionnaire_tag)
def handler_send_name(call):
    constants.client_status[call.message.chat.id] = constants.firstname
    bot.send_message(call.message.chat.id, 'Введите свое имя!')


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.lastname)
def handler_send_family(call):
    constants.client_status[call.message.chat.id] = constants.lastname
    bot.send_message(call.message.chat.id, 'Введите фамилию!')


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.email)
def handler_send_family(call):
    constants.client_status[call.message.chat.id] = constants.email
    bot.send_message(call.message.chat.id, 'Введите почту!')


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.address)
def handler_send_family(call):
    constants.client_status[call.message.chat.id] = constants.address
    bot.send_message(call.message.chat.id, 'Введите адрес!')


@bot.callback_query_handler(lambda c: json.loads(c.data)['tag'] == constants.wishes)
def handler_send_family(call):
    constants.client_status[call.message.chat.id] = constants.wishes
    bot.send_message(call.message.chat.id, 'Введите пожелание!')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    client_id = message.chat.id
    if client_id in constants.client_status:
        if constants.client_status[client_id] == constants.firstname:
            user = UserQuestionnaire.objects.get(telegram_id=client_id)
            user.first_name = message.text
            user.save()
            kb = inline_kb_from_iterable(constants.lastname, 'Ввести фамилию')
            bot.send_message(message.chat.id, "Сохранили имя. ", reply_markup=kb)
        elif constants.client_status[client_id] == constants.lastname:
            user = UserQuestionnaire.objects.get(telegram_id=client_id)
            user.last_name = message.text
            user.save()
            kb = ReplyKeyboardMarkup()
            but = KeyboardButton('Отправить телефон', request_contact=True)

            kb.add(but)
            bot.send_message(message.chat.id, "Сохранили фамилию. Отправьте телефон ", reply_markup=kb)
        elif constants.client_status[client_id] == constants.email:
            try:
                user = UserQuestionnaire.objects.get(telegram_id=client_id)
                user.email = message.text
                user.save()
                kb = inline_kb_from_iterable(constants.address, 'Ввести адрес')
                bot.send_message(message.chat.id, "Мы сохранили почту. ", reply_markup=kb)
            except ValidationError:
                kb = inline_kb_from_iterable(constants.email, 'Ввести почту')
                bot.send_message(message.chat.id, "Не верная почта. ", reply_markup=kb)

        elif constants.client_status[client_id] == constants.address:
            user = UserQuestionnaire.objects.get(telegram_id=client_id)
            user.address = message.text
            user.save()
            kb = inline_kb_from_iterable(constants.wishes, 'Ввести пожелания')
            bot.send_message(message.chat.id, "Сохранили адрес. ", reply_markup=kb)
        elif constants.client_status[client_id] == constants.wishes:
            user = UserQuestionnaire.objects.get(telegram_id=client_id)
            user.wishes = message.text
            user.save()
            bot.send_message(message.chat.id, "Спасибо что вы с нами. Все данные у нас. Мы с вами свяжемся")


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        client_id = message.chat.id
        user = UserQuestionnaire.objects.get(telegram_id=client_id)
        user.phone_number = message.contact.phone_number
        user.save()
        kb = inline_kb_from_iterable(constants.email, 'Ввести почту')
        bot.send_message(message.chat.id, "Сохранили телефон. ", reply_markup=kb)


bot.polling()