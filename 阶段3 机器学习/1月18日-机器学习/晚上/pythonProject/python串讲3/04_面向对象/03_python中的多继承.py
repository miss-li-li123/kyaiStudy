# 1.先定义类
# 定义Father类
class Father(object):
    def skill(self):
        print('生活中各种技能')


# 定义黑马学校类
class HM(object):
    def skill(self):
        print('AI大模型的技能')


# TOOD 多继承
class Student(Father, HM):
    def skill(self):
        # 如果子类想调用父类的同名方法
        # super().skill()  只找第一个父类的
        # 父类名.skill() 灵活
        Father.skill(self)
        HM.skill(self)



# 2.根据类创建对象
s = Student()
s.skill()  # 如果两个父类方法重名,优先使用第一个父类的
# 具体查找顺序
print(Student.mro())
print(Student.__mro__)
