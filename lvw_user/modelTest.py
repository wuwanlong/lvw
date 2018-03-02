from lvw_user.models import Address
#查询  获取所有地址
adds=Address.objects.all()
add=Address.objects.get(id=1,reciver='zhangsan')    #获取指定字段的记录
adds2=Address.objects.all().values_list('id','reciver')  #过滤字段
add2=Address.objects.filter(uid=1,reciver='zhangsan').all() #符合过滤的所有的记录
add3=Address.objects.filter(uid=1,reciver='zhangsan').first() #符合过滤的第一个记录


#新增
Address.objects.create(reciver='lisi',sheng='heilongjiang') #新增数据
add4=Address()
add4.reciver='wangwu'
add4.save()

# 删除
Address.objects.filter(uid=1,reciver='zhangsan').delete() #删除指定数据

#更新
Address.objects.filter(uid=1,reciver='zhangsan').update(reciver='zhaoliu',sheng='shengyang')
