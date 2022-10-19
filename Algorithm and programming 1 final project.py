import sys
MIN_YATAY_CIZGI_SAY = 3
MAX_YATAY_CIZGI_SAY = 7
HARFLER = ["A", "B", "C", "D", "E", "F", "G", "H"]

#GİRİLEN DEĞER SAYI MI DİYE KONTROL EDER, DEĞİLSE SAYI GİRİLİNCEYE KADAR İNPUT ALMAYA DEVAM EDER
def sayi_mi(yatay_cizgi_say, sayi):  # istenilen ifade sayı olarak girilene kadar input alır...
    sayi = True
    while sayi:                      # sayı olarak girilince de return eder
        try:
            yatay_cizgi_say = int(yatay_cizgi_say)
            sayi = False
            return int(yatay_cizgi_say)
        except ValueError:
            yatay_cizgi_say = input("Sayı yerine metin girdiniz...lütfen yeniden giriniz:")
            sayi = True

#BEKLENEN ARALIKTA DEĞER GİRİLİNCEYE KADAR İNPUT ALMAYA DEVAM EDER
def hata_kontrol(yatay_cizgi_say, min_aralik, max_aralik):
    sayi = True
    yatay_cizgi_say = sayi_mi(yatay_cizgi_say, sayi)
    while not (min_aralik <= yatay_cizgi_say <= max_aralik):
        yatay_cizgi_say = input("aralık dışında bir değer girdiniz... lütfen yeniden giriniz:")
        yatay_cizgi_say = sayi_mi(yatay_cizgi_say, sayi)
        yatay_cizgi_say = int(yatay_cizgi_say)
    return yatay_cizgi_say

# OYUN TAHTASINI GÖRÜNTÜLER
def oyun_alani_goruntuleme(yatay_cizgi_say, HARFLER, konum_list):
    yatay_cizgi_say = hata_kontrol(yatay_cizgi_say, MIN_YATAY_CIZGI_SAY, MAX_YATAY_CIZGI_SAY)
    tur1 = ("---" + " ") * yatay_cizgi_say
    tur2 = "|" + ("   " + "|") * yatay_cizgi_say
    HARFLER = HARFLER[
              :yatay_cizgi_say + 1]  # kullanılabilecek olası tüm harflerin bulunduğu listeden kullanacaklarımızı kestik
    print("  ", end='')  # A harfini yazmadan önce 2 satırlık boşluk bırakacak ve hizalı olmasını sağlayacak
    for harf in HARFLER:  # oyun alanının üst tarafındaki harfleri yazdıracak
        print(f"{harf:3} ", end='')
    print()  # harfleri yazma aşaması bittikten sonra bir satır aşağı inmeyi sağlayacak

    for i in range(1, yatay_cizgi_say):
        print(f"{i} {konum_list[i][1]:1}", end='')
        for j in range(yatay_cizgi_say):
            print(f"---{konum_list[i][j + 2]}", end='')
        print(f" {i}")
        print(f"  {tur2}")
    print(f"{yatay_cizgi_say} {konum_list[yatay_cizgi_say][1]}", end='')
    for k in range(yatay_cizgi_say):
        print(f"---{konum_list[yatay_cizgi_say][k + 2]:1}", end='')
    print(f"{yatay_cizgi_say:2}")

    print("  ", end='')  # A harfini yazmadan önce 2 satırlık boşluk bırakacak ve hizalı olmasını sağlayacak
    for harf in HARFLER:  # oyun alanının üst tarafındaki harfleri alta da yazdıracak
        print(f"{harf:4}", end='')
    print()
    print()

# GİRİLEN HAMLEYİ ÖNCE PARÇALAR SONRA HARFİN İNDEXİNİ BULUR
def harf_index_bulma1(hamle):
    harf_index = hamle[1:0:-1]
    for harf in HARFLER:
        if harf == harf_index:
            harf_konum = HARFLER.index(harf)
            return harf_konum

