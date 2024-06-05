class hewan:
    def __init__(self, nama):
        self.nama = nama
        
    def suara(self):
        pass

class kucing(hewan):
    def suara(self):
        return('meow')
    
class anjing(hewan):
    def suara(self):
        return('guk guk')
    
class ayam(hewan):
    def suara(self):
        return('kukuruyuk')
    
kucing = kucing('momo')
anjing = anjing('doggo')
ayam = ayam('cocka')
    
print(f'{kucing.nama} bersuara {kucing.suara()}')
print(f'{anjing.nama} bersuara {anjing.suara()}')
print(f'{ayam.nama} bersuara {ayam.suara()}')

#return = mengembalikan nilai value
#class utama = baris 1 - 6
#sub class = baris 8 - 18