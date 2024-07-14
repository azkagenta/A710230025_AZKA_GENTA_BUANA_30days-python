class Manusia:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Pelajar(Manusia):
    def _init_(self, nama, umur, kelas):
        super()._init_(nama, umur)
        self.kelas = kelas

    def info(self):
        super().info()
        print(f"Kelas: {self.kelas}")