import mongoengine as me
from datetime import datetime

me.connect('bot_lessons_11')


class UserQuestionnaire(me.Document):
    telegram_id = me.IntField(primary_key=True)
    username = me.StringField(min_length=2, max_lenght=128)
    first_name = me.StringField(min_length=2, max_lenght=128)
    last_name = me.StringField(min_length=2, max_lenght=128)
    phone_number = me.StringField(max_length=15)
    email = me.EmailField()
    address = me.StringField(max_length=250)
    wishes = me.StringField(max_length=500)