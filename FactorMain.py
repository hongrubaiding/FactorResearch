# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 09:36:53 2021

@author: zouhao
"""


import mylog as mylog_demo
import os
import pandas as pd
from FactorHandle.GetInitFactor import GetInitFacort

class FactorMain:
    def __init__(self,):
        self.logger = mylog_demo.set_log("因子研究日志")
        self.logger.info("开始了")
        self.get_init_fac = GetInitFacort(self.logger)
        self.dic_param = self.init_param()
        
    
    def init_param(self,):
        dic_param = {}
        dic_param['start_date']="2010-01-01"
        dic_param["end_date"] = "2017-01-01"
        
        #基准指数代码
        dic_param["bench_inner"] = 14110
        return dic_param
    
    
    def get_factor_info(self):
        df_fac = pd.read_excel(os.path.abspath('因子类型.xlsx')).set_index("具体因子")
        self.get_init_fac.get_main(df_fac,dic_param=self.dic_param)
    
    def start_main(self,):
        self.get_factor_info()
    
if __name__=="__main__":
    FactorMainDemo = FactorMain()
    FactorMainDemo.start_main()