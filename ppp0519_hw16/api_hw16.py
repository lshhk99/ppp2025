from ppp0519.sfarm_hw import submit_to_api
import os.path
import requests

def download_weather(station_id, year, filename):

    URL =f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas

def get_weather_date(fname):
    with open(fname) as f:
        weather_dates = []
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_dates

def sumifs(rainfalls, years, selected = [2000]):
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        year = years[i]
        if year in selected:
            total += rain
    return total

def max_temp(tmax, years, selected):
    top_temp = 0
    for i in range(len(tmax)):
        temp = tmax[i]
        year = years[i]
        if year in selected:
            if temp > top_temp:
                top_temp = temp
    return  top_temp

def maximum_temp_gap(dates, tmax, tmin, selected):
    max_gap = tmax[0]-tmin[0]
    max_gap_date = dates[0]
    for i in range(len(dates)):
        date = dates[i]
        year = date [0]
        tx = tmax[i]
        tm = tmin[i]
        gap = tx - tm
        if year in selected:
            if max_gap < gap:
                max_gap = gap
                max_gap_date = date

    return [max_gap_date, max_gap]


def main():
    filename_su_2024 = "weather(119)_2024-2024.csv"
    if not os.path.exists(filename_su_2024):
        download_weather(119, 2024, filename_su_2024)

    filename_2024 = "weather(146)_2024-2024.csv"
    if not os.path.exists(filename_2024):
        download_weather(146, 2024, filename_2024)

    filename = "weather(146)_2001-2022.csv"

    years = get_weather_data_int(filename, 0)
    years_1 = get_weather_data_int(filename_su_2024, 0)
    years_2 = get_weather_data_int(filename_2024, 0)

    rainfalls = get_weather_data(filename, 9)
    rainfalls_1 = get_weather_data(filename_su_2024, 9)
    rainfalls_2 = get_weather_data(filename_2024, 9)

    dates = get_weather_date(filename_2024)
    tmax = get_weather_data(filename_2024, 3)
    tmin = get_weather_data(filename_2024, 5)
    tavg = get_weather_data(filename, 4)

    #1. 전주시 2015년 연 강수량
    rain_2015 = round(sumifs(rainfalls, years, selected=[2015]),1)
    print(f"2015년의 총 강수량은 {rain_2015}mm 입니다.")

    #2. 전주시 2022년 최대기온
    ttemp = round(max_temp(tavg, years, [2022]), 1)
    print(f"2022년의 최대기온은은 {ttemp}℃ 입니다.")

    #3. 전주시 2024 최대 일교차
    max_gap_date, max_gap = maximum_temp_gap(dates, tmax, tmin, [2024])
    tgap = round(max_gap, 1)
    print(f"2024년  {max_gap_date[1]}/{max_gap_date[2]} 일때 최대 일교차는 {tgap}℃ 입니다")

    #4. 수원시와 전주시의 2024년 총 강수량의 차이는
    su_rain = round(sumifs(rainfalls_1, years_1, selected=[2024]), 1)
    jeon_rain = round(sumifs(rainfalls_2, years_2, selected=[2024]), 1)
    result = round(abs(su_rain - jeon_rain), 1)
    print(f"수원시와 전주시의 2024년 총가수량의 차이는 {su_rain} - {jeon_rain} = {result}")





    #http: // sfarm.digitalag.kr: 8800
    name = "이성학"
    affiliation = "스마트팜학과"
    student_id = "202210099"

    answer1 = rain_2015
    answer2 = ttemp
    answer3 = tgap
    answer4 = result

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__=="__main__":
    main()