"""Baby Day Space yasal sayfaları (GitHub Pages). Kaynak bu dosya; `python uret.py` HTML'leri yazar.

Sayfalar (TR + EN): index (destek), privacy, terms (kullanım koşulları + topluluk kuralları),
delete (hesap ve veri silme), child-safety (çocuk güvenliği standartları).
İçerik uygulamanın v1.0 veri akışıyla birebir olmalıdır (app.md "Topluluk güvenliği").
"""
from pathlib import Path

EPOSTA = "hakkitabak209@gmail.com"
TARIH = {"tr": "23 Kasım 2026", "en": "November 23, 2026"}
KOK = Path(__file__).parent

CSS = """
:root{--bg:#FBF8F4;--card:#FFFFFF;--ink:#2B2540;--soft:#6B6580;--line:#ECE6F2;--acc:#7C5CE0;--acc2:#F3EEFF}
@media (prefers-color-scheme:dark){:root{--bg:#16131F;--card:#211C2E;--ink:#F2EEFA;--soft:#B5ADC9;--line:#2F2840;--acc:#B9A4FF;--acc2:#2A2340}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans",sans-serif}
main{max-width:760px;margin:0 auto;padding:32px 16px 64px}header{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap}
.brand{font-weight:800;font-size:20px;letter-spacing:-.3px}.langs a{margin-left:10px;color:var(--soft);text-decoration:none;font-size:15px}
.langs a.on{color:var(--acc);font-weight:700}h1{font-size:30px;letter-spacing:-.6px;margin:28px 0 4px}.date{color:var(--soft);font-size:14px;margin:0 0 20px}
h2{font-size:20px;margin:28px 0 8px}section{background:var(--card);border:1px solid var(--line);border-radius:20px;padding:4px 20px 12px;margin:14px 0}
a{color:var(--acc)}.cta{display:inline-block;background:var(--acc);color:#fff;padding:12px 22px;border-radius:999px;text-decoration:none;font-weight:700;margin:6px 0}
@media (prefers-color-scheme:dark){.cta{color:#16131F}}nav.pages{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0}nav.pages a{background:var(--acc2);padding:8px 14px;border-radius:999px;text-decoration:none;font-size:15px}
table{border-collapse:collapse;width:100%;font-size:15px}td,th{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left;vertical-align:top}
footer{color:var(--soft);font-size:14px;margin-top:40px}
"""

SAYFA_AD = {
    "tr": {"index": "Destek", "privacy": "Gizlilik", "terms": "Koşullar ve topluluk kuralları",
           "delete": "Hesap silme", "child-safety": "Çocuk güvenliği"},
    "en": {"index": "Support", "privacy": "Privacy", "terms": "Terms & community guidelines",
           "delete": "Account deletion", "child-safety": "Child safety"},
}


def dosya(sayfa, dil):
    return f"{sayfa}.html" if dil == "en" else f"{sayfa}-tr.html"


def kalip(dil, sayfa, baslik, govde):
    diger = "en" if dil == "tr" else "tr"
    nav = "".join(f'<a href="{dosya(s, dil)}">{ad}</a>' for s, ad in SAYFA_AD[dil].items() if s != sayfa)
    son = "Son güncelleme" if dil == "tr" else "Last updated"
    return f"""<!doctype html><html lang="{dil}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{baslik} · Baby Day Space</title>
<meta name="description" content="Baby Day Space — {baslik}"><style>{CSS}</style></head><body><main>
<header><span class="brand">Baby Day Space</span><span class="langs">
<a href="{dosya(sayfa, 'tr')}" class="{'on' if dil == 'tr' else ''}">Türkçe</a><a href="{dosya(sayfa, 'en')}" class="{'on' if dil == 'en' else ''}">English</a></span></header>
<h1>{baslik}</h1><p class="date">{son}: {TARIH[dil]}</p>
{govde}
<nav class="pages">{nav}</nav>
<footer>Baby Day Space · <a href="mailto:{EPOSTA}">{EPOSTA}</a></footer></main></body></html>
"""


def bolum(baslik, *paragraflar):
    return "<section><h2>" + baslik + "</h2>" + "".join(
        p if p.startswith("<") else f"<p>{p}</p>" for p in paragraflar) + "</section>"


def ul(*maddeler):
    return "<ul>" + "".join(f"<li>{m}</li>" for m in maddeler) + "</ul>"


