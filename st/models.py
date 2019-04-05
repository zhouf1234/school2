from django.db import models

# Create your models here.

#学生作业表
class Stuwrite(models.Model):
    # sw_title = models.ForeignKey('Write',verbose_name="题目名称", on_delete=models.DO_NOTHING,related_name='sw_title')
    days = models.DateTimeField('最近修改时间', auto_now=True)
    answer = models.TextField('作业答案',null=True)
    message = models.CharField('学生留言',max_length=255,null=True)
    frac = models.CharField('老师打分', max_length=255, null=True)
    ask = models.CharField('老师评语', max_length=255, null=True)
    is_sub = models.BooleanField('学生是否提交',default=False)
    is_cor = models.BooleanField('老师是否批改', default=False)
    stu = models.CharField('学生姓名', max_length=255, null=True)  #实际应该关联学生信息表的，但是之前写的不太好，暂时先不了，就按cookie获得的名字
    sw_title = models.ForeignKey('Write', verbose_name="题目名称", on_delete=models.DO_NOTHING, related_name='sw_title')

#作业表
class Write(models.Model):
    title = models.TextField('题目',null=False)
    remarks = models.CharField('作业要求',max_length=255,null=True)
    subject = models.CharField('科目',max_length=255,null=True)
    teacher = models.CharField('出题老师', max_length=255, null=True)
    days = models.DateTimeField('发布时间', auto_now=True)


#试卷表：试卷名一个字段（先按10道题，全部按单选题），一个字段是一道题，题目既是字段名，一条数据既是一张试卷
#暂不用这个，搁置就可
class Spaper(models.Model):
    # 答案选项：
    EDU_LIST = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D')
    )

    ptitle = models.CharField('试卷名称',  max_length=255,null=False)
    pte = models.CharField('第一题', choices=EDU_LIST, default='A', null=True, max_length=11)
    po = models.CharField('第二题', choices=EDU_LIST, default='A', null=True, max_length=11)
    pt = models.CharField('第三题', choices=EDU_LIST, default='A', null=True, max_length=11)
    ps = models.CharField('第四题', choices=EDU_LIST, default='A', null=True, max_length=11)
    pf = models.CharField('第五题', choices=EDU_LIST, default='A', null=True, max_length=11)
    pfi = models.CharField('第六题', choices=EDU_LIST, default='A', null=True, max_length=11)
    psi = models.CharField('第七题', choices=EDU_LIST, default='A', null=True, max_length=11)
    psv = models.CharField('第八题', choices=EDU_LIST, default='A', null=True, max_length=11)
    pe = models.CharField('第九题', choices=EDU_LIST, default='A', null=True, max_length=11)
    pn = models.CharField('第十题', choices=EDU_LIST, default='A', null=True, max_length=11)

#试题库表---目前都是单选题
class Swpaper(models.Model):
    wtitle =models.CharField('题目',  max_length=255,null=False)
    is_a =models.CharField('选项A',  max_length=255,null=True)
    is_b = models.CharField('选项B', max_length=255, null=True)
    is_c = models.CharField('选项C', max_length=255, null=True)
    is_d = models.CharField('选项D', max_length=255, null=True)
    anw = models.CharField('答案', max_length=11, null=True)
    fs = models.CharField('该题计分', max_length=11, null=True)
#试卷表，多对多关联试题库表
class Ppaper(models.Model):
    ptitle = models.CharField('试卷名称', max_length=255, null=False)

    pte = models.ManyToManyField(to='Swpaper')

