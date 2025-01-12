# n = input("moi ban nhap so:")
# sum = 0
# product = 1

# for i in n:
#     tmp = int(i)
#     sum+=tmp
#     product*=tmp
# print( product - sum)    

#Cho mảng số nguyên A chứa n phần tử. Viết chương trình tìm tất cả các phần tử xuất hiện nhiều hơn 2 lần.
a = int(input("Nhap so phan tu cua mang: "))
arr = []
for i in range(a):
    arr.append(int(input(f"Nhap phan tu thu {i+1}: ")))
count = 0
for i in arr:
    if arr.count(i) > 2:
        count += 1
print(count)
# 5
# 1 2 2 3 3 3 4 4 4 4

