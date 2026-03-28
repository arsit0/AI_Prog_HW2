#依旧粘个防伪标识，以防被误判为人机....
import os
from student import Student


class ExamSystem:
    """考场管理系统：负责读取学生名单并保存学生对象列表"""

    def __init__(self, file_path):
        # 保存学生名单文件路径
        self.file_path = file_path
        # 用列表保存所有 Student 对象
        self.students = []
        # 初始化时自动读取学生名单
        self.load_students()

    @staticmethod
    def is_valid_student_id(student_id):
        # 静态方法：用于判断学号是否为纯数字
        return str(student_id).isdigit()

    def load_students(self):
        """读取学生名单文件，并将每一行数据转换为 Student 对象"""
        try:
            # 打开学生名单文件，使用 utf-8 编码读取
            with open(self.file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # 跳过第一行表头，从第二行开始读取真正的学生数据
            for line in lines[1:]:
                # 去掉每行首尾的空白字符和换行符
                line = line.strip()

                # 如果这一行是空行，就跳过
                if not line:
                    continue

                # 按制表符分割一行数据
                parts = line.split("\t")

                # 如果这一行字段数量不足 6 个，说明数据格式不完整，直接跳过
                if len(parts) < 6:
                    continue

                # 根据名单文件格式依次取出需要的字段
                name = parts[1]
                gender = parts[2]
                class_name = parts[3]
                student_id = parts[4]
                college = parts[5]

                # 创建 Student 对象
                student = Student(student_id, name, gender, class_name, college)

                # 加入学生列表
                self.students.append(student)

        except FileNotFoundError:
            print(f"错误：未找到学生名单文件 -> {self.file_path}")
        except Exception as e:
            print(f"读取学生名单时发生错误：{e}")

    def find_student_by_id(self, student_id):
        """按学号查找学生对象，找到则返回 Student，找不到返回 None"""
        # 先把输入转成字符串并去掉空格
        student_id = str(student_id).strip()

        # 如果学号不是纯数字，直接返回 None
        if not self.is_valid_student_id(student_id):
            return None

        # 遍历学生列表，寻找匹配学号的学生
        for student in self.students:
            if student.student_id == student_id:
                return student

        # 如果循环结束都没找到，就返回 None
        return None