nama = ['adi', 'uda', 'uni']
print(nama)
for data in nama:
    print(data)
print(nama[1])
print(nama[-1])
print (nama + ['wewe', 'wowo', 'wiwi'])

a = ['a', 'b', 'c', 'd']
n = [1,2,3]
x = [a,n]
print (x)
print (x[1])
print (x[1][0])

a,b = 0,1
while a < 10:
    print(a)
    a,b = b, a+b
