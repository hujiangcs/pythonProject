# 原有存款 1000元， 发工资之后存款变为2000元
# 定义模块
# 1、money.py saved_money = 1000
# 2、定义发工资模块 send_money，用来增加收入计算
# 3、定义工资查询模块 select_money，用来展示工资数额
# 4、定义一个start.py ，启动文件展示最终存款金额
#!/usr/bin/python3
saved_money = 1000
def  send_money():
    global saved_money
    saved_money=2000
    if saved_money==2000:
        print("发工资了")
    else:
        print("没有发工资")
def  select_money():
    if saved_money==2000:
       print("存款:2000元")
    else:
        print("存款:1000元")
