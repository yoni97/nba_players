import requests

years = [2022, 2023, 2024]
y3 = 2023
y2 = 2022
y4 = 2024


def get_nba_stats_games(y2):
    url_link = f'http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={y2}&&pageSize=1000'
    response = requests.get(url_link)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return f"Failed to retrieve data: {response.status_code}"



