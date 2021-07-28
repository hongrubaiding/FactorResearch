# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:11:40 2021

@author: zouhao
"""

import pandas as pd
from FactorHandle.CommonMethod import CommonMethod


class GetInitFacort:
    def __init__(self,logger):
        self.logger = logger
        self.init_fac_method()
        
    
    def init_fac_method(self,):
        dic_get_fac={}
        dic_get_fac["估值"]=self.get_fac_estimate_value
        dic_get_fac["成长"]=self.get_fac_growth
        dic_get_fac["财务质量"]=self.get_fac_financial_quality
        dic_get_fac["杠杆"]=self.get_fac_lever
        dic_get_fac["市值"]=self.get_fac_size
        dic_get_fac["动量反转"]=self.get_fac_mom_reve
        dic_get_fac["波动率"]=self.get_fac_vol
        dic_get_fac["股价"]=self.get_fac_price
        dic_get_fac["beta"]=self.get_fac_beta
        dic_get_fac["换手率"]=self.get_fac_turn
        self.dic_get_fac = dic_get_fac
          
    
    def get_fac_estimate_value(self,df_fac):
        pass
    
    def get_fac_growth(self,df_fac):
        pass
    
    def get_fac_financial_quality(self,df_fac):
        pass
    
    def get_fac_lever(self,df_fac):
        pass
    
    def get_fac_size(self,df_fac):
        pass
    
    def get_fac_mom_reve(self,df_fac):
        pass
    
    def get_fac_vol(self,df_fac):
        pass
    
    def get_fac_price(self,df_fac):
        pass
    
    def get_fac_turn(self,df_fac):
        pass
    
    def get_fac_beta(self,df_fac):
        pass
    
    
    def get_main(self,df_fac,dic_param):
        self.common_method_demo = CommonMethod(self.logger)
        if df_fac.empty:
            return
        
        df_trade_date = self.common_method_demo.get_tradedate_df(
            dic_param["start_date"], dic_param["end_date"]).set_index("TradingDate")
        
        
        for fac_style,temp_df in df_fac.groupby("大类因子"):
           if fac_style in self.dic_get_fac:
               self.dic_get_fac.get(fac_style)(temp_df)
            
            