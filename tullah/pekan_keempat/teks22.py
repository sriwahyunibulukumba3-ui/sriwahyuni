'''Latihan fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# Membuat header program
# os.system("cls")
# os.system("cls")   
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'_'*40:^40}")

# Mengambil input user
# LEBAR = int(input("Masukkan nilai lebar: "))
# PANJANG = int(input("Masukkan nilai panjang: "))

# program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG*LEBAR)

# tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header ():
    '''fungsi Header'''
    os.system("cls")
# os,system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int (input("masukkan nilai lebar: "))
    panjang = int(input("masukkan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar,panjang)

def display(massage,value):
    '''fungsi display'''
    print(f"hasil perhitungan {massage} = {value})")


# program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)
    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("program selesai, terima kasih")