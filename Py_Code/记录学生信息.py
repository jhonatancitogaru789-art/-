students = []
count = 3
for i in range(count):
    name = input("请输入学生姓名：")
    score = float(input("请输入学生成绩："))
    students.append((name,score))
    print("学生信息已添加！")
    for student in students:
        print(student[0], student[1])
