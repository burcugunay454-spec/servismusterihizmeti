# -*- coding: utf-8 -*-
"""Servis Müşteri Hizmeti — tek sayfa site üretici.
Çalıştır:  python -I _kaynak/build.py
Fotoğraflar: _kaynak/gorsel/ içine GORSEL-PROMPTLARI.md'deki adlarla (jpg/png/webp) koyun; build webp'ye çevirir.
Ayarlar ve metinler: _kaynak/icerik.py"""
import json, os, sys
from html import escape as e
from urllib.parse import quote

KAYNAK = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.dirname(KAYNAK)
sys.path.insert(0, KAYNAK)
import icerik as C  # noqa: E402
import firmalar as F  # noqa: E402

rakam = "".join(c for c in C.TEL if c.isdigit())
TEL_E164 = ("+90" + rakam[-10:]) if len(rakam) >= 10 else ""
TEL_GOSTER = C.TEL or "0 (5XX) XXX XX XX"
TEL_HREF = f"tel:{TEL_E164}" if TEL_E164 else "#iletisim"
wr = "".join(c for c in (C.WHATSAPP or C.TEL) if c.isdigit())
WA_NO = "" if C.WHATSAPP.strip().upper() == "YOK" else (("90" + wr[-10:]) if len(wr) >= 10 else "")
YAYINDA = bool(TEL_E164 and C.ALAN)
URL = C.ALAN.rstrip("/") + "/"


def wa(metin):
    return f"https://wa.me/{WA_NO}?text={quote(metin)}" if WA_NO else "#iletisim"


# ---------------- ikonlar ----------------
P = {
    "tel": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "buzdolabi": '<rect x="5" y="2" width="14" height="20" rx="2.5"/><path d="M5 9.5h14M8.5 5v2M8.5 12.5v3.5"/>',
    "camasir": '<rect x="3.5" y="2" width="17" height="20" rx="2.5"/><circle cx="12" cy="13.5" r="5"/><path d="M7 5.5h.01M10 5.5h.01M9.5 14.5c1.5 1 3.5 1 5 0"/>',
    "bulasik": '<rect x="4" y="2" width="16" height="20" rx="2.5"/><path d="M4 7h16M7.5 4.5h.01M8 11h8M8 14.5h8M8 18h8"/>',
    "firin": '<rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 8h18M6.5 5.5h.01M10 5.5h.01M7 11.5h10v6H7z"/>',
    "kombi": '<rect x="5" y="2" width="14" height="15" rx="2.5"/><path d="M9 21v-4M15 21v-4M12 5.5c-1.6 2-2.2 3.2-2.2 4.2a2.2 2.2 0 0 0 4.4 0c0-1-.6-2.2-2.2-4.2z"/>',
    "klima": '<rect x="2" y="4" width="20" height="8.5" rx="2.5"/><path d="M6 9.5h12M7 16c0 1.5-1 2-1 3.5M12 16v4M17 16c0 1.5 1 2 1 3.5"/>',
    "anahtar": '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18v3h3l6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/>',
    "onay": '<path d="M20 6 9 17l-5-5"/>',
    "bagimsiz": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "ucret": '<rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="2.5"/><path d="M6 12h.01M18 12h.01"/>',
    "parca": '<path d="M12 2 3 7v10l9 5 9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
    "belge": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    "saat": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "konum": '<path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
}
WA_YOL = '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.6.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/>'


def ik(ad):
    if ad == "wa":
        return f'<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{WA_YOL}</svg>'
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{P[ad]}</svg>'


# ---------------- görseller ----------------
def gorselleri_hazirla():
    """_kaynak/gorsel/<ad>.(jpg|png|webp) → img/<ad>-<genislik>.webp"""
    kaynak = os.path.join(KAYNAK, "gorsel")
    hazir = {}
    if not os.path.isdir(kaynak):
        return hazir
    try:
        from PIL import Image
    except ImportError:
        print("UYARI: Pillow yok, görseller atlandı")
        return hazir
    os.makedirs(os.path.join(KOK, "img"), exist_ok=True)
    for dosya in sorted(os.listdir(kaynak)):
        ad, uz = os.path.splitext(dosya)
        if uz.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        im = Image.open(os.path.join(kaynak, dosya)).convert("RGB")
        genislikler = [800, 1400] if ad in ("hero", "og-kapak") else [480, 800]
        boy = []
        for g in genislikler:
            g2 = min(g, im.width)
            h2 = round(im.height * g2 / im.width)
            hedef = os.path.join(KOK, "img", f"{ad}-{g}.webp")
            if not os.path.exists(hedef) or os.path.getmtime(hedef) < os.path.getmtime(os.path.join(kaynak, dosya)):
                im.resize((g2, h2), Image.LANCZOS).save(hedef, "WEBP", quality=80, method=6)
            boy.append((g, g2, h2))
        hazir[ad] = boy
    return hazir


GORSEL = {}


def resim(ad, alt, sizes, cls="", oncelik=False):
    if ad not in GORSEL:
        return ""
    boy = GORSEL[ad]
    srcset = ", ".join(f"img/{ad}-{g}.webp {g2}w" for g, g2, _ in boy)
    _, w0, h0 = boy[0]
    yuk = 'fetchpriority="high"' if oncelik else 'loading="lazy" decoding="async"'
    return (f'<img src="img/{ad}-{boy[0][0]}.webp" srcset="{srcset}" sizes="{sizes}" width="{w0}" height="{h0}" '
            f'alt="{e(alt)}" {yuk}{(" class=" + chr(34) + cls + chr(34)) if cls else ""}>')


