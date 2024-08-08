import os,json
import pandas as pd
from pandas import DataFrame
def get_path() -> list :
    dirname = os.path.dirname(os.path.abspath(__name__))
    file_dirname = os.path.join('每日各站進出站人數')
    name_list = []
    for filename in (os.listdir(file_dirname)):
        if '每日各站進出站人數' in filename:
            name_list.append(os.path.join(file_dirname,filename))
    return name_list

def get_station_imfo()->DataFrame:
    dirname = os.path.dirname(os.path.abspath(__name__))
    file_dirname = os.path.join('每日各站進出站人數')
    station_path = os.path.join(file_dirname,'車站基本資料集.json')
    with open (station_path,encoding='utf-8') as file:
        content =  json.load(file)
    station_imformation = pd.DataFrame(content)  
    station_imformation["stationCode"]= station_imformation['stationCode'].astype(int)
    return station_imformation

def in_out_imformation(names:list[str],stations:DataFrame):
    all_df = []
    for name in names:
        inOut=pd.read_csv(name)
        df1 = pd.merge(inOut,stations,left_on='staCode',right_on='stationCode')
        df2=df1.reindex(columns=['trnOpDate',
                                 'stationName',
                                 'gateInComingCnt',
                                 'gateOutGoingCnt'])
        df3 =df2.rename(columns={'trnOpDate':'日期',
                                 'stationName':'站名',
                                 'gateInComingCnt':'入站',
                                 'gateOutGoingCnt':'出站'})
        df3['日期'] = pd.to_datetime(df3['日期'].astype(str))
        all_df.append(df3)
    return all_df
