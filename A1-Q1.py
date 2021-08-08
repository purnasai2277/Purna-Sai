
class Student:
    def student1(self,name1,rollno1,branch1):
        self.name1 = 'purna'
        self.rollno1 = 23008
        self.branch1 = 'AI&ML'
        print(f'Student Name : {self.name1}\nStudent Roll: {self.rollno1}\nStudent_branch: {self.branch1}')
    def student2(self,name2,rollno2 ,branch2):
        self.name2 = 'sai'
        self.rollno2 = 80032
        self.branch2 ='CSE'
        print(f'Student Nmae : {self.name2}\nStudent Roll: {self.rollno2}\nStudent_branch: {self.branch2}')
    def display():
        Student.student1
        Student.student2
Student.display()
