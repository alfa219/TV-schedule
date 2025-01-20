# TV Schedule Management Program

Program ini adalah aplikasi berbasis terminal untuk mengelola jadwal acara televisi. Dengan menggunakan program ini, pengguna dapat:

1. Menambah acara ke dalam jadwal.
2. Melihat daftar acara yang sudah terjadwal.
3. Mencari acara berdasarkan genre.
4. Mencari acara berdasarkan waktu.
5. Menghapus acara dari jadwal.

Program ini dirancang menggunakan berbagai konsep pemrograman seperti percabangan, perulangan, fungsi, list, string, dan Object-Oriented Programming (OOP).

---

## Fitur Utama

1. **Tambah Acara**
   - Pengguna dapat menambahkan judul acara, genre, dan waktu acara.

2. **Lihat Jadwal**
   - Menampilkan semua acara yang sudah ditambahkan ke jadwal. Jika jadwal kosong, akan muncul pesan pemberitahuan.

3. **Cari Acara Berdasarkan Genre**
   - Mengambil daftar acara yang sesuai dengan genre yang dimasukkan pengguna.

4. **Cari Acara Berdasarkan Waktu**
   - Menampilkan acara yang dijadwalkan pada waktu tertentu.

5. **Hapus Acara**
   - Menghapus acara dari jadwal berdasarkan judul acara.

---

## Cara Menggunakan Program

1. Jalankan program dengan perintah:
   ```bash
   python TV_schedule.py
   ```

2. Pilih opsi yang tersedia di menu utama:
   - **1** untuk menambah acara.
   - **2** untuk melihat jadwal.
   - **3** untuk mencari acara berdasarkan genre.
   - **4** untuk mencari acara berdasarkan waktu.
   - **5** untuk menghapus acara.
   - **6** untuk keluar dari program.

3. Masukkan input yang diminta sesuai dengan instruksi pada terminal.

4. Program akan memberikan umpan balik setelah setiap tindakan.

---

## Konsep Pemrograman yang Digunakan

### 1. Percabangan
- Program menggunakan struktur if-elif-else untuk menangani berbagai pilihan menu.
- Contoh:
  ```python
  if choice == '1':
      title = input("Masukkan judul acara: ")
      genre = input("Masukkan genre acara: ")
      time = input("Masukkan waktu acara (hh:mm): ")
      tv_schedule.add_show(title, genre, time)
  elif choice == '2':
      tv_schedule.view_schedule()
  ```

### 2. Perulangan
- Menggunakan perulangan while untuk menjalankan menu utama hingga pengguna memilih untuk keluar.
- Contoh:
  ```python
  while True:
      print("\n========== Jadwal Televisi ==========")
      ...
      choice = input("\nMasukkan pilihan Anda: ")
      if choice == '6':
          break
  ```

### 3. function 
- Fungsi digunakan untuk memisahkan logika program menjadi bagian-bagian modular.
- Contoh:
  ```python
  def add_show(self, title, genre, time):
      new_show = Show(title, genre, time)
      self.schedule.append(new_show)
      print(f"Acara '{title}' berhasil ditambahkan!")
  ```

### 4. List
- Program menyimpan daftar acara dalam atribut `self.schedule` yang berupa list.
- Contoh:
  ```python
  self.schedule.append(new_show)
  ```

### 5. String
- Manipulasi string dilakukan untuk membandingkan genre atau judul acara secara case-insensitive.
- Contoh:
  ```python
  result = [show for show in self.schedule if show.genre.lower() == genre.lower()]
  ```

### 6. Object-Oriented Programming (OOP)
- Program menggunakan kelas `Show` dan `TVSchedule` untuk merepresentasikan acara televisi dan jadwalnya.
- Contoh:
  ```python
  class Show:
      def __init__(self, title, genre, time):
          self.title = title
          self.genre = genre
          self.time = time

      def __str__(self):
          return f"{self.time} - {self.title} ({self.genre})"
  ```

---

## Contoh Penggunaan

### Menambahkan Acara
```text
========== Jadwal Televisi ==========
1. Tambah Acara
...
Masukkan pilihan Anda: 1
Masukkan judul acara: Drama Malam
Masukkan genre acara: Drama
Masukkan waktu acara (hh:mm): 20:00
Acara 'Drama Malam' berhasil ditambahkan!
```

### Melihat Jadwal
```text
========== Jadwal Televisi ==========
2. Lihat Jadwal
...
Jadwal Televisi:
----------------
20:00 - Drama Malam (Drama)
```

### Mencari Berdasarkan Genre
```text
Masukkan genre yang ingin dicari: Drama
Acara dengan genre 'Drama':
----------------
20:00 - Drama Malam (Drama)
```

---

Program ini memberikan contoh implementasi yang baik dari konsep OOP dan struktur data dalam Python. Dengan fitur yang modular, program ini mudah dipahami, dimodifikasi, dan dikembangkan lebih lanjut sesuai kebutuhan pengguna.

