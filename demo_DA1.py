from tkinter import *
import tkinter.messagebox as mbox

class MatHang:
    def sap_xep_danh_sach(self, danh_sach):
        return sorted(danh_sach, key=lambda item: item['MaSP'])
    def kiemtrama(self, maspinput):
        self.temp = []
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        item = {'MaSP': parts[0], 'TenSP': parts[1], 'GiaNhap': parts[2], 'GiaBan': parts[3]}
                        self.temp.append(item)
        except FileNotFoundError:
            pass 
        k = 1
        for item in self.temp:
            if item['MaSP'] == maspinput:
                k = 0
        return k
    def trolai(self):
        self.TenSp.set("")
        self.MaSp.set("")
        self.GiaNhap.set("")
        self.GiaBan.set("")

    def luu_vao_file(self, line):

        with open('data.txt', 'a') as file:
            file.writelines(line)
            # i = 1
            # for item in self.data:
            #     if i == len(self.data):
            #         file.write(f"{item['MaSP']},{item['TenSP']},{item['GiaNhap']},{item['GiaBan']}\n")
            #     else:
            #         i += 1
            file.close()

    def luu_vao_file_xoa(self, line):
        with open('data.txt', 'w') as file:
            # for item in self.data1:
            #     file.write(f"{item['MaSP']},{item['TenSP']},{item['GiaNhap']},{item['GiaBan']}\n")
            file.writelines(line)
            file.close()

    def doc_tu_file(self):
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        item = {'MaSP': parts[0], 'TenSP': parts[1], 'GiaNhap': parts[2], 'GiaBan': parts[3]}
                        self.data.append(item)
        except FileNotFoundError:
            pass

    def hienthi(self):
        self.listbox.delete(0, END)
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        self.doc_tu_file()  # Đọc dữ liệu từ tệp và cập nhật danh sách self.data

        self.data.sort(key=lambda item: item['MaSP'])
        
        for item in self.data:
            tt = "MSP: " + item['MaSP'] + "   Tên SP: " + item['TenSP'] + "   Giá nhập: " + str(item['GiaNhap']) + "   Giá bán: " + str(item['GiaBan'])
            self.listbox.insert(END, tt)
            self.listbox.insert(END, '\n')
        self.data1 = self.data
        self.data.clear()

    # def lammoi(self):
    #     self.listbox.delete(0, END)
    #     #self.hienthi()
    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        TenSp = self.TenSp.get()
        MaSp = self.MaSp.get()
        GiaNhap = self.GiaNhap.get()
        GiaBan = self.GiaBan.get()
        if MaSp != "" and TenSp != "" and GiaNhap != "" and GiaBan:
            if len(MaSp) == 3:
                if(self.kiemtrama(MaSp) == 1):
                    line = MaSp + ',' + TenSp +',' + GiaNhap +',' + GiaBan + '\n'
                    item = {'MaSP': MaSp, 'TenSP': TenSp, 'GiaNhap': GiaNhap, 'GiaBan': GiaBan}
                    #self.data.append(item)
                    self.luu_vao_file(line)
                    self.trolai()
                    self.hienthi()
                    #mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                else:
                    mbox.showinfo("Thông báo", "Mã sản phẩm đã có!")
                    self.hienthi()
            else:
                mbox.showinfo("Thông báo", "Mã sản phẩm gồm có 3 kí tự!")
                self.hienthi()
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập lại dữ liệu!")
            self.hienthi()
    
    def xoa(self):
        #self.doc_tu_file()
        self.temp = []
        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        item = {'MaSP': parts[0], 'TenSP': parts[1], 'GiaNhap': parts[2], 'GiaBan': parts[3]}
                        self.temp.append(item)
        except FileNotFoundError:
            pass
        MaSpXoa = self.MaSpXoa.get()
        if len(MaSpXoa) == 3:
            for item in self.temp:
                if item['MaSP'] == MaSpXoa:
                    self.temp.remove(item)
                    self.MaSpXoa.set("")
                    with open('data.txt', 'w') as file:
                        for item in self.temp:
                            ma_sp = item['MaSP']
                            ten_sp = item['TenSP']
                            gia_nhap = item['GiaNhap']
                            gia_ban = item['GiaBan']
                            line = f"{ma_sp},{ten_sp},{gia_nhap},{gia_ban}\n"
                            file.write(line)
                        file.close()
                    #self.luu_vao_file_xoa()
                    self.hienthi()
                    return
                
        else:
            mbox.showinfo("Thông báo", "Mã sản phẩm gồm có 3 kí tự!")
        #self.hienthi()

    def __init__(self, parent):
        self.parent = parent  # Lưu tham chiếu đến cửa sổ chính
        self.TenSp = StringVar()
        self.MaSp = StringVar()
        self.GiaNhap = StringVar()
        self.GiaBan = StringVar()
        self.MaSpXoa = StringVar()
        self.data = []
        self.data1 = []


        # Tạo cửa sổ mới cho chức năng sản phẩm
        self.root = Toplevel(parent)
        self.root.title("Mặt hàng")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng

        Label(self.root, text="Tên sản phẩm").grid(row=1, column=2)
        Entry(self.root, textvariable=self.TenSp, width=20).grid(row=1, column=3)

        Label(self.root, text="Mã sản phẩm").grid(row=1, column=0)
        Entry(self.root, textvariable=self.MaSp, width=20).grid(row=1, column=1)

        Label(self.root, text="Giá nhập").grid(row=2, column=0)
        Entry(self.root, textvariable=self.GiaNhap, width=20).grid(row=2, column=1)

        Label(self.root, text="Giá bán").grid(row=2, column=2)
        Entry(self.root, textvariable=self.GiaBan, width=20).grid(row=2, column=3)

        Button(self.root, text="Lưu lại", command=self.luu).grid(row=3, column=1)
        Button(self.root, text="Nhập lại", command=self.trolai).grid(row=3, column=2)

        Label(self.root, text="Mã sản phẩm muốn xóa").grid(row=4, column=0)
        Entry(self.root, textvariable=self.MaSpXoa, width=20).grid(row=4, column=1)
        Button(self.root, text="Xóa", command=self.xoa).grid(row=4, column=2)

        Button(self.root, text="Làm mới danh sách", command=self.hienthi).grid(row=4, column=3)
        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=5, columnspan=2)
        mbox.showinfo("Chú ý", "Bạn cần bấm làm mới sau mỗi lần lưu hoặc xóa để cập nhật chính xác dữ liệu")
        #self.hienthi()


