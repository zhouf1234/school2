"""school2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path,re_path,include
from schools import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/',views.login),   #登录

    path('index0/',views.index0),#首页

    path('index/',views.index),    #一班成绩表

    # path('edit_index/', views.edit_index, name='edit_index'),
    # re_path('edit_index/(?P<iid>\d+)/', views.edit_index, name='edit_index'),

    path('index2/',views.index2), #二班成绩表
    path('index3/',views.index3), #三班成绩表

    path('teacher/', views.teacher),  #老师表
    path('add_teacher/', views.add_teacher),  #添加老师
    re_path('del_teacher/(?P<tid>\d+)/', views.del_teacher, name='del_teacher'),  #删除老师
    re_path('edit_teacher/(?P<tid>\d+)/', views.edit_teacher, name='edit_teacher'), #编辑老师

    path('classs/',views.classs),    #班级表
    path('add_class/',views.add_class),  #添加班级
    re_path('del_class/(?P<cid>\d+)/', views.del_class, name='del_class'), #删除班级
    re_path('edit_class/(?P<cid>\d+)/', views.edit_class, name='edit_class'), #编辑班级

    path('student/',views.student),   #学生信息表表（2019年添加了导入导出学生信息表的功能，导出见其html的js）
    path('add_student/',views.add_student),  #添加学生
    path('del_student/', views.del_student,name='del_student'), #删除学生
    path('edit_student/', views.edit_student, name='edit_student'), #编辑学生
    path('add_stufile/', views.add_stufile,name='add_stufile'),  #上传学生表（指定excel表格批量上传）

    path('tea_video/',views.tea_video),  #教学视频展示和播放

    path('st/',include('st.urls')),
]

