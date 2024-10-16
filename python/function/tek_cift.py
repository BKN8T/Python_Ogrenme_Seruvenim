def uyg():
    girdi = int(input("Bir sayı giriniz: "))
    islem = input("Veri tek mi çift mi? c/t : ")
    
    if islem == "c" or islem == "C" or islem == "ç" or islem == "Ç":
        if girdi%2==0:
            return f"Girilen sayı: ({girdi}) çift bir sayıdır\nDoğru Bildin!!"
        elif girdi%2!=0:
            return f"Girilen sayı: ({girdi}) tek bir sayıdır\nYanlış bildin!!"
        else:
            print("ne yaptın la")
   
    elif islem =="t" or islem=="T" :
        if girdi%2==1:
            return f"Girilen sayı: ({girdi}) tek bir sayıdır\nDoğru Bildin!!"
        elif girdi%2!=1:
            return f"Girilen sayı: ({girdi}) çift bir sayıdır\nYanlış bildin!!"
    else:
        return "Ne yaptın LA"
     
        
print(uyg())
