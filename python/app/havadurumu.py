import requests
import json

class HavaDurumu:
    def __init__(self, sehir, api_key):
        self.sehir = sehir
        self.api_key = api_key
        self.veri = self.hava_durumu_al()

    def hava_durumu_al(self):

        base_url = "http://api.weatherapi.com/v1/current.json"
        params = {
            "key": self.api_key,
            "q": self.sehir,
            "aqi": "no"  # Hava kalitesi bilgisi gerekmediği için "no" dedik
        }
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            print(json.dumps(response.json(), indent=4))  # Veriyi daha rahat görmek için
            return response.json()
        else:
            print("Veri alınamadı:", response.status_code)
            return None

    def sicaklik_bilgisi(self):
        
        if self.veri:
            sicaklik = self.veri["current"]["temp_c"]
            return f"{self.sehir} şehrinde güncel sıcaklık: {sicaklik}°C"
        else:
            return "Sıcaklık bilgisi bulunamadı."

    def hissedilen_sicaklik(self):

        if self.veri:
            hissedilen_sicaklik = self.veri["current"]["feelslike_c"]
            return f"Hissedilen sıcaklık: {hissedilen_sicaklik}°C"
        else:
            return "Hissedilen sıcaklık bilgisi bulunamadı."

    def hava_kosullari(self):

        if self.veri:
            durum = self.veri["current"]["condition"]["text"]
            return f"Hava durumu: {durum}"
        else:
            return "Hava durumu bilgisi bulunamadı."


sehir = "Istanbul"
api_key = "a0c5250551ab40e6acb205636241111"  # Buraya kendi WeatherAPI anahtarını gir

hava = HavaDurumu(sehir, api_key)
print(hava.sicaklik_bilgisi())
print(hava.hissedilen_sicaklik())
print(hava.hava_kosullari())