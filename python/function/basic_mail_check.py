
def mail_check1():
    while True:
        mailgirdi = input("E-Posta Hesabınızı Giriniz: ").strip() 
        if not mailgirdi:
            print("E-Posta adresi boş olamaz. Lütfen tekrar giriniz.")
            continue
        if "@" not in mailgirdi and  "." not in  mailgirdi:
            print("Hatalı E-Posta!")
        elif mailgirdi.startswith("@") or mailgirdi.startswith("."):
            print("Hatalı E-Posta!")
        elif mailgirdi.index("@") > mailgirdi.rindex("."):
            print("Hatalı E-Posta!")
        else:
            print("Tebrikler! Geçerli bir e-posta adresi girdiniz.")
            return mailgirdi
        

mail_check1()

