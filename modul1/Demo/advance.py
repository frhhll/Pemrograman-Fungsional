__author__ = "FarhanHilal"

data_buku = []
peminjaman_buku = {}

def tambah_buku():
    print("------------------------")
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    kategori = input("Masukkan kategori buku: ")
    data_buku.append((judul, penulis, kategori))
    print("Buku berhasil ditambahkan.")


def tampilkan_daftar_buku():
    print("\nDaftar Buku Tersedia:")
    for i, buku in enumerate(data_buku):
        print(f"{i + 1}. Judul: {buku[0]}\n Penulis: {buku[1]}\n Kategori: {buku[2]}\n")


def pinjam_buku(username):
    tampilkan_daftar_buku()
    pilihan = int(input("\nPilih buku yang ingin dipinjam (nomor): ")) - 1

    if 0 <= pilihan < len(data_buku):
        buku_dipinjam = data_buku[pilihan]
        if not cek_peminjaman(buku_dipinjam):
            peminjaman_buku[username] = buku_dipinjam
            # Formatted string
            print(
                f"Buku '{buku_dipinjam[0]}' berhasil dipinjam oleh {username}.")
        else:
            print("Buku ini sudah dipinjam oleh pengguna lain.")
    else:
        print("Nomor buku yang anda input tidak valid.")


def kembalikan_buku(username):
    if username in peminjaman_buku:
        buku_dikembalikan = peminjaman_buku.pop(username)
        # Formatted string
        print(
            f"Buku '{buku_dikembalikan[0]}' berhasil dikembalikan oleh {username}.")
    else:
        print("Anda tidak memiliki buku yang sedang dipinjam.")


def cek_peminjaman(buku):
    for user, peminjaman in peminjaman_buku.items():
        if peminjaman == buku:
            return True
    return False

db_admin = {"admin1": "1234", "admin2": "5678"}
db_user = {"farhan": "8765", "ellen": "4321"}

def menu_admin():
    while True:
        print("\nMenu Admin:")
        print("------------------------")
        print("1. Tambah Buku")
        print("2. Kembali ke Menu Utama")

        admin_pilihan = input("Pilih menu admin: ")

        if admin_pilihan == "1":
            tambah_buku()
        elif admin_pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_user(username):
    while True:
        print("\nMenu User:")
        print("------------------------")
        print("1. Pinjam Buku")
        print("2. Kembalikan Buku")
        print("3. Kembali ke Menu Utama")

        user_pilihan = input("Pilih menu user: ")

        if user_pilihan == "1":
            pinjam_buku(username)
        elif user_pilihan == "2":
            kembalikan_buku(username)
        elif user_pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_utama():
    while True:
        print("\nMenu Utama:")
        print("----------------------")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Keluar")

        akun = input("Masukkan jenis akun: ").lower()

        if akun == "1":
            # Validasi akun admin
            print("----------------------")
            username = input("Masukkan nama pengguna: ")
            password = input("Masukkan password: ")
            if db_admin.get(username) == password:
                menu_admin()
            else:
                print("Akun admin anda tidak valid.")
        elif akun == "2":
            # Validasi akun pengguna
            print("----------------------")
            username = input("Masukkan nama pengguna: ")
            password = input("Masukkan password: ")
            if db_user.get(username) == password:
                menu_user(username)
            else:
                print("Akun user anda tidak valid.")
        elif akun == "keluar":
            break
        else:
            print("Akun tidak valid. Silakan coba lagi.")


# Main
menu_utama()
