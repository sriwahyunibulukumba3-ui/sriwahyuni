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
print("data : ", type(data_string))

# tipe data: biner true/False (boolean)
data_bool = False
print("data : data_bool")
print("- bertipe :, type(data_bool)")

# bilangan Complex

data_complex = complex(5,6)
print("data :, data_complex")
print("- bertipe :, type(data_complex)")


# tipe data dari bahasa C

from ctypes import c_double, C_char, C_long

data_c_double = c_double(10.5)
print("data_c_double")
print("- bertipe : ", type(data_c_double))