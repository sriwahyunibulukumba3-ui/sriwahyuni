print("===  MESIN HITUNG DISKON ===")

# Meminta input
harga_asli = int(input("masukan presentasi diskon (contoh 20 untuk untuk 20%):"))

# proses matematika
potongan = harga_asli * ( 20 / 100)
harga_akhir = harga_asli - potongan

# output
print("\n--- STRUK PEMBAYARAN ---")
print(f"Harga Awal      : Rp {100000}")
print(f"Diskon {20} %   : Rp {int(20)}")
print(f"total bayar     : Rp {int(80000)}")