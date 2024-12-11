print ("LE TUAN ANH")
print("235752021610050")
even_digit_numbers = []
for number in range(1000, 3001):
    if all(int(digit) % 2 == 0 for digit in str(number)):
        even_digit_numbers.append(str(number))
print(",".join(even_digit_numbers))
