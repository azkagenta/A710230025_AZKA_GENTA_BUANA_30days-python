class Hewan:
    def _init_(self, jenis):
        self.jenis = jenis

class Kucing(Hewan):
    def _init_(self, jenis, warna):
        super()._init_(jenis)
        self.warna = warna

class Anjing(Hewan):
    def _init_(self, jenis, ras):
        super()._init_(jenis)
        self.ras = ras

class Singa(Hewan):
    def _init_(self, jenis, habitat):
        super()._init_(jenis)
        self.habitat =habitat  