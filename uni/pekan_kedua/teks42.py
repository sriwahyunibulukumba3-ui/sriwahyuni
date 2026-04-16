# latihan pengulangan membuat segitiga

sisi = 10

# 1. Menggunakan For

# dummy variable
count = 1
for i in range(4):
    print("*"*count)
    count += 1

# 2. Menggunakan while

count = 1
while True:
    print("*"*count)
    count += 1

    print("akhir dari for")
    if count > sisi:
        break

print("akhier white")

# 3. hanya ganjil saja

print("awal while")
count = 1
spasi = int(sisi/2)

while True:
    if (count%2):
        #  print jika ganjil
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue

    # akan break jika count melebihii sisi
    if count > sisi:
        break

print ("akhier white")
