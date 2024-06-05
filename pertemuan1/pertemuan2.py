#class utama
class kendaraan:
    def __init__(self, nama, warna, harga):
        self.nama = nama
        self.warna = warna
        self.harga = harga
        
    def tampilkan(self):
            print("Rincian: ", self.nama, self.warna, self.harga)
            
    def kecepatanmaxprtama(self):
            print("Kecepatan maximum kendaraan: ", self.nama, "adalah 150km/jam")
            
    def gantigearpertama(self):
            print("Gantigear maximum kendaraan adalah sampai 6")

#childern class            
class Mobil(kendaraan):
    def kecepatanmaxkedua(self):
        print("Kecepatan maximum kendaraan: ", self.nama, "adalah 200km/jam")
        
    def gantigearkedua(self):
        print("Kecepatan maximum kendaraan adalah sampai 7")

#memanggil fungsi dari parent class kendaraan        
Avanza = Mobil("Avanza", "Putih", 20000000)
Avanza.tampilkan()
Avanza.kecepatanmaxprtama()
Avanza.gantigearpertama()

#memanggil fungsi dari parent class kendaraan dan children class mobil 
jeep = Mobil("Jeep", "Coklat", 30000000)
jeep.tampilkan()
jeep.kecepatanmaxkedua()
jeep.gantigearkedua()
