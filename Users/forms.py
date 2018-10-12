# coding:utf-8
# @mail:879995812@qq.com

from django import forms

# 用来改善前端form的难看的样式

class CMDBUserForm(forms.Form):
    username = forms.CharField(max_length=32, label="用户账号", widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "required": "",
            "minlength": 2,
            "maxlength": 32
        }))
    # 前面是后端验证，widget是前端验证
    password = forms.CharField(max_length=32, label="用户密码", widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "required": "",
            "minlength": 2,
            "maxlength": 32
        }))
    nickname = forms.CharField(max_length=32, label="用户姓名", widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "required": ""
        }))
    phone = forms.CharField(max_length=32, label="用户电话", widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "required": ""
        }))
    email = forms.EmailField(label="用户邮箱", widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "requeired": ""
        }))
    photo = forms.ImageField(label="用户头像")

    def clean_phone(self):
        # 获取前端提交的值
        data = self.cleaned_data["phone"]
        if len(data) < 11:  # 进行条件判断
            raise forms.ValidationError("手机号不可以小于11为")  # 如果不满足条件，提出错误
        else:
            return data  # 如果满足条件返回正确的值

    # 请写方法校验上传的照片大小