# GİRİLEN DEĞER SAYI MI DİYE KONTROL EDER, TRUE FALSE DÖNDÜRÜR
def sayi_kontrol(number):
    try:
        number = int(number)
        return True
    except:
        return False

# HAMLEYİ SAYI VE HARF OLARAK PARÇALAR
def hamleyi_parcala(hamle):  # girilen degeri 2 parça halinde geri döndürür
    hamle_sayi = hamle[:1]
    hamle_harf = hamle[1:0:-1]
    return hamle_sayi, hamle_harf

# HAMLENİN BEKLENİLEN ŞEKİLDE GİRİLİP GİRİLMEDİĞİNİ KONTROL EDER
def hamle_giris_kontrol(hamle, yatay_cizgi_say):  # hamle olarak girilen değerin ilk kısmı int mi, int ise beklenilen aralıkta mı...
    hamle_sayi, hamle_harf = hamleyi_parcala(hamle)  # 2. kısmı str mi, str ise beklenilen aralıkta mı kontrol edecek fonk
    while not (sayi_kontrol(hamle_sayi) and type(hamle_harf) == str and not (sayi_kontrol(hamle))) or \
            (int(hamle_sayi) not in range(1, yatay_cizgi_say + 1)) or (hamle_harf not in HARFLER[:yatay_cizgi_say+1]) or len(hamle)>2:
        hamle = input("Yanlış veri tipi:")
        hamle = hamle.upper()
        hamle_sayi, hamle_harf = hamleyi_parcala(hamle)
    else:
        return hamle

# TAŞLAR DİZİLİRKEN HEDEF KONUMDA TAŞ VAR MI KONTROL EDER
def tas_var_mi(hamle, konum_list, deger, yatay_cizgi_say):
    sayi_index = hamle[:1]
    harf_index = harf_index_bulma1(hamle)
    if konum_list[int(sayi_index)][harf_index + 1] == ' ':
        konum_list[int(sayi_index)][harf_index + 1] = deger
    else:
        hamle = input("Zaten taş olan bir konuma hamle yapmak istiyorsunuz... Lütfen yeni değer giriniz:")
        hamle = hamle.upper()
        hamle = hamle_giris_kontrol(hamle, yatay_cizgi_say)
        hamle = tas_var_mi(hamle, konum_list, deger, yatay_cizgi_say)

# OYUN BAŞINDA SIRAYLA GİRDİ ALIR, HEDEF KONUM BOŞSA ORAYA TAŞI YERLEŞTİRİR
def taslari_listele(konum_list,yatay_cizgi_say):
    for i in range(int(yatay_cizgi_say * (yatay_cizgi_say + 1) / 2)):
        deger = "B"
        beyaz_hamle = input("beyaz hamle giriniz:")
        beyaz_hamle = beyaz_hamle.upper()
        beyaz_hamle = hamle_giris_kontrol(beyaz_hamle,yatay_cizgi_say)
        tas_var_mi(beyaz_hamle, konum_list, deger,yatay_cizgi_say)
        beyaz_sayi_index = beyaz_hamle[:1]
        beyaz_harf_index = harf_index_bulma1(beyaz_hamle)  # harf_index_bulma1 fonk çalıştırılarak harf indexi bulundu
        oyun_alani_goruntuleme(yatay_cizgi_say, HARFLER, konum_list)

        deger = "S"
        siyah_hamle = input("siyah hamle giriniz:")
        siyah_hamle = siyah_hamle.upper()
        siyah_hamle = hamle_giris_kontrol(siyah_hamle,yatay_cizgi_say)
        tas_var_mi(siyah_hamle, konum_list, deger,yatay_cizgi_say)  # hamle yapılmak istenilen konumun boş olup olmamasını kontrol eder
        siyah_sayi_index = siyah_hamle[:1]
        siyah_harf_index = harf_index_bulma1(siyah_hamle)  # harfin indexini bulur
        oyun_alani_goruntuleme(yatay_cizgi_say, HARFLER, konum_list)  # oyun tahtasını görüntüler
    return konum_list

