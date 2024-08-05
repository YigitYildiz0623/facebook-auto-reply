from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import settings as se
import random
import colorama
import pyfiglet
import pickle

class BotFunctions():

    def __init__(self):
        self.url = 'https://www.facebook.com/messages/t'
        self.last_person = None

    def bot_started(self,number):
        print(colorama.Fore.GREEN+f"Bot {number} Başlatıldı ....:")

    def start_app(self):
        colorama.init(autoreset=True)
        app_name = pyfiglet.figlet_format("FaceBook Oto Mesaj Botu")
        print(colorama.Fore.CYAN + app_name)
        description = se.DESCRIPT
        print(colorama.Fore.YELLOW + description)

    def open_driver_and_login(self,number):
        try:
            self.driver = webdriver.Chrome()
            self.driver.get(self.url)
            self.cookies = pickle.load(open(f'cookies/facebook_cookies{number}.pkl','rb'))
            for cookie in self.cookies:
                self.driver.add_cookie(cookie)

            print(self.driver.title)

            time.sleep(se.START_SLEEP)
        except Exception as e:
            print(se.ERR_COLOR+'Driver düzgün bir şekilde başlatılamadı')
            print('Hata mesajı ...: ',e)

    def get_message(self):
        with open('messages.txt','r',encoding='utf-8') as self.file:
            self.lines = self.file.readlines()
        
        self.lines = [line.strip() for line in self.lines if line.strip()]
        if self.lines:
            self.random_line = random.choice(self.lines)
        else:
            print(se.ERR_COLOR+'messages.txt Dosyasında Geçerli Mesaj Bulunamadı')


        return self.random_line
    
    def get_last_person(self):
        try:
            try:
                self.last_chat =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.CHAT_XPATH)))
            except:
                self.last_chat =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.ALT_XPATH)))
            
            self.last_person = self.last_chat.text.splitlines()[0]
            time.sleep(se.OP_SLEEP)
            return self.last_person
        except Exception as e:
            print(se.ERR_COLOR+'Son sohbet bilgisi alınamadı. Muhetmel sorun: XPATH')
            print('Hata mesajı ...: ',e)
    
    def wait_next_message(self):
        time.sleep(se.MS_SLEEP)
    
    def start_listen(self,message):
        try:
            last =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.CHAT_XPATH))).text.splitlines()[0]
        except:
            last =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.ALT_XPATH))).text.splitlines()[0]

        if self.last_person != last:
            print(se.NEW_COLOR+'Yeni Mesaj Bulundu: ',last)
            try:
                self.last_chat =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.CHAT_XPATH)))
            except:
                self.last_chat =  WebDriverWait(self.driver,se.WM_SLEEP).until(EC.presence_of_element_located((By.XPATH,se.ALT_XPATH)))
            self.last_person = last
            self.last_chat.click()
            time.sleep(se.OP_SLEEP)

            try:
                self.message_box = self.driver.find_element(By.XPATH,se.MESSAGE_XPATH)
                self.message_box.send_keys(message)
                time.sleep(se.OP_SLEEP)
                self.message_box.send_keys(Keys.ENTER)
            except Exception as e:
                print('Mesah Gönderilemedi')
                print('Hata mesajı ...: ',e)
            print(se.SEND_COLOR+f"{last}'a mesaj gönderildi")
            self.wait_next_message()
        else:
            print(se.NO_COLOR+'Yeni Mesaj Bulunamadı')
            self.wait_next_message()