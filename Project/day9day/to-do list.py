# Hãy tạo một chương trình mô phỏng trình quản lý danh sách việc cần làm (to-do list) bằng cách sử dụng hàng đợi (queue). Chương trình phải cho phép người dùng thực hiện các thao tác sau:

# Thêm một công việc vào danh sách việc cần làm.
# Nếu công việc đã có trong danh sách, thì bỏ qua và không thêm lại.
# Hiển thị danh sách việc cần làm sau khi tất cả các công việc đã được thêm vào.


import queue

class ToDoList:
    def __init__(self):
        self.queue = queue.Queue()
        self.tasks = set() # dung de loc ra nhung cai trung nhau va gom no vao thanh 1

    def add_task(self, task):
        self.queue.put(task)
        self.tasks.add(task)
        print(f"Đã thêm '{task}' vào danh sách việc cần làm.")


    def display_tasks(self):
        print("Danh sách việc cần làm:")
        for task in self.tasks:
            print(f"- {task}")

todo_list = ToDoList()


# Thêm vào danh sách việc cần làm
todo_list.add_task("Đọc Python")
todo_list.add_task("Thiết kế ứng dụng web")
todo_list.add_task("Chạy ứng dụng")
todo_list.add_task("Thiết kế ứng dụng web")
todo_list.add_task("Chạy ứng dụng")

todo_list.display_tasks()


