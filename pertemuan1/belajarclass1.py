class manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def sapa(self):
        print(f'Halo, nama saya {self.nama}')
    
    def lahir(self):
        print(f'saya lahir di tahun : {2024-self.umur}')  

andhika = manusia('andhika', 19)
kurniawan = manusia('kurniawan', 19)

andhika.sapa()
andhika.lahir()
