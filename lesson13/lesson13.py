import requests
from pprint import pprint
from requests import Response
def bike_conection() ->Response:
    youbike_url = 'https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/json?size=1000'
    try:
        Response = requests.get(youbike_url)
    except Exception  as error:
        return error
    else:
    
        return Response

def main():
        response:Response = bike_conection()
        if not isinstance(response,Response):
            print(response)
            return

        
        district = input("請輸入新北市行政區: ")
        district = district + "區"

        district_stations = []
        data = response.json()
        for station in data:
            if station['sarea'] == district:
                district_stations.append(station)


            if district_stations:
                pprint(district_stations)
                
                
        
if __name__== '__main__':
    main()