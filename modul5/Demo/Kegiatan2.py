import matplotlib.pyplot as plt
import numpy as np

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

harga_produk = list(map(lambda x: x[1], data_transaksi))
jumlah_terjual = list(map(lambda x: x[2], data_transaksi))

plt.scatter(harga_produk, jumlah_terjual, color='royalblue', label='Jumlah Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Terjual')
plt.title('Hubungan Harga Produk dan Jumlah Produk Terjual')
plt.legend()
plt.show()

pendapatan_produk = list(map(lambda item: item[1] * item[2], data_transaksi))

fig, ax = plt.subplots()
produk_labels = [item[0] for item in data_transaksi]
bar_chart = ax.bar(produk_labels, pendapatan_produk, color='steelblue', label='pendapatan')

plt.xlabel('Produk')
plt.ylabel('Pendapatan')
plt.title('Pendapatan Produk')
ax.legend()

# Menambahkan nilai pendapatan di atas setiap bar
for i, v in enumerate(pendapatan_produk):
    ax.text(i, v + 1, str(v), ha='center', va='bottom', color='dimgray')
    
plt.show()