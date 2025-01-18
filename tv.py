class Show:
    def __init__(self, title, genre, time):
        self.title = title
        self.genre = genre
        self.time = time

    def __str__(self):
        return f"{self.time} - {self.title} ({self.genre})"

class TVSchedule:
    def __init__(self):
        self.schedule = []

    def add_show(self, title, genre, time):
        new_show = Show(title, genre, time)
        self.schedule.append(new_show)
        print(f"Acara '{title}' berhasil ditambahkan!")

    def view_schedule(self):
        if not self.schedule:
            print("\nJadwal televisi kosong. Tambahkan acara terlebih dahulu!\n")
        else:
            print("\nJadwal Televisi:\n----------------")
            for show in self.schedule:
                print(show)

    def search_by_genre(self, genre):
        result = [show for show in self.schedule if show.genre.lower() == genre.lower()]
        if result:
            print(f"\nAcara dengan genre '{genre}':\n----------------")
            for show in result:
                print(show)
        else:
            print(f"\nTidak ada acara dengan genre '{genre}'.\n")

    def search_by_time(self, time):
        result = [show for show in self.schedule if show.time == time]
        if result:
            print(f"\nAcara pada jam '{time}':\n----------------")
            for show in result:
                print(show)
        else:
            print(f"\nTidak ada acara pada jam '{time}'.\n")

    def remove_show(self, title):
        for show in self.schedule:
            if show.title.lower() == title.lower():
                self.schedule.remove(show)
                print(f"Acara '{title}' berhasil dihapus.")
                return
        print(f"Acara dengan judul '{title}' tidak ditemukan.")


def main():
    tv_schedule = TVSchedule()

    while True:
        print("\n========== Jadwal Televisi ==========")
        print("1. Tambah Acara")
        print("2. Lihat Jadwal")
        print("3. Cari Acara berdasarkan Genre")
        print("4. Cari Acara berdasarkan Jam")
        print("5. Hapus Acara")
        print("6. Keluar")
        
        choice = input("\nMasukkan pilihan Anda: ")
        
        if choice == '1':
            title = input("Masukkan judul acara: ")
            genre = input("Masukkan genre acara: ")
            time = input("Masukkan waktu acara (hh:mm): ")
            tv_schedule.add_show(title, genre, time)
        elif choice == '2':
            tv_schedule.view_schedule()
        elif choice == '3':
            genre = input("Masukkan genre yang ingin dicari: ")
            tv_schedule.search_by_genre(genre)
        elif choice == '4':
            time = input("Masukkan waktu yang ingin dicari (hh:mm): ")
            tv_schedule.search_by_time(time)
        elif choice == '5':
            title = input("Masukkan judul acara yang ingin dihapus: ")
            tv_schedule.remove_show(title)
        elif choice == '6':
            print("\nTerima kasih telah menggunakan aplikasi Jadwal Televisi!")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