HERO_CIZIM = '''<svg class="cizim" viewBox="0 0 500 440" aria-hidden="true"><defs><linearGradient id="hg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#14809a"/><stop offset="1" stop-color="#0a3b47"/></linearGradient></defs>
<rect width="500" height="440" fill="url(#hg)"/><g fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity=".92">
<rect x="58" y="70" width="110" height="250" rx="14"/><path d="M58 150h110M82 100v22M82 172v40"/>
<rect x="196" y="140" width="130" height="180" rx="14"/><circle cx="261" cy="238" r="50"/><circle cx="261" cy="238" r="34" opacity=".5"/><path d="M214 162h.1M232 162h.1M290 162h24"/>
<rect x="354" y="80" width="96" height="120" rx="12"/><path d="M384 236v-36M420 236v-36M402 110c-9 12-13 19-13 25a13 13 0 0 0 26 0c0-6-4-13-13-25z"/></g>
<g fill="#f4a21b"><circle cx="402" cy="290" r="34" opacity=".95"/></g><path d="M391 289l8 8 15-16" fill="none" stroke="#1c1400" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M40 346h420" stroke="#fff" stroke-opacity=".25" stroke-width="2"/></svg>'''


def bas(baslik, aciklama, yol, robots, ek=""):
    url = URL + yol
    gtm = ""
    if C.GTM:
        gtm = ("<script>(function(w,d,id){w.dataLayer=w.dataLayer||[];var y=0;function f(){if(y)return;y=1;"
               "w.dataLayer.push({'gtm.start':Date.now(),event:'gtm.js'});var j=d.createElement('script');j.async=1;"
               "j.src='https://www.googletagmanager.com/gtm.js?id='+id;d.head.appendChild(j)}w.__gtmY=f;"
               "if(/[?&](gclid|gbraid|wbraid)=/.test(location.search)){f();return}"
               "['pointerdown','keydown','touchstart','scroll'].forEach(function(e){w.addEventListener(e,f,{once:true,passive:true})});"
               "w.addEventListener('load',function(){setTimeout(f,3500)})})(window,document,'" + C.GTM + "');</script>")
    gtag = ""
    if getattr(C, "GA4", "") or getattr(C, "AW", ""):
        ilk = C.GA4 or C.AW
        ayar = "".join(f"gtag('config','{k}');" for k in (C.GA4, C.AW) if k)
        # gtag: reklam tıklamasında (gclid) hemen, diğer ziyarette ilk etkileşimde veya yüklemeden 3,5 sn sonra yüklenir
        gtag = ("<script>(function(w,d){w.dataLayer=w.dataLayer||[];w.gtag=function(){dataLayer.push(arguments)};"
                "gtag('js',new Date());" + ayar + f"w.__awTel='{C.AW_TEL}';" +
                "var y=0;function f(){if(y)return;y=1;var j=d.createElement('script');j.async=1;"
                f"j.src='https://www.googletagmanager.com/gtag/js?id={ilk}';d.head.appendChild(j)}}w.__gtY=f;"
                "if(/[?&](gclid|gbraid|wbraid)=/.test(location.search)){f();return}"
                "['pointerdown','keydown','touchstart','scroll'].forEach(function(e){w.addEventListener(e,f,{once:true,passive:true})});"
                "w.addEventListener('load',function(){setTimeout(f,3500)})})(window,document);</script>")
    og_resim = f'<meta property="og:image" content="{URL}img/og-kapak-1400.webp">' if "og-kapak" in GORSEL else ""
    return f'''<!doctype html>
<html lang="tr"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
{gtm}{gtag}
<title>{e(baslik)}</title>
<meta name="description" content="{e(aciklama)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#0f5f73">
<meta property="og:type" content="website"><meta property="og:locale" content="tr_TR"><meta property="og:site_name" content="{e(C.FIRMA)}">
<meta property="og:title" content="{e(baslik)}"><meta property="og:description" content="{e(aciklama)}"><meta property="og:url" content="{url}">{og_resim}
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&family=Sora:wght@600;700&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700&family=Sora:wght@600;700&display=swap"></noscript>
<style>{open(os.path.join(KAYNAK, "stil.css"), encoding="utf-8").read()}</style>
{ek}
</head><body>'''


def ust(ana=True):
    on = "" if ana else "./"
    return f'''<header class="ust"><div class="kap">
<a class="logo" href="{'#ust' if ana else './'}" aria-label="{e(C.FIRMA)} ana sayfa"><span class="logo-isaret">{ik("anahtar")}</span><span>{e(C.FIRMA)}<small>Beyaz eşya · Kombi · Klima</small></span></a>
<button class="menu-ac" type="button" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu">{ik("menu")}</button>
<nav class="menu" id="menu" aria-label="Ana menü">
<a href="{on}#cihazlar">Hizmetler</a><a href="{on}#belirtiler">Arıza Rehberi</a><a href="{on}#surec">Süreç</a><a href="{on}#ilkeler">İlkelerimiz</a><a href="{on}#sss">SSS</a><a href="{on}#iletisim">İletişim</a><a href="firma-rehberi.html">Firma Rehberi</a>
<a class="btn btn-ara btn-kucuk" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="menu">{ik("tel")}<span>{e(TEL_GOSTER)}</span></a>
</nav></div></header>'''


TUZAK = '''<!-- BOT-TUZAK (gerçek ziyaretçi görmez; dokunan cihaz işaretlenir, dönüşüm göndermez) -->
<div aria-hidden="true" style="position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden">
<a href="tel:+900000000000" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">Hemen Ara</a>
<a href="https://wa.me/900000000000" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">WhatsApp Servis</a>
<a href="tuzak/" data-cf-trap="1" tabindex="-1" rel="nofollow" onclick="return __cfTrap(event)">Servis kaydı</a>
</div>'''


