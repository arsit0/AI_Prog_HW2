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
        print("0. 退出系统")

        choice = input("请输入功能编号：").strip()

        if choice == "1":
            # 输入要查询的学号
            student_id = input("请输入要查找的学号：").strip()

            # 调用系统方法查找学生
            student = system.find_student_by_id(student_id)

            # 判断是否找到
            if student:
                print("\n查询结果：")
                print(student)
            else:
                print("未找到该学号对应的学生信息，请检查后重新输入。")

        elif choice == "0":
            print("系统已退出。")
            break

        else:
            print("输入的功能编号无效，请重新输入。")


if __name__ == "__main__":
    main()