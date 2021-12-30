
from django.db import models
from .manager import CustomUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.

POSITION_CHOICES = (
    ("___", "____"),
    ("CEO", "CEO"),
    ("HR", "HR"),
    ("Project Manager", "PROJECT MANAGER"),
    ("Technical Lead/Team Leader", "TECHNICAL LEAD/TEAM LEADER"),
    ("Chief Architect", "CHIEF ARCHITECT"),
    ("Software Architect", "SOFTWARE ARCHITECT"),
    ("Senior Software Developer", "SENIOR SOFTWARE DEVELOPER"),
    ("Software Engineer", "SOFTWARE ENGINEER"),
    ("Junior Software Developer", "JUNIOR SOFTWARE DEVELOPER"),
    ("Intern Software Developer", "INTERN SOFTWARE DEVELOPER"),
    ("Software Administrator", "SOFTWARE ADMINISTRATOR"),
    ("abcd", "ABCD"),
)

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)


# def emp_id():
#     r = range(1000, 2000)
#     r += 1
#     employee_id = r
#     return employee_id
# lambda: User.objects.get('id').employee_id + 1

class User(AbstractUser):
    """ User table """
    username = None
    # override username and email(unique)
    employee_id = models.CharField(max_length=50, default=0)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICE, blank=True)
    is_employee = models.BooleanField(default=False)
    role = models.CharField(max_length=100, choices=POSITION_CHOICES, default=None, null=True)
    employment_date = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=15)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    address = models.CharField(max_length=15, default="", blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Project(models.Model):
    """ Assign projects to employees """
    project_name = models.CharField(max_length=50, default=None, unique=True)
    project_owner = models.CharField(max_length=50, default=None, null=True)
    budget = models.CharField(max_length=15, null=True)
    owner_address = models.CharField(max_length=200, null=True, blank=True)
    descriptions = models.TextField(max_length=1000)
    date_of_assign = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name

    @property
    def status_message(self):
        """ ok"""
        return "Running" if self.status else "Closed"


class ProjectDevelopment(models.Model):
    """ Project Development status """
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_fields', blank=True, null=True)
    team_leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_leader', blank=True, null=True)
    team = models.ManyToManyField(User, related_name='User', blank=True)
    dead_line = models.DateField(blank=True, null=True)
    progress = models.TextField(max_length=1000, null=True, default='working on')

    def __str__(self):
        return self.project.project_name


class Attendance(models.Model):
    """ Employees Attendance"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False, null=True)
    presents = models.CharField(max_length=50, default=0)
    leaves = models.CharField(max_length=50, default=0)
    absents = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.user_id.name
