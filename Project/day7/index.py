
# Định nghĩa mảng
numbers = [2, 1, 2, 2, 3, 9, 8, 7, 8, 4, 5, 6, 9]

# Nhập giá trị từ người dùng
n = int(input("Nhập giá trị của phần tử: "))

# Đếm số lần xuất hiện của n trong mảng bằng cách sử dụng vòng lặp for

count = 0 # cho bien dem luc dau bang 0
for num in numbers:
    if num == n: # so sanh neu so n nay bang voi so trong mang
        count += 1 # thi bien dem tự động cộng thêm 1 khi so nay bang voi so trong mang

# Hiển thị kết quả
if count == 0:
    print(f"Phần tử {n} không có trong mảng")
else:
    print(f"Phần tử {n} xuất hiện {count} lần")

# Đề 3:
#  Viết 1 chương trình hướng đối tượng có MENU như sau:
# 1- Đăng kí tài khoản (TK, PASSWORD)
# 2- Đăng nhập
# 3- Đổi mật khẩu
# 4- Lưu thông tin tài khoản vào file
# 5- In ra thông tin các tài khoản và mật khẩu
# 6- Exit

# Các lưu ý sau:
# 1. Đăng ký tài khoản sẽ cho người dùng nhập vào Tài khoản và Mật khẩu
# 2. Đăng nhập: 
# - Kiểm tra thông tin đăng nhập có đúng với tài khoản đã tạo hay không. Nếu đúng thì sẽ In ra đăng nhập thành công. Ngược lại sẽ Xuất hiện thông báo sai tên đăng nhập hoặc mật khẩu
# 3. Đổi mật khẩu: yêu cầu người dùng nhập vào tên tài khoản, nếu tài khoản tồn tại thì sẽ yêu cầu nhập mật khẩu mới.
# 4. In tất cả thông tin vào file
# 5. In ra tất cả thông tin của các tài khoản đang có trong file
# 6. CHƯƠNG TRÌNH CHỈ THOÁT KHI NGƯỜI DÙNG CHỌN SỐ 6



class account:
    def _init_(self, username, password):
        self.username = username
        self.password = password
    def change_password(self, new_password):
        self.password = new_password

class account_manager:
    def _init_(self):
        self.accounts = {}        
    def register(self, username, password):
        if username in self.accounts:
            print("Tài khoản đã tồn tại")
        else:
            self.accounts[username] = account(username, password)
            print("Đăng ký thành công")
    def login(self, username, password):
        if username in self.accounts and self.accounts[username].password == password:
            print("Đăng nhập thành công")
        else:
            print("Sai tên đăng nhập hoặc mật khẩu")

    def change_password(self, username, old_password, new_password):
        if username in self.accounts and self.accounts[username].password == old_password:
            self.accounts[username].change_password(new_password)
            print("Đổi mật khẩu thành công")
        else:
            print("Vui lòng đăng nhập để thay đổi mật khẩu")  

    def save_to_file(self):
        with open("accounts.txt", "w") as file:
            for username, account in self.accounts.items():
                file.write(f"{username},{account.password}\n")

    def load_from_file(self):
        with open("accounts.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                self.accounts[username] = account(username, password)

    def print_accounts(self):
        if self.accounts:
            for username, account in self.accounts.items():
                print(f"Tài khoản: {username}, Mật khẩu: {account.password}")
        else:
            print("Không có tài khoản nào")

def main():
    manager = account_manager()
    manager.load_from_file()

    while True:
        print("\nMENU:")
        print("1. Đăng ký tài khoản")
        print("2. Đăng nhập")
        print("3. Đổi mật khẩu")
        print("4. Lưu thông tin tài khoản vào file")
        print("5. In ra thông tin các tài khoản và mật khẩu")
        print("6. Exit")

        choice = input("Chọn một lựa chọn: ")

        if choice == '1':
            username = input("Nhập tên tài khoản: ")
            password = input("Nhập mật khẩu: ")
            manager.register(username, password)
        elif choice == '2':
            username = input("Nhập tên tài khoản: ")
            password = input("Nhập mật khẩu: ")
            manager.login(username, password)
        elif choice == '3':
            username = input("Nhập tên tài khoản: ")
            old_password = input("Nhập mật khẩu cũ: ")
            new_password = input("Nhập mật khẩu mới: ")
            manager.change_password(username, old_password, new_password)
        elif choice == '4':
            manager.save_to_file()
        elif choice == '5':
            manager.print_accounts()
        elif choice == '6':
            break
        else:
            print("Vui lòng chọn một lựa chọn hợp lệ")

if __name__ == "__main__":
    main()              










