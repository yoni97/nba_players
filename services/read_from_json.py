import json

import requests

API_LINK_2024 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2024'
API_LINK_2023 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2023'
API_LINK_2022 = 'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/season/2022'

def get_nba_stats_games(link):
    response = requests.get(link)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"
# print(get_nba_stats_games(API_LINK_2024))
# print(get_nba_stats_games(API_LINK_2023))
# print(get_nba_stats_games(API_LINK_2022))