M = f'<a href="mailto:{EPOSTA}">{EPOSTA}</a>'

# ------------------------------------------------------------------- destek
DESTEK_DILLER = [
    ("tr", "Sorun, öneri ya da bildirim için bize yazın:"), ("en", "For help, feedback or reports, email us:"),
    ("zh", "如需帮助、反馈或举报，请发送邮件："), ("es", "Para ayuda, sugerencias o denuncias, escríbenos:"),
    ("ja", "ヘルプ・ご意見・通報はメールでどうぞ："), ("de", "Für Hilfe, Feedback oder Meldungen schreib uns:"),
    ("fr", "Pour de l'aide, un avis ou un signalement, écrivez-nous :"), ("pt", "Para ajuda, sugestões ou denúncias, escreva para:"),
    ("ko", "도움, 의견 또는 신고는 이메일로 보내 주세요:"), ("ar", "للمساعدة أو الاقتراحات أو الإبلاغ راسلنا:"),
    ("hi", "सहायता, सुझाव या रिपोर्ट के लिए हमें ईमेल करें:"), ("ru", "Помощь, отзывы и жалобы — пишите нам:"),
    ("it", "Per aiuto, suggerimenti o segnalazioni scrivici:"), ("nl", "Voor hulp, feedback of meldingen, mail ons:"),
    ("pl", "Pomoc, opinie lub zgłoszenia — napisz do nas:"), ("uk", "Допомога, відгуки та скарги — пишіть нам:"),
    ("id", "Untuk bantuan, masukan, atau laporan, kirim email:"), ("vi", "Cần hỗ trợ, góp ý hoặc báo cáo, hãy gửi email:"),
    ("th", "ขอความช่วยเหลือ ข้อเสนอแนะ หรือแจ้งรายงาน ส่งอีเมลถึงเรา:"), ("bn", "সাহায্য, মতামত বা রিপোর্টের জন্য ইমেল করুন:"),
    ("fa", "برای کمک، پیشنهاد یا گزارش به ما ایمیل بزنید:"),
]

DESTEK = {
    "tr": bolum("Bize ulaşın", "Baby Day Space ile ilgili her soru, öneri, hata ya da topluluk bildirimi için:",
                f'<p><a class="cta" href="mailto:{EPOSTA}?subject=Baby%20Day%20Space%20destek">{EPOSTA}</a></p>',
                "Genellikle 1–2 iş günü içinde yanıt veririz. Topluluktaki uygunsuz içerik bildirimlerini <b>24 saat içinde</b> inceleriz.")
          + bolum("Sık sorulanlar",
                  "<b>Kayıtlarım nerede?</b> Aktivite kayıtların (uyku, emzirme, biberon, bez, banyo, katı gıda, büyüme, süt sağma) yalnız telefonunda saklanır; sunucumuza gönderilmez.",
                  "<b>Topluluğa nasıl katılırım?</b> Topluluk sekmesinde bir takma ad seç ve topluluk kurallarını kabul et. Gerçek adın ya da telefon numaran istenmez.",
                  "<b>Bir gönderiyi nasıl bildiririm?</b> Gönderinin ya da yanıtın ⋯ menüsünden <i>Bildir</i>'e dokun ve nedenini seç. Bildirdiğin içerik senden hemen gizlenir.",
                  "<b>Birini nasıl engellerim?</b> ⋯ menüsünden <i>Kullanıcıyı engelle</i>. Engellediğin kişinin gönderi ve yanıtlarını artık görmezsin; engeli Topluluk › Profil › Engellenenler'den kaldırabilirsin.",
                  f'<b>Hesabımı nasıl silerim?</b> Uygulamada Ayarlar › Hesabı sil. Ayrıntı: <a href="{dosya("delete", "tr")}">Hesap silme</a>.')
          + bolum("Diğer diller", "<table>" + "".join(f"<tr><td>{d}</td><td>{t} {M}</td></tr>" for d, t in DESTEK_DILLER) + "</table>"),
    "en": bolum("Contact us", "For any question, idea, bug or community report about Baby Day Space:",
                f'<p><a class="cta" href="mailto:{EPOSTA}?subject=Baby%20Day%20Space%20support">{EPOSTA}</a></p>',
                "We usually reply within 1–2 business days. Reports about objectionable community content are reviewed <b>within 24 hours</b>.")
          + bolum("FAQ",
                  "<b>Where are my records?</b> Your activity records (sleep, breastfeeding, bottle, diaper, bath, solids, growth, pumping) are stored only on your phone and are not sent to our servers.",
                  "<b>How do I join the community?</b> In the Community tab, pick a nickname and accept the community guidelines. We never ask for your real name or phone number.",
                  "<b>How do I report a post?</b> Tap ⋯ on a post or reply, choose <i>Report</i> and a reason. The content is hidden from you right away.",
                  "<b>How do I block someone?</b> Tap ⋯ and <i>Block user</i>. You will no longer see their posts or replies; unblock any time in Community › Profile › Blocked users.",
                  f'<b>How do I delete my account?</b> In the app: Settings › Delete account. Details: <a href="{dosya("delete", "en")}">Account deletion</a>.')
          + bolum("Other languages", "<table>" + "".join(f"<tr><td>{d}</td><td>{t} {M}</td></tr>" for d, t in DESTEK_DILLER) + "</table>"),
}

