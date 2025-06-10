#Data Collection

import requests
import pandas as pd
from collections import defaultdict
import time

API_KEY = "yYUuOKV62xS5XflsoRvC6jIiLZy5WpWnb7OqbVPe"  # My NASA API Key
ROVERS = ["curiosity", "perseverance"]  
START_DATE = "2023-01-01"
END_DATE = "2023-01-31"  # Collect data of Junuary 2023

def daterange(start_date, end_date):
    from datetime import datetime, timedelta
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    delta = timedelta(days=1)
    current = start
    while current <= end:
        yield current.strftime("%Y-%m-%d")
        current += delta

def fetch_photos(rover, date):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos"
    params = {
        "earth_date": date,
        "api_key": API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        photos = response.json().get("photos", [])
        print(f"{rover} {date} 照片數量: {len(photos)}")
        return photos
    else:
        print(f"API錯誤：{response.status_code} on {rover} {date}")
        return []

def main():
    records = []
    for rover in ROVERS:
        for date in daterange(START_DATE, END_DATE):
            photos = fetch_photos(rover, date)
            camera_counts = defaultdict(int)
            for photo in photos:
                camera_counts[photo["camera"]["name"]] += 1
            
            total_photos = len(photos)
            if total_photos > 0:
                for camera, count in camera_counts.items():
                    records.append({
                        "rover": rover,
                        "earth_date": date,
                        "camera": camera,
                        "photo_count": count,
                        "total_photos": total_photos
                    })
            else:
                records.append({
                    "rover": rover,
                    "earth_date": date,
                    "camera": None,
                    "photo_count": 0,
                    "total_photos": 0
                })
            time.sleep(1)
    
    df = pd.DataFrame(records)
    df.to_csv("/Users/vc/Downloads/mars_rover_photos_summary.csv", index=False)
    print("資料已儲存 mars_rover_photos_summary.csv")

if __name__ == "__main__":
    main()
