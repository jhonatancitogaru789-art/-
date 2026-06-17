students = []

def add_student():
    count = int(input("请输入学生数量："))
    for i in range(count):
        name = input("请输入学生姓名：")
        score = float(input("请输入学生成绩："))
        student = {"name": name, "score": score}
        students.append(student)
    print("学生信息已添加！")

def find_student():
    name = input("请输入要查询的学生姓名：")
    found = False
    for student in students:
        if student["name"] == name:
            print(f"姓名 = {student['name']}, 成绩 = {student['score']}")
            found = True
            break
    if not found:
        print("未找到该学生信息！")

def display_students():
    print("学生成绩列表：")
    for student in students:
        print(f"姓名 = {student['name']}, 成绩 = {student['score']}")

while True:
    print("\n=== 学生成绩管理系统 ===")
    print("1. 添加学生信息\t[输入1]")
    print("2. 查询学生信息\t[输入2]")
    print("3. 显示所有学生信息\t[输入3]")
    print("4. 退出系统\t[输入4]")

    choice = input("请输入操作选项：")

    if choice == "1":
        add_student()
    elif choice == "2":
        find_student()
    elif choice == "3":
        display_students()
    elif choice == "4":
        print("退出系统！")
        break
    else:
        print("无效输入，请重新选择操作选项！")


