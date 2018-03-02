# 修饰器
from django.http import HttpResponseRedirect
def login(func):
    def login_fun(request,*args,**kw):
        if request.session.has_key('user_name'):
            #如果成功登录，继续执行原函数
            return func(request,*args,**kw)
        else:
            red=HttpResponseRedirect('/user/login')
            #将当前页的url存入cookie
            red.set_cookie('url',request.get_full_path())
            return red
    return login_fun