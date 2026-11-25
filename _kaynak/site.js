(function(){
var d=document,w=window;
/* menü */
var b=d.querySelector('.menu-ac'),m=d.getElementById('menu');
if(b&&m){b.addEventListener('click',function(){var a=m.classList.toggle('acik');b.setAttribute('aria-expanded',a)});
m.querySelectorAll('a').forEach(function(x){x.addEventListener('click',function(){m.classList.remove('acik');b.setAttribute('aria-expanded','false')})});}
var y=d.getElementById('yil');if(y)y.textContent=new Date().getFullYear();

/* bot işareti: görünmez tuzağa dokunan cihaz bir daha dönüşüm göndermez */
function bot(){try{return localStorage.getItem('cf_trap')==='1'}catch(e){return false}}
w.__cfTrap=function(e){e.preventDefault();try{localStorage.setItem('cf_trap','1')}catch(x){}
 (w.dataLayer=w.dataLayer||[]).push({event:'bot_tuzak'});return false};

/* dönüşüm olayları: yalnız gerçek düğmeler (data-olay). GTM'de "Özel etkinlik" tetikleyicisi kullanın:
   arama_tiklama, whatsapp_tiklama, form_gonderim. tel:/wa.me "Bağlantı tıklaması" tetikleyicisi KULLANMAYIN (tuzak linkleri de eşleşir). */
d.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('[data-olay]');if(!a)return;
 if(a.getAttribute('href')==='#iletisim'){return}
 var ol=a.getAttribute('data-olay'),ko=a.getAttribute('data-konum')||'';
 if(!bot()){(w.dataLayer=w.dataLayer||[]).push({event:ol,konum:ko});
  if(w.gtag){gtag('event',ol,{konum:ko,transport_type:'beacon'});
   if(ol==='arama_tiklama'&&w.__awTel){gtag('event','conversion',{send_to:w.__awTel,transport_type:'beacon'})}}}
 w.__gtmY&&w.__gtmY();w.__gtY&&w.__gtY()},true);

/* WhatsApp servis formu: bal küpü + süre kontrolü */
var f=d.getElementById('servis-formu');
if(f){var t0=Date.now();
 f.addEventListener('submit',function(e){e.preventDefault();
  var g=function(n){var el=f.elements[n];return el?String(el.value||'').trim():''};
  var no=f.getAttribute('data-wa');
  if(g('web_sitesi')||Date.now()-t0<2500){try{localStorage.setItem('cf_trap','1')}catch(x){}return}
  if(!g('ad')||!g('cihaz')){f.querySelector('[name=ad]').focus();return}
  var msg='Merhaba, servis talebim var.\nAd: '+g('ad')+'\nCihaz: '+g('cihaz')+(g('ariza')?'\nArıza: '+g('ariza'):'')+(g('semt')?'\nSemt: '+g('semt'):'');
  if(!bot()){(w.dataLayer=w.dataLayer||[]).push({event:'form_gonderim',cihaz:g('cihaz')})}
  w.__gtmY&&w.__gtmY();
  if(!no){alert('Telefon numarası henüz eklenmedi.');return}
  w.open('https://wa.me/'+no+'?text='+encodeURIComponent(msg),'_blank','noopener');
 });}
})();
