from django.db import models

class HomePage(models.Model):
    message_from_founder = models.TextField(verbose_name="Message from the Founder")
    smart_learner = models.TextField(verbose_name="Smart Learner")
    our_mission = models.TextField(verbose_name="Our Mission")
    our_vision = models.TextField(verbose_name="Our Vision")
    why_smart_learner = models.TextField(verbose_name="Why Smart Learner?")
    free_education = models.TextField(verbose_name="Every child deserves the chance to learn.")

    def __str__(self):
        return "Home Page Content"

class skillbasedECprograms(models.Model):
    programs_included = models.TextField(verbose_name="Programs Included")
    program_highlights = models.TextField(verbose_name="Program Highlights")

    def __str__(self):
        return "Skill-Based Extracurricular Programs Page Content"

class PoliciesProcedures(models.Model):
    enrollment_policy = models.TextField(verbose_name="Enrollment Policy")
    attendance_policy = models.TextField(verbose_name="Attendance Policy")
    assessments_policy = models.TextField(verbose_name="Assessments Policy")
    code_of_conduct = models.TextField(verbose_name="Code of Conduct")
    cost_saving_benefits = models.TextField(verbose_name="Cost-Saving Benefits")

    def __str__(self):
        return "Policies & Procedures Page Content"

class contactusForm(models.Model):
    parent_name = models.CharField(max_length=100, verbose_name="Parent Name")
    student_first_name = models.CharField(max_length=50, verbose_name="Student First Name")
    student_last_name = models.CharField(max_length=50, verbose_name="Student Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    country = models.CharField(max_length=50, verbose_name="Country")

    def __str__(self):
        return f"Contact Form - {self.parent_name}"

class registrationForm(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    GRADE_CHOICES = [
        (1, 'Class 1'),
        (2, 'Class 2'),
        (3, 'Class 3'),
        (4, 'Class 4'),
        (5, 'Class 5'),
        (6, 'Class 6'),
        (7, 'Class 7'),
        (8, 'Class 8'),
        (9, 'Class 9'),
        (10, 'Class 10'),
    ]
    
    parent_name = models.CharField(max_length=100, verbose_name="Parent Name")
    student_first_name = models.CharField(max_length=50, verbose_name="Student First Name")
    student_last_name = models.CharField(max_length=50, verbose_name="Student Last Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    country = models.CharField(max_length=50, verbose_name="Country")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    grade = models.IntegerField(choices=GRADE_CHOICES, verbose_name="Grade")
    age = models.IntegerField(verbose_name="Age")
    subject = models.CharField(max_length=100, verbose_name="Subject of Interest")

    def __str__(self):
        return f"Registration - {self.student_first_name} {self.student_last_name}"