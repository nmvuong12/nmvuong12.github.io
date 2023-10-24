from datetime import datetime
from tkinter import*
import tkinter.messagebox as mbox
from tinhluong import tinhluong

class tongket :
    def trolai(self):
        self.date.set("")
        self.tienban.set("")
        self.tiennhap.set("")

    def luu(self):
        self.listbox.delete(0, END)  # Xóa tất cả các mục trong Listbox
        date = self.date.get()
        tienban = self.tienban.get()
        tiennhap = self.tiennhap.get()
        #k = 0 #kiểm tra định dạng ngày có đúng định dạng dd/mm/yyyy hay không
        if date!="" and tienban!="" and tiennhap!="":
            tienban = float(tienban)
            tiennhap = float(tiennhap)
            try:
                date_obj = datetime.strptime(date, '%d/%m/%Y')
                if tienban>=0 and tiennhap>=0:
                    line = date + ',' + str(tiennhap) + ',' + str(tienban) + '\n'
                    with open('tongket.txt', 'a') as file:
                            file.writelines(line)
                            file.close()
                    self.hienthi()
                    self.trolai()
                    mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")         
                else:
                    mbox.showinfo("Thông báo", "Giá trị tiền không được âm!")       
            except ValueError:
                self.hienthi()
                mbox.showinfo("Thông báo", "Định dạng ngày không hợp lệ")
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập đủ dữ liệu!")
    def hienthi(self):
        try:
            with open('tongket.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        item = {'date': parts[0], 'tiennhap': parts[1], 'tienban': parts[2]}
                        self.data.append(item)
        except FileNotFoundError:
            pass
        for item in self.data:
            date = str(item['date'])
            tiennhap = float(item['tiennhap'])
            tienban = float(item['tienban'])
            tienlai = tienban - tiennhap
            tt = f"Ngày: {date}   Tiền nhập: {tiennhap}   Tiền bán: {tienban}\n "
            tt1 = f"Tiền lãi: {tienlai}"
            self.listbox.insert(END, tt)
            self.listbox.insert(END, tt1)
            self.listbox.insert(END, '\n')
        self.data.clear()

    def mo_tinhluong(self):
        motinhluong = tinhluong(self.root)

    def __init__(self, parent):
        self.parent = parent
        self.date = StringVar()
        self.tienban = StringVar()
        self.tiennhap = StringVar()
        self.data = []

        
        
        self.root = Toplevel(parent)
        self.root.transient(parent)  # Đặt cửa sổ con làm cửa sổ con trực thuộc của cửa sổ chính
        self.root.grab_set()  # Đặt cửa sổ con để bắt sự kiện đầu vào đến khi nó đóng
        self.root.title("Tổng kết tháng")
        self.root.resizable(width=False, height=False)
        self.root.minsize(width=600, height=400)

        Label(self.root, text=("Ngày tổng kết")).grid(row=1, column=0)
        Entry(self.root, textvariable = self.date, width=20).grid(row=1, column=1)

        Label(self.root, text=("Tiền nhập")).grid(row=2, column=0)
        Entry(self.root, textvariable = self.tiennhap, width=20).grid(row=2, column=1)

        Label(self.root, text="Tiền bán").grid(row=3, column=0)
        Entry(self.root, textvariable = self.tienban).grid(row=3, column=1)

        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=4, column=0)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=4, column=1)

        Button(self.root, text="Tính lương",bg = 'grey', command= self.mo_tinhluong).grid(row=5, column=1)

        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=6, columnspan=2)
        self.hienthi()