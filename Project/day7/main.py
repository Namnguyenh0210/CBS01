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

    # def save_to_file(self):
    #     with open("accounts.txt", "w") as file:
    #         for username, account in self.accounts.items():
    #             file.write(f"{username},{account.password}\n")

    # def load_from_file(self):
    #     with open("accounts.txt", "r") as file:
    #         for line in file:
    #             username, password = line.strip().split(",")
    #             self.accounts[username] = account(username, password)

    # def print_accounts(self):
    #     if self.accounts:
    #         for username, account in self.accounts.items():
    #             print(f"Tài khoản: {username}, Mật khẩu: {account.password}")
    #     else:
    #         print("Không có tài khoản nào")

def main():
    # manager = account_manager()
    # manager.load_from_file()

    while True:
        print("\nMENU:")
        print("1. Đăng ký tài khoản")
        print("2. Đăng nhập")
        print("3. Đổi mật khẩu")
        print("4. Lưu thông tin tài khoản vào file")
        print("5. In ra thông tin các tài khoản và mật khẩu")
        print("6. Exit")

        choice = input("Chọn một lựa chọn: ")
    swiche 
        

       



if __name__ == "__main__":
    main()              

