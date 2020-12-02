import mongoengine as me
import datetime

me.connect('rest_api_lessons_10') 


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=44, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interest = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField() 

    def __str__(self):
        return f'{self.first_name} {self.age}'

    def say_hello(self):
        return f'Hello, my name is {self.first_name}'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)


if __name__ == "__main__": 
    user = User(first_name='Nikolay', interest=['Sport', 'Cars'], age=23)
    user.save() 
