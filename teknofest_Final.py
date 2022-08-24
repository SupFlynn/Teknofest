import random

kolay_secim = ['Ağaç','Deniz','Çocuk']
orta_secim = ['Barış','Toprak','Öğretmen']
zor_secim = ['Göz','Kan','Uzay']
y = 0
z = 0
while y == 0:
    print("Güncel puanınız: ")
    print(z)
    zorluk_secimi=input('Hangi zorlukta oynamak istiyorsunuz? (kolay,orta,zor) ')
    if zorluk_secimi == 'kolay' :
        x = random.choice(kolay_secim)
        print(x)
        usr_input = input('Bu kelime size neyi çağrıştırıyor ? ')
        if x == 'Ağaç' :
            if usr_input == 'Yeşil' or 'Gök' or 'Orman' or 'Kaynak' or 'Kök' or 'Işık' or 'Yağmur'  :
                print("Tebrikler doğru cevap verdin. ")
                z = z+1
            else :
                print("Üzgünüz ki yanlış cevap verdin. ")
        elif x == 'Deniz' :
            if usr_input == 'Dalga' or 'Sonsuzluk' or 'Yaşam' or 'Balık' or 'Köpekbalığı' or 'Köpük' :
                print("Tebrikler doğru cevap verdin. ")
                z = z+1
            else :
                print("Üzgünüz ki yanlış cevap verdin. ")
        elif x == 'Çocuk' :
            if usr_input == 'Sevgi' or 'Eğlence' or 'Umut' or 'Gelecek' or 'Yaramaz' or 'Oyun' 'Arı' :
                print("Tebrikler doğru cevap verdin. ")
                z = z+1
            else :
                print("Üzgünüz ki yanlış cevap verdin. ")
    elif zorluk_secimi == 'orta' :
        x = random.choice(orta_secim)
        print(x)
        usr_input = input('Bu kelime size neyi çağrıştırıyor ? ')
        if x == 'Barış' :
            if usr_input == 'Güvercin' or 'Birlik' or 'Özgürlük' or 'Savaş' or 'Çağdaşlık' or 'Uygarlık' or 'Birlik' or 'Bütün' or 'İnanç' or 'Güven' or 'Dinç' :
                print("Tebrikler doğru cevap verdin. ")
                z = z+2
            else :
                print("Maalesef ki yanlış cevap verdin. ")
        if x == 'Öğretmen' :
            if usr_input == 'Gelecek' or 'Işık' or 'Öğrenci' or 'Bilgi' or 'Sevgi' or 'Anlayış' or 'Okul' or 'Bütünleşme' :
                print("Tebrikler doğru cevap verdin. ")
                z = z+2
            else :
                print("Maalesef ki yanlış cevap verdin. ")
        if x == 'Toprak' :
            if usr_input == 'Doğa' or 'Yaşam' or 'Üretim' or 'Bolluk' or 'Ekin' or 'Bitki' or 'Ağaç' or 'Solucan' or 'Ölüm' or 'Verim' or 'Tarla' or 'Toz' or 'Duman' :
                print("Tebrikler doğru cevap verdin. ")
            else :
                print("Üzgünüz ki yanlış cevap verdin. ")
    elif zorluk_secimi == 'zor' :
        x = random.choice(zor_secim)
        print(x)
        usr_input = input('Bu kelime size neyi çağrıştırıyor ? ')
        if x == 'Göz' :
            if usr_input == 'Görüş' or 'Çukur' or 'Açık' or 'Çukur' or 'Bilgi' or 'Sevgi' or 'Öz' :
                print("Tebrikler doğru cevap verdin. ")
                z = z+3
            else :
                print("Üzgünüz ki yanlış cevap verdin. ")
                z = z-1
        if x == 'Kan' :
            if usr_input == 'Kızıl' or 'Al' or 'Yaşam' or 'Diri' or 'Damar' or 'Sağ' or 'Canlı' or 'Ölü' or 'Sevgi' or 'Yavru' or 'Yaşlı' or 'Sağlık' or 'Bebek' :
                print("Tebrikler doğru cevap verdiniz. ")
                z = z+3
            else :
                print("Üzgünüz ki yanlış cevap verdiniz. ")
                z = z-1
        if x == 'Uzay' :
            if usr_input == 'Uzak' or 'Sonsuzluk' or 'Bilinmezlik' or 'Boşluk' or 'Korku' or 'Arayış' or 'Bilim' or 'Yalnızlık' or 'Gezegen' or 'Gökizci' :
                print("Tebrikler doğru cevap verdiniz. ")
                z = z+3
            else :
                z = z-1
                print("Üzgünüz ki yanlış cevap verdiniz. ")

    else:
        print('Geçersiz zorluk seçimi lütfen yazıma dikkat ediniz.')

