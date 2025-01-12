import json

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def change_password(self, new_password):
        self.password = new_password


class AccountManager:
    def __init__(self):
        self.accounts = {}

    def register(self, username, password):
        if username in self.accounts:
            print("Tài khoản đã tồn tại.")
        else:
            self.accounts[username] = Account(username, password)
            print("Đăng ký thành công!")

    def login(self, username, password):
        if username in self.accounts and self.accounts[username].password == password:
            print("Đăng nhập thành công!")
        else:
            print("Sai tên đăng nhập hoặc mật khẩu.")

    def change_password(self, username, new_password):
        if username in self.accounts:
            self.accounts[username].change_password(new_password)
            print("Đổi mật khẩu thành công!")
        else:
            print("Tài khoản không tồn tại.")

    def save_to_file(self, filename="accounts.json"):
        with open(filename, 'w') as file:
            json.dump({username: account.password for username, account in self.accounts.items()}, file)
            print("Lưu thông tin vào file thành công.")

    def load_from_file(self, filename="accounts.json"):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for username, password in data.items():
                    self.accounts[username] = Account(username, password)
                print("Tải thông tin từ file thành công.")
        except FileNotFoundError:
            print("File không tồn tại.")

    def print_accounts(self):
        if self.accounts:
            for username, account in self.accounts.items():
                print(f"Tài khoản: {username}, Mật khẩu: {account.password}")
        else:
            print("Không có tài khoản nào.")

def main():
    manager = AccountManager()
    manager.load_from_file()
    
    while True:
        print("\nMENU:")
        print("1. Đăng ký tài khoản")
        print("2. Đăng nhập")
        print("3. Đổi mật khẩu")
        print("4. Lưu thông tin tài khoản vào file")
        print("5. In ra thông tin các tài khoản và mật khẩu")
        print("6. Exit")
        
        choice = input("Chọn một tùy chọn: ")

        if choice == '1':
            username = input("Nhập tên tài khoản: ")
            password = input("Nhập mật khẩu: ")
            manager.register(username, password)

        elif choice == '2':
            username = input("Nhập tên tài khoản: ")
            password = input("Nhập mật khẩu: ")
            manager.login(username, password)

        elif choice == '3':
            username = input("Nhập tên tài khoản: ")
            new_password = input("Nhập mật khẩu mới: ")
            manager.change_password(username, new_password)

        elif choice == '4':
            manager.save_to_file()

        elif choice == '5':
            manager.print_accounts()

        elif choice == '6':
            print("Chương trình kết thúc.")
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()
