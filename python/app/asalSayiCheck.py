

deger = input('Lütfen Bir Değer Giriniz: ')
degerInt = int(deger)
if degerInt <= 1:
    print(f"{degerInt}: sayısı asal değil")
else:
    # Asal sayı kontrolü
    x = degerInt - 1
    while x > 1:
        if degerInt % x == 0:
            print(f"{degerInt}: sayısı asal değil")
            break
        x -= 1
    else:
        print(f"{degerInt}: sayısı asal")