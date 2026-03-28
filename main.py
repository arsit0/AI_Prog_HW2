from exam_system import ExamSystem
#非人机



def main():
    # 创建系统对象，程序启动时自动读取学生名单文件
    system = ExamSystem("人工智能编程语言学生名单.txt")

    # 如果没有成功读取到学生数据，就结束程序
    if not system.students:
        print("系统初始化失败：没有读取到学生数据。")
        return

    while True:
        print("\n===== 学生信息与考场管理系统 =====")
        print("1. 按学号查找学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证文件")
        print("0. 退出系统")

        choice = input("请输入功能编号：").strip()

        if choice == "1":
            student_id = input("请输入要查找的学号：").strip()
            student = system.find_student_by_id(student_id)

            if student:
                print("\n查询结果：")
                print(student)
            else:
                print("未找到该学号对应的学生信息，请检查后重新输入。")

        elif choice == "2":
            try:
                count = int(input("请输入要随机点名的人数：").strip())
                selected_students = system.random_call(count)

                print("\n随机点名结果：")
                for index, student in enumerate(selected_students, start=1):
                    print(f"\n第{index}位：")
                    print(student)

            except ValueError as e:
                print(f"输入错误：{e}")

        elif choice == "3":
            try:
                output_path = system.generate_exam_arrangement()
                print(f"考场安排表已生成：{output_path}")
            except Exception as e:
                print(f"生成考场安排表失败：{e}")

        elif choice == "4":
            try:
                ticket_dir = system.generate_admission_tickets()
                print(f"准考证文件已生成：{ticket_dir}")
            except Exception as e:
                print(f"生成准考证失败：{e}")

        elif choice == "0":
            print("系统已退出。")
            break

        else:
            print("输入的功能编号无效，请重新输入。")


if __name__ == "__main__":
    main()