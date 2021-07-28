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
    
    
    def get_tradedate_df(self,start_date,end_date,fre="D"):
        sql_str='''SELECT TradingDate,IfWeekEnd,IfMonthEnd,IfQuarterEnd from 
        QT_TradingDayNew where IfTradingDay=1 and SecuMarket=83 and TradingDate
        between '%s' and '%s'; '''%(start_date,end_date)
        df_tradedate = pd.read_sql(sql_str,self.conn)
        return df_tradedate