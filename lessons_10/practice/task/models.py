from random import choice
import mongoengine as me
from datetime import datetime
import names

me.connect('rest_api_lessons_10_task')


class Tag(me.Document):
    name = me.StringField(min_length=2, max_length=25, unique=True)

    def save(self, *args, **kwargs):
        list_name = self.name.split(" ")
        if len(list_name) >= 2:
            raise ValueError('tag name must be one word')
        super().save(*args, **kwargs)


class Author(me.Document):
    first_name = me.StringField(min_length=2, max_length=44, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    number_of_publications = me.IntField()


class Post(me.Document):
    name = me.StringField(min_length=2, max_length=25, required=True, unique=True)
    description = me.StringField(min_length=10, max_length=300)
    created_at = me.DateTimeField()
    number_of_views = me.IntField(default=0)
    tag = me.ListField(me.ReferenceField(Tag))
    author = me.ReferenceField(Author)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        super().save(*args, **kwargs)


if __name__ == "__main__":
    list_tag = ['film', 'music', 'coronavirus', 'thebest', 'game', 'gamethebest', "help", '2020']
    for i in list_tag:
        try:
            Tag(name=i).save()
        except me.NotUniqueError:
            print('Unique tag')

    for i in range(0, 10):
        try:
            author = Author(first_name=names.get_first_name(), last_name=names.get_last_name())
            author.save()
        except me.ValidationError as error:
            print(error)
    data = [
        {
            "name": "Film 'Rocky'",
            "description": "Post about film 'Rocky'",
            "tag": [Tag.objects.get(name='film'), Tag.objects.get(name='thebest')],
            "author": choice(Author.objects)
        },
        {
            "name": "Film 'Creed'",
            "description": "Post about film 'Creed'",
            "tag": [Tag.objects.get(name='film'), Tag.objects.get(name='thebest')],
            "author": choice(Author.objects)
        },
        {
            "name": "Film 'Creed'",
            "description": "Post about film 'Creed'",
            "tag": [Tag.objects.get(name='film')],
            "author": choice(Author.objects)
        },
        {
            "name": "Music 'Eye of the tiger'",
            "description": """Rising up, back on the street \n Did my time, took my chances """,
            "tag": [Tag.objects.get(name='music'), Tag.objects.get(name='thebest')],
            "author": choice(Author.objects)
        },
        {
            "name": "Music 'Там где нас нет'",
            "description": """Ты хотя бы понимаешь что ты делаешь со своей жизнью? \n Хочешь как мать? Хочешь 
            закончить, как она?""",
            "tag": [Tag.objects.get(name='music'), Tag.objects.get(name='thebest')],
            "author": choice(Author.objects)
        },
        {
            "name": "Game 'Mafia 2'",
            "description": """Mafia II — компьютерная игра в жанре приключенческого боевика с открытым миром""",
            "tag": [Tag.objects.get(name='game'), Tag.objects.get(name='thebest'), Tag.objects.get(name='gamethebest')],
            "author": choice(Author.objects)
        },
        {
            "name": "2020 - год пандемии",
            "description": """Коронавирус (лат. Coronaviridae) — семейство вирусов, включающее на май 2020 года.""",
            "tag": [Tag.objects.get(name='coronavirus'), Tag.objects.get(name='help'), Tag.objects.get(name='2020')],
            "author": choice(Author.objects)
        },
    ]

    for i in data:
        try:
            Post(**i).save()
        except me.NotUniqueError:
            print('post unique')