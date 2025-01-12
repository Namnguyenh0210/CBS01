# print("\nHello World!\n")

# name = input("What is your name? ")
# print("Hello " + name + "!")

# """
# day la comment nhieu lan
# """

number1 = input("nhap so thu 1: ")
number2 = input("nhap so thu 2: ")

sum = float(number1) + float(number2)
difference = float(number1) - float(number2)
product = float(number1) * float(number2)
quotient = float(number1) / float(number2) 

print("tong cua {0} va {1} la: {2}".format(number1, number2, sum))
print("hieu cua {0} va {1} la: {2}".format(number1, number2, difference))
print("tich cua {0} va {1} la: {2}".format(number1, number2, product))
print("thuong cua {0} va {1} la: {2}".format(number1, number2, quotient))