# ----------------------------------------------------------------- gizlilik
GIZLILIK = {
    "tr": bolum("Özet", ul("Reklam yok, izleme yok, verini satmıyoruz.",
                           "Aktivite kayıtların yalnız telefonunda kalır.",
                           "Topluluk isteğe bağlıdır; katılırsan yalnız takma adın ve paylaştıkların sunucuda tutulur.",
                           "Hesabını uygulama içinden istediğin an kalıcı olarak silebilirsin."))
    + bolum("Veri sorumlusu ve iletişim", f"Baby Day Space bağımsız bir geliştirici tarafından sunulur. Gizlilikle ilgili tüm talepler için: {M}.")
    + bolum("Cihazında kalan veriler",
            "Bebeğin adı/takma adı, doğum tarihi (girersen), aktivite kayıtları (uyku, emzirme, biberon, bez, banyo, katı gıda, büyüme ölçümleri, süt sağma), notlar ve uygulama ayarları yalnız cihazındaki yerel veritabanında saklanır. Bu veriler bize ya da üçüncü bir tarafa gönderilmez. Uygulamayı silmek ya da Ayarlar › Hesabı sil bu verileri cihazdan kaldırır.")
    + bolum("Topluluk (isteğe bağlı) için işlenen veriler",
            "<table><tr><th>Veri</th><th>Amaç</th></tr>"
            "<tr><td>Rastgele hesap kimliği (anonim oturum)</td><td>Gönderilerini sana bağlamak, kötüye kullanımı önlemek</td></tr>"
            "<tr><td>Takma ad, isteğe bağlı bebek yaş aralığı, uygulama dili</td><td>Profilin ve dil topluluğun</td></tr>"
            "<tr><td>Gönderiler, yanıtlar, anket oyları, beğeniler, kaydettiklerin</td><td>Topluluk hizmeti</td></tr>"
            "<tr><td>Bildirimlerin, engellediğin hesaplar, koşulları kabul zamanı</td><td>Moderasyon ve güvenlik</td></tr>"
            "<tr><td>E-posta adresi (yalnız hesabını e-postana bağlarsan)</td><td>Başka cihazda/webde aynı profile giriş</td></tr>"
            "</table>",
            "Topluluğa fotoğraf yükleme bu sürümde kapalıdır. Topluluk içeriği diğer kullanıcılara açıktır; kişisel bilgilerini (tam ad, telefon, adres) paylaşma. Telefon numarası ve e-posta içeren gönderiler sistem tarafından reddedilir.")
    + bolum("Hizmet sağlayıcı ve konum",
            "Topluluk verileri Supabase (Supabase Inc.) altyapısında, Avrupa Birliği'nde (İrlanda, eu-west-1) saklanır. Supabase verileri yalnız bizim adımıza işler.")
    + bolum("Hukuki dayanak (KVKK / GDPR)",
            "Topluluk hizmetini sunmak için sözleşmenin ifası; güvenlik ve moderasyon için meşru menfaat. Cihazdaki kayıtlar bizim tarafımızdan işlenmez.")
    + bolum("Saklama ve silme",
            f'Topluluk verilerin hesabını silene kadar tutulur. Ayarlar › Hesabı sil profilini, gönderilerini, yanıtlarını, beğenilerini, bildirimlerini ve kimliğini anında ve kalıcı olarak siler. Ayrıntı: <a href="{dosya("delete", "tr")}">Hesap silme</a>.')
    + bolum("İzinler", ul("Bildirimler: süren uyku zamanlayıcısını göstermek için (yerel bildirim)."))
    + bolum("Haklarınız",
            f"Verilerine erişme, düzeltme, silme, işlemeye itiraz etme ve şikâyette bulunma hakkın vardır (KVKK md. 11, GDPR md. 15–22). Talebin için: {M}.")
    + bolum("Çocuklar", "Baby Day Space ebeveynler ve bakım verenler içindir; 18 yaş altındaki kişilere yönelik değildir ve bilerek çocuklardan veri toplamaz.")
    + bolum("Değişiklikler", "Bu politikayı güncellersek tarihini değiştirir, önemli değişiklikleri uygulamada duyururuz."),
    "en": bolum("Summary", ul("No ads, no tracking, we never sell your data.",
                              "Your activity records stay on your phone.",
                              "The community is optional; if you join, only your nickname and what you share are stored on our server.",
                              "You can permanently delete your account in the app at any time."))
    + bolum("Controller and contact", f"Baby Day Space is provided by an independent developer. For any privacy request: {M}.")
    + bolum("Data that stays on your device",
            "Your baby's name/nickname, date of birth (if entered), activity records (sleep, breastfeeding, bottle, diaper, bath, solids, growth measurements, pumping), notes and app settings are stored only in a local database on your device. They are not sent to us or to any third party. Deleting the app or using Settings › Delete account removes them from the device.")
    + bolum("Data processed for the community (optional)",
            "<table><tr><th>Data</th><th>Purpose</th></tr>"
            "<tr><td>Random account ID (anonymous session)</td><td>Link your posts to you, prevent abuse</td></tr>"
            "<tr><td>Nickname, optional baby age range, app language</td><td>Your profile and language community</td></tr>"
            "<tr><td>Posts, replies, poll votes, likes, saved posts</td><td>Community service</td></tr>"
            "<tr><td>Your reports, accounts you block, time you accepted the terms</td><td>Moderation and safety</td></tr>"
            "<tr><td>Email address (only if you link your account to email)</td><td>Sign in to the same profile on another device/web</td></tr>"
            "</table>",
            "Photo uploads to the community are not available in this version. Community content is visible to other users; do not share personal details (full name, phone, address). Posts containing phone numbers or email addresses are rejected automatically.")
    + bolum("Service provider and location",
            "Community data is stored with Supabase (Supabase Inc.) in the European Union (Ireland, eu-west-1). Supabase processes the data only on our behalf.")
    + bolum("Legal basis (GDPR)",
            "Performance of a contract to provide the community; legitimate interest for safety and moderation. On-device records are not processed by us.")
    + bolum("Retention and deletion",
            f'Community data is kept until you delete your account. Settings › Delete account immediately and permanently deletes your profile, posts, replies, likes, reports and identity. Details: <a href="{dosya("delete", "en")}">Account deletion</a>.')
    + bolum("Permissions", ul("Notifications: to show a running sleep timer (local notification)."))
    + bolum("Your rights",
            f"You have the right to access, rectify, erase, object and lodge a complaint (GDPR Art. 15–22, KVKK Art. 11). Requests: {M}.")
    + bolum("Children", "Baby Day Space is for parents and caregivers; it is not directed to people under 18 and does not knowingly collect data from children.")
    + bolum("Changes", "If we update this policy we change the date above and announce material changes in the app."),
}

# ------------------------------------------------------- koşullar + kurallar
KOSULLAR = {
    "tr": bolum("Kabul", "Baby Day Space'i kullanarak bu koşulları kabul edersin. Topluluğa katılırken topluluk kurallarını ayrıca onaylarsın.")
    + bolum("Tıbbi uyarı", "Baby Day Space bir kayıt ve topluluk uygulamasıdır; tanı koymaz, tedavi önermez. Topluluktaki yanıtlar başka ebeveynlerin deneyimidir. Sağlıkla ilgili her konuda doktoruna danış; acil durumda yerel acil numarasını ara.")
    + bolum("Topluluk kuralları — sıfır tolerans",
            "<b>Sakıncalı içerik ve kötüye kullanıma sıfır tolerans uygularız.</b> Aşağıdakiler yasaktır ve içerik kaldırılır, hesap uyarısız kapatılabilir:",
            ul("Hakaret, taciz, zorbalık, nefret söylemi, ayrımcılık",
               "Cinsel içerik, çıplaklık; çocukları içeren her türlü cinsel ya da istismar niteliğinde içerik (yetkililere bildirilir)",
               "Şiddet, kendine zarar verme teşviki, tehdit",
               "Spam, reklam, bağlantı ile yönlendirme, dolandırıcılık, ilaç ya da ürün satışı",
               "Kişisel bilgi paylaşımı (telefon, adres, e-posta, tam ad) — kendine ait olsa bile",
               "Tehlikeli tıbbi tavsiye, sahte sağlık iddiaları",
               "Başkasının fotoğrafını izinsiz paylaşmak; bebeklerin çıplak fotoğrafları"),
            "Sakıncalı ifade ya da bağlantı içeren gönderiler otomatik olarak incelemeye alınır ve onaylanana kadar yayımlanmaz.")
    + bolum("Bildirme, engelleme ve moderasyon",
            f"Her gönderi ve yanıtı ⋯ › Bildir ile bildirebilir, kötüye kullanan hesapları ⋯ › Kullanıcıyı engelle ile engelleyebilirsin. Bildirimleri <b>24 saat içinde</b> inceler, kuralları çiğneyen içeriği kaldırır ve gerekiyorsa hesabı kapatırız. Birden çok bildirim alan içerik inceleme bitene kadar herkesten gizlenir. Ulaşmak için: {M}.")
    + bolum("Senin içeriğin", "Paylaştığın içeriğin sahibi sensin. Topluluk hizmetinde gösterilmesi için bize sınırlı, ücretsiz bir kullanım izni verirsin. İçeriğini istediğin zaman silebilirsin; hesabını silmek tüm içeriğini kaldırır.")
    + bolum("Hesabın", "Topluluk hesabı takma adla açılır. 18 yaşından büyük olmalısın. Hesabını Ayarlar › Hesabı sil ile kalıcı olarak silebilirsin.")
    + bolum("Sorumluluğun sınırı", "Uygulama \"olduğu gibi\" sunulur. Kullanıcıların paylaştığı içerikten, yasaların izin verdiği ölçüde, sorumlu değiliz; ancak bildirilen içeriği kurallarımıza göre ele alırız.")
    + bolum("Apple ve Google", "Apple ve Google bu koşulların tarafı değildir ve uygulamanın desteğinden sorumlu değildir. App Store'dan indirdiysen Apple'ın standart son kullanıcı lisans sözleşmesi (Standard EULA) da geçerlidir.")
    + bolum("Değişiklikler ve iletişim", f"Koşulları güncellersek tarihini değiştiririz. Sorular: {M}."),
    "en": bolum("Acceptance", "By using Baby Day Space you accept these terms. When you join the community you also agree to the community guidelines.")
    + bolum("Medical notice", "Baby Day Space is a tracking and community app; it does not diagnose or treat. Community replies are other parents' experiences. Always consult your doctor on health matters; in an emergency call your local emergency number.")
    + bolum("Community guidelines — zero tolerance",
            "<b>There is no tolerance for objectionable content or abusive users.</b> The following are prohibited; content is removed and accounts may be terminated without notice:",
            ul("Insults, harassment, bullying, hate speech, discrimination",
               "Sexual content, nudity; any sexual or exploitative content involving children (reported to authorities)",
               "Violence, encouragement of self-harm, threats",
               "Spam, advertising, link redirects, scams, selling medicines or products",
               "Sharing personal information (phone, address, email, full name) — even your own",
               "Dangerous medical advice, false health claims",
               "Sharing other people's photos without consent; nude photos of babies"),
            "Posts containing objectionable terms or links are automatically held for review and are not published until approved.")
    + bolum("Reporting, blocking and moderation",
            f"You can report any post or reply via ⋯ › Report and block abusive accounts via ⋯ › Block user. We review reports <b>within 24 hours</b>, remove content that breaks the rules and terminate accounts where needed. Content with multiple reports is hidden from everyone until reviewed. Contact: {M}.")
    + bolum("Your content", "You own what you post. You grant us a limited, free licence to display it in the community service. You can delete your content any time; deleting your account removes all of it.")
    + bolum("Your account", "Community accounts use a nickname. You must be over 18. You can permanently delete your account via Settings › Delete account.")
    + bolum("Limitation of liability", "The app is provided \"as is\". To the extent permitted by law we are not liable for content posted by users; we handle reported content according to these rules.")
    + bolum("Apple and Google", "Apple and Google are not parties to these terms and are not responsible for supporting the app. If you downloaded from the App Store, Apple's Standard End User License Agreement (EULA) also applies.")
    + bolum("Changes and contact", f"If we update these terms we change the date above. Questions: {M}."),
}

