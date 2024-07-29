import requests
import pyinputplus as pyip
from requests import Response
from pprint import pprint
from requests import ConnectionError,TooManyRedirects,Timeout,HTTPError

def connect_youbike() -> Response | str:
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
    try:
        response:Response = requests.get(youbike_url)
        response.raise_for_status()
    except ConnectionError:
        return "連線主機出問題"
    except TooManyRedirects:
        return "太多轉址"
    except Timeout:
        return "主機正在忙"
    except HTTPError:
        return "status_不是200"
    except:
        return "不明錯誤"
    else:
        return response
def search_station(Response,district):
    data:list[dict] = Response.json()    
    district_stations = [district for station in data if station['sarea'] == district]    
    return district_stations
def get_sarea(response):
    data:list[dict] = response.json()
    Sarea:set=set()
    for site in data:
        Sarea.add(site['sarea'])
    return Sarea

def main():
    response:Response | str = connect_youbike() 
    if not isinstance(response,Response):
        print(response)
        return
    
    print("連線成功")
    searea = get_sarea(response)
    district = pyip.inputMenu(searea,"請輸入新北市行政區:\n",numbered=True)

    district_stations=search_station(response,district)
    if district_stations:
        pprint(district_stations)


if __name__ == '__main__':
    main()