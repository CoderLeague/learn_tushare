import os, sys
import time
import traceback

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))                                                                       
sys.path.insert(0, base_dir)

import tushare as ts
from datetime import datetime

codes = {
  "510050": "华夏上证50ETF",
  "510300": "华泰柏瑞沪深300ETF",
  "510500": "南方中证500ETF",
  "159915": "易方达创业板ETF",
  "159902": "华夏中小板ETF",
  "510230": "国泰上证180金融ETF",
  "510880": "华泰柏瑞上证红利ETF",
  "159928": "汇添富中证主要消费ETF",
  "510900": "易方达恒生国企",
  "513660": "华夏沪港通恒生ETF",
  "513100": "国泰纳斯达克100ETF",
  "513500": "博时标普500ETF",
  "513030": "华安德国30(DAX)ETF",
  "511010": "国泰上证5年期国债ETF",
  "511220": "海富通上证可质押城投债ETF",
  "518800": "黄金基金",

  "510050": "XD50ETF",
  "510300": "300ETF",
  "510500": "500ETF",
  "512660": "军工ETF",
  "512880": "证券ETF",
  "518880": "黄金ETF",
  "159915": "创业板",
  "510810": "上海国企",
  "510900": "H股ETF",
  "513100": "纳指ETF",
  "513500": "标普500",
  "513030": "德国30",
  "512990": "MSCIA股",
  "510880": "红利ETF",
  "159938": "广发医药",
  "159920": "恒生ETF",
  "161631": "人工智能",
}

def debug_1():
    
    conn = ts.get_apis()
    for code in codes:
        try:
            pd = ts.bar(code, conn=conn, start_date=None, end_date=None, freq='D', asset='INDEX', 
                   market='',
                   adj = None,
                   ma = [],
                   factors = [],
                   retry_count = 2, row_count = 10)
            
            if pd == None:
                print('None')
            else:
                print(pd)
        except:
            pass
    
if __name__ == '__main__':
    t1 = datetime.now()
    debug_1()
    t2 = datetime.now()
    
    print()
    print(t1)
    print(t2)
    print(t2 - t1)