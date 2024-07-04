#Kelime Tahmin oyunu.
import random

# Kelime listesi
kelimeler = ["system", "data", "algorithm", "such", "base", "node", "model", "case",
"program", "information", "set", "code", "function", "process", "application", "software",
"class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
"memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
"compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
"step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
"access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
"address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
"programming", "field", "key", "parameter", "distribution", "definition", "instance",
"interaction", "internet", "representation", "edge", "stack", "return", "procedure",
"link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
"detection", "write", "execute", "least", "key"]
# Kelimeler içerisinden random ile rastgeel bir kelime seçtim ve uzunluğunu aldım ve uzunluk kadar "_" oluşturdum.
kelime = random.choice(kelimeler)
harfSayisi = len(kelime)
tahminEdilen = '_' * harfSayisi
# Tahmin hakkını ve puanı oluşturdum.
yanlisTahminHakki = harfSayisi // 2
if harfSayisi % 2 !=0:
    yanlisTahminHakki +=1
puan = 0
"""
Burada önceden tahmin edilen harfi tekrar denersek doğru ise bedavadan puan kazanılabiliyoru. Bu bugu düzeltmek için yeni bir string oluşturdum ve 
içerisine tahmin edilen harfleri attım. Böylece 1 daha tahmin edilen tekrar tahmin edilince kullanıcıyı uytarıyor ve fazladan "-" ve "+" puan hesaplanmıyor.
"""
oncedenTahminEdilen=""
print("Tahmin etmeniz gereken kelimenin {} harfi var: {}\nTahmin hakkınız: {} . Güncel puanınız: {}".format(harfSayisi, tahminEdilen, yanlisTahminHakki, puan))
turkceKarakterler = "çğıöşü"
# Burada oyunu kazanmamızı, kaybetmemizi ve oyunun devam etmesini sağlayan döngüyü oluşturdum.
while yanlisTahminHakki > 0:
    harf = input("\nBir harf tahmin edin : ")
    # Türkçe karakter kontrolü yaptım.
    if harf.lower() in turkceKarakterler:
        print("Gecersiz karakter girdiniz tekrar deneyiniz.")
    else:
        if harf.lower() in oncedenTahminEdilen:
            print("Bu harf denendi lutfen farkli bir harf deneyiniz!!!")
            continue
        oncedenTahminEdilen = oncedenTahminEdilen + harf
        # Harf aranan kelimede var mı diye kontrol ettirdim.
        if harf.lower() in kelime:
            # Kelime boyunca harfi bulup "_" yerine harfi koymasını sağladım.
            for i in range(harfSayisi):
                if kelime[i] == harf.lower():
                    tahminEdilen = tahminEdilen[:i] + harf.lower() + tahminEdilen[i + 1:]
            print("Doğru tahmin! Tahmin edilen kelime: {}".format(tahminEdilen))
            # Eğer tahmin edilen kelimede hiç "_" kalmadıysa tüm harfler bulunmuş olacağından kazandınız mesajı yazdırdım ve tekrar oynamak istiyor mu diye sordum.
            # Ardından seçime göre tekrar kelime ürettim ve ya döngüden çıktım.
            if '_' not in tahminEdilen:
                print("Tebrikler! Kelimeyi dogru tahmin ettiniz!")
                devam = input("Tekrar oynamak ister misiniz? (E/H): ")
                if devam.lower() == 'e':
                    kelime = random.choice(kelimeler)
                    harfSayisi = len(kelime)
                    tahminEdilen = '_' * harfSayisi
                    yanlisTahminHakki = harfSayisi // 2
                    print("Tahmin etmeniz gereken kelimenin {} harfi var: {}".format(harfSayisi, tahminEdilen))
                else:
                    break
            # Burada puanlandırma sistemini yaptım.
            else:
                if harf.lower() in 'aeiou':
                    puan += 3 * kelime.count(harf.lower())
                else:
                    puan += 2 * kelime.count(harf.lower())
                print("Güncel puanınız: {}".format(puan))
        else:
            yanlisTahminHakki -= 1
            puan -= 4
            print("Yanlış tahmin! Kalan tahmin hakkınız: {}. Güncel puanınız: {}".format(yanlisTahminHakki, puan))
            if yanlisTahminHakki == 0:
                print("Tahmin hakkınız bitti! Kaybettiniz.")