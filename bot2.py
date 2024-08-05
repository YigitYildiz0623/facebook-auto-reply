
from model import BotFunctions

bf = BotFunctions()

bf.bot_started('2')

bf.open_driver_and_login(2)
bf.get_last_person()

while True:
    bf.start_listen(message=bf.get_message())
