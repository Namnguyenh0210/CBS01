# Hàm thêm điểm mới vào danh sách
def them_diem(danh_sach_diem):
    diem_moi = input("Nhập điểm mới (0-100): ")
    
    try:
        diem_moi = float(diem_moi)
        if 0 <= diem_moi <= 100:
            danh_sach_diem.append(diem_moi)
            print(f"Đã thêm điểm {diem_moi}")
        else:
            print("Điểm không hợp lệ! Vui lòng nhập giá trị từ 0 đến 100.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")

# Hàm lưu danh sách điểm vào file
def luu_bao_cao(danh_sach_diem, ten_file="grades.txt"):
    with open(ten_file, "w") as file:
        # luoc bo di close khi can dong file
        for diem in danh_sach_diem:
            file.write(f"{diem}\n")
    print(f"Đã lưu báo cáo vào file {ten_file}")

# Chương trình chính
def main():
    danh_sach_diem = []
    
    # Đọc điểm từ file (nếu đã tồn tại)
    try:
        with open("grades.txt", "r") as file:
            danh_sach_diem = [float(line.strip()) for line in file.readlines()]
        print("Đã tải danh sách điểm từ file.")
    except FileNotFoundError:
        print("Chưa có file grades.txt, sẽ tạo mới khi lưu.")

    while True:
        print("\nChọn một tùy chọn:")
        print("1. Thêm điểm mới")
        print("2. Lưu và thoát")
        lua_chon = input("Lựa chọn: ")

        if lua_chon == "1":
            them_diem(danh_sach_diem)
        elif lua_chon == "2":
            luu_bao_cao(danh_sach_diem)
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

    print("Đã thoát.")
    

if __name__ == "__main__":
    main()

