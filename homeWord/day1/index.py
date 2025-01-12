def tong_so_le(n):
    tong = sum(i for i in range(1, n+1) if i % 2 != 0)
    return tong

def la_so_nguyen_to(n):
    
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def uoc_so(n):
    uoc = [i for i in range(1, n + 1) if n % i == 0]
    return uoc

n = int(input("Nhập một số nguyên dương n: "))
print(f"Tổng các số lẻ từ 1 đến {n}: {tong_so_le(n)}")

if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")

print(f"Các ước số của {n} là: {uoc_so(n)}")



# def main():
#     total = 0
#     while True:
#         number = input("nhap so mot nguyen: ")
#         if number == " " or number == "":
#             break
#     print("The total is:", total)
#     try: 
#         number = int(number)
#         total += number
#     except ValueError:
#         print("nhap so nguyen")
# print("The total is:{total}",)

# if __name__ == "__main__":
#     main()