# TAŞLAR OYUN TAHTASINA YERLEŞTİRİLDİKTEN SONRA KAÇAR TANE KARE OLUŞTUĞUNU SAYAR
def kare_saydirma(beyaz_kare_say, siyah_kare_say, yatay_cizgi_say, konum_list):
    for i in range(yatay_cizgi_say - 1):
        for j in range(yatay_cizgi_say):
            if konum_list[i+1][j+1] == konum_list[i+1][j+2] == konum_list[i+2][j+2] == konum_list[i+2][j+1]:
                if konum_list[i + 1][j + 1] == 'B':
                    beyaz_kare_say += 1
                else:  # hatalı giriş durumlarını önceden kontrol ettiğimiz için burada direkt else kullanabiliriz
                    siyah_kare_say += 1
    return siyah_kare_say, beyaz_kare_say

# GİRİLEN DEĞERE GÖRE, GEREKLİ KONTROLLERİ YAPTIKTAN SONRA TAŞI ÇIKARTIR
def bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say,tas_tur):
    cikarilacak_tas = hamle_giris_kontrol(cikarilacak_tas, yatay_cizgi_say)
    cikarilacak_tas_sayi = cikarilacak_tas[:1]
    cikarilacak_tas_harf_index = harf_index_bulma1(cikarilacak_tas)
    bayrak = kare_olustu_mu(cikarilacak_tas_sayi,cikarilacak_tas_harf_index,tas_tur,konum_list,0,0,0,0)
    if konum_list[int(cikarilacak_tas_sayi)][cikarilacak_tas_harf_index + 1] != tas_tur:
        cikarilacak_tas = input("Bu taşı çıkaramazsınız...lütfen yeniden giriniz:")
        cikarilacak_tas = cikarilacak_tas.upper()
        bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say, tas_tur)
    elif bayrak:
        cikarilacak_tas = input("rakibin karesini bozamazsınız...lütfen yeniden giriniz:")
        cikarilacak_tas = cikarilacak_tas.upper()
        bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say, tas_tur)
    else:
        konum_list[int(cikarilacak_tas_sayi)][cikarilacak_tas_harf_index + 1] = ' '
        oyun_alani_goruntuleme(yatay_cizgi_say, HARFLER, konum_list)  # oyun tahtasını görüntüler

# TAŞLARI HAREKET ETTİRMEYE BAŞLAMADAN ÖNCE, OLUŞAN KARE SAYISINA GÖRE TAŞLARI ÇIKARTIR
def taslari_cikarma(beyaz_kare_say, siyah_kare_say, konum_list, yatay_cizgi_say):
    if beyaz_kare_say == siyah_kare_say == 0:
        tas_tur = 'S'  # çıkarılacak olan taş tipi
        cikarilacak_tas = input("Çıkarmak istediğiniz taşı giriniz:")
        cikarilacak_tas = cikarilacak_tas.upper()
        bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say, tas_tur)

    else:
        for i in range(beyaz_kare_say):
            tas_tur = 'S'  # çıkarılacak olan taş tipi
            cikarilacak_tas = input("Çıkarmak istediğiniz taşı giriniz:")
            cikarilacak_tas = cikarilacak_tas.upper()
            bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say, tas_tur)
        for j in range(siyah_kare_say):
            tas_tur = 'B'  # çıkarılacak olan taş tipi
            cikarilacak_tas = input("Çıkarmak istediğiniz taşı giriniz:")
            cikarilacak_tas = cikarilacak_tas.upper()
            bir_tas_cikarma(konum_list, cikarilacak_tas, yatay_cizgi_say, tas_tur)

# 2. HAMLE TÜRÜNDE HARF İNDEX BULUR
def harf_index_bulma2(hamle):
    harf_index = hamle[4:5]
    for harf in HARFLER:
        if harf == harf_index:
            harf_konum = HARFLER.index(harf)
            return int(harf_konum)

