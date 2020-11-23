 import shelve

FILE = 'countries'


def add_country_and_capital(country, capital):

    with shelve.open(FILE) as db:
        db[country] = capital


def get_capital_by_county(country):

    with shelve.open(FILE) as db:
        return db.get(country, 'Нет такой страны в БД')


add_country_and_capital('Ukraine', 'Kyiv')
add_country_and_capital('Belarus', 'Minsk')

# f = get_capital_by_county('Ukraine')
# print(f)