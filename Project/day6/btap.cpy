def insertion_sort_desc(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        flag = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
                flag = True
        if not flag:
            break
    return arr

def check_sorted(arr, ascending=True):
    if ascending:
        return arr == sorted(arr)
    else:
        return arr == sorted(arr, reverse=True)

def main():
    # Nhập kích thước mảng N
    while True:
        try:
            N = int(input("Nhập kích thúc mảng 11112: "))
            if N > 0:
                break
            else:
                print("Kích thúc mảng phẢi nhất 1.")
        except ValueError:
            print("Vui này nhập kích thúc mảng.")
    # Nhập mảng từ người dùng
    arr = []
    for i in range(N):
        while True:
            try:
                value = int(input(f"Nhập phần tử thứ {i + 1}: "))
                arr.append(value)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên.")
    
    # Hiển thị menu lựa chọn
    while True:
        print("\nMenu lựa chọn:")
        print("1. Sắp xếp theo thứ tự giảm dần (sử dụng Insertion Sort)")
        print("2. Sắp xếp theo thứ tự tăng dần (sử dụng Bubble Sort)")
        print("3. Thoát chương trình")
        choice = input("Chọn lựa: ")

        if choice == '1':
            if check_sorted(arr, ascending=False):
                print("MẢNG ĐÃ ĐƯỢC SẮP XẾP")
            else:
                sorted_arr = insertion_sort_desc(arr[:])  # Sử dụng bản sao của mảng
                print("Mảng sau khi sắp xếp giảm dần:", sorted_arr)

        elif choice == '2':
            if check_sorted(arr, ascending=True):
                print("MẢNG ĐÃ ĐƯỢC SẮP XẾP")
            else:
                sorted_arr = bubble_sort_asc(arr[:])  # Sử dụng bản sao của mảng
                print("Mảng sau khi sắp xếp tăng dần:", sorted_arr)

        elif choice == '3':
            print("Thoát chương trình.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
