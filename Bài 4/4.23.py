print ("LE TUAN ANH")
print("235752021610050")
input_string = input("Nhập một câu: ")
upper_count = sum(1 for char in input_string if char.isupper()) 
lower_count = sum(1 for char in input_string if char.islower())  
print("Chữ hoa:", upper_count)
print("Chữ thường:", lower_count)
