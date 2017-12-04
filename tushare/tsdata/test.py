# -*- coding: utf-8 -*-

import tushare.tsdata as tdata
import time

dapi = tdata.DataApi("tcp://127.0.0.1:8911")
dapi.login("testdd","123")
def callback(evt, data):
    print "callback", evt, data
    
data, b = dapi.query(view="adjFactor", 
                                code="000001",
                                fields="", 
                                filter="", 
                                orderby="",
                                data_format='pandas')
print data

dapi.close()