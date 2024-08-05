import subprocess
import settings as se
from model import BotFunctions

bf = BotFunctions()

bf.start_app()

def run_bot(bot_name):
    try:
        with open(f"logs/bot{bot_name}_log.txt", "w") as f:
            subprocess.Popen([se.PYTHON_PATH ,f'bot{bot_name}.py'], stdout=f, stderr=f)
        print(f"Bot {bot_name} başarıyla başlatıldı (Çıktı: bot{bot_name}_log.txt)")
    except Exception as e:
        print(f'Bot {bot_name} dosyası başlatılamadı: {e}')


def main():
    while True:
        bot_name = input("Lütfen çalıştırmak istediğiniz botu girin (Çıkmak için 'exit' yazın): ")
        if bot_name.lower() == 'exit':
            print("Çıkılıyor...")
            break

        else:
            run_bot(bot_name)


if __name__ == "__main__":
    main()
