def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas

def get_weather_date(fname):
    with open(fname) as f:
        weather_dates = []
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_dates



def maxinum_temp_gap(dates, tmax, tmin, selected):
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
    filename = "weather(146)_2001-2022.csv"
    dates = get_weather_date(filename)
    tmax = get_weather_data(filename, 3)
    tmin = get_weather_data(filename, 5)
    years = 2000
    for i in range(1, 23):
        years += 1
        max_gap_date, max_gap = maxinum_temp_gap(dates, tmax, tmin, [years])
        print(f"{years}/{max_gap_date[1]}/{max_gap_date[2]} 일때 일교차는 {max_gap:.1f}℃ 입니다")

if __name__=="__main__":
    main()