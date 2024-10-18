import math

def HataKodlari():

    # SyntaxError örneği
    try:
        eval("5 + ")  # Eksik ifade nedeniyle SyntaxError
    except SyntaxError:
        print("SyntaxError: Geçersiz sözdizimi!")

    # TypeError örneği
    try:
        print(5 + "a")  # Sayı ile string toplanamaz
    except TypeError:
        print("TypeError: Farklı veri tiplerini birleştiremezsiniz!")
    
    # IndexError örneği
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Liste 3 elemanlı ancak 5. indeks yok
    except IndexError:
        print("IndexError: Liste dışındaki bir indekse erişmeye çalıştınız!")
    
    # KeyError örneği
    try:
        my_dict = {'ad': 'Berk'}
        print(my_dict['yaş'])  # 'yaş' anahtarı yok
    except KeyError:
        print("KeyError: Sözlükte bu anahtar mevcut değil!")

    # ValueError örneği
    try:
        int("abc")  # String'in sayıya çevrilememesi durumu
    except ValueError:
        print("ValueError: Geçersiz değer tipi!")

    # ZeroDivisionError örneği
    try:
        result = 10 / 0  # Sıfıra bölme
    except ZeroDivisionError:
        print("ZeroDivisionError: Bir sayı sıfıra bölünemez!")

    # AttributeError örneği
    try:
        "hello".foo()  # String nesnesinin foo() metodu yok
    except AttributeError:
        print("AttributeError: Nesnenin böyle bir özelliği/metodu yok!")

    # FileNotFoundError örneği
    try:
        with open("olmayan_dosya.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("FileNotFoundError: Dosya bulunamadı!")

    # ImportError örneği
    try:
        import nonexistent_module  # Bu isimde bir modül yok
    except ImportError:
        print("ImportError: Modül bulunamadı!")

    # NameError örneği
    try:
        print(undefined_variable)  # undefined_variable tanımlı değil
    except NameError:
        print("NameError: Değişken tanımlı değil!")

    # OverflowError örneği
    try:
        print(math.exp(1000))  # Sonuç aşırı büyük
    except OverflowError:
        print("OverflowError: Sayısal sonuç aşırı büyük!")

    # MemoryError örneği (bu kod küçük sistemlerde hata verebilir)
    try:
        big_list = [1] * (10**10)  # Çok büyük bir liste oluşturma
    except MemoryError:
        print("MemoryError: Bellek doldu!")

    # RuntimeError örneği
    try:
        raise RuntimeError("Bu bir runtime hatasıdır!")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")

    # IndentationError: Beklenmedik girinti hatası
    try:
        eval('def func():\nprint("Merhaba")')  # Eksik girinti
    except IndentationError:
        print("IndentationError: Girinti hatası!")

HataKodlari()