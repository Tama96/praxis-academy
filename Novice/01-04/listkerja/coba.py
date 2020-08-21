def sapa (nama) :
    print ("Halo" + nama + "Selamat Pagi!")
sapa('Joko')

def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))