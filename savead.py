
import   money

def  send_money():
    global saved_money
    money.saved_money=2000
    if money.saved_money==2000:
        print("发工资了")
    else:
        print("没有发工资")
