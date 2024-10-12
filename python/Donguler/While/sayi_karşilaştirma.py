while True:
    a = input("A değeri giriniz: ")
    b = input("B değeri giriniz: ")

    try:
        aInt = int(a)
        bInt = int(b)
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz!")
        break

    if aInt == bInt:
        print(f"{aInt} = {bInt}")
        break
    elif aInt > bInt:
        print(f"{aInt} > {bInt}")
        break
    else:
        print(f"{aInt} < {bInt}")
        break