def alt():
    satirlar = [("tel", f'<a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="alt">{e(TEL_GOSTER)}</a>')]
    if WA_NO:
        satirlar.append(("wa", f'<a href="{wa("Merhaba, servis talebim var.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="alt">WhatsApp</a>'))
    if C.EPOSTA:
        satirlar.append(("belge", f'<a href="mailto:{e(C.EPOSTA)}">{e(C.EPOSTA)}</a>'))
    if C.ADRES:
        satirlar.append(("konum", e(C.ADRES)))
    li = "".join(f"<li>{s}</li>" for _, s in satirlar)
    unvan = f" ({e(C.UNVAN)})" if C.UNVAN else ""
    return f'''<footer><div class="kap">
<div><div class="logo"><span class="logo-isaret">{ik("anahtar")}</span><span>{e(C.FIRMA)}<small>Beyaz eşya · Kombi · Klima</small></span></div>
<p>Beyaz eşya, kombi ve klima için adreste arıza tespiti, onarım ve bakım.</p></div>
<div><h3>İletişim</h3><ul>{li}<li>{e(C.SAAT)}</li></ul></div>
<div><h3>Sayfalar</h3><ul><li><a href="./#cihazlar">Hizmetler</a></li><li><a href="./#sss">Sık sorulanlar</a></li><li><a href="firma-rehberi.html">Firma rehberi</a></li><li><a href="gizlilik.html">Gizlilik ve KVKK</a></li></ul></div>
<p class="yasal">{e(C.FIRMA)}{unvan} bağımsız bir özel teknik servistir; hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir.
Marka garantisi kapsamındaki cihazlarınız için üreticinin yetkili servisine başvurabilirsiniz. © <span id="yil">2026</span> {e(C.FIRMA)}</p>
</div>
<div class="serit" role="note"><b>Bağımsız özel servis</b> Hiçbir markanın yetkili servisi değildir.</div></footer>'''


def yapiskan():
    w = (f'<a class="btn btn-wa" href="{wa("Merhaba, servis talebim var.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="mobil">{ik("wa")}<span>WhatsApp</span></a>'
         if WA_NO else "")
    return f'<div class="yapiskan"><a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="mobil">{ik("tel")}<span>Hemen Ara</span></a>{w}</div>'


def js():
    return "<script>" + open(os.path.join(KAYNAK, "site.js"), encoding="utf-8").read() + "</script>"


