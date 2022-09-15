#Menghitung temperatur

print("PROGRAM KONVERSI TEMPERATUR")

#Celcius
celcius = float(input("Masukkan suhu dalam celcius: "))
print("Suhu", celcius, "C")

C_R = 4/5*celcius
C_F = 9/5*celcius + 32
C_K = celcius + 273

print("Suhu dalam Reamur: ", C_R, "R")
print("Suhu dalam Fahrenheit: ", C_F, "F")
print("Suhu dalam Kelvin: ", C_K, "K")

#Reamur
reamur = float(input("Masukkan suhu dalam reamur: "))
print("Suhu", reamur, "R")

R_C = 5/4*reamur
R_F = 9/4*reamur+32
R_K = 5/4*reamur+273

print("Suhu dalam Celcius: ", R_C, "C")
print("Suhu dalam Fahrenheit: ", R_F, "F")
print("Suhu dalam Kelvin: ", R_K, "K")

#Fahrenheit
fahrenheit = float(input("Masukkan suhu dalam fahrenheit: "))
print("Suhu", fahrenheit, "F")

F_C = 5/9*(fahrenheit-32)
F_R = 4/9*(fahrenheit-32)
F_K = 5/9*(fahrenheit-32) + 273

print("Suhu dalam Celcius: ", F_C, "C")
print("Suhu dalam Reamur: ", F_R, "R")
print("Suhu dalam Kelvin: ", F_K, "K")

#Kelvin
kelvin = float(input("Masukkan suhu dalam kelvin: "))
print("Suhu", kelvin, "K")

K_C = kelvin - 273
K_R = 4/5*(kelvin-273)
K_F = 9/5*(kelvin-273) + 32

print("Suhu dalam Celcius: ", K_C, "C")
print("Suhu dalam Reamur: ", K_R, "R")
print("Suhu dalam Fahrenheit: ", K_F, "F")