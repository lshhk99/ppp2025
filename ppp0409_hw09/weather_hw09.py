def read_db(filename):
    weather_dic = []
    with open(filename, encoding="utf-8-sig") as f:
        lines = f.readlines()
        header =lines[0].strip().split(",")
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            data = {}
            for i in range(len(header)):
                data[header[i]] = tokens[i]
            weather_dic.append(data)
    return weather_dic




def main():
    weather = read_db("weather(146)_2022-2022.csv")
    #일 평균 기온으로 연 평균 기온 구하기
    total_tavg = 0
    for i in weather:
        total_tavg += float(i[' tavg'])
    aver = total_tavg / len(weather)
    total_rainfall = 0
    # 5mm이상 강우일수 구하기
    count = 0
    for i in weather:
        if float(i[' rainfall']) >= 5:
            count += 1

    #총 강우량 구하기
    for i in weather:
        total_rainfall += float(i[' rainfall'])


    print(f"연 평균 기온은{aver:.3f}℃ 이다.")
    print(f"5㎜이상 강우일수는 {count}이다.")
    print(f"총 강우량은 {total_rainfall:.3f}이다.")





if __name__=="__main__":
    main()