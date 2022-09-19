#Operasi Logika
#Terdapat not, or, and, xor

#NOT    
a = False
c = not a
print("Data A: ", a)
print("Data C: ", c)

#OR    
a = True
b = False
c = a or b
print("Data A: ", a)
print("Data B: ", b)
print("Data C: ", c)
#Jika salah satu atau keduanya true maka hasil adalah true
#Jika keduanya adalah false maka hasil adalah false

#AND
a = True
b = False
c = a and b
print("Data A: ", a)
print("Data B: ", b)
print("Data C: ", c)
#Jika salah satu atau keduanya false maka hasil adalah false
#Jika keduanya adalah true maka hasil adalah true

#XOR
a = True
b = False
c = a ^ b
print("Data A: ", a)
print("Data B: ", b)
print("Data C: ", c)
#Hasil akan bernilai true jika kedua nilai berbeda
#Hasil akan bernilai false jika keduanya bernilai sama