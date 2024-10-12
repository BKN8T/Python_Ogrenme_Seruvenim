isimler = ["Furkan Berk Budağ", "Ahmet Yılmaz","Elif Demir","Canan Kara",]
isimSayisi = len(isimler)

sıfır = 0 

for dongu in isimler : 
    sıfır += 1 
    parcalar = dongu.split()

    if len(parcalar)== 3 :
        ad = parcalar[0] + " "+ parcalar[1]
        soyisim = parcalar[2]
    elif len(parcalar)== 2 :
        ad = parcalar[0]
        soyisim= parcalar[1]
    else:
        print("Ne yaptın la :D")


    print(f"{sıfır}: İsim: {ad} Soyİsim:{soyisim} ")
    