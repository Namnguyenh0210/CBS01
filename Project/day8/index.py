#Viết chương trình cho người dùng nhập vào tên và họ rồi in ra tên đầy đủ của họ.
name = input("Enter your name: ")
last_name = input("Enter your last name: ")

full_name = f"{last_name}, {name}"

print(f"Your full name is: {full_name}")


# Viết chương trình chuyển những gì người dùng nhập vào
# thành chữ hoa.


text = input("Enter some text: ")

upper_case_text = text.upper()

print(f"Your text in upper case is: {upper_case_text}")

# Viết chương trình cho người dùng nhập vào một số rồi in ra
# bình phương của số vừa nhập.


number = int(input("Enter a number: "))
square = number ** 2
print(f"The square of {number} is: {square}")

# Viết chương trình cho người dùng nhập vào một số rồi dùng
# turtle vẽ một hình tròn có bán kính đúng bằng số mà người
# dùng nhập vào.

import turtle

number = int(input("Enter a number: "))
turtle.circle(number)
turtle.done()

