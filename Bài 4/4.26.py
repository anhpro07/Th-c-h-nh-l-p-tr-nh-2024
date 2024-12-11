print ("LE TUAN ANH")
print("235752021610050")
balance = 0
print("Nhập nhật ký giao dịch (D/W số tiền). Nhập trống để kết thúc:")

while True:
    transaction = input()  
    if not transaction:  
        break

    
    parts = transaction.split()
    if len(parts) != 2:
        print("Giao dịch không hợp lệ. Vui lòng nhập lại.")
        continue

    action, amount = parts[0].upper(), parts[1]
    if not amount.isdigit():
        print("Số tiền không hợp lệ. Vui lòng nhập lại.")
        continue

    amount = int(amount)

    
    if action == "D":  
        balance += amount
    elif action == "W":  
        if amount > balance: 
            print("Số dư không đủ để rút tiền.")
        else:
            balance -= amount
    else:
        print("Loại giao dịch không hợp lệ. Vui lòng nhập lại.")


print("Số tiền thực trong tài khoản là:", balance)
