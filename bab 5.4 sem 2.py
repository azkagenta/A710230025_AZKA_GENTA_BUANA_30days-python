class Kendaraan:
    def _init_(self, jenis):
        self.jenis = jenis

class Sepeda(Kendaraan):
     def _init_(self, jenis, warna):
        super()._init_(jenis)
        self.warna = warna

class SepedaMotor(Sepeda):
    def _init_(self, jenis, warna, merk):
        super()._init_(jenis, warna)
        self.merk=merk