import requests
import json
import os

def fetch_data_and_save():
    url = "https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_had.aspx"
    response = requests.get(url)
    
    if response.status_code == 200:
        # 提取JSON數據
        data = response.json()
        
        # 從JSON數據中提取並保留指定的鍵值
        matches = data.pop('matches', [])
        new_matches = []
        for match in matches:
            new_match = {
                "matchTime": match["matchTime"],
                "frontEndId": match["frontEndId"],
                "homeTeam": {
                    "teamNameCH": match["homeTeam"]["teamNameCH"],
                    "teamNameEN": match["homeTeam"]["teamNameEN"]
                },
                "awayTeam": {
                    "teamNameCH": match["awayTeam"]["teamNameCH"],
                    "teamNameEN": match["awayTeam"]["teamNameEN"]
                },
                "isESOffer": match["isESOffer"],
                "tournament": {
                    "tournamentNameCH": match["tournament"]["tournamentNameCH"],
                    "tournamentNameEN": match["tournament"]["tournamentNameEN"]
                },
                "liveEvent": {
                    "hasLiveInfo": match["liveEvent"]["hasLiveInfo"]
                },
                "anyInplaySelling": match["anyInplaySelling"]
            }
            new_matches.append(new_match)
        
        # 建立新的JSON物件，只包含matches部分
        new_data = {'matches': new_matches}
        
        # 將新的JSON物件寫入文件
        file_path = os.path.join(os.getcwd(), "data.json")  # 存儲路徑為當前工作目錄
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(new_data, f, ensure_ascii=False, indent=4)
        print("Data fetched and saved successfully.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_data_and_save()
