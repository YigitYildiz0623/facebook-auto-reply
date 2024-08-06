# facebook-auto-reply
FaceBook Otomatik Cevap Botu (Sınırsız Hesapta Aynı Anda Çalıştırabilirsiniz)

# Kurulumlar
Bu bölümde program ilk indirildiğinde çalıştırılması için gereken kütüphanelerin nasıl indirileceğini ve bot hesapların nasıl ekleneceğini detaylı bir şekilde açıklayacağım.

### Kütüphanelerin İndirilmesi
Bunun için iki farklı yöntem bulunmakta. İlk olarak en basit şekilde "pip install -r requirements.txt" komutunu çalıştırabilirsiniz. İkinci yol ise "pip install 'kütüphane_adı' şeklinde rquirements dosyasındaki tü$
 
### Settings.py Dosyası
Yapmanız gereken en önemli diğer bir ayar ise settings.py dosyasındaki PYTHON_PATH kısmına kendi python yolunuzu girmeniz gerekmektedir. Ayrıca uygulamanın tüm ayarlarını buradan yapabilirsiniz.      

### Hesap Cookielerinin Çekilmesi
cookies klasörünün içindeki getcookies.py dosyasını çalıştırdıktan sonra sizden cookie numarası ister buna istediğiniz değeri girebilirsiniz. Sonrasında sizi facebook giriş ekranı sizi karşılar. Burada bot olarak $
Not:Giriş yapmak için verilen varsayılan süre 120 saniyedir. Bunu dosyanın içinden değiştirebilirsiniz.

### Bot Oluşturulması
Ana dizinde addBot.py dosyasını çalıştırarak bot ekleme işlemini gerçekleştirebilirsiniz. Sizden en başta bot numarası istenir. Bu bot numarasına istediğiniz değeri girebilirsiniz. Sonrasında botlarımızı çalıştıra$
Bu şekilde istediğimiz sayıda bot ekleyebiliriz yazılımımıza.

# Botun Çalıştırılması
Botlarımızı eklediğimize göre artık main.py dosyamızı çalıştırarak yazılımımızı başlatabiliriz. Çalıştırmak istediğimiz botu girdiğimiz anda tarayıcı facebooka girip birkaç saniye içinde bota bağladığımız cookiele$
Not: Botlar mesaja cevap vermeyi en üstteki sohbete göre yapar. En üstteki kişi değiştiğinde yeni en üstteki kişiye mesajı gönderir.

#### Alt Profiller
Botlar alt profillere geçildiğinde de sorunsuz çalışır. Sadece cevap verme süresi birkaç saniye daha uzar.

### Messages.txt
Bu dosyanın altında mesajlarınızı listeleyebilirsiniz. Mesajlar bot tarafından rastgele seçilip gönderilir.
Dikkat edilmesi gereken hususlar: Her mesajın tek satırda yazılması ve bmp formatına uygun(Emoji veya şekilli yazıların olmaması) olması.


## Kullanıcı ve Geliştiricilere Not
Umarım bot işinize yaramış ve düzgünce kullanmakta sorun yaşamamışsınızdır. Eğer bir bug bulup düzeltmek isterseniz veya yeni bir özellik eklemek isterseniz istediğiniz zaman istek oluşturabilirsiniz.
