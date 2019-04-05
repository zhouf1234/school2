from django.urls import path
from . import views

urlpatterns = [
    path('write_list/', views.writeList, name='writeList'),  # 我的作业（含提交作业，查看作业详情）
    path('detail_sw/', views.detailSw, name='detailSw'),  # 学生的作业详情
    path('edit_sw/', views.editSw, name='editSw'),  # 学生作业编辑/提交---获取页面
    path('update_sw/', views.updateSw, name='updateSw'),  # 学生作业编辑/提交---上传数据

    path('add_write/', views.addWrite, name='addWrite'),  # 老师布置作业展示界面
    path('adds_write/', views.addsWrite, name='addsWrite'),  # 布置作业添加--获取新页面
    path('addss_write/', views.addssWrite, name='addssWrite'),  # 布置作业添加--上传数据

    path('editt_write/', views.edittWrite, name='edittWrite'),  # 老师批改作业展示界面
    path('detail_tw/', views.detailTw, name='detailTw'),  # 老师的批改作业的作业详情
    path('edit_tw/', views.editTw, name='editTw'),  # 老师的批改/批改作业---获取页面
    path('update_tw/', views.updateTw, name='updateTw'),  # 老师的批改/批改作业---上传数据

    path('add_wpaper/', views.addWpaper, name='addWpaper'),  # 老师试题添加--获取新页面
    path('addss_wpaper/', views.addssWpaper, name='addssWpaper'),  # 试题添加--上传数据
    path('wpaper_list/', views.wpaperList, name='wpaperList'), #试题展示
    path('detail_wpaper/', views.detailWpaper, name='detailWpaper'),  # 查看试题详情

    path('add_paper/', views.addPaper, name='addPaper'),  # 老师试卷添加--获取新页面
    path('addss_paper/', views.addssPaper, name='addssPaper'),  # 试卷添加--上传数据
    path('paper_list/', views.paperList, name='paperList'),  # 试卷展示
    path('detail_paper/', views.detailPaper, name='detailPaper'), #查看试卷详情

    path('stu_paper/', views.stuPaper, name='stuPaper'), #学生在线测试展示试卷
    path('cs_paper/', views.csPaper, name='csPaper'),  # 学生在线测试--获取新页面
    path('sub_paper/', views.subPaper, name='subPaper'),  # 学生在线测试--提交答案获取分数

]