print("=== MESIN KOENVERSI WAKTU===")   
# Meminta input
jam = float(input("Masukkan jumlah waktu dalam jam (contoh 1,5): "))
#proses matematika
# 1 Jam = 60 Menit, 1 menit = 60 detik, 1 Jam = 3600 detik
menit = jam * 60
detik = jam * 3600
# output
print("\n--- HASIL KONVERSI ---")
print(f"Waktu yang Anda masukkan:{jam} Jam")
print(f"setara dengan : {menit} menit")
print(f"setara dengan : {detik} detik")