from django.shortcuts import render,HttpResponse,redirect
import json
from django.http import JsonResponse
from . models import Stuwrite,Write,Swpaper,Ppaper
from schools.models import Student

# Create your views here.

#登录进去之后的主页面显示的学生的，schools的login已经写了
# def indexs(request):
#     value = request.session.get('k1')
#     return render(request, 'stu/indexs.html', {'value':value})

#登录进去之后的主页面显示的老师的，schools的login已经写了
# def indext(request):
#     value = request.session.get('k1')
#     return render(request, 'tea/indext.html', {'value':value})

#学生查看作业--展示界面
def writeList(request):
    value = request.session.get('k1')       #session获取到当前登录用户名，用于在学生作业表找到所有对应作业
    swrites = Stuwrite.objects.filter(stu=value)
    context = {'swrites':swrites}
    return render(request, 'stu/stu_write.html', context=context)

#老师布置作业--展示界面，需要先写添加
def addWrite(request):
    writes = Write.objects.all()
    context = {'writes':writes}
    return render(request, 'tea/write.html',context=context)

#老师布置作业--添加--获取新页面
def addsWrite(request):
    return render(request, 'tea/add_write.html')

#老师布置作业--添加--上传数据----用于add_write
#即每添加一道作业题，学生作业表里就会添加该题对应的所有学生，有多少个学生就有多少行
#存在的问题：提交时，因为csrf的原因吧，每次提交都会跳回登陆页面，但实际上，post操作是做到了的,此功能成功实现的
#后续把登录的问题改进试试
def addssWrite(request):
    title = request.POST.get('title')
    remarks = request.POST.get('remarks',None)
    subject = request.POST.get('subject',None)
    teacher = request.POST.get('teacher',None)
    # print(title,remarks,subject,teacher)

    Write.objects.create(
        title=title,
        remarks=remarks,
        subject=subject,
        teacher=teacher
    )

    student_name = Student.objects.all()
    for n in student_name:
        lii = []
        lii.append(title)
        # li.append(remarks)
        # li.append(subject)
        # li.append(teacher)
        lii.append(n.name)
        # print(n.name)
        # print(lii)   #获得一个个列表，用这个列表的名字去更新学生作业信息表的学生名字
        #按titie获得作业的id，然后添加进去学生作业表
        wr_id = Write.objects.get(title=lii[0]).id
        # print(wr_id)
        Stuwrite.objects.create(
            sw_title_id=wr_id,
            stu=lii[1],
        )

    return JsonResponse({
        'status': 'success',
        'message': '创建成功',
        'info': ''
    })

#老师布置作业--添加--上传数据----用于add_write1
# def addssWrite(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         remarks = request.POST.get('remarks',None)
#         subject = request.POST.get('subject',None)
#         teacher = request.POST.get('teacher',None)
#         print(title,remarks,subject,teacher)
#         return redirect('/st/add_write/')

#学生的我的作业--详情
def detailSw(request):
    sw_id = request.POST.get('sw_id', None)
    sw = Stuwrite.objects.get(id=sw_id)
    return render(request, 'stu/detail_sw.html', context={'sw': sw})

#学生作业编辑/提交---获取页面
def editSw(request):
    sw_id = request.POST.get('sw_id', None)
    sw = Stuwrite.objects.get(id=sw_id)
    return render(request, 'stu/edit_sw.html', context={'sw': sw})

#学生作业编辑/提交---上传数据
#这里提交的时候就没有出现addssWrite的问题，不会跳回登录页面去。。。
def updateSw(request):
    sw_id = request.POST.get('sw_id', None)
    data = request.POST.get('data', None)

    data = json.loads(data)
    sw = Stuwrite.objects.get(id=sw_id)

    if data['answer'] != '':
        sw.answer=data['answer']
    if data['message'] != '':
        sw.message=data['message']
    sw.is_sub = 1
    sw.save()
    return JsonResponse({
        "status": "success",
        "message": "成功",
        "info": ""
    })

#批改作业--展示界面
def edittWrite(request):
    stwrites = Stuwrite.objects.all()
    context = {'stwrites':stwrites}
    return render(request, 'tea/editt_write.html', context=context)

#老师的批改作业--详情
def detailTw(request):
    tw_id = request.POST.get('tw_id', None)
    sw = Stuwrite.objects.get(id=tw_id)
    return render(request, 'tea/detail_tw.html', context={'sw': sw})

#老师的批改/批改作业---获取页面
def editTw(request):
    tw_id = request.POST.get('tw_id', None)
    sw = Stuwrite.objects.get(id=tw_id)
    return render(request, 'tea/edit_tw.html', context={'sw': sw})

