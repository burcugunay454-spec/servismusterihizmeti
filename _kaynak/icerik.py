# -*- coding: utf-8 -*-
"""Servis Müşteri Hizmeti — tüm ayarlar ve metinler.
Kurallar (Google Ads "kabul edilemez iş uygulamaları" / yanıltıcı beyan):
  * Hiçbir marka adı ve logosu yazılmaz/gösterilmez; "yetkili", "resmi", "orijinal" denmez.
  * "Bağımsız özel servis, hiçbir markanın yetkili servisi değildir" açıklaması sayfanın en altında (footer şeridi) görünür.
  * Doğrulanmamış iddia (yıl, garanti süresi, dakika, fiyat, yorum, puan) yazılmaz.
  * Ücret işlem öncesi bildirilir; onay olmadan işlem yapılmaz.
"""

# ---------------- AYARLAR (yalnız burayı doldurun) ----------------
FIRMA = "Servis Müşteri Hizmeti"
ALAN = "https://servismusterihizmeti.com.tr"
TEL = "0 (232) 332 22 19"            # örn. "0532 123 45 67" — boşken site noindex ve yer tutucu numara
WHATSAPP = "YOK"    # "YOK": WhatsApp düğmeleri ve form gizlenir; boşsa TEL kullanılır
UNVAN = ""          # resmi ticari unvan (varsa; Ads doğrulaması için önerilir)
ADRES = ""          # açık adres (varsa)
SAAT = "Hafta içi ve hafta sonu, randevu ile"   # doğrulanmış çalışma saati yazın
EPOSTA = ""
GTM = ""            # örn. "GTM-XXXXXXX"
GA4 = "G-ZC50CXV20Z"                              # Google Analytics 4 ölçüm kimliği (kelekramiz@gmail.com, mülk "servismusterihizmeti.com.tr")
AW = "AW-18575593481"                             # Google Ads 200-368-6301
AW_TEL = "AW-18575593481/k9YlCOX4qb8dEImgxJlF"    # Ads dönüşümü "Telefon tiklama" (Kişi, sayım: Bir)
# ------------------------------------------------------------------

ACIKLAMA_KISA = "Bağımsız özel teknik servis — hiçbir markanın yetkili servisi değildir."

TITLE = "Beyaz Eşya, Kombi ve Klima Servisi | " + FIRMA
DESC = ("Buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın, kombi ve klima arızalarında adreste "
        "arıza tespiti ve onarım. Ücret işlemden önce bildirilir, onayınız olmadan işlem yapılmaz.")

# 2. bölüm — cihazlar (anahtar, başlık, metin, görsel dosya adı)
CIHAZLAR = [
    ("buzdolabi", "Buzdolabı", "Soğutma kaybı, karlanma, su sızıntısı, fan ve termostat sorunları.", "buzdolabi"),
    ("camasir", "Çamaşır Makinesi", "Su boşaltmama, sıkmama, kapak kilidi, aşırı titreşim ve hata uyarıları.", "camasir"),
    ("bulasik", "Bulaşık Makinesi", "Temiz yıkamama, su almama, kurutmama ve pompa arızaları.", "bulasik"),
    ("firin", "Fırın ve Ocak", "Isınmama, rezistans, termostat, fan ve ocak gözü arızaları.", "firin"),
    ("kombi", "Kombi", "Sıcak su sorunu, basınç düşmesi, arıza kodları ve yıllık bakım.", "kombi"),
    ("klima", "Klima", "Soğutmama, su damlatma, koku, ses ve mevsimlik bakım.", "klima"),
]

# 3. bölüm — belirti → ne yapmalı (güvenli, genel öneriler)
BELIRTILER = [
    ("Buzdolabı soğutmuyor", "Kapağın tam kapandığından ve arkada hava boşluğu olduğundan emin olun. Düzelmezse fişi çekmeden önce bizi arayın; içerideki yiyecekleri korumak için kapağı az açın."),
    ("Çamaşır makinesi suyu boşaltmıyor", "Programı durdurun, kapağı zorlamayın. Pompa filtresi tıkanmış olabilir; emin değilseniz müdahale etmeden servis isteyin."),
    ("Bulaşık makinesi temiz yıkamıyor", "Alt filtreyi ve pervane deliklerini kontrol edin. Sorun sürüyorsa su alma veya ısıtma kaynaklı olabilir."),
    ("Kombi basıncı sürekli düşüyor", "Basıncı kılavuzdaki değere getirin. Sık tekrar ediyorsa tesisatta ya da kombide kaçak olabilir; teknik kontrol gerekir."),
    ("Klimadan su damlıyor", "Cihazı kapatın ve prizden çekin. Tahliye hattı tıkanmış veya filtre kirlenmiş olabilir."),
    ("Fırın ısınmıyor", "Sigortayı ve ayarı kontrol edin. Rezistans ya da termostat arızasında elektrikli parçalara dokunmayın."),
]

# 4. bölüm — süreç
ADIMLAR = [
    ("Arayın", "Cihazın türünü, modelini ve gördüğünüz arızayı kısaca anlatın."),
    ("Randevu", "Size uygun gün ve saat birlikte belirlenir."),
    ("Adreste tespit", "Teknisyen cihazı inceler, arızayı ve yapılacak işlemi açıklar."),
    ("Ücret ve onay", "Ücret işlemden önce söylenir. Onay vermezseniz işlem yapılmaz."),
    ("Onarım ve test", "Onarım sonrası cihaz sizin yanınızda çalıştırılarak teslim edilir."),
]

# 5. bölüm — çalışma ilkeleri (şeffaflık; politika uyumu)
ILKELER = [
    ("bagimsiz", "Bağımsız özel servis", "Hiçbir üretici markanın yetkili servisi, bayisi veya çağrı merkezi değiliz. Marka garantisi kapsamındaki cihazlar için önce üreticinin yetkili servisine başvurmanızı öneririz."),
    ("ucret", "Ücret önce söylenir", "Arıza tespitinden sonra ücreti açıkça bildiririz. Onayınız olmadan parça değişimi veya onarım yapılmaz."),
    ("parca", "Parça bilgisi açık", "Değişecek parçanın ne olduğunu ve neden değiştiğini anlatırız; çıkan parçayı isterseniz size bırakırız."),
    ("belge", "Yazılı kayıt", "Yapılan işlem ve ödenen ücret için isteğinize göre yazılı servis formu veya belge düzenlenir."),
]

# 6. bölüm — SSS
SSS = [
    ("Hangi cihazlara bakıyorsunuz?", "Buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın ve ocak gibi beyaz eşyalar ile kombi ve klimalara arıza, bakım ve onarım hizmeti veriyoruz."),
    ("Ücreti ne zaman öğrenirim?", "Arıza tespitinden sonra, işleme başlamadan önce. Ücret cihaza, arızaya ve gerekiyorsa değişecek parçaya göre belirlenir. Onay vermezseniz işlem yapılmaz."),
    ("Adrese geliyor musunuz?", "Evet, randevu ile adreste servis veriyoruz. Arayarak adresinizi ve arızayı iletebilirsiniz."),
    ("Kombi ve klima bakımı ne zaman yapılmalı?", "Kombi için ısıtma sezonu başlamadan, klima için yoğun kullanım dönemi öncesinde yılda bir bakım genel olarak önerilir."),
    ("Kişisel bilgilerim nasıl kullanılıyor?", "Paylaştığınız ad, telefon ve adres yalnızca servis talebiniz için kullanılır. Ayrıntılar Gizlilik ve KVKK sayfamızdadır."),
]
