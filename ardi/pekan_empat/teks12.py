''' Fungsi dengan argument (input)'''

# Template
# def nama_fungsi(argument)
#     Badan fungsi


def hellow_world(nama):
    '''fungsi hellow world menerima input dengan variable'''
    print(f"selamat datang dunia wahai{nama}")


hellow_world("ucup")  

# program tambah


def tambah(angka_1,angka_2):
    '''fungsi tambah'''
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    '''fungsi say hi'''
    data_peserta = list_peserta.copy()
    for peserta in data_peserta:
        print(f"Yang terhormat {peserta}")

anggota_boyband = ["ucup","otong","dudung"]

say_hi(anggota_boyband)
