from django.db import models


# Create your models here.


class Department(models.Model):
    """"部门表"""
    title = models.CharField(verbose_name="部门标题", max_length=32)


class UserInfo(models.Model):
    """"员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateTimeField(verbose_name="创建时间")
    # 无约束
    # department_id = models.IntegerField(verbose_name="部门ID")

    # 有约束
    # to与那一张表关联
    # to_fields与表中那一列关联
    depart = models.ForeignKey(to="Department",to_field='id', null=True, blank=True, on_delete=models.CASCADE)

    gender_choices = (
        (1, "男"),
        (1, "女"),
    )
    gender = models.SmallIntegerField(verbose_name="性别", null=True, blank=True, choices=gender_choices)
