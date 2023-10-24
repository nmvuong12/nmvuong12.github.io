from datetime import datetime
from tkinter import*
import tkinter.messagebox as mbox
class thongke :
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
    def luu_vao_file(self, line):

        with open('thongke.txt', 'a') as file:
            file.writelines(line)
            # i = 1
            # for item in self.data:
            #     if i == len(self.data):
            #         file.write(f"{item['MaSP']},{item['TenSP']},{item['GiaNhap']},{item['GiaBan']}\n")
            #     else:
            #         i += 1
            file.close()
    def trolai(self):
        date = self.date.set("")
        ca = self.ca.set("")
        self.MaSP.set("")
        self.SLBan.set("")
        
    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        date = self.date.get()
        ca = self.ca.get()
        MaSP = self.MaSP.get()
        SLBan = self.SLBan.get()
        
        try:
            date_obj = datetime.strptime(date, '%d/%m/%Y')
            if ca>='1' and ca<='3':
                if len(MaSP) == 3:
                    if MaSP[0].isdigit() and MaSP[1].isdigit() and MaSP[2].isdigit():
                        if self.kiemtrama(MaSP) == 0:
                            SLBan = int(SLBan)
                            if SLBan >=0:
                                line =date + ',' + ca + ',' + MaSP + ',' + str(SLBan) + '\n'
                                with open('thongke.txt', 'a') as file:
                                        file.writelines(line)
                                        file.close()
                                self.hienthi()
                                MaSP = self.MaSP.set("")
                                SLBan = self.SLBan.set("")
                                mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                            else:
                                mbox.showinfo("Thông báo", "Giá trị số lương bán không đúng!")
                                
                        else:
                            mbox.showinfo("Thông báo", "Mã sản phẩm không tồn tại")
                            self.hienthi()
                    else:
                        mbox.showinfo("Thông báo", "Mã sản phẩm sai định dạng")
                        self.hienthi()
                else:
                    mbox.showinfo("Thông báo", "Mã sản phẩm sai định dạng")
                    self.hienthi()
            else:
                mbox.showinfo("Thông báo", "Ca làm việc phải >= 1 hoặc <= 3")
                self.hienthi()
        except ValueError:
            mbox.showinfo("Thông báo", "Định dạng ngày không hợp lệ")
            self.hienthi()
    def doc_tu_file(self):
        try:
            with open('thongke.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        item = {'date': parts[0], 'ca': parts[1], 'MaSP': parts[2], 'SLBan': parts[3]}
                        self.datatk.append(item)
        except FileNotFoundError:
            pass

        try:
            with open('data.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        item = {'MaSP': parts[0], 'TenSP': parts[1], 'GiaNhap':parts[2], 'GiaBan' :parts[3]}
                        self.datasp.append(item)
        except FileNotFoundError:
            pass
    
    def hienthi(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        self.doc_tu_file()  # Đọc dữ liệu từ tệp và cập nhật danh sách self.data
        for item in self.datatk:
            date = str(item['date'])
            ca = str(item['ca'])
            MaSP = str(item['MaSP'])
            SLBan = float(item['SLBan'])
            
            ten_sp = ""  # Tên sản phẩm mặc định
            tien = 0.0  # Số tiền mặc định

            for sp in self.datasp:
                if 'MaSP' in sp and sp['MaSP'] == MaSP:  # Chắc chắn rằng có 'MaSP' trong sp
                    ten_sp = sp['TenSP']
                    gia_ban = float(sp['GiaBan'])
                    tien = gia_ban * SLBan
                    break

            # Tạo một dòng hiển thị đầy đủ thông tin
            tt = f"Ngày: {date}   Ca: {ca}"
            tt1 = f"Mã SP: {MaSP}   Tên SP: {ten_sp}    Tiền bán được: {tien}\n "
            self.listbox.insert(END, tt)
            self.listbox.insert(END, tt1)
            self.listbox.insert(END, '\n')

        self.datatk.clear()
        self.datasp.clear()

    def __init__(self, parent):
        self.parent = parent
        self.date = StringVar()
        self.ca = StringVar()
        self.MaSP = StringVar()
        self.SLBan = StringVar()
        self.datatk = []
        self.datasp = []

        
        
        self.root = Toplevel(parent)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng
        self.root.title("Thống kê")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)

        Label(self.root, text=("Ngày làm việc")).grid(row=1, column=0)
        Entry(self.root, textvariable = self.date, width=20).grid(row=1, column=1)

        Label(self.root, text=("Ca số")).grid(row=2, column=0)
        Entry(self.root, textvariable = self.ca, width=20).grid(row=2, column=1)

        Label(self.root, text="Mã sản phẩm").grid(row=3, column=0)
        Entry(self.root, textvariable = self.MaSP).grid(row=3, column=1)

        Label(self.root, text="Số lượng bán").grid(row=4, column=0)
        Entry(self.root, textvariable = self.SLBan).grid(row=4, column=1)


        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=5, column=0)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=5, column=1)

        #Button(self.root, text="Thống kê",bg = 'grey').grid(row=5, column=1)

        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=6, columnspan=2)
        self.hienthi()