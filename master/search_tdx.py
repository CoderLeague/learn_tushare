'''
Created on 2017年11月16日

@author: Coder_J
'''
from pytdx.hq import TdxHq_API
from datetime import datetime

api = TdxHq_API()


# def select_best_ip():
#     QA_util_log_info('Selecting the Best Server IP of TDX')
#     listx = ['218.75.126.9', '115.238.90.165',
#              '124.160.88.183', '60.12.136.250', '218.108.98.244', '218.108.47.69',
#              '14.17.75.71', '180.153.39.51']
#     data = [ping(x) for x in listx]
#     QA_util_log_info('===The BEST SERVER is :  %s ===' %
#                      (listx[data.index(min(data))]))
#     return listx[data.index(min(data))]
# best_ip = select_best_ip()

def s1():
    if api.connect('119.147.212.81', 7709):
    # ... same codes...
        data = api.to_df(api.get_security_bars(9, 0, '000001', 0, 5)) # 返回DataFrame
        print(data)
    
        api.disconnect()

def s2():
    # 验证
    t1 = datetime.now()
    with api.connect('119.147.212.81', 7709):
    # some codes
        data = api.get_security_bars(9, 0, '000001', 0, 2)
        data = api.to_df(data)
        print(data)
        
    t2 = datetime.now()
    print(t1)
    print(t2)
    print(t2 - t1)
    
    
def s3():
    # 获取1分钟K线
    with api.connect('119.147.212.81', 7709):
        datas = api.get_security_bars(1, 0, '000001', 4, 3)
        
        for data in datas:
            print(data['datetime'])
            
            print(data)

def s4():
    # 获取股票代码
    with api.connect('119.147.212.81', 7709):
        datas = api.get_security_list(1, 0)
        for data in datas:
            print(data['name'])
            
            print(data)


def s5():
    # 获取股票行情
    with api.connect('119.147.212.81', 7709):
        i = 10
        while i>0:
            datas = api.get_security_quotes([(0, '000001')])
            for data in datas:
        #             print(data['name'])
                
                print(data)
            
            i -= 1

def s6():
    # 获取K线
    with api.connect('119.147.212.81', 7709):
        i = 1
        while i>0:
            datas = api.get_security_bars(1, 0, '000001', 4, 3)
            for data in datas:
                print(data['datetime'])
                
                print(data)
            
            i -= 1

if __name__ == '__main__':
    t1 = datetime.now()
#     s1()
#     s2()
#     s3()
#     s4()
#     s5()
    s6()
    
    t2 = datetime.now()
    print(t1)
    print(t2)
    print(t2 - t1)