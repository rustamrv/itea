import mongoengine as me
from datetime import datetime
import names
from random import choice, randint

me.connect('test_lessons_9')


class Faculty(me.Document):
    name = me.StringField(equired=True, unique=True, min_length=4, max_length=120)


class Curator(me.Document):
    name = me.StringField(equired=True, unique=True, min_length=4, max_length=120)


class Group(me.Document):
    name = me.StringField(equired=True, unique=True, min_length=4, max_length=120)


class Subject(me.Document):
    name = me.StringField(min_length=4, max_length=120)
    group = me.ReferenceField(Group)


class Student(me.Document):
    first_name = me.StringField(min_length=3, max_length=50)
    last_name = me.StringField(min_length=4, max_length=120)
    created_at = me.DateTimeField()
    group = me.ReferenceField(Group)
    faculty = me.ReferenceField(Faculty)
    curator = me.ReferenceField(Curator)

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        super().save(*args, **kwargs)


class RateList(me.Document):
    rate = me.IntField()
    student = me.ReferenceField(Student)
    subject = me.ReferenceField(Subject)


class ManagerDb:

    def __init__(self):
        pass

    @staticmethod
    def run_faculty():
        list_faculty = [f'Faculty - {i}' for i in range(0, 5)]
        for name in list_faculty:
            fac = Faculty(name=name)
            fac.save()

    @staticmethod
    def run_curator():
        for i in range(0, 50):
            cur = Curator(name=names.get_full_name())
            cur.save()

    @staticmethod
    def run_group():
        list_group = [f'Group - {i}' for i in range(0, 10)]
        for name in list_group:
            cur = Group(name=name)
            cur.save()

    @staticmethod
    def run_subject():
        list_subject = [f'Subject - {i}' for i in range(0, 10)]
        list_group = [f'Group - {i}' for i in range(0, 10)]
        for name in list_subject:
            group = Group.objects(name=choice(list_group))
            cur = Subject(name=name)
            cur.group = group[0]
            cur.save()

    @staticmethod
    def run_student():
        list_group = [f'Group - {i}' for i in range(0, 10)]
        list_faculty = [f'Faculty - {i}' for i in range(0, 5)]
        for i in range(0, 101):
            try:
                student = Student(first_name=names.get_first_name(), last_name=names.get_last_name())
                student.group = Group.objects(name=choice(list_group))[0]
                student.faculty = Faculty.objects(name=choice(list_faculty))[0]
                student.curator = choice(Curator.objects)
                student.created_at = datetime.now()
                student.save()
            except me.ValidationError as error:
                print(error)

    @staticmethod
    def run_rate():
        list_subject = Subject.objects
        students = Student.objects
        for student in students:
            for subject in list_subject:
                rate = RateList()
                rate.student = student
                rate.subject = subject
                rate.rate = randint(2, 5)
                rate.save()


if __name__ == "__main__":
    mn = ManagerDb()
    # mn.run_faculty()
    # mn.run_curator()
    # mn.run_group()
    # mn.run_subject()
    # mn.run_student()
    # mn.run_rate()