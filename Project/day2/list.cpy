nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(nums)

#  do dai list
print(len(nums))
# len tra ve do dai cua 1 chuoi kieu du lieu (in)

#thay doi gia tri
animals = ['cat', 'dog', 'rabbit']
animals[1] = 'ferret'
print(animals)

#xoa phan tu
mixed = ['a', 1, 'b', 2, 'c', 3]
del mixed[0:3]
print(mixed)


#them phan tu
mixed.append('d')
print(mixed)

#duyet phan tu
for i in mixed:
    print(i) 

#tim kiem phan tu
print('a' in mixed)

# #sap xep giam dan
# mixed.sort(reverse=True)
# print(mixed)

# #sap xep tang dan
# mixed.sort()
# print(mixed)



