# latihan

# kalkulator sederhana
print(20*"=")
print("kalkulator sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukkan angka 1 = "))
operator = input("operator (=,-,x/) : ")
angka_2 = float(input("masukkan angka 2 = "))

# percabangan

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "_":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif operator == "x":
     hasil = angka_1 * angka_2
     print(f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
else:
    print("masukkan yang benar dong! aku pusying")

    print("akhir dari program, terima gajih!")
