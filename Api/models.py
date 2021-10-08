from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Difficulty(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class MathQ(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    option1 = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    option1 = models.CharField(max_length=250)
    answer = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.course

class Info(models.Model):
    notice = models.CharField(max_length=100)
    break_time = models.IntegerField(default=0)
    daily_bonus = models.CharField(max_length=250)
    dollar_for_instll = models.CharField(max_length=250)
    how_to_work_link = models.CharField(max_length=250)
    math_point = models.CharField(max_length=250)
    watch_video_point = models.CharField(max_length=250)
    need_help = models.CharField(max_length=250)
    privacy_link = models.CharField(max_length=250)
    rateus_link = models.CharField(max_length=250)
    telegram_link = models.CharField(max_length=250)
    wathdraw_notice = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.notice

class Withdraw(models.Model):
    Status = (
        ('Success', 'Success'),
        ('Pending', 'Pending'),
    )
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.CharField(max_length=100)
    amount = models.DecimalField(default=0, decimal_places=2, max_digits=15)
    method = models.CharField(max_length=250)
    status = models.CharField(max_length=30, choices=Status)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.account

     

    









