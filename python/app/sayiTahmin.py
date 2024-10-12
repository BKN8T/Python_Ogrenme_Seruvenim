import random

sayi = random.randint(1 , 100)
print(sayi)
while True:
    kullanicisayi = input("Bir değer giriniz: ")
    try:
        kullanicisayiINT = int(kullanicisayi)    
    except ValueError:
        print("LÜtfen sayı giriniz!")
        continue
    if kullanicisayiINT > sayi:
        print("Daha küçük bir sayı giriniz")
    elif kullanicisayiINT < sayi:
        print("Daha büyük bir sayı giriniz")
    else:
        print("Doğru bildiniz")
        break


