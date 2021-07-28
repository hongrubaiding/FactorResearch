# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:40:37 2021

@author: zouhao
"""
from GetDataPack.ConnectDataBase import ConnectDataBase
import pandas as pd

class CommonMethod:
    def __init__(self,logger):
        connect_database_demo = ConnectDataBase()
        self.conn = connect_database_demo.connect_database(flag="JYDB-Formal")
        self.logger = logger
        
    def get_bench_stock(self,index_inner,start_date,end_date):
        '''
        Parameters
        ----------
        index_inner : 指数内码.
        start_date : 开始日期.
        end_date : 截止日期.

        Returns
        -------
        df : 指数成分股信息.

        '''
        
        sql_str= '''SELECT InnerCode,EndDate,Weight from LC_IndexComponentsWeight 
        where IndexCode=%s and EndDate between '%s' and '%s';
        '''%(index_inner,start_date,end_date)
        df = pd.read_sql(sql_str,self.conn)
        return df 
    
    
    def get_tradedate_df(self,start_date,end_date,fre="D"):
        '''
        Parameters
        ----------
        start_date : 获取交易日的开始日期.
        end_date :获取交易日的截止日期.
        fre :交易日频率，默认为天. The default is "D"
        
        Returns
        -------
        df_tradedate : 交易日
        '''
        
        sql_str='''SELECT TradingDate,IfWeekEnd,IfMonthEnd,IfQuarterEnd from 
        QT_TradingDayNew where IfTradingDay=1 and SecuMarket=83 and TradingDate
        between '%s' and '%s'; '''%(start_date,end_date)
        df_tradedate = pd.read_sql(sql_str,self.conn)
        return df_tradedate