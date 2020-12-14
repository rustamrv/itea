import mongoengine as me
import datetime

me.connect('test_lessons_9')


class UserProfile(me.Document):
    login = me.StringField(required=True, unique=True, min_length=4, max_length=128)
    password = me.StringField(required=True, min_length=8)
    about_me = me.StringField()
    likes = me.IntField(default=0)


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=44, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    interest = me.ListField()
    age = me.IntField(min_value=12, max_value=99)
    created_at = me.DateTimeField()
    user_profile = me.ReferenceField(UserProfile)

    def __str__(self):
        return f'{self.first_name} {self.age}'

    def say_hello(self):
        return f'Hello, my name is {self.first_name}'

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)


if __name__ == "__main__":
    user_profile = UserProfile(login='Nikolay', password='12345678')
    user_profile.save()
    user = User(first_name='Nikolay', interest=['Sport', 'Cars'], age=23,
                user_profile=user_profile)
    user.save()
    users = User.objects() #(me.Q(age__gte=20))
    print(users)
    for u in users:
        print(u.say_hello(), user.user_profile)
        print("*"*10)