class kendaraan:
    roda = 0
    kecepatan = 0
    cc = 0

    #constructor
    def __init__(self):
        total = 0
        for i in range(10):
            total += i
        self.roda = total + 20
    
    def nyala(self):
        print('brum brum')

    def maju(self):
        if self.roda > 0:
            self.kecepatan = self.kecepatan + 10
    
    def mundur(self):
        pass

#inheritance (pewarisan)
class Motor(kendaraan):
    pass

m1 = Motor()
m1.nyala()
m1.roda = 3
print(m1.roda)