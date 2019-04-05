from django.shortcuts import render,redirect,HttpResponse
from . import models
from django.shortcuts import reverse
# Create your views here.

def login(request):
    if request.method=='POST':
        user=request.POST.get('user')
        pwd=request.POST.get('pwd')
        if user=='evev'and pwd=='123456':           #后台管理员
            request.session['k1']=user
            return redirect('/index0/')

        student_list = models.Student.objects.all().values('name')
        stu_name = []
        for i in student_list:
            stu_name.append(i['name'])
        # print(stu_name)
        if user in stu_name and pwd == '123456':      #学生，目前都按统一的密码
            request.session['k1']=user
            value = request.session.get('k1')
            return render(request, 'stu/indexs.html',{'value':value})

        if user=='安老师'and pwd=='23456':     #教师
            request.session['k1']=user
            value = request.session.get('k1')
            return render(request, 'tea/indext.html',{'value':value})
        else:
            error = '用户名或密码错误！请重新输入！'
            return render(request,'login.html',{'error':error})
    return render(request,'login.html')

#登录进去之后的主页面显示的
def index0(request):
    value = request.session.get('k1')
    return render(request, 'index.html',{'value':value})


def index(request):
    value=request.session.get('k1')
    student_list = models.Student.objects.filter(sclass__cname='一班')
    kec_list=models.Class.objects.filter(id=1)
    return render(request,'students.html',{'value':value,'student_list': student_list,'kec_list':kec_list})


def index2(request):
    value = request.session.get('k1')
    student_list = models.Student.objects.filter(sclass__cname='二班')
    kec_list=models.Class.objects.filter(id=2)
    return render(request,'students.html',{'student_list': student_list,'kec_list':kec_list,'value':value})

#没有写新的学生html，直接按班级id传入数据了
def index3(request):
    value = request.session.get('k1')
    student_list = models.Student.objects.filter(sclass__cname='三班')
    kec_list=models.Class.objects.filter(id=3)
    return render(request,'students.html',{'student_list': student_list,'kec_list':kec_list,'value':value})

#学生信息表
def student(request):
    student_list=models.Student.objects.all()
    return render(request, 'student0.html',{'student_list':student_list})

#班主任表
def teacher(request):
    teacher_list=models.Teacher.objects.all()
    # teacher_count=models.Student.objects.all()
    # v=teacher_count.count()
    return render(request, 'teacher.html',{'teacher_list':teacher_list})

# 班级表
def classs(request):
    class_list=models.Class.objects.all()
    return render(request, 'classs.html',{'class_list':class_list})

#添加班级
def add_class(request):
    if request.method == 'POST':
        cname=request.POST.get('cname')
        ckec = request.POST.getlist('ckec')

        class_obj=models.Class.objects.create(cname=cname)
        class_obj.ckec.add(*ckec)
        return redirect('/classs/')
    kec_list = models.Kec.objects.all()
    return render(request,'add_class.html',{'kec_list':kec_list})


#删除班级
def del_class(request,cid):
    models.Class.objects.get(id=cid).delete()
    return redirect('/classs/')

#修改班级
def edit_class(request,cid):
    class_obj = models.Class.objects.get(id=cid)
    if request.method == 'POST':
        cname = request.POST.get('cname')
        ckec = request.POST.getlist('ckec')

        class_obj.cname = cname
        class_obj.ckec.set(ckec)
        class_obj.save()
        return redirect('/classs/')

    kec_list = models.Kec.objects.all()
    return render(request,'edit_class.html',{'kec_list':kec_list,'class':class_obj})

# 添加新班主任信息
def add_teacher(request):
    if request.method == 'POST':
        tname = request.POST.get('tname')
        tclass = request.POST.getlist('tclass')

        teacher_obj=models.Teacher.objects.create(tname=tname)
        teacher_obj.tclass.add(*tclass)
        return redirect('/teacher/')
    class_list=models.Class.objects.all()
    return render(request, 'add_teacher.html',{'class_list':class_list})

# 删除老师信息
def del_teacher(request,tid):
    models.Teacher.objects.get(id=tid).delete()
    return redirect('/teacher/')

#修改老师信息
def edit_teacher(request,tid):
    teacher_obj = models.Teacher.objects.get(id=tid)
    if request.method == 'POST':
        tname = request.POST.get('tname')
        tclass = request.POST.getlist('tclass')

        teacher_obj.tname=tname
        teacher_obj.tclass.set(tclass)
        teacher_obj.save()
        return redirect('/teacher/')

    class_list=models.Class.objects.all()
    return render(request, 'edit_teacher.html', {'class_list': class_list,'teacher':teacher_obj})

# 添加新学生信息
def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sclass = request.POST.get('sclass')
        city = request.POST.get('city')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')

        models.Data.objects.create(city=city, age=age, sex=sex, phone=phone)
        models.Student.objects.create(name=name, sclass_id=sclass,data_id=models.Data.objects.last().id)

        return redirect('/student/')
    class_list=models.Class.objects.all()
    return render(request,'add_student.html',{'class_list':class_list})


# 删除学生信息，。。。。还得同时删除学生成绩信息，不删的话成绩依然存在
#问题在于，一对一的删除的同时，会把学生姓名和id一起删除，多个一对一的删除怎么操作？
def del_student(request):
    student_id = request.GET.get("student_id")
    models.Data.objects.get(id=models.Student.objects.get(id=student_id).data_id).delete()
    # models.Yuwen.objects.get(id=models.Student.objects.get(id=student_id).detall_id).delete()
    # models.Math.objects.get(id=models.Student.objects.get(id=student_id).deta_id).delete()
    # models.English.objects.get(id=models.Student.objects.get(id=student_id).de_id).delete()
    # models.Four.objects.get(id=models.Student.objects.get(id=student_id).fou_id).delete()
    # models.Five.objects.get(id=models.Student.objects.get(id=student_id).fiv_id).delete()
    return redirect('/student/')