#老师的批改/批改作业---上传数据
#这里提交的时候就没有出现addssWrite的问题，不会跳回登录页面去。。。
def updateTw(request):
    tw_id = request.POST.get('tw_id', None)
    data = request.POST.get('data', None)

    data = json.loads(data)
    sw = Stuwrite.objects.get(id=tw_id)
    # print(data)
    if data['answer'] != '':
        sw.answer=data['answer']
    if data['message'] != '':
        sw.message=data['message']
    if data['frac'] != '':
        sw.frac = data['frac']
    if data['ask'] != '':
        sw.ask = data['ask']

    sw.is_cor=1
    sw.save()
    return JsonResponse({
        "status": "success",
        "message": "成功",
        "info": ""
    })

# 试题添加--获取新页面
def addWpaper(request):
    return render(request,'tea/add_wpaper.html')

# 试题添加--上传数据---没有出现添加作业时出现的问题。。。
def addssWpaper(request):
    wtitle = request.POST.get('wtitle')
    is_a = request.POST.get('is_a',None)
    is_b = request.POST.get('is_b',None)
    is_c = request.POST.get('is_c',None)
    is_d = request.POST.get('is_d', None)
    anw = request.POST.get('anw', None)
    fs = request.POST.get('fs', None)
    # print(wtitle,is_a,is_b,is_c,is_d,anw,fs)

    Swpaper.objects.create(
        wtitle=wtitle,
        is_a=is_a,
        is_b=is_b,
        is_c=is_c,
        is_d=is_d,
        anw=anw,
        fs=fs,
    )

    return JsonResponse({
        'status': 'success',
        'message': '创建成功',
        'info': ''
    })

#所有试题展示
def wpaperList(request):
    wpaper = Swpaper.objects.all()
    context = {'wpaper':wpaper}
    return  render(request,'tea/wpaper_list.html',context=context)

# 试卷添加--获取新页面
def addPaper(request):
    wpaper = Swpaper.objects.all()
    context = {'wpaper': wpaper}
    return render(request,'tea/add_paper.html',context=context)

# 试卷添加--上传数据----多对多的表不允许为空，也不允许重复---没有出现布置作业添加的问题
def addssPaper(request):
    ptitle = request.POST.get('ptitle')
    pte = request.POST.get('pte', None)
    pte2 = request.POST.get('pte2', None)
    pte3 = request.POST.get('pte3', None)
    pte4 = request.POST.get('pte4', None)
    pte5 = request.POST.get('pte5', None)
    pte6 = request.POST.get('pte6', None)
    pte7 = request.POST.get('pte7', None)
    pte8 = request.POST.get('pte8', None)
    pte9 = request.POST.get('pte9', None)
    pte0 = request.POST.get('pte0', None)
    # print(ptitle,pte,pte2,pte3,pte4,pte5,pte6,pte7,pte8,pte9,pte0)

    Ppaper.objects.create(ptitle=ptitle)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte2)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte3)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte4)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte5)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte6)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte7)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte8)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte9)
    Ppaper.objects.get(ptitle=ptitle).pte.add(pte0)

    return JsonResponse({
        'status': 'success',
        'message': '创建成功',
        'info': ''
    })

#所有试卷展示
def paperList(request):
    paper = Ppaper.objects.all()
    context = {'paper':paper}
    return  render(request,'tea/paper_list.html',context=context)

#查看试卷详情
def detailPaper(request):
    p_id = request.POST.get('p_id',None)
    paper = Ppaper.objects.get(id=p_id)
    pw_list = []
    for pa in paper.pte.all():
        pw_list.append(pa)
    # print(pw_list)
    pte = pw_list[0]
    pte2 = pw_list[1]
    pte3 = pw_list[2]
    pte4= pw_list[3]
    pte5 = pw_list[4]
    pte6 = pw_list[5]
    pte7 = pw_list[6]
    pte8 = pw_list[7]
    pte9 = pw_list[8]
    pte0 = pw_list[9]

    context = {
        'paper': paper,
        'pw_list': pw_list,
        'pte':pte,
        'pte2': pte2,
        'pte3': pte3,
        'pte4': pte4,
        'pte5': pte5,
        'pte6': pte6,
        'pte7': pte7,
        'pte8': pte8,
        'pte9': pte9,
        'pte0': pte0,
    }
    return render(request, 'tea/detail_paper.html', context=context)

#查看试题详情
def detailWpaper(request):
    wp_id = request.POST.get('wp_id',None)
    wpaper = Swpaper.objects.get(id=wp_id)
    context = {
        'wpaper': wpaper,
    }
    return render(request,'tea/detail_wpaper.html',context=context)

#学生在线测试---所有试卷展示
def stuPaper(request):
    paper = Ppaper.objects.all()
    context = {'paper':paper}
    return  render(request,'stu/paper_list.html',context=context)

#学生在线测试--获取新页面
def csPaper(request):
    cp_id = request.POST.get('cp_id', None)
    paper = Ppaper.objects.get(id=cp_id)
    pw_list = []
    for pa in paper.pte.all():
        pw_list.append(pa)
    # print(pw_list)
    pte = pw_list[0]
    pte2 = pw_list[1]
    pte3 = pw_list[2]
    pte4 = pw_list[3]
    pte5 = pw_list[4]
    pte6 = pw_list[5]
    pte7 = pw_list[6]
    pte8 = pw_list[7]
    pte9 = pw_list[8]
    pte0 = pw_list[9]

    context = {
        'paper': paper,
        'pw_list': pw_list,
        'pte': pte,
        'pte2': pte2,
        'pte3': pte3,
        'pte4': pte4,
        'pte5': pte5,
        'pte6': pte6,
        'pte7': pte7,
        'pte8': pte8,
        'pte9': pte9,
        'pte0': pte0,
    }
    return render(request, 'stu/cs_paper.html', context=context)

def subPaper(request):
    sp_id = request.POST.get('sp_id', None)
    data = request.POST.get('data', None)

    data = json.loads(data)
    paper = Ppaper.objects.get(id=sp_id)
    answ = []
    wt = []
    for pa in paper.pte.all():
        answ.append(pa.anw)    #通过试卷名称获取对应的所有试题的答案和题目
        wt.append(pa.wtitle)
    # print(answ)
    # print(wt)
    # print(data)
    # print(paper)

    fss = []
    if data['pte'] == answ[0]:
        fs = Swpaper.objects.get(wtitle=wt[0], anw=data['pte']).fs
        fss.append(fs)
    else:
        fs = 0
        fss.append(fs)

    if data['pte2'] == answ[1]:
        fs2 = Swpaper.objects.get(wtitle=wt[1], anw=data['pte2']).fs
        fss.append(fs2)
    else:
        fs2 = 0
        fss.append(fs2)

    if data['pte3'] == answ[2]:
        fs3 = Swpaper.objects.get(wtitle=wt[2], anw=data['pte3']).fs
        fss.append(fs3)
    else:
        fs3 = 0
        fss.append(fs3)

    if data['pte4'] == answ[3]:
        fs4 = Swpaper.objects.get(wtitle=wt[3], anw=data['pte4']).fs
        fss.append(fs4)
    else:
        fs4 = 0
        fss.append(fs4)

    if data['pte5'] == answ[4]:
        fs5 = Swpaper.objects.get(wtitle=wt[4], anw=data['pte5']).fs
        fss.append(fs5)
    else:
        fs5 = 0
        fss.append(fs5)

    if data['pte6'] == answ[5]:
        fs6 = Swpaper.objects.get(wtitle=wt[5], anw=data['pte6']).fs
        fss.append(fs6)
    else:
        fs6 = 0
        fss.append(fs6)

    if data['pte7'] == answ[6]:
        fs7 = Swpaper.objects.get(wtitle=wt[6], anw=data['pte7']).fs
        fss.append(fs7)
    else:
        fs7 = 0
        fss.append(fs7)

    if data['pte8'] == answ[7]:
        fs8 = Swpaper.objects.get(wtitle=wt[7], anw=data['pte8']).fs
        fss.append(fs8)
    else:
        fs8 = 0
        fss.append(fs8)

    if data['pte9'] == answ[8]:
        fs9 = Swpaper.objects.get(wtitle=wt[8], anw=data['pte9']).fs
        fss.append(fs9)
    else:
        fs9 = 0
        fss.append(fs9)

    if data['pte0'] == answ[9]:
        fs0 = Swpaper.objects.get(wtitle=wt[9], anw=data['pte0']).fs
        fss.append(fs0)
    else:
        fs0 = 0
        fss.append(fs0)
    # print(fss)      #分数列表，对就计分，不对就计0分，都写入列表fss中
    fssss = int(fss[0])+int(fss[1])+int(fss[2])+int(fss[3])+int(fss[4])+int(fss[5])+int(fss[6])+int(fss[7])+int(fss[8])+int(fss[9])
    # print(fssss)  # 计算出总分数
    stfs = '分数：'+str(fssss)
    return JsonResponse({
        "status": "success",
        "message": "成功",
        "info": stfs,
    })

