print("LE TUAN ANH")
print("MSSV: 235752021610050")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
     
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        
        return self.chieu_dai * self.chieu_rong


hinh = Hinhchunhat(5, 3)  
dien_tich = hinh.tinh_dien_tich()  
print("Diện tích hình chữ nhật là:", dien_tich)