class NhanSu:
    def kiemtrama(self, manvinput):
        self.temp = []
        try:
            with open('nhansu.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        item = {'MaNV': parts[0], 'TenNV': parts[1], 'SDT': parts[2], 'NgaySinh': parts[3], 'DiaChi': parts[4]}
                        self.temp.append(item)
        except FileNotFoundError:
            pass 
        k = 1
        for item in self.temp:
            if item['MaNV'] == manvinput:
                k = 0
        return k
    def trolai(self):
        self.TenNV.set("")
        self.MaNV.set("")
        self.SDT.set("")
        self.NgaySinh.set("")
        self.DiaChi.set("")

    def luu_vao_file(self, line):

        with open('nhansu.txt', 'a') as file:
            file.writelines(line)
            # i = 1
            # for item in self.data:
            #     if i == len(self.data):
            #         file.write(f"{item['MaSP']},{item['TenSP']},{item['GiaNhap']},{item['GiaBan']}\n")
            #     else:
            #         i += 1
            file.close()

    def doc_tu_file(self):
        try:
            with open('nhansu.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        item = {'MaNV': parts[0], 'TenNV': parts[1], 'SDT': parts[2], 'NgaySinh': parts[3], 'DiaChi': parts[4]}
                        self.datanv.append(item)
        except FileNotFoundError:
            pass

    def hienthi(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        self.doc_tu_file()  # Đọc dữ liệu từ tệp và cập nhật danh sách self.data

        self.datanv.sort(key=lambda item: item['MaNV'])

        for item in self.datanv:
            tt = "MNV: " + str(item['MaNV']) + "   Tên NV: " + str(item['TenNV']) + "   SĐT: " + str(item['SDT']) + "   Ngày sinh: " + str(item['NgaySinh']) + "  Địa chỉ: " + str(item['DiaChi'])
            self.listbox.insert(END, tt)
            self.listbox.insert(END, '\n')
        self.datanv.clear()

    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        TenNV = self.TenNV.get()
        MaNV = self.MaNV.get()
        SDT = self.SDT.get()
        NgaySinh = self.NgaySinh.get()
        DiaChi = self.DiaChi.get()
        if MaNV != "" and TenNV != "" and SDT != "" and NgaySinh != "" and DiaChi != "":
            if len(MaNV) == 3:
                if(self.kiemtrama(MaNV) == 1):
                    line = MaNV + ',' + TenNV +',' + SDT +',' + NgaySinh + ',' + DiaChi +'\n'
                    item = {'MaNV': MaNV, 'TenNV': TenNV, 'SDT': SDT, 'NgaySinh': NgaySinh , 'DiaChi': DiaChi}
                    # self.data1.append(item)
                    # self.luu_vao_file(line)
                    with open('nhansu.txt', 'a') as file:
                            file.writelines(line)
                    
                    self.trolai()
                    self.hienthi()
                    #mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                else:
                    mbox.showinfo("Thông báo", "Mã nhân viên đã có!")
                    self.hienthi()
            else:
                mbox.showinfo("Thông báo", "Mã nhân viên gồm có 3 kí tự!")
                self.hienthi()
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập lại dữ liệu!")
            self.hienthi()

    
    # def xoa(self):
    #     #self.doc_tu_file()
    #     MaSpXoa = self.MaSpXoa.get()
    #     for item in self.datanv:
    #         if item['MaSP'] == MaSpXoa:
    #             self.data.remove(item)
    #             self.MaSpXoa.set("")

    #             self.luu_vao_file_xoa()
    #             return
    #     #self.hienthi()
    def __init__(self, parent):
        self.parent = parent  # Lưu tham chiếu đến cửa sổ chính
        self.TenNV = StringVar()
        self.MaNV = StringVar()
        self.SDT = StringVar()
        self.NgaySinh = StringVar()
        self.DiaChi = StringVar()
        self.datanv = []
        self.data1 = []

        # Tạo cửa sổ mới cho chức năng sản phẩm
        self.root = Toplevel(parent)
        self.root.title("Nhân sự")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng

        Label(self.root, text="Tên nhân viên").grid(row=1, column=2)
        Entry(self.root, textvariable=self.TenNV, width=20).grid(row=1, column=3)

        Label(self.root, text="Mã nhân viên").grid(row=1, column=0)
        Entry(self.root, textvariable=self.MaNV, width=20).grid(row=1, column=1)

        Label(self.root, text="Số điện thoại").grid(row=2, column=0)
        Entry(self.root, textvariable=self.SDT, width=20).grid(row=2, column=1)

        Label(self.root, text="Ngày sinh").grid(row=2, column=2)
        Entry(self.root, textvariable=self.NgaySinh, width=20).grid(row=2, column=3)

        Label(self.root, text="Địa chỉ").grid(row=3, column=0)
        Entry(self.root, textvariable=self.DiaChi, width=70).grid(row=3, column=1)

        Button(self.root, text="Lưu lại", command=self.luu).grid(row=4, column=1)
        Button(self.root, text="Nhập lại", command=self.trolai).grid(row=4, column=2)

        Button(self.root, text="Cập nhật", command=self.hienthi).grid(row=4, column=3)

        #Button(self.root, text="THOÁT", bg="red", command=self.root.quit).grid(row=5, column=3)
        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=5, columnspan=2)
        self.hienthi()



def main():
    root = Tk()
    root.title("Quản lí cửa hàng")
    root.resizable(width=False, height=False)
    root.minsize(width=600, height=350)
    Label(root, text="TÊN CỬA HÀNG", fg='red', font=50).grid(row=0, column=0)
    FrameButton = Frame()

    Button(FrameButton, text="Sản phẩm", bd=3, height=15, width=20, command=lambda: MatHang(root)).pack(side=LEFT)
    Button(FrameButton, text="Nhân sự", bd=3, height=15, width=20, command=lambda: NhanSu(root)).pack(side=LEFT)  # Thêm chức năng Nhân sự
    Button(FrameButton, text="Ca làm việc", bd=3, height=15, width=20).pack(side=LEFT)  # Thêm chức năng Ca làm việc
    Button(FrameButton, text="Tổng kết tháng", bd=3, height=15, width=20).pack(side=LEFT)  # Thêm chức năng Tổng kết tháng

    FrameButton.grid(row=1, columnspan=3)

    Button(root, text="THOÁT", bg="red", command=root.quit).grid(row=2, column=2)
    root.mainloop()

if __name__ == "__main__":
    main()
