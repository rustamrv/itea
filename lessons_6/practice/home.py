from parser import Parser


if __name__ == '__main__':
    address = 'https://meteo.ua/sputnik'
    parser = Parser(address)
    if not parser.check_valid():
        print('Указанный ресурс не найден!')
    else:
        print(f'Ресурс {address} - найден!') 
        parser.get_weather() 