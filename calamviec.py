from datetime import datetime
from tkinter import*
import tkinter.messagebox as mbox
from thongke import thongke

class CaLamViec :
    def kiemtramanvtrongca(self, date, ca, manvinput):
        self.temp = []
        try:
            with open('calamviec.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        item = {'date': parts[0], 'ca': parts[1], 'MaNV': parts[2]}
                        self.temp.append(item)
        except FileNotFoundError:
            pass 
        k = 1
        for item in self.temp:
            if item['MaNV'] == manvinput and item['date'] == date and item['ca'] == ca:
                k = 0
        return k
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
        self.date.set("")
        self.ca.set("")
        self.MaNV.set("")


    def luu_vao_file(self, line):

        with open('calamviec.txt', 'a') as file:
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
            with open('calamviec.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        item = {'date': parts[0], 'ca': parts[1], 'MaNV': parts[2]}
                        self.data.append(item)
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

    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        date = self.date.get()
        ca = self.ca.get()
        MaNV = self.MaNV.get()
        #k = 0 #kiểm tra định dạng ngày có đúng định dạng dd/mm/yyyy hay không
        if date!="" and ca!="" and MaNV!="":
            try:
                date_obj = datetime.strptime(date, '%d/%m/%Y')
                if ca>='1' and ca<='3':
                    if len(MaNV) == 3:
                        if MaNV[0].isdigit() and MaNV[1].isdigit() and MaNV[2].isdigit():
                            if self.kiemtrama(MaNV) == 0:
                                if self.kiemtramanvtrongca(date, ca, MaNV):
                                    line = date + ',' + ca + ',' + MaNV + '\n'
                                    with open('calamviec.txt', 'a') as file:
                                            file.writelines(line)
                                            file.close()
                                    self.hienthi()
                                    self.trolai()
                                    mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                                else:
                                    mbox.showinfo("Thông báo", "Một nhân viên không thể có hai tên trong cùng 1 ca")
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
                else:
                    mbox.showinfo("Thông báo", "Ca làm việc phải >= 1 hoặc <= 3")
                    self.hienthi()
            except ValueError:
                mbox.showinfo("Thông báo", "Định dạng ngày không hợp lệ")
                self.hienthi()
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập đủ dữ liệu!")
            self.hienthi()

    def hienthi(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        self.doc_tu_file()  # Đọc dữ liệu từ tệp và cập nhật danh sách self.data
        for item in self.data:
            date = str(item['date'])
            ca = str(item['ca'])
            MaNV = str(item['MaNV'])
            
            # Tìm tên nhân viên tương ứng trong danh sách datanv
            ten_nv = ""
            for nv in self.datanv:
                if nv['MaNV'] == MaNV:
                    ten_nv = nv['TenNV']
                    break

            # Tạo một dòng hiển thị đầy đủ thông tin
            tt = f"Ngày: {date}   Ca: {ca}"
            tt1 = f"Mã NV: {MaNV}   Tên NV: {ten_nv}\n "
            self.listbox.insert(END, tt)
            self.listbox.insert(END, tt1)
            self.listbox.insert(END, '\n')

        self.data.clear()
        self.datanv.clear()
    def mo_thong_ke(self):
        mothongke = thongke(self.root)

    def __init__(self, parent):
        self.parent = parent
        self.date = StringVar()
        self.ca = StringVar()
        self.MaNV = StringVar()
        self.data = []
        self.datanv = []

        
        
        self.root = Toplevel(parent)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng
        self.root.title("Ca làm việc")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)

        Label(self.root, text=("Ngày làm việc")).grid(row=1, column=0)
        Entry(self.root, textvariable = self.date, width=20).grid(row=1, column=1)

        Label(self.root, text=("Ca số")).grid(row=2, column=0)
        Entry(self.root, textvariable = self.ca, width=20).grid(row=2, column=1)

        Label(self.root, text="Mã nhân viên").grid(row=3, column=0)
        Entry(self.root, textvariable = self.MaNV).grid(row=3, column=1)

        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=4, column=0)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=4, column=1)

        Button(self.root, text="Thống kê",bg = 'grey', command= self.mo_thong_ke).grid(row=5, column=1)

        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=6, columnspan=2)
        self.hienthi()