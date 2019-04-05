from django.db import models

# Create your models here.

#学生表，和学生成绩表，信息表一对一，和选修课多对多，和班级表多对一
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    data=models.OneToOneField(to='Data',on_delete=models.CASCADE,null=True)

    detall = models.OneToOneField(to='Yuwen',on_delete=models.CASCADE,null=True)
    deta=models.OneToOneField(to='Math',on_delete=models.CASCADE,null=True)
    de=models.OneToOneField(to='English',on_delete=models.CASCADE,null=True)
    fou=models.OneToOneField(to='Four',on_delete=models.CASCADE,null=True)
    fiv=models.OneToOneField(to='Five',on_delete=models.CASCADE,null=True)

    xecs = models.ManyToManyField(to='Xec')
    sclass=models.ForeignKey(to="Class",to_field="id",on_delete=models.CASCADE)


#学生信息表，学生资料
class Data(models.Model):
    city = models.CharField(max_length=32)
    age = models.PositiveIntegerField()
    sex=models.CharField(max_length=32)
    phone = models.IntegerField()

#学生语文成绩表，和课程表一对一对应(问题：照理来说，是多个成绩分数对一个课程)
class Yuwen(models.Model):
    yuwen =models.DecimalField(max_digits=4,decimal_places=2)
    skec=models.ManyToManyField(to='Kec')

#学生数学成绩表，和课程表一对一对应
class Math(models.Model):
    math=models.DecimalField(max_digits=4,decimal_places=2)
    skecs=models.ManyToManyField(to='Kec')

#学生英语成绩表，和课程表一对一对应
class English(models.Model):
    english=models.DecimalField(max_digits=4,decimal_places=2)
    skecess=models.ManyToManyField(to='Kec')

class Four(models.Model):
    four=models.DecimalField(max_digits=4,decimal_places=2)
    skecesss=models.ManyToManyField(to='Kec')

class Five(models.Model):
    five=models.DecimalField(max_digits=4,decimal_places=2)
    skecessss=models.ManyToManyField(to='Kec')

#课程表
class Kec(models.Model):
    id = models.AutoField(primary_key=True)
    kname=models.CharField(max_length=32)

#选修课表
class Xec(models.Model):
    id = models.AutoField(primary_key=True)
    xname=models.CharField(max_length=32)

#老师表，要和班级多对多关联
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    tname=models.CharField(max_length=32)
    tclass = models.ManyToManyField(to='Class')

#班级表，应该和课程表多对多关联,
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=32)
    ckec = models.ManyToManyField(to='Kec')


