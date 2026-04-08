# Variabel adalah tempat menyimpam Data

# Menaruh / assigment nilai

a = 10
x = 5
panjang = 1000

print(a)

# Pemanggilan pertama
Print("Nilai a = ", a)
print("Nilai x ", x)
print("Nilai panjang = ", panjang)

# penamaan
nilai_y = 15 # dengan menggunakan undescore
juta10 = 100000 # ini boleh
nilaiz = 17.5 # ini boleh

# pemanggilan kedua
print("Nilai a ", a)
a = 7
print("Nilai a = " a)

# asignment indirect
b = a
print ("Nilai a = ", a)



### Tipe Data

# a = 10, a adalah variabel dengan nilai 10

# tipe data: Angka satuan (integer)
# koma nya (integer)
data_integer = 11
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

#tipe data: angka dengan koma (float)
print("data ;, data_float")
data_float = 1.5
print("- bertipe : ", type(data_float))

# tipe data: kumpulan karakter (string)
data_string = "ucup"
print("data : ", type(data_sring))

# tipe data: biner true/false (boolean)
data_bool = false
print("data : data_bool")
print("- bertipe :, type(data_bool)")

## Tipe data khusus

# bilangan kompleks
data_complex(5,6)
print("data :, data_complex")
print("- bertipe : ", type9data_complex")

# tipe data dari bahasa C
# 
from ctypes import c_double, C_char, C_long

data_c_double = c_double(10.5)
print("data_c_double")
print("- bertipe : ", type(data_c_double))
        