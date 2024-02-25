import requests
import json
import os

def fetch_data_and_save():
    url = "https://bet.hkjc.com/football/getJSON.aspx?jsontype=odds_had.aspx"
    response = requests.get(url)
    
    if response.status_code == 200:
        # 將JSON數據寫入文件
        data = response.json()
        file_path = os.path.join(os.path.dirname(__file__), "data.json")  # 存儲路徑為腳本所在目錄
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("Data fetched and saved successfully.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    fetch_data_and_save()
