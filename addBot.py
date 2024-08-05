import os

template = """
from model import BotFunctions

bf = BotFunctions()

bf.bot_started('{bot_number}')

bf.open_driver_and_login({cookie_number})
bf.get_last_person()

while True:
    bf.start_listen(message=bf.get_message())
"""

while True:
    bot_number = input("Lütfen Bot Numarasın Giriniz ...:")

    if os.path.exists(f'bot{bot_number}.py'):
        print('Girdiğiniz bot numarasına sahip bot zaten mevcut')

    else:
        cookie_number = input("Lütfen Cookie Numarasını Giriniz ...:")

        full_code = template.format(bot_number=bot_number,cookie_number=cookie_number)

        approve = input('Bot oluşumuna onay vermek istiyor musunuz: (y/N) ')

        if approve.lower() == 'y':
            with open(f'bot{bot_number}.py','w') as file:
                file.write(full_code)

            print('Bot Başarıyla Oluşturuldu')
            break

        else:
            print('Bot oluşumuna onay vermediniz.')
