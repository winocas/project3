import requests
import pandas as pd

def get_tot_coro():
    url_total   = "https://api.corona-19.kr/korea/?serviceKey=TaOMDorm6Zn5fsAijcyuWdhqBC7z12vtY"
    response_tot = requests.get(url_total) 
    json_tot = response_tot.json()
    return json_tot

def get_city_coro():
    url_region   = "https://api.corona-19.kr/korea/country/new/?serviceKey=TaOMDorm6Zn5fsAijcyuWdhqBC7z12vtY"
    response_region = requests.get(url_region) 
    json_region = response_region.json()
    city_coro = {k: response_region.json()[k] for k in list(json_region.keys())[2:-1]}
    return city_coro

# print(get_tot_coro())
# print(list(json_tot.keys())[2:-1][0], json_tot[list(json_tot.keys())[2:-1][0]])
# print(json_tot)