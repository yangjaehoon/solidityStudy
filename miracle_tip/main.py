import pyautogui
import time
import pandas as pd

# 몇 초 뒤에 입력할지 설정
time.sleep(3)  # 3초 대기 후 실행

#file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_polygon_prize.xlsx'
#file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_base_prize.xlsx'
#file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_opbnb_prize.xlsx'
#file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_arbitrum_prize.xlsx'
#file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_xpla_prize.xlsx'
file_path = 'C:/Users/lljhm/Desktop/miracleplay_whale club/final_avalanche_prize.xlsx'
df = pd.read_excel(file_path)

# discord_name과 cp 값을 추출하며, discord_name이 유효한 경우만 선택
valid_rows = df[df.iloc[:, 7].notna()]  # 이름이 NaN이 아닌 행만 선택
valid_rows = valid_rows[valid_rows.iloc[:, 7].str.strip() != ""]  # 이름이 빈 문자열이 아닌 행만 선택

discord_name = valid_rows.iloc[:, 7].str.replace(" ", "").str.lower().tolist()
cp = valid_rows.iloc[:, 5].tolist()

# "!tip mlge 1000 @discord_name" 입력
for name, num in zip(discord_name, cp):
    # 이름과 CP 출력
    print(f"Processing: {name}, CP: {int(num*1.1)}")

    # pyautogui를 이용한 명령어 입력
    pyautogui.typewrite(f"!tip mpt {int(num*1.1)} @{name}")

    # 엔터 두 번 입력
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(12)
