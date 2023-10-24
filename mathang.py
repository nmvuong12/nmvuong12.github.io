from tkinter import*
import tkinter.messagebox as mbox
class MatHang:
    #sắp xếp thông tin mặt hàng theo mã nhân viên
    def sap_xep_danh_sach(self, danh_sach):
        return sorted(danh_sach, key=lambda item: item['MaSP'])
    
    #kiểm tra xem mã nhân viên đã tồn tại hay chưa
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
    
    #reset lại các trường dữ liệu
    def trolai(self):
        self.TenSp.set("")
        self.MaSp.set("")
        self.GiaNhap.set("")
        self.GiaBan.set("")

    #lưu thông tin nhân viên vào file
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
                    mbox.showinfo("Thông báo", "Bạn đã nhập dữ liệu thành công!")
                else:
                    mbox.showinfo("Thông báo", "Mã sản phẩm đã tồn tại!")
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
            k = 0
            for item in self.temp:
                if item['MaSP'] == MaSpXoa:
                    k = 1
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
            if k == 0:
                mbox.showinfo("Thông báo", "Mã sản phẩm không tồn tại!")
                
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

        Button(self.root, text="Lưu lại",bg = 'grey', command=self.luu).grid(row=3, column=1)
        Button(self.root, text="Nhập lại",bg = 'grey', command=self.trolai).grid(row=3, column=2)

        Label(self.root, text="Mã sản phẩm muốn xóa").grid(row=4, column=0)
        Entry(self.root, textvariable=self.MaSpXoa, width=20).grid(row=4, column=1)
        Button(self.root, text="Xóa",bg = 'grey', command=self.xoa).grid(row=4, column=2)

        #Button(self.root, text="Làm mới danh sách",bg = 'grey', command=self.hienthi).grid(row=4, column=3)
        self.listbox = Listbox(self.root, width=70, height=30)
        self.listbox.grid(row=5, columnspan=2)
        #mbox.showinfo("Chú ý", "Bạn cần bấm làm mới sau mỗi lần lưu hoặc xóa để cập nhật chính xác dữ liệu")
        self.hienthi()
