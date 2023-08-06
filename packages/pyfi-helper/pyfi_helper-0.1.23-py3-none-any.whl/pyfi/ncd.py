import pandas as pd
import numpy as np
import datetime
import calendar
from pyfi import WindHelper as w
from pyfi import return_gen
from pyfi import line_graph

#读取同业存单数据
data0 = pd.read_excel("data_final.xlsx")
# data0 = pd.read_excel("同业存单_2018.xlsx")
data = data0[data0['发行人类型'] == '股份制商业银行']
data = data.sort_values(by="起息日", ascending=True)
data.index = data['起息日']


def get_time2():
    time_tmp = datetime.datetime.now() - datetime.timedelta(days=1)
    return time_tmp.strftime("%Y-%m-%d")


def gen_index(df):
    """
    返回日期起始范围
    """
    index_tmp = []
    for i in range(len(df)):
        if df.index[i] not in index_tmp:
            index_tmp.append(df.index[i])
    return index_tmp


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def data_index(begin_date, term, data):
    """
    begin_date: 开始日期，为字符串形式，如：'2019-1-8'
    term:期限，如：3，6，9，12
    data:包含所有期限数据的DataFrame
    """
    # begin_date = '2019-4-3'
    # term = 3
    data = data[begin_date:]
    index = gen_index(data)
    data_term = pd.DataFrame()
    for i in range(len(index)):
        data_tmp = data[data.index == index[i]]
        if term in list(data_tmp['期限(月)']):
            data_tmp2 = data_tmp[data_tmp['期限(月)'] == term]
            data_term = data_term.append(data_tmp2.sort_values(by="参考收益率(%)", ascending=True)[0:1])

        else:  # 当天没有相应期限的存单，取上一天的存单来接近
            tmp = data_term[-1:]
            tmp.index = [index[i]]
            data_term = data_term.append(tmp)
    return data_term


def next_date(index, date):
    '''
    当前日期date非交易日，返回index中第一个交易日
    '''
    if date not in index:
        for a in index:
            if a > pd.Timestamp(date):
                return a
                break
    else:
        return date


