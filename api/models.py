from django.db import models

class User(models.Model):
  login = models.CharField(max_length=256, unique=True)
  password = models.CharField(max_length=256)
  token = models.CharField(max_length=256, null=True)
  role = models.ForeignKey('Role', default=2, on_delete=models.SET_DEFAULT)
  name = models.CharField(max_length=256)
  surname = models.CharField(max_length=256)
  patronymic = models.CharField(max_length=256)

  def __str__(self):
    return self.login

class Role(models.Model):
  name = models.CharField(max_length=256)
  users = models.BooleanField(default=False)
  lessons = models.BooleanField(default=False)
  exams = models.BooleanField(default=False)
  exams_admin = models.BooleanField(default=False)
  disciplines = models.BooleanField(default=False)
  groups = models.BooleanField(default=False)
  docs = models.BooleanField(default=False)

  def __str__(self):
    return self.name

class Discipline(models.Model):
  name = models.CharField(max_length=256)
  teacher = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.name

class Theme(models.Model):
  name = models.CharField(max_length=256)
  discipline = models.ForeignKey('Discipline', null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return self.name

class Group(models.Model):
  name = models.CharField(max_length=256)
  date_create = models.DateField()

  def __str__(self):
    return self.name

class Statement(models.Model):
  date_open = models.DateField()
  date_close = models.DateField(null=True)
  discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)
  group = models.ForeignKey('Group', on_delete=models.CASCADE)

  def __str__(self):
    return str(self.date_open) + ' - ' + str(self.discipline)

class Lesson(models.Model):
  date = models.DateField()
  statement = models.ForeignKey('Statement', on_delete=models.CASCADE)
  # theme = models.CharField(max_length=256)
  theme = models.ForeignKey('Theme', on_delete=models.CASCADE)
  homework = models.CharField(max_length=256, null=True)
  control1 = models.CharField(max_length=256, null=True)
  control2 = models.CharField(max_length=256, null=True)

  def __str__(self):
    return str(self.date) + ' - ' + str(self.theme)

class Student(models.Model):
  name = models.CharField(max_length=256)
  surname = models.CharField(max_length=256)
  patronymic = models.CharField(max_length=256, null=True)
  group = models.ForeignKey('Group', on_delete=models.CASCADE)
  record_book = models.CharField(max_length=256, null=True)

  def __str__(self):
    return str(self.name) + ' ' + str(self.surname) + ' из ' + str(self.group)

class Record(models.Model):
  lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
  student = models.ForeignKey('Student', on_delete=models.CASCADE)
  mark1 = models.CharField(max_length=1, default='*')
  mark2 = models.CharField(max_length=1, default='*')

class Exam(models.Model):
  date = models.DateField()
  group = models.ForeignKey('Group', on_delete=models.CASCADE)
  discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE)
  closed = models.BooleanField()

  def __str__(self):
    return str(self.date) + ' - ' + str(self.discipline)

class ExamList(models.Model):
  exam = models.ForeignKey('Exam', on_delete=models.CASCADE)
  student = models.ForeignKey('Student', on_delete=models.CASCADE)
  ticket = models.CharField(max_length=256, null=True)
  mark = models.CharField(max_length=1, null=True)

  def __str__(self):
    return str(self.exam) + ' - ' + str(self.student) + ' - ' + str(self.mark)
