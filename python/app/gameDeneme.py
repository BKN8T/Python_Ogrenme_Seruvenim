import random


oyuncuİsimi = input("Lütfen Karakteriniz İçin Bir İsim Giriniz : ")

oyuncuDict = {
    "İsim": oyuncuİsimi,
    "Sağlık": 100,
    "Mutluluk": 50,
    "Açlık": 100,
    "Yemek Sayısı": 4,
    "Gün": 1 
}


sabah_aktiviteleri = ["kahvaltı yap", "spor yap", "kitap oku", "sosyal medyada gezin", "meditasyon yap", "yürüyüş yap", "yemek ye", "yemek yap"]
öğle_aktiviteleri = ["öğle yemeği ye", "alışveriş yap", "arkadaşlarınla buluş", "film izle", "çalışma yap"]
akşam_aktiviteleri = ["akşam yemeği ye", "dinlen", "müzik dinle", "gece yürüyüşü yap", "aile zamanı"]

def aktivite_secim(vakit, aktiviteler):
    
    secilen_aktiviteler = random.sample(aktiviteler, 3)
    print(f"\n{vakit} vakti için seçenekleriniz:")
    for i, aktivite in enumerate(secilen_aktiviteler, 1):
        print(f"{i}. {aktivite}")

    def kullanıcı_secim():
        while True:
            try:
                secim = input("Bir aktivite seçin (1, 2 veya 3) ya da çıkmak için 'q' tuşuna basın: ")
                if secim == 'q':
                    exit() 
                secim = int(secim)
                if secim in [1, 2, 3]:
                    return secim
                else:
                    print("Yanlış İşlem Yaptınız! Bir aktivite seçin (1, 2 veya 3): ")
            except ValueError:
                print("Geçersiz giriş! Lütfen 1, 2 veya 3 giriniz.")

    secim = kullanıcı_secim()
    secilen_aktivite = secilen_aktiviteler[secim - 1]
    

    if secilen_aktivite in ["kahvaltı yap", "öğle yemeği ye", "akşam yemeği ye"]:
        if oyuncuDict["Yemek Sayısı"] <= 0:
            print(f"Yeterli yemeğiniz kalmadı! {secilen_aktivite} işlemini yapamazsınız.")
        else:
            oyuncuDict["Mutluluk"] += 5
            oyuncuDict["Açlık"] += 20
            oyuncuDict["Yemek Sayısı"] -= 1
            oyuncuDict["Sağlık"] += 5
            print(f"{vakit.capitalize()} yemeğinizi yediniz. Mutluluğunuz arttı!")
    elif secilen_aktivite == "spor yap":
        oyuncuDict["Sağlık"] += 10
        oyuncuDict["Mutluluk"] += 5
        oyuncuDict["Açlık"] -= 20
        print(f"{vakit.capitalize()} spor yaptınız. Sağlığınız ve mutluluğunuz arttı! Açlığınız arttı!")
    elif secilen_aktivite == "kitap oku":
        oyuncuDict["Mutluluk"] += 3
        print(f"Bir kitap okudunuz. Mutluluğunuz arttı!")
    elif secilen_aktivite == "sosyal medyada gezin":
        oyuncuDict["Mutluluk"] += 20
        oyuncuDict["Sağlık"] -= 10
        print(f"Sosyal medyada gezindiniz. Mutluluğunuz arttı! Sağlığınız azaldı!")
    elif secilen_aktivite == "meditasyon yap":
        oyuncuDict["Sağlık"] += 5
        oyuncuDict["Mutluluk"] += 3
        oyuncuDict["Açlık"] -= 10
        print(f"Sabah meditasyonu yaptınız. Sağlığınız ve mutluluğunuz arttı! Açlığınız azaldı")
    elif secilen_aktivite == "yürüyüş yap":
        oyuncuDict["Sağlık"] += 20
        oyuncuDict["Mutluluk"] += 15
        oyuncuDict["Açlık"] -= 20
        print(f"{vakit.capitalize()} yürüyüşü yaptınız. Sağlığınız arttı!")



    print(f"\nGüncel Durum: Sağlık: {oyuncuDict['Sağlık']} | Mutluluk: {oyuncuDict['Mutluluk']} | Açlık: {oyuncuDict['Açlık']} | Yemek Sayısı: {oyuncuDict['Yemek Sayısı']}")


    if oyuncuDict["Sağlık"] <= 0 or oyuncuDict["Mutluluk"] <= 0 or oyuncuDict["Açlık"] <= 0:
        print("Oyun Bitti! Sağlık, mutluluk veya açlık değeriniz sıfır veya altına düştü.")
        exit()

def gunluk_dongu():
    print(f"\n===== Gün {oyuncuDict['Gün']} =====")
    aktivite_secim("sabah", sabah_aktiviteleri)
    aktivite_secim("öğle", öğle_aktiviteleri)
    aktivite_secim("akşam", akşam_aktiviteleri)


    oyuncuDict["Gün"] += 1
    print(f"\nGün {oyuncuDict['Gün'] - 1} tamamlandı. Güncel Durum: Sağlık: {oyuncuDict['Sağlık']} | Mutluluk: {oyuncuDict['Mutluluk']} | Açlık: {oyuncuDict['Açlık']} | Yemek Sayısı: {oyuncuDict['Yemek Sayısı']}")
    print("Bir sonraki güne geçiyorsunuz...\n")

while True:
    gunluk_dongu()
    