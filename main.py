from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import os

# Chrome 서비스 설정
service = Service(ChromeDriverManager().install())

# 드라이버 생성 및 페이지 접근
with webdriver.Chrome(service=service) as driver:
    driver.get('https://polygon.miracleplay.gg/club/detail/132')  # 페이지 URL

    # 버튼이 있으면 계속 클릭
    while True:
        try:
            load_more_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[4]/section[2]/div/article[3]/button'))
            )
            load_more_button.click()
            time.sleep(1)
        except:
            print("더 이상 클릭할 버튼이 없습니다.")
            break

    # 테이블 데이터 추출
    table = driver.find_element(By.XPATH, '/html/body/div/div[4]/section[2]/div/article[3]/div/table')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    # 데이터 저장용 리스트
    table_data = []
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        if cells:
            # 필요한 인덱스(0, 1, 5, 6)만 추출
            cell_data = [cells[i].text for i in [0, 1, 5, 6]]
            table_data.append(cell_data)

    # 데이터프레임으로 변환
    df = pd.DataFrame(table_data, columns=['rank', 'name', 'cp', 'contribution'])

    # 현재 작업 디렉토리에 엑셀 파일로 저장
    file_path = os.path.join(os.getcwd(), "whale_club_cp_polygon.xlsx")
    df.to_excel(file_path, index=False)

print(f"엑셀 파일로 저장 완료: {file_path}")
