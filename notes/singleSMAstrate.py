#!/usr/bin/env python
# coding: utf-8

# In[1]:


import backtrader as bt
import datetime

# import pandas as pd


# In[3]:


class SingleSMAStrategy(bt.Strategy):
    params = (
        ('maperiod', 15),
    )
    
        
    def __init__(self):
        # Add a MovingAverageSimple indicator
        self.sma = bt.indicators.SMA(
             self.data0.close, period=self.p.maperiod)
    
        self.crossover = bt.indicators.CrossOver(self.data0.close, self.sma, plot=False)
        # To keep track of pending orders
        self.order = None
        
        
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        if order.status in [order.Completed, order.Canceled, order.Margin, order.Rejected]:
            # Write down: no pending order
            self.order = None

    def next(self):
        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return
        
        # Check if we are in the market
        if not self.position:
            # Not yet ... we MIGHT BUY if ...
            if self.crossover[0] == 1:
                # Keep track of the created order to avoid a 2nd order
                self.order = self.buy()
        else:
            # Already in the market ... we might sell
            if self.crossover[0] == -1:
                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()
                
    def stop(self):
        print('(MA Period {:2d}) Ending Value {:.2f}'.format(
            self.params.maperiod, self.broker.getvalue()))


# cerebro = bt.Cerebro()
# 
# # pandasdata feeder
# df_feeder = bt.feeds.PandasData(dataname=dataframe, openinterest=None)
# 
# cerebro.adddata(df_feeder, name= 'etf300')
# 
# #cerebro.addstrategy(SingleSMAStrategy, maperiod=18)
# cerebro.optstrategy(SingleSMAStrategy, maperiod=range(15,91))
# 
# 
# # 小场面1万起始资金
# cerebro.broker.setcash(10000.0)
# 
# # 手续费万5
# cerebro.broker.setcommission(0.0005)
# 
# # 以发出信号当日收盘价成交
# cerebro.broker.set_coc(True)
# 
# # Add a FixedSize sizer according to the stake
# cerebro.addsizer(bt.sizers.AllInSizerInt, percents=99)
# 
# print('Starting Portfolio Value: {:.2f}'.format(cerebro.broker.getvalue()))
# 
# cerebro.addanalyzer(bt.analyzers.AnnualReturn)
# cerebro.addanalyzer(bt.analyzers.TimeDrawDown)
# cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)
# cerebro.addanalyzer(bt.analyzers.SQN)
# 
# result = cerebro.run()
# 

# cols = ['sqn','trades','won_ratio','net','maxdd','maxddperiod']
# res_df = pd.DataFrame(columns=cols)
# annualreturn_df = pd.DataFrame(columns=range(2013,2020))
# 
# for ret_list in result:
#     ret = ret_list[0]
#     l = list()
#     ana = ret.analyzers.sqn.get_analysis()
#     l.append(ana['sqn'])
#     l.append(ana['trades'])
#     
#     ana = ret.analyzers.tradeanalyzer.get_analysis()
#     won_ratio = 100*ana['won']['total']/ana['total']['closed']
#     l.append(won_ratio)
#     l.append(ana['pnl']['net']['total'])
#     
#     ana = ret.analyzers.timedrawdown.get_analysis()
#     l.append(ana['maxdrawdown'])
#     l.append(ana['maxdrawdownperiod'])
# 
#     row = pd.Series(l, index=cols, name=ret.p.maperiod)
#     res_df = res_df.append(row)
#     
#     ana = ret.analyzers.annualreturn.get_analysis()
#     row = pd.Series(list(ana.values()), index=ana.keys(), name=ret.p.maperiod)
#     annualreturn_df = annualreturn_df.append(row)
# 
# res_df

# %matplotlib auto
# 
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# _, axes = plt.subplots(3, 2, figsize=(10, 10), sharex=True)
# 
# sns.set(style="darkgrid")
# 
# sns.lineplot(markers=True, data=res_df[['sqn']], ax=axes[0,0])
# sns.lineplot(markers=True, data=res_df[['trades']], ax=axes[0,1])
# sns.lineplot(markers=True, data=res_df[['won_ratio']], ax=axes[1,0])
# sns.lineplot(markers=True, data=res_df[['net']], ax=axes[1,1])
# sns.lineplot(markers=True, data=res_df[['maxdd']], ax=axes[2,0])
# sns.lineplot(markers=True, data=res_df[['maxddperiod']], ax=axes[2,1])
# 
# #print(res_df['sqn'])
# 

# sns.heatmap(annualreturn_df, annot=True, fmt=".3f")

# In[12]:


cerebro = bt.Cerebro()

# pandasdata feeder
df_feeder = bt.feeds.BacktraderCSVData(dataname='./510300_btf.csv')


cerebro.adddata(df_feeder, name= 'etf300')
cerebro.addstrategy(SingleSMAStrategy, maperiod=79)

# 小场面1万起始资金
cerebro.broker.setcash(10000.0)

# 手续费万5
cerebro.broker.setcommission(0.0005)

# 以发出信号当日收盘价成交
cerebro.broker.set_coc(True)

# Add a FixedSize sizer according to the stake
cerebro.addsizer(bt.sizers.AllInSizerInt, percents=99)

cerebro.run()
cerebro.plot()


# In[ ]:




