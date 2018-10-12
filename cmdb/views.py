# coding:utf-8
# @mail:879995812@qq.com

from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from Users.forms import CMDBUserForm
from Service.models import CMDBUser
from cmdb.settings import BASE_DIR
from django.http import HttpResponse
from django.db import connection
import os, datetime


def loginValid(func):  # 装饰器的固定写法，valid的第二个参数是可变参数列表，第三个是可变参数字典
    def valid(request, *args, **keywords):
        username = request.COOKIES.get("username")
        if username:
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponseRedirect("/login/", locals())
            else:
                return func(request)
        else:
            return HttpResponseRedirect("/login/", locals())

    return valid


# def base(request):
#
#     return render(request,'blank.html')
@loginValid
def index(request):
    forms = CMDBUserForm()  # 定义form表单
    if request.method == "POST" and request.POST and request.FILES:
        # 判断
        # 1、请求方式是post
        # 2、post请求有内容
        # 3、文件请求有内容
        formsData = CMDBUserForm(data=request.POST, files=request.FILES)  # 接收回来的数据
        # 校验提交的数据和文件
        if formsData.is_valid():
            requestData = formsData.cleaned_data
            username = requestData.get("username")  # get里面的是前端input里面的name
            password = requestData.get("password")
            nickname = requestData.get("nickname")
            phone = requestData.get("phone")
            email = requestData.get("email")
            photo = requestData.get("photo").name  # 这里获取到的不是一个值，而是一个文件对象
            # 存入数据库的应该是一个名字

            user = CMDBUser()  # 实例化数据库，保存数据，存入数据库
            user.username = username
            user.password = password
            user.nickname = nickname
            user.phone = phone
            user.email = email
            user.photo = photo
            user.save()

            # 保存文件，这里没有限制文件格式，上传啥都行
            photofile = request.FILES.get("photo")
            path = os.path.join(BASE_DIR, "static\\images\\%s" % photofile.name)
            with open(path, "wb") as f:
                for chunk in photofile.chunks():  # 图片的解析阅读方式
                    f.write(chunk)
        else:
            print(formsData.errors)
    return render(request, 'index.html', locals())


def echartExample(request):
    return render(request, "echartExample.html")


def login(request):
    if request.method == "POST" and request.POST:
        # 获取校验cookie
        # 获取普通的cookie
        # login_cookie = request.COOKIES.get("login_cookie")
        # 取出加盐的cookie
        login_cookie = request.get_signed_cookie(key="login_cookie", salt="nihao")
        if login_cookie:
            data = request.POST
            username = data.get("username")
            password = data.get("password")
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponse("用户不存在")
            else:
                db_password = user.password
                if password == db_password:
                    response = HttpResponseRedirect("/index/", locals())
                    response.set_cookie(key="username", value=user.username)
                    return response
                else:
                    return HttpResponse("密码错误")
        else:
            return HttpResponse("404")
    else:
        # 登陆页面，login.html GET请求
        # 生成response实例
        response = render(request, "login.html")
        # 设置cookie
        response.set_signed_cookie("login_cookie", "helloworld", salt="nihao", max_age=3600)
        # 返回设置了cookie的响应
        return response


def logout(request):
    cookie = request.COOKIES.get(key="login_cookie")
    response = render(request, "login.html")
    response.delete_cookie()
    return response


def getPage(sql, page, num=10):
    """
    当前函数是后端分页函数
    :param sql:  查询语句
    :param page:  当前页码
    :param num:  单页条数
    :return:
    """
    page = int(page)
    num = int(num)
    start_page = (page - 1) * num
    # 工作当中Python操作原生数据库语句用的最多的就是字符拼接
    page_sql = sql + " limit %s,%s" % (start_page, num)
    cursor = connection.cursor()
    cursor.execute(page_sql)
    page_data = cursor.fetchall()
    keys = [key[0] for key in cursor.description]
    result = [dict(zip(keys, d)) for d in page_data]
    return {"page_data": result}

def vueExample(request):
    return render(request,"vueExample.html")

def gate(request):
    return render(request,"gateoneExample.html")
