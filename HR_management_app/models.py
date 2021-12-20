from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

POSITION_CHOICES = (
    ("1", "PROJECT MANAGER"),
    ("2", "TECHNICAL LEAD/TEAM LEADER"),
    ("3", "CHIEF ARCHITECT"),
    ("4", "SOFTWARE ARCHITECT"),
    ("5", "SENIOR SOFTWARE DEVELOPER"),
    ("6", "SOFTWARE ENGINEER"),
    ("7", "JUNIOR SOFTWARE DEVELOPER"),
    ("8", "INTERN SOFTWARE DEVELOPER"),
    ("9", "SOFTWARE ADMINISTRATOR"),
    ("abc", "ABCD"),

),

GENDER_CHOICE = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)


class User(AbstractUser):
    """ User table """
    username = None
    # override username and email(unique)
    name = models.CharField(max_length=100,  null=False)
    email = models.EmailField(max_length=200, unique=True, blank=False)
    gender = models.EmailField(max_length=200, choices=GENDER_CHOICE, blank=True)
    is_employee = models.BooleanField(default=False)
    role = models.CharField(max_length=100, choices=POSITION_CHOICES, default=None, null=False)
    contact = models.CharField(max_length=15, blank=False)
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    address = models.CharField(max_length=15, default=None, blank=True, null=True)

    REQUIRED_FIELDS = ['email', ]

    # require the email to be the unique identifier
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


# company assets, owned by the employer
class Project(models.Model):
    """ Assign projects to employees """
    title = models.CharField(max_length=50, blank=False, primary_key=True)
    description = models.TextField(max_length=1000)
    date_of_assign = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Development(models.Model):
    """ Project Development status """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.project.title


class Attendance(models.Model):
    """ Employees Attendance"""
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False, null=True)
    presents = models.CharField(default=0)
    leavs = models.CharField(default=0)
    absents = models.CharField(default=0)

    def __str__(self):
        return self.project.title
