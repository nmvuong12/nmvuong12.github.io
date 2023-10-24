from datetime import datetime
from tkinter import*
import tkinter.messagebox as mbox
class tinhluong :
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
    def luu_vao_file(self, line):

        with open('tinhluong.txt', 'a') as file:
            file.writelines(line)
            # i = 1
            # for item in self.data:
            #     if i == len(self.data):
            #         file.write(f"{item['MaSP']},{item['TenSP']},{item['GiaNhap']},{item['GiaBan']}\n")
            #     else:
            #         i += 1
            file.close()
    def trolai(self):
        self.date.set("")
        self.MaNV.set("")
        self.SoCaLam.set("")
        
    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        date = self.date.get()
        MaNV = self.MaNV.get()
        SoCaLam = self.SoCaLam.get()
        if date!="" and MaNV!="" and SoCaLam!="":
            try:
                date_obj = datetime.strptime(date, '%d/%m/%Y')
                if len(MaNV) == 3:
                    if MaNV[0].isdigit() and MaNV[1].isdigit() and MaNV[2].isdigit():
                        if self.kiemtrama(MaNV) == 0:
                            SoCaLam = int(SoCaLam)
                            if SoCaLam >= 0:
                                line =date + ',' + MaNV + ',' + str(SoCaLam) + '\n'
                                with open('tinhluong.txt', 'a') as file:
                                        file.writelines(line)
                                        file.close()
                                self.hienthi()
                                self.MaNV.set("")
                                self.SoCaLam.set("")
                                mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                            else:
                                mbox.showinfo("Thông báo", "Số ca làm phi >= 0")
                                self.hienthi()
                        else:
                            mbox.showinfo("Thông báo", "Mã nhân viên không tồn tại")
                            self.hienthi()
                    else:
                        mbox.showinfo("Thông báo", "Mã nhân viên sai định dạng")
                        self.hienthi()
                else:
                    mbox.showinfo("Thông báo", "Mã nhân viên sai định dạng")
                    self.hienthi()
                
            except ValueError:
                mbox.showinfo("Thông báo", "Định dạng ngày không hợp lệ")
                self.hienthi()
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập đủ dữ liệu")
            self.hienthi()
    def doc_tu_file(self):
        try:
            with open('tinhluong.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        item = {'date': parts[0], 'MaNV': parts[1], 'SoCaLam': parts[2]}
                        self.datatl.append(item)
        except FileNotFoundError:
            pass

        try:
            with open('nhansu.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 5:
                        item = {'MaNV': parts[0], 'TenNV': parts[1], 'sdt':parts[2], 'ngaysinh' :parts[3], 'diachi' :parts[4]}
                        self.datanv.append(item)
        except FileNotFoundError:
            pass
    
    def hienthi(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        self.doc_tu_file()  # Đọc dữ liệu từ tệp và cập nhật danh sách self.data
        for item in self.datatl:
            date = str(item['date'])
            MaNV= str(item['MaNV'])
            SoCaLam = float(item['SoCaLam'])
            
            ten_nv = ""  # Tên sản phẩm mặc định
            tien = 0.0  # Số tiền mặc định

            for nv in self.datanv:
                if 'MaNV' in nv and nv['MaNV'] == MaNV:  # Chắc chắn rằng có 'Manv' trong nv
                    ten_nv = nv['TenNV']
                    #gia_ban = float(sp['GiaBan'])
                    tien = 150000 * SoCaLam
                    break

            # Tạo một dòng hiển thị đầy đủ thông tin
            tt = f"Ngày: {date}"
            tt1 = f"Mã NV: {MaNV}   Tên NV: {ten_nv}    Tiền lương: {tien}\n "
            self.listbox.insert(END, tt)
            self.listbox.insert(END, tt1)
            self.listbox.insert(END, '\n')

        self.datatl.clear()
        self.datanv.clear()

    def __init__(self, parent):
        self.parent = parent
        self.date = StringVar()
        self.MaNV = StringVar()
        self.SoCaLam = StringVar()
        self.datatl = []
        self.datanv = []

        
        
        self.root = Toplevel(parent)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng
        self.root.title("Tính lương")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)

        Label(self.root, text=("Ngày trả lương")).grid(row=1, column=0)
        Entry(self.root, textvariable = self.date, width=20).grid(row=1, column=1)

        Label(self.root, text=("Mã nhân viên")).grid(row=2, column=0)
        Entry(self.root, textvariable = self.MaNV, width=20).grid(row=2, column=1)

        Label(self.root, text="Số ca làm").grid(row=3, column=0)
        Entry(self.root, textvariable = self.SoCaLam).grid(row=3, column=1)


        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=4, column=0)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=4, column=1)

        #Button(self.root, text="Thống kê",bg = 'grey').grid(row=5, column=1)

        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=5, columnspan=2)
        self.hienthi()