def ana_sayfa():
    sema = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": C.FIRMA, "url": URL, "inLanguage": "tr-TR"},
        {"@context": "https://schema.org", "@type": "FAQPage",
         "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in C.SSS]},
        {"@context": "https://schema.org", "@type": "Service", "serviceType": "Beyaz eşya, kombi ve klima teknik servisi",
         "provider": {"@type": "Organization", "name": C.FIRMA, "url": URL},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Servis hizmetleri",
                             "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"{b} servisi"}} for _, b, _, _ in C.CIHAZLAR]}},
    ]
    if YAYINDA:
        isletme = {"@context": "https://schema.org", "@type": "HomeAndConstructionBusiness", "name": C.FIRMA, "url": URL,
                   "telephone": TEL_E164, "description": C.DESC}
        if C.UNVAN:
            isletme["legalName"] = C.UNVAN
        if C.ADRES:
            isletme["address"] = {"@type": "PostalAddress", "streetAddress": C.ADRES, "addressCountry": "TR"}
        if "hero" in GORSEL:
            isletme["image"] = URL + "img/hero-1400.webp"
        sema.insert(0, isletme)
    ek = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sema)
    if "hero" in GORSEL:
        ek += '<link rel="preload" as="image" href="img/hero-800.webp" imagesrcset="img/hero-800.webp 800w, img/hero-1400.webp 1400w" imagesizes="100vw" fetchpriority="high">'
    robots = "index,follow,max-image-preview:large" if YAYINDA else "noindex,nofollow"

    ara = f'<a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="hero">{ik("tel")}<span>Hemen Ara</span></a>'
    yaz = (f'<a class="btn btn-wa" href="{wa("Merhaba, cihazım için servis talebim var.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="hero">{ik("wa")}<span>WhatsApp ile Yaz</span></a>'
           if WA_NO else "")
    hero_gorsel = resim("hero", "Teknisyen mutfakta çamaşır makinesini tamir ediyor, arkada anne ve kızı", "100vw", oncelik=True) or HERO_CIZIM

    cihaz = "".join(
        f'<article class="cihaz"><div class="cihaz-foto">{resim(g, b + " onarımı yapan teknisyen", "(max-width:640px) 92vw, (max-width:1020px) 46vw, 370px") or ik(k)}</div>'
        f'<div class="cihaz-ic"><h3>{e(b)} Servisi</h3><p>{e(m)}</p>'
        + (f'<a href="{wa("Merhaba, " + b.lower() + " için servis talebim var.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="cihaz">Servis talebi gönder →</a>' if WA_NO else f'<a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="cihaz">Servis için arayın →</a>')
        + '</div></article>' for k, b, m, g in C.CIHAZLAR)
    belirti = "".join(f'<div class="belirti"><span class="no">{i}</span><h3>{e(b)}</h3><p>{e(m)}</p></div>' for i, (b, m) in enumerate(C.BELIRTILER, 1))
    surec = "".join(f'<li><h3>{e(b)}</h3><p>{e(m)}</p></li>' for b, m in C.ADIMLAR)
    ilke = "".join(f'<div class="ilke">{ik(k)}<h3>{e(b)}</h3><p>{e(m)}</p></div>' for k, b, m in C.ILKELER)
    sss = "".join(f'<details><summary>{e(s)}</summary><p>{e(c)}</p></details>' for s, c in C.SSS)
    secenek = "".join(f"<option>{e(b)}</option>" for _, b, _, _ in C.CIHAZLAR)
    firma_satir = [("Firma", e(C.FIRMA))]
    if C.UNVAN:
        firma_satir.append(("Ünvan", e(C.UNVAN)))
    firma_satir += [("Telefon", f'<a href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="firma">{e(TEL_GOSTER)}</a>'), ("Çalışma", e(C.SAAT))]
    if C.ADRES:
        firma_satir.append(("Adres", e(C.ADRES)))
    firma_satir.append(("Statü", "Bağımsız özel servis — yetkili servis değildir"))
    firma = "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in firma_satir)
    wa_kanal = (f'<a class="kanal wa" href="{wa("Merhaba, servis talebim var.")}" target="_blank" rel="noopener" data-olay="whatsapp_tiklama" data-konum="iletisim"><span class="kk">{ik("wa")}</span><span><small>WhatsApp</small><b>Mesaj gönderin</b></span></a>'
                if WA_NO else "")
    tel_kanal = (f'<a class="kanal" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="iletisim"><span class="kk">{ik("tel")}</span><span><small>Telefon</small><b>{e(TEL_GOSTER)}</b></span></a>' if WA_NO else "")
    if WA_NO:
        ilt_metin = "Arayın ya da formu doldurun; mesajınız WhatsApp'ta hazır açılır, siz yalnızca gönderirsiniz."
        form_blok = f'''<form class="form" id="servis-formu" data-wa="{WA_NO}" novalidate>
<h3>WhatsApp ile servis talebi</h3><p>Bilgiler yalnızca servis talebiniz için kullanılır.</p>
<label for="f-ad">Adınız</label><input id="f-ad" name="ad" autocomplete="name" required>
<label for="f-cihaz">Cihaz</label><select id="f-cihaz" name="cihaz" required><option value="">Seçin</option>{secenek}<option>Diğer</option></select>
<label for="f-ariza">Arıza (kısaca)</label><textarea id="f-ariza" name="ariza" placeholder="Örn. su boşaltmıyor, ekranda hata kodu var"></textarea>
<label for="f-semt">Semt / mahalle</label><input id="f-semt" name="semt" autocomplete="address-level3">
<div class="bal" aria-hidden="true"><label for="f-web">Web siteniz</label><input id="f-web" name="web_sitesi" tabindex="-1" autocomplete="off"></div>
<button class="btn btn-wa" type="submit">{ik("wa")}<span>WhatsApp ile Gönder</span></button>
<p class="kvkk">Göndererek <a href="gizlilik.html">Gizlilik ve KVKK aydınlatma metnini</a> okuduğunuzu kabul edersiniz.</p>
</form>'''
    else:
        ilt_metin = "Servis talebiniz için bizi arayın; cihazınızı, arızayı ve adresinizi kısaca anlatın, randevu birlikte planlansın."
        form_blok = f'''<div class="ara-kutu"><span class="ak-ikon">{ik("tel")}</span><h3>Servis hattı</h3><p>Hafta içi ve hafta sonu, randevu ile.</p>
<a class="ak-no" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="iletisim-kutu">{e(TEL_GOSTER)}</a>
<a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="iletisim-dugme">{ik("tel")}<span>Hemen Ara</span></a></div>'''

    return bas(C.TITLE, C.DESC, "", robots, ek) + ust() + f'''
<main id="ust">
<!-- 1 · GİRİŞ -->
<section class="hero" aria-labelledby="h1">
<div class="hero-gorsel">{hero_gorsel}</div>
<div class="kap">
<div class="hero-ic">
<span class="ust-etiket"><i></i>Adreste arıza tespiti ve onarım</span>
<h1 id="h1">Beyaz eşya, kombi ve <em>klima servisi</em></h1>
<p class="giris">Buzdolabı, çamaşır makinesi, bulaşık makinesi, fırın, kombi ve klima arızalarında teknisyenimiz adresinize gelir, arızayı tespit eder ve ücreti işlemden önce söyler.</p>
<a class="hero-tel" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="hero-numara"><small>Servis hattı</small>{e(TEL_GOSTER)}</a>
<div class="dugmeler">{ara}{yaz}</div>
</div>
</div></section>
<div class="kurumsal"><div class="kap">
<div class="k-oge">{ik("anahtar")}<span><b>Adreste arıza tespiti</b>Teknisyen evinize gelir</span></div>
<div class="k-oge">{ik("belge")}<span><b>Ücretlendirme</b>Onayınız olmadan işlem yok</span></div>
<div class="k-oge">{ik("onay")}<span><b>Onarım sonrası test</b>Cihaz çalışırken teslim</span></div>
<div class="k-oge">{ik("bagimsiz")}<span><b>Hafta sonu da randevu</b>Size uygun saatte</span></div>
</div></div>

<!-- 2 · HİZMETLER -->
<section class="bolum beyaz" id="cihazlar" aria-labelledby="h-cihaz"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Hizmetlerimiz</span><h2 id="h-cihaz">Hangi cihaza servis veriyoruz?</h2>
<p>Evinizdeki beyaz eşya, kombi ve klimanın arıza, bakım ve onarımı için tek numara.</p></div>
<div class="izgara cihazlar">{cihaz}</div>
</div></section>

<!-- 3 · ARIZA REHBERİ -->
<section class="bolum" id="belirtiler" aria-labelledby="h-bel"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Arıza rehberi</span><h2 id="h-bel">Servis çağırmadan önce kontrol edin</h2>
<p>Sık görülen belirtiler ve güvenle yapabileceğiniz ilk kontroller.</p></div>
<div class="izgara belirtiler">{belirti}</div>
<p class="uyari-kutu"><b>Güvenlik:</b> Gaz kokusu alırsanız cihazı ve elektrik düğmelerini kullanmayın, ortamı havalandırın ve doğal gaz acil hattı 187'yi arayın. Elektrikli parçalara cihaz prize takılıyken dokunmayın.</p>
</div></section>

<!-- 4 · SÜREÇ -->
<section class="bolum beyaz" id="surec" aria-labelledby="h-sur"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Nasıl çalışırız?</span><h2 id="h-sur">Beş adımda şeffaf servis</h2>
<p>Arızayı ve ücreti öğrenmeden hiçbir işlem yapılmaz.</p></div>
<ol class="surec">{surec}</ol>
<div class="surec-alt"><p>Randevu için arayın; cihazınızı ve arızayı kısaca anlatın.</p><div class="dugmeler">{ara.replace('data-konum="hero"', 'data-konum="surec"')}</div></div>
</div></section>

<!-- 5 · İLKELER -->
<section class="bolum koyu" id="ilkeler" aria-labelledby="h-ilk"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Çalışma ilkelerimiz</span><h2 id="h-ilk">Kim olduğumuzu açıkça söylüyoruz</h2>
<p>Bağımsız bir özel servisiz. Hiçbir markayı temsil etmiyoruz, ücreti ve işlemi önceden söylüyoruz.</p></div>
<div class="izgara ilkeler">{ilke}</div>
</div></section>

<!-- 6 · SSS -->
<section class="bolum" id="sss" aria-labelledby="h-sss"><div class="kap dar">
<div class="bas"><span class="ust-etiket"><i></i>Sık sorulan sorular</span><h2 id="h-sss">Merak edilenler</h2></div>
<div class="sss">{sss}</div>
</div></section>

<!-- 7 · İLETİŞİM -->
<section class="bolum beyaz" id="iletisim" aria-labelledby="h-ilt"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>İletişim</span><h2 id="h-ilt">Servis talebi oluşturun</h2>
<p>{ilt_metin}</p></div>
<div class="iletisim">
<div>
{tel_kanal}{wa_kanal}
<div class="firma"><dl>{firma}</dl></div>
</div>
{form_blok}
</div>
</div></section>
</main>
''' + alt() + TUZAK + yapiskan() + js() + "\n</body></html>\n"