# 2. HAMLE TÜRÜNDE HAMLEYİ SAYI VE HARFLERE PARÇALAR
def hamleyi_parcala2(hamle):
    eski_konum_sayi = hamle[:1]
    eski_konum_harf_index = harf_index_bulma1(hamle)
    yeni_konum_sayi = hamle[3:4]
    yeni_konum_harf_index = harf_index_bulma2(hamle)
    return eski_konum_sayi, eski_konum_harf_index, yeni_konum_sayi, yeni_konum_harf_index

# OYUN OYNANIRKEN YENİ KARE OLUŞMUŞSA, ÖNCE İNPUT ALIR, GEREKLİ KONTROLLERDEN SONRA TAŞI ÇIKARTIR
def tas_cikar(beyaz_tas_top,siyah_tas_top, konum_list, yatay_cizgi_say,sira,flag):
    cikarilacak_tas = input("Çıkarmak istediğiniz taşı giriniz:")
    cikarilacak_tas = cikarilacak_tas.upper()
    cikarilacak_tas = hamle_giris_kontrol(cikarilacak_tas, yatay_cizgi_say)
    cikarilacak_tas_sayi = cikarilacak_tas[:1]
    cikarilacak_tas_sayi = int(cikarilacak_tas_sayi)
    cikarilacak_tas_harf_index = harf_index_bulma1(cikarilacak_tas)
    tas = konum_list[cikarilacak_tas_sayi][cikarilacak_tas_harf_index+1]
    flag = kare_olustu_mu(cikarilacak_tas_sayi,cikarilacak_tas_harf_index,tas,konum_list,beyaz_tas_top,siyah_tas_top,yatay_cizgi_say,sira)
    if sira % 2 == 0:
        if konum_list[cikarilacak_tas_sayi][cikarilacak_tas_harf_index + 1] != 'B':
            print("bu konumdan taş çıkaramazsınız...")
            siyah_tas_top,beyaz_tas_top = tas_cikar(beyaz_tas_top,siyah_tas_top, konum_list,yatay_cizgi_say,sira,flag)
        elif flag:
            print("rakibin oluşturduğu kareyi bozamazsınız... lütfen başka bir taş çıkarın")
            siyah_tas_top,beyaz_tas_top = tas_cikar(beyaz_tas_top, siyah_tas_top, konum_list, yatay_cizgi_say, sira,flag)
        else:
            print("beyaz taş çıkarıldı...")
            konum_list[cikarilacak_tas_sayi][cikarilacak_tas_harf_index+1] = ' '
            beyaz_tas_top -= 1
    else:
        if konum_list[cikarilacak_tas_sayi][cikarilacak_tas_harf_index + 1] != 'S':
            print("bu konumdan taş çıkaramazsınız...")
            print(konum_list[int(cikarilacak_tas_sayi)][cikarilacak_tas_harf_index + 1])
            siyah_tas_top, beyaz_tas_top =tas_cikar(beyaz_tas_top,siyah_tas_top, konum_list,yatay_cizgi_say,sira,flag)
        elif flag:
            print("rakibin oluşturduğu kareyi bozamazsınız... lütfen başka bir taş çıkarın")
            siyah_tas_top,beyaz_tas_top = tas_cikar(beyaz_tas_top, siyah_tas_top, konum_list, yatay_cizgi_say, sira,flag)
        else:
            print("siyah taş çıkarıldı...")
            konum_list[cikarilacak_tas_sayi][cikarilacak_tas_harf_index + 1] = ' '
            siyah_tas_top -= 1
    return siyah_tas_top,beyaz_tas_top

