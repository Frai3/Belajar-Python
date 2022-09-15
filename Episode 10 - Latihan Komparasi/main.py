#Setiap hasil dari komparasi adalah boolean (T/F)
#>, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

hasil = a > 3
print(hasil)
hasil = b > 3
print(hasil)

#Menggunakan is
print("Nilai a: ", a, " ,ID = ", hex(id(a)))
print("Nilai b: ", b, " ,ID = ", hex(id(b)))
#Membandingkan dengan variabel, bukan nilai
hasil = a is b
print(hasil)
hasil = a is not b
print(hasil)