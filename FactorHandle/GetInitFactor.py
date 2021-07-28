# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:11:40 2021

@author: zouhao
"""

import pandas as pd
from FactorHandle.CommonMethod import CommonMethod
from datetime import datetime,timedelta


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
        
        # 按月获取行情，减少请求数据量
        df_trade_date = self.common_method_demo.get_tradedate_df(
            dic_param["start_date"], dic_param["end_date"])
        df_trade_date["TradingDate"] = [datetime.strftime(date_str,"%Y-%m-%d") 
                                for date_str in df_trade_date["TradingDate"]]
        month_end_list = df_trade_date[df_trade_date["IfMonthEnd"]==1]["TradingDate"]
        
        # 指数成分股信息,前推半年，确保回测开始有成分股信息
        start_date = (datetime.strptime(dic_param["start_date"],"%Y-%m-%d")-
        timedelta(days=180)).strftime("%Y-%m-%d")
        df_index_stock = self.common_method_demo.get_bench_stock(
            dic_param["bench_inner"],start_date , dic_param["end_date"])
        
        last_date = df_trade_date["TradingDate"].min()
        for month_end in month_end_list:
            date_list =df_trade_date[(df_trade_date["TradingDate"]<=month_end)
                &(df_trade_date["TradingDate"]>last_date)]["TradingDate"].tolist()
            self.logger.info("本次因子计算开始日期:%s;截止日期:%s"%(date_list[0],date_list[-1]))
            
            index_start = df_index_stock[df_index_stock["EndDate"]<=date_list[0]]["EndDate"].max()
            index_end = df_index_stock[df_index_stock["EndDate"]>=date_list[-1]]["EndDate"].min()
            temp_index_stock = df_index_stock[(df_index_stock["EndDate"]>=index_start)&
                                              (df_index_stock["EndDate"]<=index_end)]
            
            index_adjust_date = temp_index_stock["EndDate"].unique().tolist()
            index_adjust_date = [datetime.strftime(date_str,"%Y-%m-%d") 
                                for date_str in temp_index_stock["EndDate"].unique()]
                                     
            for fac_style,temp_df in df_fac.groupby("大类因子"):
               if fac_style in self.dic_get_fac:
                   self.dic_get_fac.get(fac_style)(temp_df,temp_index_stock,date_list)
                
            