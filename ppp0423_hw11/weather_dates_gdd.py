def get_weather_date(fname):
    with open(fname) as f:
        weather_dates = []
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_dates

def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def gdd_season(tavg, dates, selected):
    base_temp = 5
    temp_cum = 0
    for i in range(len(tavg)):
        t = tavg[i]
        if dates[i][0] in [selected]:
            if dates[i][1] in [5, 6 ,7, 8 ,9]:
                if t >= base_temp:
                    temp_cum += (t-base_temp)
    return temp_cum

def main():
    filename = "weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tavg = get_weather_data(filename, 4)
    year = 2000
    for i in range(1, 23):
        years = year + i
        print(f"{years}년 5~6월의 gdd는 {gdd_season(tavg, dates, years):.1f}입니다.")



if __name__=="__main__":
    main()