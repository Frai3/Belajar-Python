#tipe data angka satuan (int)
data_integer = 1
print("Data : ", data_integer)
print("Tipe : ", type(data_integer))

#tipe data angka dengan koma (float)
data_float = 1.5
print("Data : ", data_float)
print("Tipe : ", type(data_float))

#tipe data karakter (string)
data_string = "Steve Jobs"
print("Data : ", data_string)
print("Tipe : ", type(data_string))

#tipe data biner true/false (boolean)
data_bool = False
print("Data : ", data_bool)
print("Tipe : ", type(data_bool))

#Tipe data khusus
#Bilangan kompleks
data_complex = complex(5,6)
print("Data : ", data_complex)
print("Tipe : ", type(data_complex))

#Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data : ", data_c_double)
print("Tipe : ", type(data_c_double))