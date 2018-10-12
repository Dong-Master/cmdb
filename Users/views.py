from django.shortcuts import render
from Users.forms import *
from Service.models import *
from cmdb.settings import BASE_DIR
import os
from django.http import JsonResponse   #ajax 过来就是json格式

def register(request):
    result = {
        "submit":"success"
    }
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
            return JsonResponse(result)
        else:
            print(formsData.errors)
            result["submit"] = "error"
            return JsonResponse(result)
    else:
        return JsonResponse({"method":"get"})
