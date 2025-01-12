import time

# Hàm tìm kiếm tuần tự
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Hàm tìm kiếm nhị phân (mảng phải được sắp xếp trước)
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Hàm đo thời gian chạy và in kết quả
def test_search_algorithms(arr, x):
    # Thời gian chạy của linear_search
    start_time = time.time()
    linear_result = linear_search(arr, x)
    linear_time = time.time() - start_time
    
    # Thời gian chạy của binary_search
    start_time = time.time()
    binary_result = binary_search(arr, x)
    binary_time = time.time() - start_time
    
    print(f"Kết quả tìm kiếm tuần tự: {linear_result}, Thời gian chạy: {linear_time:.6f} giây")
    print(f"Kết quả tìm kiếm nhị phân: {binary_result}, Thời gian chạy: {binary_time:.6f} giây")

# Ví dụ sử dụng
arr = list(range(100000))  # Mảng mẫu với 100000 phần tử đã sắp xếp
x = 99999  # Phần tử cần tìm

test_search_algorithms(arr, x)
