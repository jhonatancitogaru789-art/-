# name = input("请输入学生姓名：")
# score = float(input("请输入学生成绩："))
# def add_student():
#     students = []
#     count = int(input("请输入学生数量："))
#     for i in range(count):
#         name = input("请输入学生姓名：")
#         score = float(input("请输入学生成绩："))
#         students.append((name, score))
#         print("学生信息已添加！")
# def find_student():
#     name = input("请输入要查询的学生姓名：")
#     for student in students:
#         if student[0] == name:
#             print(f"姓名 = {student[0]}, 成绩 = {student[1]} ")
#         else:
#             print("未找到该学生信息！")
# def display_students():
#     print("学生成绩列表：")
#     for student in students:
#         print(f" 姓名 = {student[0]}, 成绩 = {student[1]}")
def main():
    while True:
        print("=== 学生成绩管理系统 ===")
        print("1. 添加学生信息\t\t[输入1]")
        print("2. 查询学生信息\t\t[输入2]")
        print("3. 显示所有学生信息\t[输入3]")
        print("4. 退出系统\t\t[输入4]")
main()

     


