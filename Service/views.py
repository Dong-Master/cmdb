from Service.models import Service
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponse
from cmdb.views import getPage


def server(request, page=1):  # url默认执行第一页
    # 查询所有数据
    servers = Service.objects.all()
    # 进行分页
    p_servers = Paginator(servers, 10)  # 对指定序列以每10条为一页进行分页
    pageData = p_servers.page(int(page))
    # 返回分页数据
    # 为了防止前端注入，一个locals把所有的变量都可以靠猜获取到
    return render(request, "ServerList.html", {"pageData": pageData, "pageRange": p_servers.page_range})
                    # pageData:是所有的数据  pageRange：一共多少页

def Ajax_server(request):
    if request.method == "GET" and request.GET:
        sql = "select * from Service_service limit 0,10"
        page_data = Service.objects.raw(sql)

from django.db import connection
def Ajax_user(request):
    if request.method == "GET" and request.GET:
        sql = "select * from Service_cmdbuser"
        cursor = connection.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()


def AjaxServer(request, page=1):
    sql = "select * from Service_service"
    page_data = getPage(sql=sql, page=page)
    return JsonResponse(page_data)


def ServerList_ajax(request):
    return render(request, "ServerList_ajax.html")

def getConnect(request):
    if request.method == "GET" and request.GET:
        id = int(request.GET.get("id"))
        server = Service.objects.get(id=id)
        return render(request, "getConnect.html", locals())
    else:
        return HttpResponse('your request must be get')

import time,hmac,hashlib,json

def authodj(secret,*parts):
    """
        对secret值安装gateone的要求加密
    """
    hash = hmac.new(secret,digestmod = hashlib.sha1)
    for parts in parts:
        hash.update(str(parts))
    return hash.hexdigest()

def gateValid(request):
    user = "root"
    gateone_server = "https://10.10.10.69:443" #后期代码整理，我们可以放到settings当中

    secret = "MDdlNTFjYWZjN2U0NDdjMGJjN2Y5NDQ2Zjg0ZGJkNDlmY".encode()
    api_key = "NjBhYmJhYzI5NDA3NGVmYWEyZTk0MzY3ZjEzMDllMjgyM"

    authodj_dict = {
        'api_key': api_key,
        'upn': 'gateone',
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(secret,digestmod = hashlib.sha1)
    update_data = authodj_dict['api_key'] + authodj_dict['upn'] + authodj_dict['timestamp']
    my_hash.update(update_data.encode())

    authodj_dict['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authodj_dict}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)