# YAPILAN HER HAMLEDEN SONRA YENİ KARE OLUŞTU MU KONTROL EDER, TRUE FALSE DÖNDÜRÜR
def kare_olustu_mu(yeni_konum_sayi, yeni_konum_harf_index, tas, konum_list, beyaz_tas_top, siyah_tas_top, yatay_cizgi_say,sira):
    if tas == konum_list[int(yeni_konum_sayi)][yeni_konum_harf_index + 2] == konum_list[int(yeni_konum_sayi) + 1][
        yeni_konum_harf_index + 2] == konum_list[int(yeni_konum_sayi) + 1][yeni_konum_harf_index + 1]:
        return True
    elif tas == konum_list[int(yeni_konum_sayi)][yeni_konum_harf_index + 2] == konum_list[int(yeni_konum_sayi) - 1][
        yeni_konum_harf_index + 2] == konum_list[int(yeni_konum_sayi) - 1][yeni_konum_harf_index + 1]:
        return True
    elif tas == konum_list[int(yeni_konum_sayi)][yeni_konum_harf_index] == konum_list[int(yeni_konum_sayi) + 1][
        yeni_konum_harf_index] == konum_list[int(yeni_konum_sayi) + 1][yeni_konum_harf_index + 1]:
        return True
    elif tas == konum_list[int(yeni_konum_sayi)][yeni_konum_harf_index] == konum_list[int(yeni_konum_sayi) - 1][
        yeni_konum_harf_index] == konum_list[int(yeni_konum_sayi)-1][yeni_konum_harf_index + 1]:
        return True
    else:
        return False

# OYUNUN OYNANMASINI YÖNETİR
def oynama(sira, konum_list, yatay_cizgi_say, beyaz_tas_top, siyah_tas_top):
    while beyaz_tas_top > 3 and siyah_tas_top > 3:
        if sira % 2 == 0:
            print("sıra siyah taş oynayan oyuncuda...")
        else:
            print("sıra beyaz taş oynayan oyuncuda...")
        hamle = input("yapmak istediğiniz hamleyi giriniz:")
        hamle = hamle.upper()
        eski_konum_sayi, eski_konum_harf_index, yeni_konum_sayi, yeni_konum_harf_index = hamleyi_parcala2(hamle)
        while not(sayi_kontrol(eski_konum_sayi) and sayi_kontrol(yeni_konum_sayi) and type(hamle[4:5]) == str
              and type(hamle[1:0:-1])) == str or len(hamle)!=5 or hamle[4:5] not in HARFLER or hamle[1:0:-1] not in HARFLER :
            hamle = input("Hamleyi beklenen şekilde girmediniz...lütfen yeniden giriniz:")
            hamle = hamle.upper()
            eski_konum_sayi, eski_konum_harf_index, yeni_konum_sayi, yeni_konum_harf_index = hamleyi_parcala2(hamle)

        if eski_konum_sayi == yeni_konum_sayi and eski_konum_harf_index == yeni_konum_harf_index:
            print("Taşınızın eski konumu ile yeni konumunu aynı girdiniz...")
            oynama(sira,konum_list,yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
        tas = konum_list[int(eski_konum_sayi)][int(eski_konum_harf_index) + 1]
        if sira % 2 == 0:  # sira çifttir ve oynama sırası siyahtadır
            if tas != 'S':
                print("Sadece kendi taşınızı oynatabilirsiniz...")
                oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
        else:  # sira tektir ve oynama sırası beyazdadır
            if tas != 'B':
                print("Sadece kendi taşınızı oynatabilirsiniz...")
                oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)

        if eski_konum_sayi != yeni_konum_sayi and eski_konum_harf_index != yeni_konum_harf_index:
            print("Taşları yalnızca yatay ya da dikey olarak hareket ettirebilirsiniz...")
            oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
        if int(yeni_konum_sayi) - int(eski_konum_sayi) != 0:  # aşağıya doğru hamle yapılması durumu
            if yeni_konum_sayi > eski_konum_sayi:
                for i in range(int(yeni_konum_sayi) - int(eski_konum_sayi)):
                    if konum_list[int(eski_konum_sayi) + i + 1][eski_konum_harf_index + 1] != ' ':
                        print("Yol üzerinde taş olduğu için bu konuma hamle yapamazsınız...")
                        oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
            else:  # yukarıya doğru hamle yapılması durumu
                for i in range(int(eski_konum_sayi) - int(yeni_konum_sayi)):
                    if konum_list[int(eski_konum_sayi) - i - 1][eski_konum_harf_index + 1] != ' ':
                        print("Yol üzerinde taş olduğu için bu konuma hamle yapamazsınız...")
                        oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
        elif (yeni_konum_harf_index - eski_konum_harf_index) != 0:  # yana doğru hamle yapılması durumu
            if yeni_konum_harf_index > eski_konum_harf_index:  # sağa doğru hareket edilmesi durumu
                for i in range(eski_konum_harf_index + 1, yeni_konum_harf_index + 1):
                    if konum_list[int(eski_konum_sayi)][i + 1] != ' ':
                        print("Yol üzerinde taş olduğu için bu konuma hamle yapamazsınız...")
                        oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)
            else:  # sola doğru hamle yapılması durumu
                for i in range(eski_konum_harf_index-1,yeni_konum_harf_index-1,-1):
                    if konum_list[int(yeni_konum_sayi)][i + 1] != ' ':
                        print("Yol üzerinde taş olduğu için bu konuma hamle yapamazsınız...")
                        oynama(sira,konum_list, yatay_cizgi_say,beyaz_tas_top,siyah_tas_top)

        konum_list[int(eski_konum_sayi)][eski_konum_harf_index + 1] = ' '  # taşı bulunduğu konumdan sildik
        konum_list[int(yeni_konum_sayi)][yeni_konum_harf_index + 1] = tas
        flag = kare_olustu_mu(yeni_konum_sayi,yeni_konum_harf_index,tas,konum_list,beyaz_tas_top,siyah_tas_top,yatay_cizgi_say,sira)
        if flag:  # flag True dönerse kare oluştu demektir, bu durumda taş çıkarma fonk çalışacak
            siyah_tas_top, beyaz_tas_top = tas_cikar(beyaz_tas_top, siyah_tas_top, konum_list, yatay_cizgi_say, sira,flag)

        oyun_alani_goruntuleme(yatay_cizgi_say, HARFLER, konum_list)
        sira += 1
    if siyah_tas_top == 3:
        print("Kazanan: Beyaz}")
    else:
        print("Kazanan: Siyah")
    sys.exit()

