import random

class Robot:
    def __init__(self, nama, serangan, hp, akurasi_serangan=0.8):
        self.nama = nama
        self.serangan = serangan
        self.hp = hp
        self.hp_max = hp
        self.akurasi_serangan = akurasi_serangan

    def serang_musuh(self, musuh):
        if random.random() < self.akurasi_serangan:
            kerusakan = self.serangan
            musuh.terima_serangan(kerusakan)
            print(f"{self.nama} menyerang {musuh.nama} dan menyebabkan kerusakan sebesar {kerusakan}!")
        else:
            print(f"Serangan {self.nama} meleset!")

    def terima_serangan(self, kerusakan):
        self.hp -= kerusakan
        if self.hp <= 0:
            print(f"{self.nama} telah dikalahkan!")
        else:
            print(f"{self.nama} menerima kerusakan sebesar {kerusakan}. HP {self.nama}: {self.hp}")

    def pulihkan_hp(self):
        self.hp = min(self.hp_max, self.hp + 10)  # Pulihkan 10 HP

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.putaran = 0

    def mulai_permainan(self):
        print("----- Permainan Dimulai -----")
        while self.robot1.hp > 0 and self.robot2.hp > 0:
            self.putaran += 1
            print(f"--- Putaran {self.putaran} ---")
            self.robot1.serang_musuh(self.robot2)
            if self.robot2.hp <= 0:
                break  # Robot 2 dikalahkan
            self.robot2.serang_musuh(self.robot1)
            if self.robot1.hp <= 0:
                break  # Robot 1 dikalahkan
            self.robot1.pulihkan_hp()
            self.robot2.pulihkan_hp()

        print("----- Permainan Berakhir -----")
        print(f"Total Putaran: {self.putaran}")
        if self.robot1.hp <= 0:
            print(f"{self.robot2.nama} menang!")
        elif self.robot2.hp <= 0:
            print(f"{self.robot1.nama} menang!")

# Contoh Penggunaan:
robot1 = Robot("Robot1", serangan=10, hp=200)
robot2 = Robot("Robot2", serangan=20, hp=140)

permainan = Game(robot1, robot2)
permainan.mulai_permainan()
