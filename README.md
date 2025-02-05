# OOP-python

## 📄 Laporan OOP - Python

*Muhammad Alvino*

---

##  1. Konsep 
![concept](https://github.com/user-attachments/assets/5a4364d4-7ac1-4694-89ee-26e206437200)

Konsep ini menunjukkan struktur pewarisan dalam OOP, di mana "Toko" berperan sebagai parent class dan "Buku", "Majalah", serta "Koran" sebagai child class yang mewarisi atributnya. 

---

## 2. Class Diagram
![Class](https://github.com/user-attachments/assets/fae1198a-6761-412d-85dd-277df2d8f770)

penerapan prinsip pewarisan (inheritance) dalam pemrograman berorientasi objek (OOP).

- Toko menyediakan atribut dan metode dasar yang digunakan oleh semua jenis item.
- Buku, Majalah, dan Koran menambahkan atribut spesifiknya masing-masing.
- TokoManager berfungsi untuk mengelola daftar item.

###  *Struktur Kelas*
💠 *Kelas Toko* (Superclass)
- *Atribut:*
  - title: String → Menyimpan judul buku/majalah/koran.
  - PublicationDate: Date → Menyimpan tanggal terbit dalam format tanggal.
  - pages: Integer → Menyimpan jumlah halaman.
  - rating: Float → Menyimpan rating item.
  - additionalInfo: Dict → Menyimpan informasi tambahan dalam bentuk dictionary.

###  *Subclass Toko*
#### ⿡ *Kelas Buku*
- *Tambahan Atribut:*
  - author: String → Menyimpan nama penulis buku
- *Modifikasi:*
  - display_info() → Menampilkan informasi buku
  
#### ⿢ *Kelas Majalah*
- *Tambahan Atribut:*
  - editionNumber: String → Menyimpan nomor edisi majalah
- *Modifikasi:*
  - display_info() → Menampilkan informasi majalah

#### ⿣ *Kelas Koran*
- *Tambahan Atribut:*
  - publisher: String → Menyimpan nama penerbit koran
- *Modifikasi:*
  - display_info() → Menampilkan informasi koran

---

## 3. Usecase Diagram
![usecase](https://github.com/user-attachments/assets/554e19bb-ee00-441f-bcda-80c4dffdc6e6)

Use case diagram di atas menggambarkan interaksi antara aktor Admin dengan sistem yang memiliki empat fungsi utama, yaitu:
- Tambah Item : Admin dapat menambahkan item baru ke dalam sistem.
- Delete Item : Admin memiliki akses untuk menghapus item yang sudah ada dalam sistem.
- Display Item : Admin dapat menampilkan daftar item yang tersedia di dalam sistem.
- Keluar Program : Admin memiliki opsi untuk keluar dari sistem atau menutup aplikasi.

---

## 4. Sequence Diagram
![sequence](https://github.com/user-attachments/assets/5f33ade9-2444-48a1-9aa1-0192a98fe3cf)

interaksi antara tiga entitas utama: Admin, Sistem, dan Item dalam suatu proses manajemen item
- Pilih Menu : Admin memilih menu yang tersedia dalam sistem
- Tambah Item : Admin mengirimkan permintaan untuk menambahkan item baru ke sistem
- Hapus Item : Admin mengirim permintaan untuk menghapus item tertentu
- Lihat Semua : Admin meminta untuk melihat semua item yang tersedia dalam sistem
- Menampilkan Info :  Sistem mengirimkan semua informasi item yang diperoleh ke Admin

