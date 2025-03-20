# q1
# Base class Course
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"Course Code: {self.course_code}, Name: {self.course_name}, Credit Hours: {self.credit_hours}"

# Subclass CoreCourse
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        return super().display_info() + f", Required for Major: {self.required_for_major}"

# Subclass ElectiveCourse
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        return super().display_info() + f", Elective Type: {self.elective_type}"

# Creating objects and displaying information
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("ART201", "Modern Art", 2, "liberal arts")

print(core_course.display_info())
print(elective_course.display_info())