# ------------------------------------------------------------- hesap silme
SILME = {
    "tr": bolum("Uygulamadan silme (önerilen)", ul("Baby Day Space'i aç.", "Ayarlar › Hesabı sil'e dokun.", "Onayla. Silme anında ve kalıcıdır."))
    + bolum("Silinen veriler", ul("Topluluk profilin, takma adın, gönderilerin, yanıtların, anket oyların, beğenilerin, kaydettiklerin",
                                  "Bildirimlerin, engel listen, koşul kabul kaydın, hesabına bağlı e-posta",
                                  "Cihazdaki tüm aktivite kayıtları ve ayarlar"),
            "Saklanan veri yoktur: silme sonrası yedek ya da arşiv tutulmaz.")
    + bolum("Uygulamaya erişemiyorsan", f"Uygulamayı sildiysen ya da açamıyorsan {M} adresine \"Hesap silme\" konulu bir e-posta gönder; topluluktaki takma adını yaz. Talebini 7 gün içinde tamamlar ve sana bildiririz."),
    "en": bolum("Delete in the app (recommended)", ul("Open Baby Day Space.", "Go to Settings › Delete account.", "Confirm. Deletion is immediate and permanent."))
    + bolum("What is deleted", ul("Your community profile, nickname, posts, replies, poll votes, likes, saved posts",
                                  "Your reports, block list, terms acceptance record, linked email",
                                  "All activity records and settings on the device"),
            "Nothing is retained: no backup or archive is kept after deletion.")
    + bolum("If you can't access the app", f"If you uninstalled the app or cannot open it, email {M} with the subject \"Account deletion\" and include your community nickname. We complete the request within 7 days and confirm by email."),
}

