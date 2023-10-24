from tkinter import*
import tkinter.messagebox as mbox
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
                    #item = {'MaNV': MaNV, 'TenNV': TenNV, 'SDT': SDT, 'NgaySinh': NgaySinh , 'DiaChi': DiaChi}
                    # self.data1.append(item)
                    # self.luu_vao_file(line)
                    with open('nhansu.txt', 'a') as file:
                            file.writelines(line)
                    
                    self.trolai()
                    self.hienthi()
                    mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                else:
                    mbox.showinfo("Thông báo", "Mã nhân viên đã tồn tại!")
                    self.hienthi()
            else:
                mbox.showinfo("Thông báo", "Mã nhân viên gồm có 3 kí tự!")
                self.hienthi()
        else:
            mbox.showinfo("Thông báo", "Bạn hãy nhập lại dữ liệu!")
            self.hienthi()

    
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

        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=4, column=2)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=4, column=3)

        #Button(self.root, text="Cập nhật", command=self.hienthi).grid(row=4, column=3)

        #Button(self.root, text="THOÁT", bg="red", command=self.root.quit).grid(row=5, column=3)
        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=5, columnspan=2)
        self.hienthi()