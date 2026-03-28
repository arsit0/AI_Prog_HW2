class Student:
    """学生数据类：是为了保存单个学生的基础信息"""

    def __init__(self, student_id, name, gender, class_name, college):
        #保存学生学号，并去掉首尾空格（然后ctrl c+V+V+....）
        self.student_id = str(student_id).strip()
        #保存学生姓名，并去掉首尾空格
        self.name = str(name).strip()
        #保存学生性别，并去掉首尾空格
        self.gender = str(gender).strip()
        #保存学生班级，并去掉首尾空格
        self.class_name = str(class_name).strip()
        #保存学生学院，并去掉首尾空格
        self.college = str(college).strip()

    def __str__(self):
        #定义对象打印格式，后面 print(student) 时会直接显示这些信息(这是督促ai严格使用老师的面向对象oop的第一条)
        return (
            f"学号：{self.student_id}\n"
            f"姓名：{self.name}\n"
            f"性别：{self.gender}\n"
            f"班级：{self.class_name}\n"
            f"学院：{self.college}"
        #注释的语气写的好像ai啊，这是为什么呢（加上这句就不像了bushi）
        )