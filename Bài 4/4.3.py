print ("LE TUAN ANH")
print("235752021610050")

S = input("Nhập chuỗi: ")
for char in S:
    if char not in (' ', '\t'):
        print(char.upper())