def main():
     sira = 1
     beyaz_kare_say = 0  # kare sayılarını bulmak için kullanılan sayaçlar
     siyah_kare_say = 0
     yatay_cizgi_say = input("Yatay çizgi sayısını giriniz:")
     yatay_cizgi_say = hata_kontrol(yatay_cizgi_say, MIN_YATAY_CIZGI_SAY, MAX_YATAY_CIZGI_SAY)
     konum_list = [[" "] * (int(yatay_cizgi_say) + 3) for i in range(int(yatay_cizgi_say) + 2)]  # matris oluşturuldu
     oyun_alani_goruntuleme(yatay_cizgi_say,HARFLER,konum_list)
     taslari_listele(konum_list,yatay_cizgi_say)
     siyah_kare_say, beyaz_kare_say = kare_saydirma(siyah_kare_say, beyaz_kare_say,yatay_cizgi_say, konum_list)
     beyaz_tas_top = yatay_cizgi_say * (yatay_cizgi_say + 1) / 2 - siyah_kare_say
     siyah_tas_top = yatay_cizgi_say * (yatay_cizgi_say + 1) / 2 - beyaz_kare_say
     print(f"{siyah_kare_say} tane siyah {beyaz_kare_say} tane beyaz taş çıkarabilirsiniz")
     taslari_cikarma(beyaz_kare_say, siyah_kare_say,konum_list, yatay_cizgi_say)
     oynama(sira,konum_list,yatay_cizgi_say,beyaz_tas_top, siyah_tas_top)
main()