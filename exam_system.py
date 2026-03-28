#依旧粘个防伪标识，以防被误判为人机....
import os
import random
from datetime import datetime
from student import Student


class ExamSystem:
    """考场管理系统：负责读取学生名单并保存学生对象列表"""

    def __init__(self, file_path):
        # 保存学生名单文件路径
        self.file_path = file_path
        # 用列表保存所有 Student 对象
        self.students = []
        # 保存考场安排结果，列表中的每个元素是 (座位号, student对象)
        self.exam_arrangement = []
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
        student_id = str(student_id).strip()

        if not self.is_valid_student_id(student_id):
            return None

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def random_call(self, count):
        """随机点名：返回指定数量的不重复学生对象列表"""
        if count <= 0:
            raise ValueError("点名人数必须大于 0。")

        if count > len(self.students):
            raise ValueError("点名人数不能超过学生总人数。")

        return random.sample(self.students, count)

    def generate_exam_arrangement(self):
        """生成考场安排表文件，并返回输出文件路径"""
        if not self.students:
            raise ValueError("当前没有学生数据，无法生成考场安排表。")

        # 复制一份学生列表，避免直接打乱原列表
        shuffled_students = self.students[:]
        random.shuffle(shuffled_students)

        # 清空旧的考场安排结果
        self.exam_arrangement = []

        # 为每个学生分配座位号，座位号从 1 开始
        for seat_number, student in enumerate(shuffled_students, start=1):
            self.exam_arrangement.append((seat_number, student))

        # 获取当前脚本所在目录，确保文件生成在项目根目录
        base_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(base_dir, "考场安排表.txt")

        # 按要求生成时间字符串
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(f"生成时间：{now_str}\n")
            file.write("座位号\t姓名\t学号\n")

            for seat_number, student in self.exam_arrangement:
                file.write(f"{seat_number}\t{student.name}\t{student.student_id}\n")

        return output_path

    def generate_admission_tickets(self):
        """生成准考证目录与文件，并返回准考证文件夹路径"""
        # 如果还没有考场安排，就先自动生成
        if not self.exam_arrangement:
            self.generate_exam_arrangement()

        # 获取项目根目录
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # 创建“准考证”文件夹
        ticket_dir = os.path.join(base_dir, "准考证")
        os.makedirs(ticket_dir, exist_ok=True)

        # 按考场安排为每位学生生成对应准考证文件
        for seat_number, student in self.exam_arrangement:
            # 文件名格式要求：01.txt、02.txt……
            file_name = f"{seat_number:02d}.txt"
            file_path = os.path.join(ticket_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write("准考证\n")
                file.write(f"座位号：{seat_number}\n")
                file.write(f"姓名：{student.name}\n")
                file.write(f"学号：{student.student_id}\n")

        return ticket_dir