import requests
import json
from collections import Counter

class SucRaporu ():


    def __init__(self,bolge , tarih , suc_tipi ="all-crime"):
        self.bolge = bolge
        self.tarih = tarih
        self.suc_tipi = suc_tipi
        self.suclar = self.suclari_bul()

    def suclari_bul (self):
        crime_categories_URL ="https://data.police.uk/api/crimes-no-location"
        payload = {
            "category":self.suc_tipi,
            "date":self.tarih,
            "force":self.bolge  
            }
        response = requests.get(crime_categories_URL, params=payload)
        

        if response.status_code == 200:
            return response.json()
        else:
            return None
        
    def sucları_raporla (self):
        suclarListesi = [ ]
        if self.suclar is not None:
            for suc in self.suclar:
                suclarListesi.append(suc["category"])
            return Counter(suclarListesi)
            


sr = SucRaporu("leicestershire","2024-01",)
print(sr.sucları_raporla())
