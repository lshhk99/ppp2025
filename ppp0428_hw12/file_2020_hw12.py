import os.path

import requests

def average(nums):
    return sum(nums) / len(nums)

def download_weather(station_id, year, filename):

    URL =f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def count_bigger_days(nums, criteria):
    count = 0
    for num in nums:
        if num >= criteria:
            count += 1
    return count

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def main():
    filename = "weather(146)_2020-2020.csv"
    if not os.path.exists(filename):
        download_weather(146, 2020, filename)

    # 1. 일평균 기온의 연평균
    tavgs = get_weather_data(filename, 4)
    print(f"연평균 기온 (avg. of 일평균) = {average(tavgs):.2f}℃")

    # 2. 5mm이상 강우일수
    rainfalls = get_weather_data(filename, 9)
    count_over5_rain = count_bigger_days(rainfalls, 5)
    print(f"5mm이상 강우일수 = {count_over5_rain}일")

    # 3. 총 강우량
    print(f"총 강우량 = {sum(rainfalls):.1f}mm")

    # 결과를 다른 CSV 파일에 저장
    with open("weather_result_hw12.csv", "w", encoding="UTF-8") as f:
        f.write("항목 값\n")
        f.write(f"연평균 기온  {average(tavgs):.2f}℃\n")
        f.write(f"5mm이상 강우일수 {count_over5_rain}일\n")
        f.write(f"총 강우량 {sum(rainfalls):.1f}mm\n")

if __name__=="__main__":
    main()