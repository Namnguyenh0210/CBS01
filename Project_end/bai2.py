# Cho mảng số nguyên nums chứa n phần tử.
# Viết chương trình tìm tất cả các phần tử xuất hiện nhiều hơn n/3 lần (làm tròn dưới).
# Giới hạn:
# • 1 <= nums.length <= 5 * 104
# • -109 <= nums[i] <= 109
# Yêu cầu:
# • Sử dụng cấu trúc dữ liệu phù hợp
# • Sử dụng thuật toán độ phức tạp O(n) để đạt tối đa số điểm

def find_repeating_elements(nums):
    n = len(nums)
    count = {} # từ điển luu lan suat hien cua phan tu
    for num in nums: 
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    result = []
    for num, freq in count.items(): # freq tần suất, count.items tra ve danh sach cac phan tu
        if freq > n // 3:
            result.append(num)

    return result

nums = [1,2]

result = find_repeating_elements(nums)
print(result)