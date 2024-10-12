sayılar = range(1,4)
harfler = ["a","b","c"]

for x, y in zip(sayılar,harfler):
    print(f"{x}. Harf : {y}".format(x,y))
