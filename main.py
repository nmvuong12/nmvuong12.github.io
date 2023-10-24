from tkinter import*
from mathang import MatHang
from nhansu import NhanSu
from calamviec import CaLamViec
from tongket import tongket
def main():
    root = Tk()
    root.title("Quản lí cửa hàng")
    root.resizable(width=False, height=False)
    root.minsize(width=600, height=350)
    Label(root, text="TÊN CỬA HÀNG", fg='red', font=50).grid(row=0, column=0)
    FrameButton = Frame()

    Button(FrameButton, text="Sản phẩm", bd=3, height=15, width=20, command=lambda: MatHang(root)).pack(side=LEFT)
    Button(FrameButton, text="Nhân sự", bd=3, height=15, width=20, command=lambda: NhanSu(root)).pack(side=LEFT)  # Thêm chức năng Nhân sự
    Button(FrameButton, text="Ca làm việc", bd=3, height=15, width=20, command=lambda: CaLamViec(root)).pack(side=LEFT)  # Thêm chức năng Ca làm việc
    Button(FrameButton, text="Tổng kết tháng", bd=3, height=15, width=20, command=lambda: tongket(root)).pack(side=LEFT)  # Thêm chức năng Tổng kết tháng

    FrameButton.grid(row=1, columnspan=3)

    Button(root, text="THOÁT", bg="red", command=root.quit).grid(row=2, column=2)
    root.mainloop()

if __name__ == "__main__":
    main()