def data_pre(data, begin_date, term, rf, base):
    """
    输入：data:包含历史所有存单的发行信息的DataFrame
         begin_date:开始日期，格式如'2019-1-8'
         term: 存单期限，如3，6，9，12个月
         perct:一次能买入单一发行存单的比例,如10%，输入0.1
         rf:存款年化利率，如2.5%，输入0.025
         base:基准期限，如以三个月期限为基准
    输出：累计收益、下行波动率
    """
    #    begin_date = '2019-1-28'
    #    term = 3
    #    rf = 0.025
    #    base = 1

    df_index = data_index(data.index[0], term, data)
    data = data[begin_date:]
    start_date = data.index[0]

    data_term = pd.DataFrame()
    tar_date = add_months(start_date, base)
    final_return = []
    flag = 0
    while pd.Timestamp(tar_date) <= data.index[-1]:
        if flag == 0:
            start_date = next_date(df_index.index, start_date)
            code = df_index['交易代码'][start_date]
            df_tmp = w.wsd(code, paras=["net_cnbd"], begin_date=start_date.strftime("%Y-%m-%d"),
                           end_date=tar_date.strftime("%Y-%m-%d"))
            df_tmp = df_tmp[0:-1]
            signal = np.zeros(len(df_tmp))
            signal = signal + 1
            signal[-1] = 0
            df_tmp['signal'] = signal
            df_tmp = df_tmp.rename(columns={'net_cnbd': 'price'})
            return_tmp = return_gen(df_tmp.price, df_tmp.signal)[0]
            df_tmp['cum_return'] = return_tmp
            data_term = data_term.append(df_tmp)
            start_date = tar_date
            tar_date = add_months(tar_date, base)
            for i in range(len(df_tmp)):
                final_return.append(df_tmp.cum_return[i])
            flag = 1
        else:
            start_date = next_date(df_index.index, start_date)
            code = df_index['交易代码'][start_date]
            df_tmp = w.wsd(code, paras=["net_cnbd"], begin_date=start_date.strftime("%Y-%m-%d"),
                           end_date=tar_date.strftime("%Y-%m-%d"))
            df_tmp = df_tmp[0:-1]
            signal = np.zeros(len(df_tmp))
            signal = signal + 1
            signal[-1] = 0
            df_tmp['signal'] = signal
            df_tmp = df_tmp.rename(columns={'net_cnbd': 'price'})
            return_tmp = return_gen(df_tmp.price, df_tmp.signal)[0]
            df_tmp['cum_return'] = return_tmp
            data_term = data_term.append(df_tmp)
            start_date = tar_date
            tar_date = add_months(tar_date, base)
            list_tmp = []
            for i in range(len(df_tmp)):
                tmp = df_tmp.cum_return[i] + final_return[-1] * pow(1 + rf, (i + 1) / 245)
                list_tmp.append(tmp)
            final_return = final_return + list_tmp

    start_date = next_date(df_index.index, start_date)
    endd_date = get_time2()
    endd_date = pd.Timestamp(endd_date).date()
    if pd.Timestamp(start_date) > pd.Timestamp(endd_date):
        data_term['final_return'] = final_return
        daily_return = np.diff(data_term.final_return)
        down_return = daily_return[daily_return < 0]
        return data_term.final_return, down_return.std(), data_term

    else:
        code2 = df_index['交易代码'][start_date]
        df_tmp2 = w.wsd(code2, paras=["net_cnbd"], begin_date=start_date.strftime("%Y-%m-%d"),
                        end_date=endd_date.strftime("%Y-%m-%d"))
        if len(df_tmp2) == 1:
            data_term['final_return'] = final_return
            daily_return = np.diff(data_term.final_return)
            down_return = daily_return[daily_return < 0]
            return data_term.final_return, down_return.std(), data_term
        else:
            signal = np.zeros(len(df_tmp2))
            signal = signal + 1
            df_tmp2['signal'] = signal
            df_tmp2 = df_tmp2.rename(columns={'net_cnbd': 'price'})
            return2 = return_gen(df_tmp2.price, df_tmp2.signal)[0]
            df_tmp2['cum_return'] = return2
            list_tmp2 = []
            for i in range(len(df_tmp2)):
                tmp2 = df_tmp2.cum_return[i] + final_return[-1] * pow(1 + rf, (i + 1) / 245)
                list_tmp2.append(tmp2)
            final_return = final_return + list_tmp2
            data_term = data_term.append(df_tmp2)
            data_term['final_return'] = final_return
            daily_return = np.diff(data_term.final_return)
            down_return = daily_return[daily_return < 0]

            return data_term.final_return, down_return.std(), data_term

if __name__ == "__main__":
    Risk_Free_Rate = 0.025
    Holding_Period = 1
    yield_NCD = []
    vol = []
    index = data_index('2019-1-9', 3, data).index
    for i in range(57, 100):
        print(i)
        NCD_date = index[i]
        result = data_pre(data, NCD_date, 3, 0.025, Holding_Period)
        yield_NCD.append(result[0][-1])
        vol.append(result[1])

    print(yield_NCD, vol)

    return3 = data_pre(data, '2019-1-9', 3, 0.025, 3)
    return6 = data_pre(data, '2019-1-9', 6, 0.025, 3)
    return9 = data_pre(data, '2019-1-9', 9, 0.025, 3)
    return12 = data_pre(data, '2019-1-9', 12, 0.025, 3)

    line_graph([return3[0], return6[0], return9[0], return12[0]], legend_list=["3m", "6m", "9m", "12m"])
    line_graph([return3[0], return6[0], return9[0]], legend_list=["3m", "6m", "9m"])