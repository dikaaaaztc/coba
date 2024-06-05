#class utama
class manusia:
    def __init__(self, nama, pekerjaan, umur):
        self.nama = nama
        self.pekerjaan = pekerjaan
        self.umur = umur
        
    def tampilkan(self):
            print("Nama saya adalah:", self.nama, "Berusia", self.umur)
            
    def pekerjaansatu(self):
            print("Pekerjaan saya adalah:", self.pekerjaan)
            
    def petugassatu(self):
            print("Saya bertugas menjaga pertahanan Negara")

#childern class            
class peranan(manusia):
    def pekerjaandua(self):
            print("Pekerjaan saya adalah:", self.pekerjaan)
            
    def petugasdua(self):
            print("Saya bertugas memeriksa orang sakit")
            
    def pekerjaantiga(self):
            print("Pekerjaan saya adalah:", self.pekerjaan)
            
    def petugastiga(self):
            print("Saya bertugas memproduksi bahan pangan negara")



#memanggil fungsi dari parent class kendaraan        
manusia1 = peranan("budi", "tenatara", 30)
manusia1.tampilkan()
manusia1.pekerjaansatu()
manusia1.petugassatu()
print()
#memanggil fungsi dari parent class kendaraan dan children class mobil 
manusia2 = peranan("supri", "dokter", 27)
manusia2.tampilkan()
manusia2.pekerjaandua()
manusia2.petugasdua()
print()
manusia3 = peranan("balmon", "petani", 36)
manusia3.tampilkan()
manusia3.pekerjaantiga()
manusia3.petugastiga()