def gizlilik():
    kim = e(C.FIRMA) + (f" ({e(C.UNVAN)})" if C.UNVAN else "")
    return bas(f"Gizlilik ve KVKK Aydınlatma Metni | {C.FIRMA}", "Kişisel verilerin işlenmesi, çerezler ve haklarınız hakkında bilgilendirme.",
               "gizlilik.html", "index,follow" if YAYINDA else "noindex,nofollow") + ust(False) + f'''
<main class="kap dar"><article class="metin">
<h1>Gizlilik ve KVKK Aydınlatma Metni</h1>
<p>Bu metin, 6698 sayılı Kişisel Verilerin Korunması Kanunu kapsamında veri sorumlusu sıfatıyla {kim} tarafından hazırlanmıştır.</p>
<h2>Hangi verileri işliyoruz?</h2>
<p>Telefonla{' veya WhatsApp ile' if WA_NO else ''} bize ilettiğiniz ad, telefon numarası, adres/semt ve cihaz-arıza bilgileri.</p>
<h2>Hangi amaçla?</h2>
<p>Servis talebinizi almak, randevu oluşturmak, adreste hizmet vermek ve yapılan işleme ilişkin kayıt tutmak. Verileriniz pazarlama amacıyla üçüncü kişilere satılmaz veya kiralanmaz.</p>
<h2>Firma rehberi başvuruları</h2>
<p>Firma rehberi başvuru formunda ilettiğiniz firma adı, yetkili adı, telefon, e-posta, adres ve hizmet bilgileri başvurunun değerlendirilmesi ve onaylanırsa firmanın rehberde yayınlanması amacıyla işlenir. Form, e-posta iletim hizmeti FormSubmit (formsubmit.co) aracılığıyla bize e-posta olarak ulaşır. Rehberde yalnızca firma adı, il/ilçe, hizmetler, firma telefonu ve isterseniz adres, web sitesi ve tanıtım metni yayınlanır; yetkili adı ve e-posta yayınlanmaz.</p>
<h2>Hukuki sebep</h2>
<p>Bir sözleşmenin kurulması veya ifasıyla doğrudan ilgili olması ve kanunlarda öngörülen kayıt yükümlülükleri (KVKK md. 5/2-a, c, ç).</p>
<h2>Aktarım</h2>
<p>{'Form gönderdiğinizde mesajınız sizin cihazınızda WhatsApp uygulamasında açılır; gönderim WhatsApp hizmet şartlarına tabidir. ' if WA_NO else ''}Sitede ziyaret ve reklam ölçümü için Google araçları (Google Tag Manager, Google Analytics, Google Ads) ve sahte tıklama önleme amacıyla güvenlik araçları kullanılabilir; bu araçlar çerez ve benzeri teknolojilerle cihaz bilgisi toplayabilir.</p>
<h2>Haklarınız</h2>
<p>KVKK md. 11 uyarınca verilerinizin işlenip işlenmediğini öğrenme, düzeltilmesini veya silinmesini isteme ve itiraz etme haklarına sahipsiniz. Başvurularınızı {e(TEL_GOSTER)} numarasından{(" veya " + e(C.EPOSTA) + " adresinden") if C.EPOSTA else ""} iletebilirsiniz.</p>
<h2>Bağımsız servis bilgilendirmesi</h2>
<p>{e(C.FIRMA)} bağımsız bir özel teknik servistir; hiçbir üretici markanın yetkili servisi, bayisi veya müşteri hizmetleri hattı değildir.</p>
<p><a class="btn btn-cizgi btn-kucuk" href="./">← Ana sayfaya dön</a></p>
</article></main>''' + alt() + yapiskan() + js() + "\n</body></html>\n"