# --------------------------------------------------------- çocuk güvenliği
COCUK = {
    "tr": bolum("Standartlarımız", "Baby Day Space çocukların cinsel istismarı ve sömürüsüne (CSAE) ve çocuk cinsel istismarı materyaline (CSAM) karşı sıfır tolerans uygular.",
                ul("Çocukları cinselleştiren her içerik yasaktır ve derhal kaldırılır; hesap kalıcı olarak kapatılır.",
                   "Bebek ve çocukların çıplak ya da mahrem fotoğraflarının paylaşımı yasaktır.",
                   "Kullanıcılar içerikleri uygulama içinden bildirebilir; bildirimler 24 saat içinde incelenir.",
                   "Tespit edilen CSAM ilgili yasal mercilere ve gerektiğinde NCMEC'e bildirilir."),
                f"Çocuk güvenliği irtibat noktası: {M}"),
    "en": bolum("Our standards", "Baby Day Space has zero tolerance for child sexual abuse and exploitation (CSAE) and child sexual abuse material (CSAM).",
                ul("Any content that sexualises children is prohibited and removed immediately; the account is permanently terminated.",
                   "Sharing nude or intimate photos of babies or children is prohibited.",
                   "Users can report content in the app; reports are reviewed within 24 hours.",
                   "Identified CSAM is reported to the relevant authorities and, where applicable, to NCMEC."),
                f"Child safety point of contact: {M}"),
}

ICERIK = {"index": DESTEK, "privacy": GIZLILIK, "terms": KOSULLAR, "delete": SILME, "child-safety": COCUK}

if __name__ == "__main__":
    for sayfa, diller in ICERIK.items():
        for dil, govde in diller.items():
            (KOK / dosya(sayfa, dil)).write_bytes(kalip(dil, sayfa, SAYFA_AD[dil][sayfa], govde).encode("utf-8"))
    (KOK / ".nojekyll").write_bytes(b"")
    print("yazıldı:", sorted(p.name for p in KOK.glob("*.html")))