# 修改学生信息
def edit_student(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        sclass = request.POST.get('sclass')
        city = request.POST.get('city')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone')

        models.Data.objects.filter(id=models.Student.objects.get(id=id).data_id).update(city=city, age=age, sex=sex, phone=phone)
        models.Student.objects.filter(id=id).update(name=name, sclass=sclass,data_id=models.Student.objects.get(id=id).data_id)
        return redirect('/student/')

    student_id = request.GET.get('student_id')
    student_obj=models.Student.objects.get(id=student_id)

    class_list = models.Class.objects.all()
    return render(request, 'edit_student.html',{'student':student_obj,'class_list':class_list})

#编辑一班成绩信息,未完
# def edit_index(request):
#     if request.method == 'POST':
#         id = request.POST.get('id')
#         name = request.POST.get('name')
#         sclass = request.POST.get('sclass')
#         detall = request.POST.get('yuwen')
#         deta = request.POST.get('math')
#         de = request.POST.get('english')
#         fou = request.POST.get('four')
#         fiv = request.POST.get('five')
#         xecs = request.POST.get('xkc')
#
#         kec1 = request.POST.get('kec1')
#         kec2 = request.POST.get('kec2')
#         kec3 = request.POST.get('kec3')
#         kec4 = request.POST.get('kec4')
#         kec5 = request.POST.get('kec5')
#
#         #分数数据类型和上传的不一致，无法上传。。问题太多。。：mysql数据库创库时设置的小数点数据类型
#         models.Yuwen.objects.filter(id=models.Student.objects.get(id=id).detall_id).update(yuwen=detall)
#         models.Math.objects.filter(id=models.Student.objects.get(id=id).deta_id).update(math=deta)
#         models.English.objects.filter(id=models.Student.objects.get(id=id).de_id).update(english=de)
#         models.Four.objects.filter(id=models.Student.objects.get(id=id).fou_id).update(four=fou)
#         models.Five.objects.filter(id=models.Student.objects.get(id=id).fiv_id).update(five=fiv)
#
#         models.Student.objects.filter(id=id).update(name=name, sclass=sclass,detall_id=models.Student.objects.get(id=id).detall_id)
#         models.Student.objects.filter(id=id).update(deta_id=models.Student.objects.get(id=id).deta_id,de_id=models.Student.objects.get(id=id).de_id)
#         models.Student.objects.filter(id=id).update(fou_id=models.Student.objects.get(id=id).fou_id,fiv_id=models.Student.objects.get(id=id).fiv_id)
#
#         student_obj2 = models.Student.objects.get(id=id)
#         student_obj2.xecs.set(xecs)
#         student_obj2.save()
#
#         student_obj2.detall.skec.set(kec1)
#         student_obj2.save()
#
#         student_obj2.deta.skecs.set(kec2)
#         student_obj2.save()
#
#         student_obj2.de.skecess.set(kec3)
#         student_obj2.save()
#
#         student_obj2.fou.skecesss.set(kec4)
#         student_obj2.save()
#
#         student_obj2.fiv.skecessss.set(kec5)
#         student_obj2.save()
#
#         return redirect('/index/')
#     student_id = request.GET.get('student_id')
#     student_obj=models.Student.objects.get(id=student_id)
#
#     xkc_list=models.Xec.objects.all()
#     class_list = models.Class.objects.all()
#     return render(request, 'edit_index.html',{'class_list':class_list,'student':student_obj,'xuc_list':xkc_list})

# 导入新学生信息文件，此次是指定了这个文件名和地址的，内部只有内容可以改，sheet名和行列不可删除
#已成功上传指定excel表格数据
import xlrd
import xlwt
def add_stufile(request):
    workbook = xlrd.open_workbook(r'C:\Users\admin\Desktop\stu.xls')
    # print(workbook.sheet_names())   #输出sheet名：学生信息表
    sheet2 = workbook.sheet_by_name('学生信息表')
    nrows = sheet2.nrows     #共15行
    ncols = sheet2.ncols    #共9列
    #print(nrows, ncols)
    # cell_A = sheet2.cell(1, 1).value  #输出第二行第二列的值
    # print(int(cell_A))  #50    #得到的是学生id
    # print(sheet2.row_values(1))  #得到一行的数据，是个列表
    for i in range(1,nrows):
        idlist = sheet2.row_values(i)  #得到15个列表

        city = idlist[4]        #一对一的表的数据，要先去更新一对一的表的值，才能拿到它的id
        age = int(idlist[5])
        sex = idlist[6]
        phone = int(idlist[7])
        # print(city,age,sex,phone)
        models.Data.objects.create(city=city, age=age, sex=sex, phone=phone)
        data_id = models.Data.objects.last().id
        # print(data_id)

        id = int(idlist[1])
        name = idlist[2]
        # print(id,name)          #学生表里写的部分

        sclass_id = models.Class.objects.get(cname=idlist[3]).id
        # print(sclass_id)        #外键关联班级表的部分

        models.Student.objects.create(id=id,name=name, sclass_id=sclass_id, data_id=data_id)
    return redirect('/student/')

#教学视频展示：页面效果出来了，可以播放暂停，但是在django运行时报了一些错误，后续完善吧
def tea_video(request):
    return render(request,'tea_vedio.html')
