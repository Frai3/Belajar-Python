#Membuat gabungan area rentang dari angka

print("===============5CASE 1===============")
#++++3----10++++
#Jika < 3 atau > 10 maka bernilai true, selain itu false

inputNilai = float(input("Masukkan nilai kurang dari 3 atau lebih dari 10: "))

batasBawah = (inputNilai < 3)
print("Nilai Kurang Dari 3: ", batasBawah)

batasAtas = (inputNilai > 10)
print("Nilai Lebih Dari 10: ", batasAtas)

hasil = batasBawah or batasAtas
print("Hasil nilai yang ada masukkan adalah ", hasil)

print("\n",40*"-","\n")

print("===============CASE 2===============")
# ----3++++10----
#Jika > 3 dan < 10 maka bernilai true, selain itu false

inputNilai = float(input("Masukkan nilai kurang dari 3 atau lebih dari 10: "))

batasBawah = (inputNilai > 3)
print("Nilai Lebih Dari 3: ", batasBawah)

batasAtas = (inputNilai < 10)
print("Nilai Kurang Dari 10: ", batasAtas)

hasil = batasBawah and batasAtas
print("Hasil nilai yang ada masukkan adalah ", hasil)

print("\n",40*"-","\n")

print("===============SOAL 1===============")
#----0++++5----8++++11----
inputNilai = float(input("Masukkan nilai: "))

batas1 = (inputNilai > 0)
print("Nilai lebih dari 0: ", batas1)

batas2 = (inputNilai < 5)
print("Nilai kurang dari 5: ", batas2)

batas3 = (inputNilai > 8)
print("Nilai lebih dari 8: ", batas3)

batas4 = (inputNilai < 11)
print("Nilai kurang dari 11: ", batas4)

hasil = (batas1 and batas2) or (batas3 and batas4)
print("Hasil nilai yang ada masukkan adalah ", hasil)

print("\n",40*"-","\n")

print("===============SOAL 2===============")
#----0++++5----8++++11----
inputNilai = float(input("Masukkan nilai: "))

batas1 = (inputNilai < 0)
print("Nilai kurang dari 0: ", batas1)

batas2 = (inputNilai > 5)
print("Nilai lebih dari 5: ", batas2)

batas3 = (inputNilai < 8)
print("Nilai kurang dari 8: ", batas3)

batas4 = (inputNilai > 11)
print("Nilai lebih dari 11: ", batas4)

hasil = (batas1 or batas2) and (batas3 or batas4)
print("Hasil nilai yang ada masukkan adalah ", hasil)