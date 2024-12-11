print ("LE TUAN ANH")
print("235752021610050")
input_string = input("Nhập một chuỗi: ")
result = ''.join(char for char in input_string if not char.isdigit())
print("Chuỗi sau khi loại bỏ chữ số:", result)

