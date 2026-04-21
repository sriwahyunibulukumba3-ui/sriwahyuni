## Teknik menduplikat list

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# adderss dari kedua list a dan b
print(f"adderss a = {hex(id(a))}")
print(f"adderss b = {hex(id(b))}")

# menduplikat list dengan copy 

print(f"membuat list c dengan a.copy()")
c = a.copy() # full duplikat \ data baru

print(f"adderss a = {hex(id(a))}")
print(f"adderss b = {hex(id(b))}")
print(f"adderss c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 0")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print("kita ubah data 1")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")