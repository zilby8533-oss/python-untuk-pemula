class Siswa:
    def __init__(self, nama, nis):
        self.nama = nama
        self.nis = nis
    def perkenalan(self):
        return f"Saya {self.nama}, NIS {self.nis}"

s = Siswa("Farhan", 105850925)
print(s.perkenalan())