REHBER_SSS = [
    ("Rehbere kayıt ücretli mi?", "Hayır. Teknik servis firmaları başvuru formunu doldurarak ücretsiz başvurabilir."),
    ("Başvurum ne zaman yayına girer?", "Başvurular tek tek incelenir; firma bilgileri ve telefon numarası doğrulandıktan sonra rehbere eklenir."),
    ("Rehberdeki firmalar yetkili servis mi?", "Rehber, bağımsız teknik servis firmalarının iletişim bilgilerini bir araya getirir. Bir firmanın bir markanın yetkili servisi olup olmadığını üreticinin resmi sitesinden kontrol edebilirsiniz."),
    ("Bilgilerimi nasıl güncellerim veya kaldırırım?", "Formu 'güncelleme' notuyla yeniden gönderin ya da bizi arayın; bilgileriniz düzeltilir veya rehberden kaldırılır."),
    ("Rehberdeki bir firmadan şikâyetim var.", "Hizmet doğrudan ilgili firma tarafından verilir. Yaşadığınız sorunu bize iletebilirsiniz; gerekli görülürse firma rehberden çıkarılır. Tüketici hakları için Tüketici Hakem Heyeti'ne de başvurabilirsiniz."),
]

SECIM = [
    ("belge", "Ücreti önceden sorun", "Servis ücreti, parça ve işçilik bedelini işlem başlamadan öğrenin; onay vermeden işlem yaptırmayın."),
    ("bagimsiz", "Yetkili servis iddiasını kontrol edin", "Marka adını kullanan bir firmanın yetkili olup olmadığını üreticinin resmi sitesinden doğrulayın."),
    ("parca", "Değişen parçayı isteyin", "Değiştirilen eski parçayı görmek ve yeni parçanın garantisini sormak hakkınızdır."),
    ("onay", "Fatura ve garanti alın", "Yapılan iş için fatura veya servis fişi isteyin; onarım garantisinin süresini yazılı alın."),
    ("konum", "Yakındaki firmayı tercih edin", "Size yakın firma daha hızlı gelir; ilçenizi seçerek rehberde arayın."),
    ("saat", "Randevuyu netleştirin", "Teknisyenin geliş saatini ve size kimin geleceğini önceden öğrenin."),
]


