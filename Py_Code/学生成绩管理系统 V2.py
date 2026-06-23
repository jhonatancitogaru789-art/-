students = []
def get_student_name(name):
    for student in students:
        if student["name"] == name:
            return student
    return None
def add_student():
    count =int(input("请输入需要添加到学生数量；"))
    for i in range(count):
        student = {"name": input("请输入学生姓名："), \
                   "score": float(input("请输入学生成绩：")), \
                   "age": int(input("请输入学生年龄："))}
        students.append(student)
        print("学生信息已添加！")
def find_student():
    print("a. 按姓名查询学生信息")
    print("b. 按成绩查询学生信息")
    print("c. 按年龄查询学生信息")
    choice = input("请选择查询方式：")
    if choice =="a":
        name = input("请输入要查询的学生姓名：")
        student = get_student_name(name)
        if student is None:
            print("未找到该学生信息！")
        else:
            print(f"姓名 = {student['name']}, 成绩 = {student['score']}, 年龄 = {student['age']}")
    elif choice =="b":
        score = float(input("请输入要查询的学生成绩："))
        found = False
        for student in students:
            if student["score"] == score:
                print(f"姓名 = {student['name']}, 成绩 = {student['score']}, 年龄 = {student['age']}")
                found = True
                break
        if not found:
            print("未找到该成绩的学生！")
    elif choice =="c":
        age = int(input("请输入要查询的学生年龄："))
        found = False
        for student in students:
            if student["age"] == age:
                print(f"姓名 = {student['name']}, 成绩 = {student['score']}, 年龄 = {student['age']}")
                found = True
                break
        if not found:
            print("未找到该年龄的学生！")
def display_students():
    print("全部学生成绩列表：")
    for student in students:
            print(f"姓名 = {student['name']}, 成绩 = {student['score']}, 年龄 = {student['age']}")
def modify_student():
    name = input("请输入要修改的学生姓名：")
    student = get_student_name(name)
    if student is None:
        print("未找到该学生信息！")
        return
    print("a. 修改姓名")
    print("b. 修改成绩")
    print("c. 修改年龄")
    choice = input("请选择修改内容：")
    if choice == "a":
        new_name = input("请输入新的学生姓名：")
        student["name"] = new_name
        print("学生姓名已修改！")
    elif choice == "b":
        new_score = float(input("请输入新的学生成绩："))
        student["score"] = new_score
        print("学生成绩已修改！")
    elif choice == "c":
        new_age = int(input("请输入新的学生年龄："))
        student["age"] = new_age
        print("学生年龄已修改！")
    else:
        print("无效输入，请重新选择！")
def delete_student():
    name = input("请输入要删除的学生姓名：")
    student = get_student_name(name)
    if student is None:
        print("未找到该学生信息！")
        return
    del student
    print("学生信息已删除！")
def statistic():
    if len(students) == 0:
        print("没有学生信息，无法进行统计！")
        return
    students_count = len(students)
    highest_score = students[0]["score"]
    lowest_score = students[0]["score"]
    fail_count = 0
    total_score = 0
    for student in students:
        if student["score"] > highest_score:
            highest_score = student["score"]
        if student["score"] < lowest_score:
            lowest_score = student["score"]
        if student["score"] < 60:
            fail_count += 1
        total_score += student["score"]
        average_score = total_score / students_count
    print(f"学生总数 = {students_count}")
    print(f"平均成绩 = {average_score}")
    print(f"最高成绩 = {highest_score}")
    print(f"最低成绩 = {lowest_score}")
    print(f"不及格人数 = {fail_count}")
def menu():
    while True:
        print("=== 学生成绩管理系统 ===")
        print("1. 添加学生信息\t[输入1]")
        print("2. 查询学生信息\t[输入2]")
        print("3. 显示所有信息\t[输入3]")
        print("4. 修改学生信息\t[输入4]")
        print("5. 删除学生信息\t[输入5]")
        print("6. 统计学生信息\t[输入6]")
        print("0. 退出系统\t[输入0]")
        choice = input("请选择操作：")
        if choice == "1":
            add_student()
        elif choice == "2":
            find_student()
        elif choice == "3":
            display_students()
        elif choice == "4":
            modify_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            statistic()
        elif choice == "0":
            print("感谢使用学生成绩管理系统！")
            break
        else:
            print("无效输入，请重新选择！")
menu()
