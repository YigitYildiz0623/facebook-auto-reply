from selenium import webdriver
import time
import pickle

print('Tarayıcı Açıldıktan Sonra Giriş Yapmanız İçin 60 Saniye Bulunmaktadır')
time.sleep(0.5)
print('.')
print('Cookiler Otomatik olaracak Çekilecektir')
print('..')
time.sleep(0.5)
print('Lütfen Tarayıcı Otomatik Kapanmayana Kadar Kapatmayınız')
time.sleep(0.5)
print('...')
cookie_number = input('Cookie Numarasını Giriniz:')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

time.sleep(120)

cookies = driver.get_cookies()
with open(f"facebook_cookies{cookie_number}.pkl", "wb") as f:
    pickle.dump(cookies, f)