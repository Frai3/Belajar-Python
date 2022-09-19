#Operator bitwise adalah operasi dari masing masing satuan bit

a = 9
b = 5

#Bitwise OR (|)
c = a | b
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai b: ", b, "||", "Binary b: ", format(b, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))

#Bitwise AND (&)
c = a & b
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai b: ", b, "||", "Binary b: ", format(b, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))

#Bitwise XOR (^)
c = a ^ b
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai b: ", b, "||", "Binary b: ", format(b, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))

#Bitwise NOT (~)
c = ~a
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))
# c = -(a+1)
#Shifting
#Shif Right (>>)
c = a >> 1
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))

#Shif Left (<<)
c = a << 3
print("Nilai a: ", a, "||", "Binary a: ", format(a, '08b'))
print("Nilai c: ", c, "||", "Binary c: ", format(c, '08b'))