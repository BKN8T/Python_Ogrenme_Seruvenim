#   RANGE

a = range( 10 )
print(a)
print(type(a))
print("a")

print()
##########################################

b = list(range(10))  
print(b)
print(type(b))
print("b")

print()
##########################################

c = [*range(10)] # ---> bu kullanım b ye göre daha iyi 
print(c)
print(type(c))
print("c")

print()
##########################################

d = [*range(1,10)] 
print(d)
print(type(d))
print("d")

print()
##########################################

e = [*range(5,10,2)] 
print(e)
print(type(e))
print("e")

print()
##########################################

f = [*range(-10, 0)]
print (f)
print (type (f))
print ("f")

print()
##########################################