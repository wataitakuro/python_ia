from django.db import models

# Create your models here.

class StaffInformation(models.Model):
    staff_name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', blank=True, null=True)
    adress = models.CharField('住所', blank=True, null=True, max_length=100)
    birthday = models.DateTimeField('誕生日', blank=True, null=True)
    hire_date = models.DateField('入社日', blank=True, null=True)
    at_desk = models.BooleanField('出社状態', default=False)

class Staff(models.Model):
    name = models.CharField('ビジネスネーム', maxlength=100)
    information = models.OneToOneField(
        StaffInformation, on_delete=models.CASCADE,
        verbose_name='社員情報', null=True, blank=True
    )

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField('部署名', unique=True, max_length=100)

    def __str__(self):
        return self.name

    department = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        verbose_name='所属部署', null=True,blank=True
    )

    def __str__(self):
        return self.name

