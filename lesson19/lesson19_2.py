
if __name__ == "__main__":
    name_list = get_path()
    stations_imfo = get_station_imfo()
    all_in_out = in_out_imformation(name_list,stations_imfo)
    station_in_out = pd.concat(all_in_out)
    station_in_out.to_csv("進出站人數表.csv")
    day = ['2020-01-01']
    print(station_in_out[
        station_in_out['日期'].isin(day)])