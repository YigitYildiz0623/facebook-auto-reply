from colorama import Fore

##### BEKLEME SÜRELERİ ######
#Tarayıcı Başlangıcında Uyuma Süresi
START_SLEEP = 20

#Tarayıcı İşlemleri Sonrası Bekleme Süresi
OP_SLEEP = 2

#Mesaj Attıktan Sonraki Uyuma Süresi
MS_SLEEP = 3

#Mesaj Alanı Bekleme Süresi
WM_SLEEP = 10


#Bot Açıklaması
DESCRIPT = '''

'''


##### YOLLAR #####
#ChromeDriver PATH
PYTHON_PATH = '/Users/yigityildiz/Desktop/Facebook_Bot_Project/venv/bin/python'


#Sohbet Kutusu XPATH
CHAT_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[5]/div/div/div/div/div/div/div[2]/div/div[1]"

#Sohbet Kutusu Alt Hesap XPATH
ALT_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div/div[1]"

#Mesaj Kutusu XPATH
MESSAGE_XPATH = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div[2]/div/div[1]/div[1]/p"


###### RENKLER ######
#Hata Mesajı Rengi
ERR_COLOR = Fore.RED

#Yeni Kişi Bulundu
NEW_COLOR = Fore.YELLOW

#Mesaj Gönderildi
SEND_COLOR = Fore.GREEN

#Yeni Mesaj Bulunamadı
NO_COLOR = Fore.BLUE