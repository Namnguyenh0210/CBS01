# Định nghĩa lớp cơ sở TaiKhoan (tài khoản ngân hàng)
class TaiKhoan:
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du):
        self.so_tai_khoan = so_tai_khoan
        self.ten_chu_tai_khoan = ten_chu_tai_khoan
        self.so_du = so_du

    def thong_tin_tai_khoan(self):
        return f"Tài khoản: {self.so_tai_khoan}, Chủ tài khoản: {self.ten_chu_tai_khoan}, Số dư: {self.so_du} VND"

# Định nghĩa lớp TaiKhoanChinh kế thừa từ lớp TaiKhoan
class TaiKhoanChinh(TaiKhoan):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du, han_muc_the_tin_dung):
        super().__init__(so_tai_khoan, ten_chu_tai_khoan, so_du)
        self.han_muc_the_tin_dung = han_muc_the_tin_dung

    def thong_tin_tai_khoan(self):
        thong_tin = super().thong_tin_tai_khoan()
        return thong_tin + f", Hạn mức thẻ tín dụng: {self.han_muc_the_tin_dung} VND"

# Định nghĩa lớp TaiKhoanTietKiem kế thừa từ lớp TaiKhoan
class TaiKhoanTietKiem(TaiKhoan):
    def __init__(self, so_tai_khoan, ten_chu_tai_khoan, so_du, lai_suat):
        super().__init__(so_tai_khoan, ten_chu_tai_khoan, so_du)
        self.lai_suat = lai_suat

    def thong_tin_tai_khoan(self):
        thong_tin = super().thong_tin_tai_khoan()
        return thong_tin + f", Lãi suất: {self.lai_suat}%"

    def tinh_lai_suat(self):
        return self.so_du * self.lai_suat / 100

# Menu cho người dùng chọn loại tài khoản và nhập thông tin
def tao_tai_khoan():
    while True:
        print("\nChào mừng đến hệ thống quản lý tài khoản ngân hàng!")
        print("Vui lòng chọn loại tài khoản:")
        print("1. Tài khoản chính")
        print("2. Tài khoản tiết kiệm")
        print("3. Thoát")

        # Nhận loại tài khoản từ người dùng
        loai_tai_khoan = input("Chọn loại tài khoản (1, 2, hoặc 3): ")

        if loai_tai_khoan == "1":
            # Tài khoản chính
            so_tai_khoan = input("Nhập số tài khoản: ")
            ten_chu_tai_khoan = input("Nhập tên chủ tài khoản: ")
            so_du = float(input("Nhập số dư: "))
            han_muc_the_tin_dung = float(input("Nhập hạn mức thẻ tín dụng: "))
            tk = TaiKhoanChinh(so_tai_khoan, ten_chu_tai_khoan, so_du, han_muc_the_tin_dung)
            print("\nThông tin tài khoản chính của bạn:")
            print(tk.thong_tin_tai_khoan())

        elif loai_tai_khoan == "2":
            # Tài khoản tiết kiệm
            so_tai_khoan = input("Nhập số tài khoản: ")
            ten_chu_tai_khoan = input("Nhập tên chủ tài khoản: ")
            so_du = float(input("Nhập số dư: "))
            lai_suat = float(input("Nhập lãi suất (%): "))
            tk = TaiKhoanTietKiem(so_tai_khoan, ten_chu_tai_khoan, so_du, lai_suat)
            print("\nThông tin tài khoản tiết kiệm của bạn:")
            print(tk.thong_tin_tai_khoan())
            print(f"Lãi suất tính là: {tk.tinh_lai_suat()} VND")

        elif loai_tai_khoan == "3":
            print("Cảm ơn đã sử dụng hệ thống! Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")

# Gọi hàm menu để người dùng tạo tài khoản
tao_tai_khoan()
