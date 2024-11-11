import requests
from PIL import Image
from io import BytesIO

# Grafik URL'sini ve temel parametreleri belirle
base_url = "https://image-charts.com/chart"

def grafik_parametrelerini_ayarla():
    """
    Kullanıcıdan grafik türü, veri ve boyut bilgilerini alır.
    """
    print("Grafik Türleri:")
    print("bvg: Çubuk Grafik")
    print("lc: Çizgi Grafik")
    print("p3: Pasta Grafik")

    grafik_turu = input("Grafik türünü gir (Örneğin: bvg): ")
    veri = input("Grafik verilerini virgülle ayırarak gir (Örn: 10,20,30): ")
    boyut = input("Grafik boyutunu gir (Örn: 700x400): ")
    
    return {
        "cht": grafik_turu,  # Grafik türü
        "chd": f"t:{veri}",   # Veri
        "chs": boyut          # Boyut
    }

def grafik_url_olustur(base_url, params):

    response = requests.get(base_url, params=params)
    return response.url

def grafik_goster(url):

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def yardim():

    print("\nYardım Menüsü:")
    print("1. Grafik Türleri: 'bvg', 'lc', 'p3' gibi türler seçilebilir.")
    print("2. Veri: Grafik üzerinde gösterilecek verileri virgülle ayırarak girin.")
    print("3. Grafik Boyutu: Grafik boyutunu '700x400' gibi belirleyebilirsiniz.")
    print("4. Yardım: Bu menüde grafikle ilgili genel bilgi ve açıklamalar bulunur.")

# Ana Program
if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Grafik Oluştur")
        print("2. Yardım Menüsünü Göster")
        print("3. Çıkış")

        secim = input("Bir seçenek girin: ")

        if secim == "1":
            params = grafik_parametrelerini_ayarla()
            grafik_url = grafik_url_olustur(base_url, params)
            print("Grafiğinizin URL'si:", grafik_url)
            grafik_goster(grafik_url)
        elif secim == "2":
            yardim()
        elif secim == "3":
            print("Çıkıyor...")
            break
        else:
            print("Geçersiz seçenek, tekrar deneyin.")