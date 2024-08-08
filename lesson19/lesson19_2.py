from tools import get_path,in_out_imformation,get_station_imfo
import pandas as pd
if __name__ == "__main__":
    name_list = get_path()
    stations_imfo = get_station_imfo()
    all_in_out = in_out_imformation(name_list,stations_imfo)
    station_in_out = pd.concat(all_in_out)
    data=station_in_out[station_in_out['日期'].isin(['2020-01-01'])]
    data.to_csv("當日進出站人數.csv")