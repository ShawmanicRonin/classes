from Student import Student
from graduate_student import Graduate_Student
       
#jay_pike is an instance of the student class
jay_pike = Student.from_fullname("Jay Pike", "Sophomore", 3456) #Object of the student class
jane_doe = Student("Jane", "Doe", "Senior", 1234) #object of the student class
waldo_wildcat = Student("Waldo", "Wildcat", "Senior")
grad_student1 = Graduate_Student("Michael", "Scott", "Graduate")

all_students_in_class = Student.get_all_students()
for student in all_students_in_class:
    student.print_student_data()
    
    
#     SWORD class
#     attack:
#         sound clink
        
#     GUN class
#     attack:
#         sound boom
#         ammo -=1
        
        
# weapon.attack