import requests
from pprint import pprint

def main():
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
    try:
        response = requests.get(youbike_url)
    except Exception  as error:
        print(error)
    else:
        data = response.json()
        while True:
            district = input("請輸入新北市行政區: ")
            district = district + "區"

            district_stations = []
            for station in data:
                if station['sarea'] == district:
                    district_stations.append(station)


            if district_stations:
                pprint(district_stations)
                break
            else:
                print(f"沒有找到 {district} 行政區的站點資訊。請再輸入一次")
if __name__== '__main__':
    main()