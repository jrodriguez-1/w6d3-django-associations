from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Student: {self.name}"

class Instructor(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"Instructor: {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128, default="")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return f"Course: {self.name}"

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    grade = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return f"{self.student} is enrolled in {self.course}. Grade: {'none' if self.grade is None else self.grade}"