def firma_rehberi():
    kayit = [dict(f, kategoriler=list(f.get("kategoriler", []))) for f in F.FIRMALAR]
    il_sec = "".join(f"<option>{e(i)}</option>" for i in F.ILLER)
    kat_sec = "".join(f"<option>{e(k)}</option>" for k in F.KATEGORILER)
    kat_kutu = "".join(f'<label class="rh-kutu"><input type="checkbox" name="kategoriler" value="{e(k)}"><span>{e(k)}</span></label>' for k in F.KATEGORILER)
    secim = "".join(f'<div class="ilke">{ik(k)}<h3>{e(b)}</h3><p>{e(m)}</p></div>' for k, b, m in SECIM)
    sss = "".join(f'<details><summary>{e(s)}</summary><p>{e(c)}</p></details>' for s, c in REHBER_SSS)
    baslik = f"Teknik Servis Firma Rehberi | {C.FIRMA}"
    aciklama = ("Beyaz eşya, kombi ve klima teknik servis firmaları rehberi: il, ilçe ve hizmete göre firma arayın. "
                "Teknik servis firmanızı rehbere ücretsiz ekleyin.")
    sema = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Teknik Servis Firma Rehberi", "url": URL + "firma-rehberi.html",
             "inLanguage": "tr-TR", "isPartOf": {"@type": "WebSite", "name": C.FIRMA, "url": URL}},
            {"@context": "https://schema.org", "@type": "FAQPage",
             "mainEntity": [{"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in REHBER_SSS]}]
    if kayit:
        sema.append({"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i, "item": {"@type": "LocalBusiness", "name": f["ad"], "telephone": f.get("tel", ""),
                                                          "address": {"@type": "PostalAddress", "addressLocality": f.get("ilce", ""), "addressRegion": f.get("il", ""), "addressCountry": "TR"}}}
            for i, f in enumerate(kayit, 1)]})
    ek = "".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in sema)
    robots = "index,follow" if YAYINDA else "noindex,nofollow"
    form_url = f"https://formsubmit.co/{F.FORM_EPOSTA}"
    sonraki = URL + "firma-rehberi.html?gonderildi=1#basvuru"
    veri = json.dumps(kayit, ensure_ascii=False).replace("</", "<\\/")
    return bas(baslik, aciklama, "firma-rehberi.html", robots, ek) + ust(False) + f'''
<main id="ust">
<section class="bolum koyu rh-giris" aria-labelledby="rh-h1"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Firma rehberi</span>
<h1 id="rh-h1">Teknik servis firma rehberi</h1>
<p>Beyaz eşya, kombi ve klima servis firmalarını il, ilçe ve hizmete göre bulun. Firmanız rehberde yoksa ücretsiz ekleyin.</p></div>
<form class="rh-ara" id="rh-ara" role="search" onsubmit="return false">
<label><span>İl</span><select id="rh-il"><option value="">Tüm iller</option>{il_sec}</select></label>
<label><span>Hizmet</span><select id="rh-kat"><option value="">Tüm hizmetler</option>{kat_sec}</select></label>
<label class="rh-genis"><span>Firma adı veya ilçe</span><input id="rh-q" type="search" placeholder="Örn. Bornova, kombi servisi" autocomplete="off"></label>
<a class="btn btn-ara" href="#basvuru">{ik("belge")}<span>Firmanızı ekleyin</span></a>
</form>
</div></section>

<section class="bolum" id="liste" aria-labelledby="rh-h-liste"><div class="kap">
<div class="rh-ust"><h2 id="rh-h-liste">Kayıtlı firmalar</h2><p id="rh-sayi" aria-live="polite"></p></div>
<div class="rh-liste" id="rh-liste"></div>
<div class="rh-bos" id="rh-bos" hidden><span class="ak-ikon">{ik("konum")}</span><h3>Bu aramada kayıtlı firma yok</h3>
<p>Rehber yeni; firmalar başvuru ve doğrulamadan sonra eklenir. Bölgenizde teknik servis firması işletiyorsanız ilk siz ekleyin.</p>
<a class="btn btn-ara" href="#basvuru">{ik("belge")}<span>Firmanızı ücretsiz ekleyin</span></a></div>
</div></section>

<section class="bolum beyaz" id="secim" aria-labelledby="rh-h-secim"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Servis seçme rehberi</span><h2 id="rh-h-secim">Teknik servis seçerken dikkat edin</h2>
<p>Rehberden ya da başka bir yerden servis çağırırken bu altı noktayı kontrol edin.</p></div>
<div class="izgara ilkeler rh-secim">{secim}</div>
</div></section>

<section class="bolum" id="basvuru" aria-labelledby="rh-h-form"><div class="kap">
<div class="bas"><span class="ust-etiket"><i></i>Ücretsiz kayıt</span><h2 id="rh-h-form">Firmanızı rehbere ekleyin</h2>
<p>Formu doldurun; bilgileriniz kontrol edildikten sonra firmanız rehberde yayınlanır. Yalnızca gerçek, faaliyette olan teknik servis firmaları kabul edilir.</p></div>
<div class="rh-form-alan">
<div class="rh-kriter"><h3>Rehbere giriş koşulları</h3><ul>
<li>{ik("onay")}Faaliyette olan, ulaşılabilir bir teknik servis firması olmak</li>
<li>{ik("onay")}Telefon numarasının firmaya ait olması (arayarak doğrulanır)</li>
<li>{ik("onay")}Bir markanın yetkili servisi değilseniz bunu ima etmemek</li>
<li>{ik("onay")}Ücret ve garanti konusunda müşteriyi önceden bilgilendirmek</li>
</ul><p class="rh-not">Başvuru ücretsizdir. Bilgileriniz yalnızca rehber kaydı için kullanılır.</p></div>
<form class="form rh-form" id="rh-form" action="{form_url}" method="POST">
<div class="rh-tamam" id="rh-tamam" hidden>{ik("onay")}<b>Başvurunuz alındı.</b> Bilgileriniz kontrol edildikten sonra sizinle iletişime geçeceğiz.</div>
<input type="hidden" name="_subject" value="Yeni firma rehberi başvurusu - {e(C.FIRMA)}">
<input type="hidden" name="_next" value="{sonraki}">
<input type="hidden" name="_template" value="table">
<div class="bal" aria-hidden="true"><label for="rh-honey">Boş bırakın</label><input id="rh-honey" type="text" name="_honey" tabindex="-1" autocomplete="off"></div>
<div class="rh-iki">
<div><label for="rh-f-ad">Firma adı *</label><input id="rh-f-ad" name="Firma adı" required maxlength="80" autocomplete="organization"></div>
<div><label for="rh-f-yetkili">Yetkili adı soyadı *</label><input id="rh-f-yetkili" name="Yetkili" required maxlength="60" autocomplete="name"></div>
<div><label for="rh-f-tel">Telefon *</label><input id="rh-f-tel" name="Telefon" type="tel" required maxlength="20" autocomplete="tel" placeholder="0 (5XX) XXX XX XX"></div>
<div><label for="rh-f-eposta">E-posta</label><input id="rh-f-eposta" name="E-posta" type="email" maxlength="80" autocomplete="email"></div>
<div><label for="rh-f-il">İl *</label><select id="rh-f-il" name="İl" required><option value="">Seçin</option>{il_sec}</select></div>
<div><label for="rh-f-ilce">İlçe *</label><input id="rh-f-ilce" name="İlçe" required maxlength="40"></div>
</div>
<fieldset class="rh-kat"><legend>Verdiğiniz hizmetler *</legend>{kat_kutu}</fieldset>
<label for="rh-f-adres">Açık adres</label><input id="rh-f-adres" name="Adres" maxlength="160" autocomplete="street-address">
<label for="rh-f-web">Web sitesi</label><input id="rh-f-web" name="Web sitesi" type="url" maxlength="100" placeholder="https://">
<label for="rh-f-unvan">Ticari unvan / vergi no</label><input id="rh-f-unvan" name="Ticari unvan - vergi no" maxlength="120">
<label for="rh-f-acik">Firmanızı kısaca tanıtın</label><textarea id="rh-f-acik" name="Tanıtım" maxlength="200" placeholder="En fazla 200 karakter"></textarea>
<label class="rh-onay"><input type="checkbox" name="KVKK onayı" value="Evet" required><span><a href="gizlilik.html">Gizlilik ve KVKK aydınlatma metnini</a> okudum; firma bilgilerimin rehberde yayınlanmasını kabul ediyorum. *</span></label>
<p class="rh-hata" id="rh-hata" hidden>Lütfen en az bir hizmet seçin.</p>
<button class="btn btn-ara" type="submit">{ik("belge")}<span>Başvuruyu gönder</span></button>
</form>
</div>
</div></section>

<section class="bolum beyaz" id="sss" aria-labelledby="rh-h-sss"><div class="kap dar">
<div class="bas"><span class="ust-etiket"><i></i>Sık sorulan sorular</span><h2 id="rh-h-sss">Firma rehberi hakkında</h2></div>
<div class="sss">{sss}</div>
</div></section>
</main>
''' + alt() + yapiskan() + js() + f'''<script>(function(){{
var F={veri},L=document.getElementById('rh-liste'),B=document.getElementById('rh-bos'),S=document.getElementById('rh-sayi'),
il=document.getElementById('rh-il'),kat=document.getElementById('rh-kat'),q=document.getElementById('rh-q');
function n(t){{return(t||'').toLocaleLowerCase('tr')}}
function esc(t){{return String(t||'').replace(/[&<>"]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
function ciz(){{var a=F.filter(function(f){{return(!il.value||f.il===il.value)&&(!kat.value||(f.kategoriler||[]).indexOf(kat.value)>-1)&&
(!q.value||n([f.ad,f.il,f.ilce,(f.kategoriler||[]).join(' '),f.aciklama].join(' ')).indexOf(n(q.value))>-1)}});
L.innerHTML=a.map(function(f){{var t=(f.tel||'').replace(/\\D/g,'');t=t.length>=10?'+90'+t.slice(-10):'';
return'<article class="rh-firma"><h3>'+esc(f.ad)+'</h3><p class="rh-yer">'+esc(f.ilce)+(f.ilce?', ':'')+esc(f.il)+'</p>'+
'<p class="rh-etiketler">'+(f.kategoriler||[]).map(function(k){{return'<span>'+esc(k)+'</span>'}}).join('')+'</p>'+
(f.aciklama?'<p>'+esc(f.aciklama)+'</p>':'')+(f.adres?'<p class="rh-adres">'+esc(f.adres)+'</p>':'')+
'<div class="rh-dugme">'+(t?'<a class="btn btn-cizgi btn-kucuk" href="tel:'+t+'" rel="nofollow">'+esc(f.tel)+'</a>':'')+
(f.web?'<a class="btn btn-cizgi btn-kucuk" href="'+esc(f.web)+'" target="_blank" rel="nofollow noopener">Web sitesi</a>':'')+'</div></article>'}}).join('');
B.hidden=a.length>0;S.textContent=F.length?(a.length+' firma'):'';}}
[il,kat].forEach(function(x){{x.addEventListener('change',ciz)}});q.addEventListener('input',ciz);ciz();
var fm=document.getElementById('rh-form');fm.addEventListener('submit',function(ev){{
var k=fm.querySelectorAll('input[name=kategoriler]:checked').length,h=document.getElementById('rh-hata');
if(!k){{ev.preventDefault();h.hidden=false;h.scrollIntoView({{block:'center'}});return}}h.hidden=true;
var s=[].map.call(fm.querySelectorAll('input[name=kategoriler]:checked'),function(c){{return c.value}}).join(', ');
var g=fm.querySelector('input[name=Hizmetler]');if(!g){{g=document.createElement('input');g.type='hidden';g.name='Hizmetler';fm.appendChild(g)}}g.value=s;
[].forEach.call(fm.querySelectorAll('input[name=kategoriler]'),function(c){{c.disabled=true}});
window.dataLayer=window.dataLayer||[];dataLayer.push({{event:'rehber_basvuru'}});}});
if(/[?&]gonderildi=1/.test(location.search)){{document.getElementById('rh-tamam').hidden=false}}
}})();</script>
</body></html>
'''


