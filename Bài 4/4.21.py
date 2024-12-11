print ("LE TUAN ANH")
print("235752021610050")
input_string = input("Nhập chuỗi các số nhị phân 4 chữ số (phân tách bởi dấu phẩy): ")
binary_numbers = input_string.split(',')
result = [binary for binary in binary_numbers if int(binary, 2) % 5 == 0]
print(",".join(result))
