print("LE TUAN ANH")
print("MSSV: 235752021610050")​
def say_hello():
    a="Hello"
    print(a)
    print(a)

def get_sum(*num):
    tmp=0
    
    for i in num:
        tmp +=i
    return tmp
result = get_sum(1,2,3,4,5)
print(result)
