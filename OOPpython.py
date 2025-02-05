from datetime import datetime

# Class Parent
class Toko:
    def __init__(self, title, publication_date, pages, rating, additional_info=None):
        self.title = title  # String
        self.publication_date = datetime.strptime(publication_date, "%Y-%m-%d")  # Date
        self.pages = pages  # Integer
        self.rating = rating  # Float
        self.additional_info = additional_info if additional_info else {}  # Dictionary
    
    def display_info(self):
        print(f"\nJudul: {self.title}")
        print(f"Tanggal Terbit: {self.publication_date.strftime('%d-%m-%Y')}")
        print(f"Jumlah Halaman: {self.pages}")
        print(f"Rating: {self.rating}")
        print(f"Informasi Tambahan: {self.additional_info}")

# Class Child 1
class Buku(Toko):
    def __init__(self, title, publication_date, pages, rating, author):
        additional_info = {"Penulis": author}  
        super().__init__(title, publication_date, pages, rating, additional_info)

# Class Child 2
class Majalah(Toko):
    def __init__(self, title, publication_date, pages, rating, editionNumber):
        additional_info = {"Nomor Edisi": editionNumber}  
        super().__init__(title, publication_date, pages, rating, additional_info)

# Class Child 3
class Koran(Toko):
    def __init__(self, title, publication_date, pages, rating, publisher):
        additional_info = {"Penerbit": publisher}  
        super().__init__(title, publication_date, pages, rating, additional_info)

# Class TokoManager
class TokoManager:
    def __init__(self):
        self.items = []  # Menyimpan daftar objek Buku, Majalah, Koran

    def add_item(self):
        print("\nTambah Item:")
        title = input("Judul: ")
        publication_date = input("Tanggal Terbit (YYYY-MM-DD): ")
        pages = int(input("Jumlah Halaman: "))
        rating = float(input("Rating (1.0 - 5.0): "))

        print("Pilih Jenis Item: 1. Buku, 2. Majalah, 3. Koran")
        choice = input("Pilihan: ")

        if choice == "1":
            author = input("Penulis: ")
            self.items.append(Buku(title, publication_date, pages, rating, author))
        elif choice == "2":
            editionNumber = input("Nomor Edisi: ")
            self.items.append(Majalah(title, publication_date, pages, rating, editionNumber))
        elif choice == "3":
            publisher = input("Penerbit: ")
            self.items.append(Koran(title, publication_date, pages, rating, publisher))
        else:
            print("Pilihan tidak valid!")

    def delete_item(self):
        title = input("\nMasukkan judul item yang ingin dihapus: ")
        for i, item in enumerate(self.items):
            if item.title == title:
                self.items.pop(i)
                print("Item berhasil dihapus!\n")
                return
        print("Item tidak ditemukan!\n")

    def display_all_items(self):
        print("\n=== DAFTAR BUKU ===")
        for item in self.items:
            if isinstance(item, Buku):
                item.display_info()
        
        print("\n=== DAFTAR MAJALAH ===")
        for item in self.items:
            if isinstance(item, Majalah):
                item.display_info()
        
        print("\n=== DAFTAR KORAN ===")
        for item in self.items:
            if isinstance(item, Koran):
                item.display_info()

# main
def main():
    toko_manager = TokoManager()

    while True:
        print("\n=== Toko ===")
        print("1. Tambah Item")
        print("2. Hapus Item")
        print("3. Lihat Semua Item")
        print("4. Keluar")
        
        choice = input("Pilihan Anda: ")

        if choice == "1":
            toko_manager.add_item()
        elif choice == "2":
            toko_manager.delete_item()
        elif choice == "3":
            toko_manager.display_all_items()
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
