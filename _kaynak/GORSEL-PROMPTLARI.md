# Görsel promptları — Servis Müşteri Hizmeti

Üretilen görselleri `_kaynak/gorsel/` klasörüne **aşağıdaki dosya adlarıyla** kaydedin (jpg, png veya webp).
Sonra `python -I _kaynak/build.py` çalıştırın: görseller webp'ye çevrilip sayfaya otomatik yerleşir.

## Her prompta eklenecek ortak kurallar (Google Ads politikası için önemli)
Bu satırı her promptun sonuna ekleyin:

> photorealistic, natural daylight, modern Turkish apartment interior, **no brand names, no logos, no text, no labels on appliances or clothing**, plain unbranded appliances, realistic hands, no watermark

- Cihazlarda ve tulumda **marka, logo ya da yazı olmamalı.** Marka logosu görünen görsel, Ads'te "yanıltıcı beyan / kabul edilemez iş uygulaması" redinin en sık sebebi.
- Teknisyen kıyafeti: **düz lacivert veya petrol mavisi iş tulumu, logosuz.**
- Görselleri sahte "ekibimiz" gibi sunmayacağız; alt metinler genel ("teknisyen ... inceliyor").

---

## 1. `hero` — ana görsel (yatay, 5:4 ya da 4:3, en az 1400 px genişlik)
A professional appliance repair technician in a plain navy blue work uniform kneeling in front of an open front-loading washing machine in a bright modern kitchen, checking the drum with a small flashlight, tool bag on the floor beside him, calm and trustworthy atmosphere, shallow depth of field, warm natural light from a window

## 2. `buzdolabi` — buzdolabı kartı (yatay 16:10, en az 800 px)
Technician in a plain navy work uniform inspecting the back panel of a white two-door refrigerator in a home kitchen, using a multimeter, refrigerator pulled slightly away from the wall, clean and tidy setting

## 3. `camasir` — çamaşır makinesi kartı (yatay 16:10)
Close-up of a technician's hands in work gloves removing the drain pump filter from the bottom front panel of a white front-loading washing machine, small towel on the floor, bathroom/laundry room setting

## 4. `bulasik` — bulaşık makinesi kartı (yatay 16:10)
Technician in a plain navy uniform crouching at an open built-in dishwasher, holding the removed bottom filter, lower basket pulled out, modern kitchen cabinets around

## 5. `firin` — fırın ve ocak kartı (yatay 16:10)
Technician with a screwdriver servicing a built-in electric oven with the door open, inspecting the heating element, stainless steel kitchen, soft daylight

## 6. `kombi` — kombi kartı (yatay 16:10)
Technician in a plain navy uniform checking the pressure gauge of a white wall-mounted gas combi boiler with the front cover removed, pipes visible below, utility room setting

## 7. `klima` — klima kartı (yatay 16:10)
Technician standing on a small step ladder cleaning the filter of a white wall-mounted split air conditioner indoor unit in a bright living room, front cover lifted open

## 8. `og-kapak` — paylaşım görseli (1200×630, yatay)
Clean flat-lay composition on a light teal background: a professional tool bag, multimeter, screwdrivers, a small wrench and a smartphone, generous empty space on the left side, top-down view, soft shadows

---

### Notlar
- Dosya adları önemli: `hero.jpg`, `buzdolabi.jpg`, `camasir.jpg`, `bulasik.jpg`, `firin.jpg`, `kombi.jpg`, `klima.jpg`, `og-kapak.jpg`.
- Görsel olmayan kartlarda sade çizgi ikon görünür; site görselsiz de düzgün çalışır.
- Yüzü net görünen kişi istemiyorsanız promptlara `face not visible, shot from behind or hands only` ekleyin.
