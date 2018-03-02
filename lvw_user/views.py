from django.shortcuts import render,redirect
from hashlib import sha1
from lvw_user.models import User,Address
from django.http import HttpResponseRedirect,JsonResponse
from lvw_goods.models import GoodInfo
from lvw_user import user_decorator

# Create your views here.
def login(request):
    uname=request.COOKIES.get('uname','')  #如果拿不到uname值就返回空字符串
    pwd=request.COOKIES.get('upwd','')
    context={'uname':uname,
             'pwd':pwd,
             'error':0}
    try:
        url=request.META['HTTP_REFERER']
        print(url)
        if '/user/register' in url: raise Exception()
    except:url='/'
    response=render(request,'lvw_user/login.html',context)
    response.set_cookie('url',url)
    return response

def register(request):
    return render(request,'lvw_user/register.html')

def login_handle(request):
    #接受表单数据
    post=request.POST
    uname=post.get('user_name')
    upwd1=post.get('pwd')
    #设置默认值
    remember=post.get('remember','0')

    #加密
    s1=sha1() #创建 sha1对象
    s1.update(upwd1.encode('utf8')) #编码
    upwd=s1.hexdigest()

    #验证用户是否正确
    user=User.objects.filter(uname=uname).filter(upwd=upwd).first();

    if user:
        url=request.COOKIES.get('url','/') #第二个参数为默认参数，如果没有url则返回首页
        red=HttpResponseRedirect(url)

        #如果记住密码则将用户名和密码写入cookise
        if remember=='1':
            red.set_cookie('uname',user.uname.encode('utf-8'))
            red.set_cookie('upwd',upwd1)
        else:
            red.set_cookie('uname','',max_age=-1)
            red.set_cookie('upwd','',max_age=-1)
            #页应该写入selvwion，会安全一点
            #request.COOKISE['userinfo']=[user.uname,user.upwd]
            #将uname和id写入selvwion用来保持登录状态
        request.session['user_name']=uname
        request.session['uid']=user.id
        return red
    else:
        #如果没有用户，返回错误参数，模板界面，根据错误信息给出提示
        context={'error':1,'uname':uname}
        return render(request,'lvw_user/login.html',context)

def register_handle(request):
    #接收用户输入
    post=request.POST
    uname=post.get('user_name','')
    pwd=post.get('pwd','')
    cpwd=post.get('cpwd','')
    uemail=post.get('email','')
    #allow=post.get('allow")
    #判断密码是否相等
    if pwd!=cpwd:
        return redirect('/user/register')
    #密码加密
    #使用sha1加密
    s1=sha1()
    #sha1加密前，要先编码为比特
    s1.update(pwd.encode('utf8'))
    pwd=s1.hexdigest()
    #存入数据库
    user=User()
    user.uname=uname
    user.upwd=pwd
    user.uemil=uemail
    user.save()
    return redirect('/user/login')

def logout(request):
    request.session.flush()#清空所有selvwion
    return redirect('/')

def register_exist(request):
    uname=request.GET.get('un')
    count=User.objects.filter(uname=uname).count()
    #print(count)
    #返回json字典，判断是否存在
    return  JsonResponse({'count':count})
@user_decorator.login
def user_center_info(request):
    user_name=request.session.get('user_name','')
    user=User.objects.filter(uname=user_name).first()

    #获取最近浏览的商品
    goodids=request.COOKIES.get('goodids','')
    goods_list = []  # 用来存放商品列表，并维持顺序不变
    if goodids!='':
        goodids1=goodids.split(',')#拆分为列表
        #这样查询可以得到所需商品，但顺序无法维护，无法为原先设定的顺序
        #GoodInfo.objects.filter(id__in=goodids)
        for good_id in goodids1:
            goods=GoodInfo.objects.filter(pk=good_id).first()
            goods_list.append(goods)
            pass
    return render(request,'lvw_user/会员中心 - 个人资料.html',locals())

def user_update(request):
    post = request.POST
    uid=request.session.get('uid','')
    user=User.objects.filter(id=uid).first()
    user.uname=post.get('user_name', '')
    user.uemil=post.get('uemil', '')
    user.uphone=post.get('uphone', '')
    user.usex=post.get('usex', '')
    user.save()
    request.session['user_name'] = user.uname
    return redirect('/')

@user_decorator.login
def user_center_site(request):
    adds=Address.objects.filter(uid=request.session.get('uid', ''),scbz=0)
    return render(request,'lvw_user/会员中心 - 配送地址.html',locals())

@user_decorator.login
def user_center_site2(request):

    return render(request,'lvw_user/会员中心 - 配送地址2.html')

@user_decorator.login
def add_save(request):
    post = request.POST
    aid=post.get('aid')
    if aid:
        Address.objects.filter(id=aid).update(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
        detialaddr=post.get('detialaddr'),rphone=post.get('rphone'),yzbm=post.get('yzbm'))
    else: Address.objects.create(reciver=post.get('reciver'),sheng=post.get('sheng'),shi=post.get('shi'),
        detialaddr=post.get('detialaddr'),rphone=post.get('rphone'),yzbm=post.get('yzbm'),uid=request.session['uid'])
    adds = Address.objects.filter(uid=request.session.get('uid', ''), scbz=0)
    return render(request, 'lvw_user/会员中心 - 配送地址.html',locals())

@user_decorator.login
def mrdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.all().update(mrdz=0)
    Address.objects.filter(id=dzid).update(mrdz=1)
    return redirect('/user/会员中心 - 配送地址')

@user_decorator.login
def scdz(request):
    dzid=request.GET.get('dzid')
    Address.objects.filter(id=dzid).update(scbz=1)
    return redirect('/user/会员中心 - 配送地址')

@user_decorator.login
def bjdz(request):
    dzid=request.GET.get('dzid')
    add=Address.objects.get(id=dzid,scbz=0)
    adds=Address.objects.filter(uid=request.session.get('uid', ''),scbz=0)
    return render(request,'lvw_user/会员中心 - 配送地址2.html',locals())
