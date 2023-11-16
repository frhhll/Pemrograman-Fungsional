expenses = [
{'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
{'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
{'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000}, ]

def add_expense(expenses):
    tanggal=input('Tanggal YY-MM-DD: ')
    deskripsi=input('Deskripsi: ')
    jumlah=int(input('Jumlah: '))
    expenses.append({'tanggal': tanggal, 'deskripsi': deskripsi, 'jumlah': jumlah})
    return expenses

def calculate_total_expenses(expenses):
    return sum(map(lambda x: x['jumlah'], expenses))

def get_expenses_by_date(expenses):
    tanggal = input('Tanggal yang dicari YY-MM-DD: ')
    list = [expense for expense in expenses if expense['tanggal'] == tanggal]
    return list

def generate_expenses_report(expenses):
    report = (f"Date: {expense['tanggal']}, Description: {expense['deskripsi']}, Amount: {expense['jumlah']}" for expense in expenses)
    return '\n'.join(report)

def display_menu():
    print("\n======= Aplikasi Pencatat Pengeluaran Harian =======")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")

def main():
    global expenses
    while True:
        display_menu()
        get_user_input = lambda command: int(input(command))
        choice = get_user_input("Pilih Menu : ")

        if choice == 1:
            add_expense(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            get_expenses_by_date(expenses)
            print("List Pengeluaran berdasarkan Tanggal")
            print(get_expenses_by_date(expenses))
        elif choice == 4:
            generate_expenses_report(expenses)
            print("Laporan Pengeluaran Harian")
            print(generate_expenses_report(expenses))
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")

if __name__ == '__main__':
    main()