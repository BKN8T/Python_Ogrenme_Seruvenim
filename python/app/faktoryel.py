max_hata = 3
hata_sayisi = 1 
while True :
    fak = input("Sayı Giriniz :")
    sonuc = 1
    if hata_sayisi >= max_hata:
        print("Çok fazla geçersiz giriş yaptınız, program sonlanıyor.")
        break
    try: 
        fakINT = int(fak)
        if fakINT < 0:
            number = fakINT  
            result = 1  
            

            while number <= -1:
                result *= number
                number += 1

            print(f"Sonuç: {result}")
            break
        elif fakINT > 100:
            print("100'den büyük sayılar kullanılmaz")
            hata_sayisi += 1
            continue
    except ValueError: 
        print("Bir sayı Giriniz")
        hata_sayisi += 1
        continue
    while fakINT > 1 :
        sonuc = sonuc * fakINT
        fakINT -= 1
    print(sonuc)
    break