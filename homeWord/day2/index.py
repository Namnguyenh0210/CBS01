def average_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    if len(even_numbers) == 0:
        return 0
    return sum(even_numbers) / len(even_numbers)

# Ví dụ sử dụng
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))

print("Trung bình các số chẵn là:", average_even_numbers(numbers))