def bulunamadi():
    return bas(f"Sayfa bulunamadı | {C.FIRMA}", "Aradığınız sayfa bulunamadı.", "404.html", "noindex") + ust(False) + f'''
<main class="kap dar"><article class="metin" style="text-align:center">
<h1>Sayfa bulunamadı</h1><p>Aradığınız sayfa taşınmış veya kaldırılmış olabilir.</p>
<div class="dugmeler" style="justify-content:center"><a class="btn btn-ara" href="{TEL_HREF}" data-olay="arama_tiklama" data-konum="404">{ik("tel")}<span>Hemen Ara</span></a><a class="btn btn-cizgi" href="./">Ana sayfa</a></div>
</article></main>''' + alt() + yapiskan() + js() + "\n</body></html>\n"


def yaz(ad, metin):
    yol = os.path.join(KOK, ad)
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    with open(yol, "w", encoding="utf-8", newline="\n") as f:
        f.write(metin)


def main():
    GORSEL.update(gorselleri_hazirla())
    yaz("index.html", ana_sayfa())
    yaz("gizlilik.html", gizlilik())
    yaz("firma-rehberi.html", firma_rehberi())
    yaz("404.html", bulunamadi())
    # tuzak sayfası: robots ile yasak; buraya gelen = kuralı çiğneyen bot
    yaz("tuzak/index.html", '<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex,nofollow"><title>Servis kaydı</title>'
        '<script>try{localStorage.setItem("cf_trap","1")}catch(e){}</script><p>Kayıt bulunamadı.</p>\n')
    yaz("favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="9" fill="#0f5f73"/>'
        '<path d="M19.6 8.4a5.3 5.3 0 0 0-7.2 7.2L5 23v4h4l7.4-7.4a5.3 5.3 0 0 0 7.2-7.2l-3.3 3.3-3.2-.8-.8-3.2z" fill="#fff"/></svg>\n')
    yaz("robots.txt", "User-agent: *\nDisallow: /tuzak/\nAllow: /\n" + (f"\nSitemap: {URL}sitemap.xml\n" if YAYINDA else ""))
    yaz("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        f'<url><loc>{URL}</loc></url><url><loc>{URL}firma-rehberi.html</loc></url><url><loc>{URL}gizlilik.html</loc></url></urlset>\n')
    yaz("CNAME", C.ALAN.split("//")[-1].strip("/") + "\n")
    yaz(".nojekyll", "")
    print("Sayfalar yazıldı | görsel:", ", ".join(sorted(GORSEL)) or "yok (çizim kullanılıyor)", "|",
          "YAYINA HAZIR (index)" if YAYINDA else "TELEFON BEKLENIYOR - noindex")


if __name__ == "__main__":
    main()
