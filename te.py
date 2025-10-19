#TN:
'''
1.D
2.B
3.A
4.B
5.D
6.B
7.B
8.D
9.B
10.B
'''
#TH:
class HocSinh:
    def __init__(self):
        self.name = input("Nhap ten hoc sinh: ")
        self.address = input("Nhap dia chi hoc sinh: ")
        self.can = input("Nhap can nang hoc sinh: ")
        self.hl = input("Nhap hoc luc hoc sinh: ")
    def show(self):
        print(f">>TTHS<<")
        print(f"Ten hoc sinh: {self.name}")
        print(f"Dia chi: {self.address}")
        print(f"Can nang: {self.can}")
        print(f"Hoc luc: {self.hl}")
        print(f"____________________________")
    def updtaddress(self):
        self.address = input("Nhap dia chi moi: ")
    def updtcan(self):
        self.can = float(input("Nhap can nang moi: "))
hoc_sinh = HocSinh()
hoc_sinh.show()
hoc_sinh.updtaddress()
hoc_sinh.updtcan()
hoc_sinh.show()